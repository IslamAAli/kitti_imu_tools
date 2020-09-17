# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import pandas as pd
import file_tools

# System Configurations
TESTING_MODE = True
DATA_DIR = '../../../data/'
INPUT_DIR = '../../../input/'
OUTPUT_DIR = '../../../output/'

files_list = []


# Testing mode configurations
if TESTING_MODE:
    INPUT_SEQ_FILE_PATH = INPUT_DIR+'sequences_list_min.txt'
else:
    INPUT_SEQ_FILE_PATH = INPUT_DIR+'sequences_list_full.txt'


# Initialization of the pandas package
def pandas_config():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)


# Application initialization function interface
def app_init():
    pandas_config()
    global files_list
    files_list = file_tools.read_seq_list()
