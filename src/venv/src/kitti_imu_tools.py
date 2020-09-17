# ---------------------------------------
# Author: Islam A. Ali
# KITTI IMU Tools (v1p0)
# ---------------------------------------

import config
import imu_files_utils
import file_tools
import sequence_utils
import interface_utils


def main():

    # Configuration
    config.app_init()

    # Menu Control
    while True:
        interface_utils.main_menu()
        selected_option = input('\n[*] Your Selection is:  ')
        interface_utils.option_selector(selected_option)


if __name__ == "__main__":
    main()
