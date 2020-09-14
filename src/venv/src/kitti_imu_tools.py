# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import config
import files_utils
import file_tools
import sequence_utils
import interface_utils

def main():

    # Configuration
    config.pandas_config()

    # Menu Control
    while True:
        interface_utils.main_menu()
        selected_option = input('Your Selection is:  ')
        interface_utils.option_selector(selected_option)


    # input_path = "../../../data/oxts/data"
    # output_path = '../../../output/test.txt'
    # files_utils.concat_imu_files(input_path, output_path)
    #
    # file_content = file_tools.read_file_content(output_path)
    # print(file_content)


if __name__ == "__main__":
    main()
