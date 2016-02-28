#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import logging.config
import datetime

from UtilsManager import UtilsManager
from EnvManager import EnvManager

cfg_reader = UtilsManager().get_config_parser()
log_file = os.path.join(
    EnvManager().get_env_var("PJ_LOGS_DIR"), cfg_reader.get('LOGGING', 'LOG_FILE'))
log_file = log_file.split(".")[0] + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S").replace(":", "-") + "." + log_file.split(".")[1]
log_size = cfg_reader.get('LOGGING', 'LOG_FILE_MAX_SIZE')
bckup_count = cfg_reader.get('LOGGING', 'LOG_BACKUP_COUNT')
LOG_FILENAME = log_file

def get_logger(log_file=None):
    logger = logging.getLogger("OrderBotLogger")
    logger.setLevel(logging.DEBUG)
    ch = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=int(log_size), backupCount=int(bckup_count))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    return logger
