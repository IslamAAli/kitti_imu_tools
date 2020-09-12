# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import pandas as pd


def read_file_content(file_name):

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

