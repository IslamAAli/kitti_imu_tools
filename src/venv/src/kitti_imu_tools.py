# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import config
import files_utils
import file_tools
import sequence_utils


def main():

    config.pandas_config()
    sequence_utils.download_all_sequences()


    # input_path = "../../../data/oxts/data"
    # output_path = '../../../output/test.txt'
    # files_utils.concat_imu_files(input_path, output_path)
    #
    # file_content = file_tools.read_file_content(output_path)
    # print(file_content)


if __name__ == "__main__":
    main()
