# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import sys
import wget
import zipfile
import os
import pandas as pd
from distutils.dir_util import copy_tree
import shutil
import file_tools
import config
import imu_files_utils


# ========================================================================================================
def download_all_sequences():

    # Read all sequences names
    count = 0
    total_seq = len(config.files_list)
    for line in config.files_list:
        count += 1
        seq_name = line.rstrip('\n')
        print('Sequence ', count, ' of ', total_seq, ' : ',  seq_name)

        # for each sequence:
        # --- (0) check if it was downloaded before
        if os.path.exists(config.DATA_DIR+seq_name+"_oxts"):
            print('=> ', seq_name, ' Already exists.\n')
        else:
            # --- (1) download the sequence
            download_seq(seq_name)

            # --- (2) Extract the file and remove vision and LiDAR files
            print("---- Unzipping")
            with zipfile.ZipFile(config.DATA_DIR+seq_name+'.zip', "r") as zip_ref:
                zip_ref.extractall(config.DATA_DIR+seq_name)

            # --- (3) Copy oxts folder into data folder
            print("---- Extracting IMU information")
            copy_tree(config.DATA_DIR+seq_name+'/'+seq_name[0:10]+'/'+seq_name+'_sync/oxts',
                      config.DATA_DIR+seq_name+"_oxts")

            # --- (4) Delete Downloaded files
            print("---- Cleaning up !")
            shutil.rmtree(config.DATA_DIR+seq_name)
            os.remove(config.DATA_DIR+seq_name+'.zip')

    print('------------------------------------')


# ========================================================================================================
def merge_files():

    total_seq = len(config.files_list)
    count = 0
    for line in config.files_list:
        seq_dir = line.rstrip('\n')
        count += 1
        print('Merging Sequence ', count, ' of ', total_seq, ' : ', seq_dir)

        # define paths
        input_path = config.DATA_DIR + seq_dir + '_oxts/data'
        output_path = config.OUTPUT_DIR + '/imu_data/' + seq_dir + '_imu.txt'
        timestamp_path = config.DATA_DIR + seq_dir + '_oxts/timestamps.txt'

        # merge the IMU data files into a single file
        imu_files_utils.concat_imu_files(input_path, output_path)

        # read the merged file into pandas dataframe
        imu_file_content = imu_files_utils.read_imu_file_content(output_path)

        # read timestamps file
        timestamps_file_content = imu_files_utils.read_timestamps_file(timestamp_path)

        # concatenate both data frames into a single data frame
        imu_timestamped_df = pd.concat([timestamps_file_content, imu_file_content], axis=1)

        # Save concatenated data frame as hdf5 file
        imu_timestamped_df.to_hdf(config.OUTPUT_DIR + 'imu_timestamp_df/' + seq_dir + '_df.h5', 'data')


# ========================================================================================================
def download_seq(seq_name):
    print('=> Downloading', seq_name)
    url = "https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/"+seq_name+"/"+seq_name+"_sync.zip"
    filename = wget.download(url, '../../../data/'+seq_name+'.zip', bar=bar_custom)
    print("\n----", seq_name, ' Downloaded !')


# ========================================================================================================
def bar_custom(current, total, width=80):
    progress_message = "---- Downloading: %d%% [%d / %d] MegaBytes" % (current / total * 100, current/1e6, total/1e6)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()
