# ! /usr/bin/env python

"""
Set all necessary variables to run the project
"""
import os, sys


class EnvManager(object):
    src_root = None
    config_dir = None
    config_file = None
    utils_dir = None

    def __init__(this):
        pre_file = os.path.realpath(__file__)
        pre_dir, f = os.path.split(pre_file)
        pre_dir, f = os.path.split(pre_dir)
        this.src_root = os.path.abspath(pre_dir)
        this.config_dir = os.path.join(this.src_root, "Config")
        this.pj_config_file = os.path.join(this.config_dir, "config.cfg")
        this.utils_dir = os.path.join(this.src_root, "Utils")
        this.logs_dir = os.path.join(this.src_root, "logs")
        this.set_env_vars()


    def set_env_vars(this):
        os.environ['PJ_ROOT'] = this.src_root
        os.environ['PJ_CONFIG_DIR'] = this.config_dir
        os.environ['PJ_CONFIG_FILE'] = this.pj_config_file
        os.environ['PJ_UTILS_DIR'] = this.utils_dir
        os.environ['PJ_LOGS_DIR'] = this.logs_dir


    def get_env_var(this, var):
        value = ""
        value = os.getenv(var)
        if ( value is not None ):
            # Uncomment the below print for debugging mode
            #print var[3:] , "=", value
            return value
        else:
            print "Environment Variable", var[3:], "not set"
            return None


    def dump_all_vars(this):
        for k, v in this.__dict__.iteritems():
            print k, "=", v
