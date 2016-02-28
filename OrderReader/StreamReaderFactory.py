#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main Base Abstract Factory 
This is the interface to get in to other factories as well as utilities
"""
import abc


class StreamReaderFactory(object):
    """
    Factory to return matching stream reader
    """

    __metaclass__ = abc.ABCMeta

    def __init__(this):
        pass


    @classmethod
    def get_order_placer(cls, stream_type, max_proc, order_dest):
        """
        Production Machine to return the child(concrete product)
        Return the correct product based on the input stream
        """
        stream_type= stream_type.title()
        if (stream_type == "File"):
            for cl in cls.__subclasses__():
                if (stream_type in cl.__name__):
                    return cl(max_proc, order_dest)


    @abc.abstractmethod
    def read_order(this):
        """
        Interface for placing order
        Derived classes must implement it
        """
        pass

