# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import pandas as pd
import file_tools

# System Configurations
TESTING_MODE = False
DATA_DIR = '../../../data/'
INPUT_DIR = '../../../input/'
OUTPUT_DIR = '../../../output/'

files_list = []

stats_df = pd.DataFrame(columns=['ax_max', 'ax_min', 'ax_median', 'ax_mean',
                                 'ay_max', 'ay_min', 'ay_median', 'ay_mean',
                                 'az_max', 'az_min', 'az_median', 'az_mean',

                                 'wx_max', 'wx_min', 'wx_median', 'wx_mean',
                                 'wy_max', 'wy_min', 'wy_median', 'wy_mean',
                                 'wz_max', 'wz_min', 'wz_median', 'wz_mean',

                                 'vx_max', 'vx_min', 'vx_median', 'vx_mean',
                                 'vy_max', 'vy_min', 'vy_median', 'vy_mean',
                                 'vz_max', 'vz_min', 'vz_median', 'vz_mean',

                                 'rx_max', 'rx_min', 'rx_median', 'rx_mean',
                                 'py_max', 'py_min', 'py_median', 'py_mean',
                                 'yz_max', 'yz_min', 'yz_median', 'yz_mean'])

# Testing mode configurations
if TESTING_MODE:
    INPUT_SEQ_FILE_PATH = INPUT_DIR + 'sequences_list_min.txt'
else:
    INPUT_SEQ_FILE_PATH = INPUT_DIR + 'sequences_list_full.txt'


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
