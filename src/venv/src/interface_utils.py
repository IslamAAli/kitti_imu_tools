import sequence_utils
import stats_utils
import visualization_utils
import sys


def main_menu():
    print('----------------------------')
    print('>> Select an options:')
    print('----------------------------')
    print('[1] Download and Extract IMU Data')
    print('[2] Merge IMU Files')
    print('[3] Calculate Stats')
    print('[4] Visualize Stats')
    print('[5] Exit')


def option_selector(m_selection):
    print('\n\n')
    print('----------------------------')
    if m_selection == "1":
        print('[Selected] [1] Download and Extract IMU Data\n')
        sequence_utils.download_all_sequences()
        wait_key_fn()

    elif m_selection == "2":
        print('[Selected] [2] Merge IMU Files\n')
        sequence_utils.merge_files()
        wait_key_fn()

    elif m_selection == "3":
        print('[Selected] [3] Calculate Stats\n')
        stats_utils.read_all_hdf_files()
        wait_key_fn()

    elif m_selection == "4":
        print('[Selected] [4] Visualize Stats\n')
        visualization_utils.visualize_stats()
        wait_key_fn()

    elif m_selection == "5":
        sys.exit()

    else:
        print('[**Error**] Select a Valid Option !\n')


def wait_key_fn():
    input('\n[--INFO--] Press Any Key to Continue !\n\n')

