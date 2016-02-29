#!/usr/bin/env python

#Python STL Imports
import sys
from  multiprocessing import Process, Lock, JoinableQueue, Manager, log_to_stderr
import logging
import uuid
from optparse import OptionParser

#3rd Party Libraries

#Local Imports
from OrderReader.StreamReaderFactory import StreamReaderFactory
from OrderReader.FileStreamReader import FileStreamReader
from Utils.UtilsManager import UtilsManager
from Utils.StatusCodes import OrderStatusCodes
from InventoryProcessor.InventoryAllocator import InventoryAllocator

def parallel_processor(que, lck, processed_list):
    while True:
        try:
            # No more show stopper based exit like None & break
            # Untill we dont have anything in the queue, will get out by catching the Empty error
            # in catch block
            lck.acquire(block=True, timeout=10)
            task = que.get_nowait()
            task()
            que.task_done()
            lck.release()
            if len(processed_list) == 1:
                if (processed_list.keys()[0]).strip() == "NO_STOCK":
                    break
        except Exception as err:
            lck.release()
            break


def initialize(order_stream, order_dest):
    cfg_parser = UtilsManager().get_config_parser()
    max_proc = cfg_parser.get("FILE_STREAM", "MAX_PROCESS")
    placer = StreamReaderFactory.get_order_placer(order_stream, int(max_proc), order_dest)
    order_list = placer.read_order()

    proc_que = JoinableQueue()
    proc_mgr = Manager()
    lck = Lock()
    processed_list = proc_mgr.dict()

    procs = []
    # Enable the below if you want process level debug info
    # log_to_stderr(logging.DEBUG)

    # Made the files list as iterable for memory efficiency
    for ord_set in iter(order_list):
        ord_exec = InventoryAllocator(ord_set, str(uuid.uuid1()).split("-")[0], processed_list)
        proc_que.put(ord_exec)
        proc = Process(target=parallel_processor, args=(proc_que, lck, processed_list))
        procs.append(proc)
        proc.start()

    """
    procs = []
    log_to_stderr(logging.DEBUG)
    for _ in xrange(len(order_list)):
        proc = Process(target=parallel_processor, args=(proc_que, lck, processed_list))
        procs.append(proc)
        proc.start()

    """

    for p in procs:
        p.join()

    print "*"*110,"\n"
    print "Finale List of Processed Order: ", __import__("json").dumps(processed_list.copy(), indent=1)
    print "*"*110


if __name__ == "__main__":
    usage = "usage: python . -s/--stream <stream_type> -i/--inputPath <inbound_orders_dir>" 
    parser = OptionParser(usage, version="OrderBot Version 1.0")
    parser.add_option("-s", "--stream", dest="in_stream", action="store", type=str, help="Input Streams File/DB/Network/Hadoop")
    parser.add_option("-i", "--inputPath", dest="in_order_path", action="store", type=str, help="Optional Input Orders Path for File Stream")
    (options, args) = parser.parse_args()
    if (options.in_stream is None or options.in_order_path is None):
        parser.print_help()
        sys.exit(OrderStatusCodes.ERROR)
    order_stream = options.in_stream
    order_dest = options.in_order_path
    initialize(order_stream, order_dest)

