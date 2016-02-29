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
        aws_key = cfg_parser.get("AWS", "AWS_KEY")
        # search using BOTO library GET call


