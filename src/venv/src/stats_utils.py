import config
import pandas as pd


def read_hdf_file(file_name):
    file_content = pd.read_hdf(file_name)
    return file_content


def read_all_hdf_files():
    # get the list of file
    stats_list = []
    count = 0
    total_seq = len(config.files_list)
    for line in config.files_list:
        count += 1
        seq_name = line.rstrip('\n')
        hdf_file_path = config.OUTPUT_DIR + "imu_timestamp_df/" + seq_name + "_df.h5"
        hdf_file_content = read_hdf_file(hdf_file_path)
        stats_list.append([
            # Accelerations
            hdf_file_content["ax"].max(),
            hdf_file_content["ax"].min(),
            hdf_file_content["ax"].median(),
            hdf_file_content["ax"].mean(),

            hdf_file_content["ay"].max(),
            hdf_file_content["ay"].min(),
            hdf_file_content["ay"].median(),
            hdf_file_content["ay"].mean(),

            hdf_file_content["az"].max(),
            hdf_file_content["az"].min(),
            hdf_file_content["az"].median(),
            hdf_file_content["az"].mean(),

            # Angular Velocities
            hdf_file_content["wx"].max(),
            hdf_file_content["wx"].min(),
            hdf_file_content["wx"].median(),
            hdf_file_content["wx"].mean(),

            hdf_file_content["wy"].max(),
            hdf_file_content["wy"].min(),
            hdf_file_content["wy"].median(),
            hdf_file_content["wy"].mean(),

            hdf_file_content["wz"].max(),
            hdf_file_content["wz"].min(),
            hdf_file_content["wz"].median(),
            hdf_file_content["wz"].mean(),

            # Velocities
            hdf_file_content["vn"].max(),
            hdf_file_content["vn"].min(),
            hdf_file_content["vn"].median(),
            hdf_file_content["vn"].mean(),

            hdf_file_content["ve"].max(),
            hdf_file_content["ve"].min(),
            hdf_file_content["ve"].median(),
            hdf_file_content["ve"].mean(),

            hdf_file_content["vf"].max(),
            hdf_file_content["vf"].min(),
            hdf_file_content["vf"].median(),
            hdf_file_content["vf"].mean(),

            # Orientation
            hdf_file_content["roll"].max(),
            hdf_file_content["roll"].min(),
            hdf_file_content["roll"].median(),
            hdf_file_content["roll"].mean(),

            hdf_file_content["pitch"].max(),
            hdf_file_content["pitch"].min(),
            hdf_file_content["pitch"].median(),
            hdf_file_content["pitch"].mean(),

            hdf_file_content["yaw"].max(),
            hdf_file_content["yaw"].min(),
            hdf_file_content["yaw"].median(),
            hdf_file_content["yaw"].mean(),
        ])
    config.stats_df = pd.DataFrame(stats_list, columns=['ax_max', 'ax_min', 'ax_median', 'ax_mean',
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

    print(config.stats_df)
    # saving the stats to an hd5 file
    config.stats_df.to_hdf(config.OUTPUT_DIR + 'stats/KITTI_stats.h5', 'data')
