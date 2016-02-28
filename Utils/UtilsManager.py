#!/usr/bin/env python

import os

from ConfigParser import SafeConfigParser

from StatusCodes import OrderStatusCodes
from EnvManager import EnvManager

class UtilsManager(object):
    config_parser = None
    config_file = None

    def __init__(this): 
        this.config_parser = SafeConfigParser()
        this.config_file = EnvManager().get_env_var("PJ_CONFIG_FILE")

    def get_config_parser(this):
        if (this.config_file is not None):
            try: 
                this.config_parser.read(this.config_file)
            except Exception as err:
                print err 
                print "Unable to read config file"
                return (OrderStatusCodes.ERROR)
        return (this.config_parser)
    
    def get_config_file(this):
        return (this.config_file)
