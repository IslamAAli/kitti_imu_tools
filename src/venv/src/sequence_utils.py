# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------


import sys
import wget
import zipfile
import os
from distutils.dir_util import copy_tree
import shutil


# ========================================================================================================
def download_all_sequences():
    seq_name = '2011_09_28_drive_0128'

    # for each sequence:
    # --- (0) check if it was downloaded before
    if os.path.exists('../../../data/'+seq_name+"_oxts"):
        print('=> ', seq_name, ' Already exists.')
    else:
        # --- (1) download the sequence
        download_seq(seq_name)

        # --- (2) Extract the file and remove vision and LiDAR files
        print("---- Unzipping")
        with zipfile.ZipFile('../../../data/'+seq_name+'.zip', "r") as zip_ref:
            zip_ref.extractall('../../../data/'+seq_name)

        # --- (3) Copy oxts folder into data folder
        print("---- Extracting IMU information")
        copy_tree('../../../data/'+seq_name+'/'+seq_name[0:10]+'/'+seq_name+'_sync/oxts',
                  '../../../data/'+seq_name+"_oxts")

        # --- (4) Delete Downloaded files
        print("---- Cleaning up !")
        shutil.rmtree('../../../data/'+seq_name)
        os.remove('../../../data/'+seq_name+'.zip')

    print('------------------------------------')


# ========================================================================================================
def download_seq(seq_name):
    print('=> Downloading', seq_name)
    url = "https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/"+seq_name+"/"+seq_name+"_sync.zip"
    filename = wget.download(url, '../../../data/'+seq_name+'.zip', bar=bar_custom)
    print("\n----", seq_name, ' Downloaded !')


# ========================================================================================================
def bar_custom(current, total, width=80):
    progress_message = "---- Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()
