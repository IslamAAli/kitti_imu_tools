# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import pandas as pd
import os

import config


def read_seq_list():
    if os.path.isfile(config.INPUT_SEQ_FILE_PATH):
        seq_file = open(config.INPUT_SEQ_FILE_PATH, 'r')
        return seq_file.readlines()
    else:
        print('[**ERROR**] Sequences File Dose NOT Exist !')


