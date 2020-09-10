from typing import List, Any, Union
import glob


def concat_imu_files(input_path):

    # read files names in a certain directory
    filenames = glob.glob(input_path+"/*.txt")

    # concatenate the content of the IMU/GNSS files
    with open('../../output/test.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())