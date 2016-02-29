#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StreamReaderFactory import StreamReaderFactory

class HadoopReader(StreamReaderFactory):
    """
    Hadoop Stream Reader
    """

    def __init__(this):
        pass

    def read_order(this):
        """
        I will read any order coming from Hadoop
        Pesudo-code
        1. Install PyHive library
        2. Connect to hive schema and  Run hive query to fetch the data
        """
        pass

