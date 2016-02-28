#!/usr/bin/env python

import glob
import os
import json

from StreamReaderFactory import StreamReaderFactory
from Utils.UtilsManager import UtilsManager


class FileStreamReader(StreamReaderFactory):

    def __init__(this, max_proc, in_src_path=None):
        """
        src_path is where we store orders
        Users can specify their own path to override  it
        or we will get the default path from config file
        """
        cfg_parser = UtilsManager().get_config_parser()
        this.order_file_names = cfg_parser.get("FILE_STREAM", "ORDER_FILE_NAME")
        if in_src_path is None:
            inbound_path = cfg_parser.get("FILE_STREAM", "INBOUND_DIR")
            this.src_path = inbound_path
        else:
            this.src_path = in_src_path
        this.max_proc = max_proc


    def __str__(this):
        return repr("File Stream Reader")

    def read_order(this):
        in_dir_path = os.path.join(this.src_path, this.order_file_names)
        orders = []
        new_ord = []
        for ord_file in iter(glob.glob(in_dir_path)):
            with open(ord_file) as in_file:
                data = json.load(in_file)
                orders.append(data)
        if len(orders) > this.max_proc:
            while orders:
                new_ord.append(orders[0:this.max_proc])
                orders[0:this.max_proc] = []
        else:
            new_ord.append([orders])
        msg = ("Orders to Process: %s") % (json.dumps(new_ord, indent=3))
        print msg
        return new_ord

