# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

from typing import List, Any, Union
import glob
import pandas as pd


def concat_imu_files(input_path, output_path):

    # read files names in a certain directory
    filenames = glob.glob(input_path+"/*.txt")

    # concatenate the content of the IMU/GNSS files
    with open(output_path, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())


def read_imu_file_content(file_name):

    data = pd.read_csv(file_name, sep=" ", header=None)
    data.columns = ['lat',
                    'lon',
                    'alt',
                    'roll',
                    'pitch',
                    'yaw',
                    'vn',
                    've',
                    'vf',
                    'vl',
                    'vu',
                    'ax',
                    'ay',
                    'az',
                    'af',
                    'al',
                    'au',
                    'wx',
                    'wy',
                    'wz',
                    'wf',
                    'wl',
                    'wu',
                    'pos_accuracy',
                    'vel_accuracy',
                    'navstat',
                    'numsats',
                    'posmode',
                    'velmode',
                    'orimode']
    return data


def read_timestamps_file(file_name):
    data = pd.read_csv(file_name, sep="\t", header=None)
    data.columns = ['timestamp']

    return data

