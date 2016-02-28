#!/usr/bin/env python

import json
import os

from Config.Constants import *
from Utils.UtilsManager import UtilsManager
from Utils.EnvManager import EnvManager
from Utils.OrderBotLogger import get_logger; logger = get_logger()


class InventoryAllocator(object):
    def __init__(this, in_order, finger_print, processed_list):
        this.in_order_list = in_order
        this.uid = finger_print
        this.processed_list = processed_list

    def __call__(this):
       this.process_inbound_order()

    def compile_db_path(this):
        cfg_parser = UtilsManager().get_config_parser()
        db_dir = cfg_parser.get("FILE_STREAM", "WAREHOUSE_PATH")
        db_file = cfg_parser.get("FILE_STREAM", "WAREHOUSE_DATA")
        pj_root = EnvManager().get_env_var("PJ_ROOT")
        db_data = os.path.join(pj_root, db_dir, db_file)
        return db_data

    def process_inbound_order(this):
        print "Processing Unique Order id: ", this.uid
        order_done = []
        db_data = this.compile_db_path()

        with open (db_data, "r") as ware_house_data:
            ware_house_stock = json.load(ware_house_data)
            msg = ("Current Available Stock: %s") % (ware_house_stock)
            logger.info("%s", msg)

        if not this.check_stock(ware_house_stock):
            msg = "Warehouse Busted.Oh My GOD, somebody please call 911..."
            print msg
            logger.error(msg)
            this.processed_list["NO_STOCK"] = "WAREHOUSE_EMPTY"
            return this.processed_list

        # Iterable instead of list, less memory usage
        for ord in iter(this.in_order_list):
            for k,v in iter(ord.items()):
                #No more hard coding like if k.strip() == "Header", usage of MACRO saves life
                if k.strip() == UNIQUE_KEY_NAME:
                    curr_header = v
                elif k.strip() == ORDER_IDENTIFIER:
                    print "-"*110
                    # Iterable instead of list, less memory usage
                    for ele in iter(v):
                        try:
                            msg =  ("Ordered Product: %s") % (str(ele["Product"]))
                            print msg
                            ordered_product = str(ele["Product"])
                            logger.info(msg)
                            current_stock = ware_house_stock[ordered_product]
                        except Exception as err:
                            msg = ("Requested product not available in stock.\nProceeding to next order ")
                            print msg
                            logger.info(msg)
                            print "-"*110
                            logger.warn(err)
                            continue
                        else:
                            placed = 0
                            bck_orded = 0
                            requested = int(ele["Quantity"])
                            print "Requested Quantity: ", requested
                            if requested == 0 or requested > 5:
                                print "Invalid Order: "
                                continue
                            print "Current Stock:", current_stock
                            if current_stock == 0:
                                msg = ("Requested Product %s Out of Stock.Doing back order and Proceeding to next order...") \
                                % (ordered_product)
                                print msg
                                logger.info(msg)
                                bck_orded = requested
                            elif current_stock > requested:
                                msg = "Allocating items from ware house..."
                                print msg
                                logger.info(msg)
                                current_stock = current_stock - int(requested)
                                ware_house_stock[ordered_product] = current_stock
                                placed = requested
                                msg = "Order Completed Successfully"
                                logger.info(msg)
                                print msg
                            else:
                                msg = ("Requested product %s out of stock. Doing back order, Will get back to you soon.") % (ordered_product)
                                logger.info(msg)
                                bck_orded = requested
                                print msg
                            commit_log = {"Header":curr_header, "OrderedProduct": ordered_product, "OrderDetails": [requested, placed, bck_orded]}
                            order_done.append(commit_log)
                            msg = ("Remaining Stock: %s") % (ware_house_stock)
                            print msg
                            logger.info(msg)
                            with open(db_data, "w") as update:
                                json.dump(ware_house_stock, update, indent=4)

                        print "-"*110
            this.processed_list[this.uid] = order_done
                           

    def check_stock(this, ware_house_stock):
        return any(ware_house_stock.values())
         
