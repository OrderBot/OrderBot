#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StreamReaderFactory import StreamReaderFactory
from Utils.UtilsManager import UtilsManager

class ElasticDBReader(StreamReaderFactory):
    """
    Hadoop Stream Reader
    """

    def __init__(this):
        pass

    def read_order(this):
        """
        I will search any order in Elastic Server
        Below is the Pesudo-code, not actual
        """
        cfg_parser = UtilsManager().get_config_parser()
        elastic_host = cfg_parser.get("ELASTIC_DB", "ELASTIC_SEARCH_HOST")
        elastic_port = cfg_parser.get("ELASTIC_DB", "ELASTIC_SEARCH_PORT")
        order_id = "fb578538"
        query = {order_id: "value"}
        # search using requests library GET call


