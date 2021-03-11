import pandas as pd
import numpy
import config
import matplotlib.pyplot as plt


# =================================================================================================
def read_stats_file(file_name):
    file_content = pd.read_hdf(file_name)
    return file_content


# =================================================================================================
def visualize_stats():
    KITTI_stats = read_stats_file(config.OUTPUT_DIR + 'stats/KITTI_stats.h5')

    # [1] plot accelerometer  data
    limit = 20
    plot_data_item(KITTI_stats['ax_max'],
                   KITTI_stats['ax_min'],
                   KITTI_stats['ax_mean'],
                   'Acceleration - x',
                   'Acceleration (m/sec^2)', [-limit, limit])

    plot_data_item(KITTI_stats['ay_max'],
                   KITTI_stats['ay_min'],
                   KITTI_stats['ay_mean'],
                   'Acceleration - y',
                   'Acceleration (m/sec^2)', [-limit, limit])

    plot_data_item(KITTI_stats['az_max'],
                   KITTI_stats['az_min'],
                   KITTI_stats['az_mean'],
                   'Acceleration - z',
                   'Acceleration (m/sec^2)', [-limit, limit])

    # ===========================================================================
    # [2] plot gyroscope data
    limit = 50
    plot_data_item(KITTI_stats['wx_max']*(180/numpy.pi),
                   KITTI_stats['wx_min']*(180/numpy.pi),
                   KITTI_stats['wx_mean']*(180/numpy.pi),
                   'Angular Velocity - x',
                   'Angular Velocity (deg/sec)', [-limit, limit])

    plot_data_item(KITTI_stats['wy_max']*(180/numpy.pi),
                   KITTI_stats['wy_min']*(180/numpy.pi),
                   KITTI_stats['wy_mean']*(180/numpy.pi),
                   'Angular Velocity - y',
                   'Angular Velocity (deg/sec)', [-limit, limit])

    plot_data_item(KITTI_stats['wz_max']*(180/numpy.pi),
                   KITTI_stats['wz_min']*(180/numpy.pi),
                   KITTI_stats['wz_mean']*(180/numpy.pi),
                   'Angular Velocity - z',
                   'Angular Velocity (deg/sec)', [-limit, limit])

    # ===========================================================================
    # [3] plot velocity data
    limit = 50
    plot_data_item(KITTI_stats['vx_max'],
                   KITTI_stats['vx_min'],
                   KITTI_stats['vx_mean'],
                   'Velocity - x',
                   'Velocity (m/sec)', [-limit, limit])

    plot_data_item(KITTI_stats['vy_max'],
                   KITTI_stats['vy_min'],
                   KITTI_stats['vy_mean'],
                   'Velocity - y',
                   'Velocity (m/sec)', [-limit, limit])

    plot_data_item(KITTI_stats['vz_max'],
                   KITTI_stats['vz_min'],
                   KITTI_stats['vz_mean'],
                   'Velocity - z',
                   'Velocity (m/sec)', [-limit, limit])

    # ===========================================================================
    # [3] plot orientation data
    limit = 20
    plot_data_item(KITTI_stats['rx_max']*(180/numpy.pi),
                   KITTI_stats['rx_min']*(180/numpy.pi),
                   KITTI_stats['rx_mean']*(180/numpy.pi),
                   'Orientation - roll',
                   'Orientation (deg)', [-limit, limit])

    plot_data_item(KITTI_stats['py_max']*(180/numpy.pi),
                   KITTI_stats['py_min']*(180/numpy.pi),
                   KITTI_stats['py_mean']*(180/numpy.pi),
                   'Orientation - pitch',
                   'Orientation (deg)', [-limit, limit])

    plot_data_item(KITTI_stats['yz_max']*(180/numpy.pi),
                   KITTI_stats['yz_min']*(180/numpy.pi),
                   KITTI_stats['yz_mean']*(180/numpy.pi),
                   'Orientation - yaw',
                   'Orientation (deg)', [-200, 200])


# =================================================================================================
def plot_data_item(max_list, min_list, avg_list, title, y_axis, y_lim):
    x = range(0 , 151)
    plt.figure(figsize=(15, 8))
    plt.title(title)
    plt.ylim(y_lim)

    plt.plot(x, avg_list, linestyle='dashed')
    plt.plot(x, max_list, color='k', alpha=0.2)
    plt.plot(x, min_list, color='k', alpha=0.2)
    plt.fill_between(x, min_list, max_list, color='k', alpha=0.1)

    plt.axhline(y=max(max_list), color='r', linestyle='dashed')
    plt.axhline(y=min(min_list), color='r', linestyle='dashed')

    # plt.axhline(y=100, color='g', linestyle='dashed')
    # plt.axhline(y=-100, color='g', linestyle='dashed')
    plt.text(90, max(max_list) + 0.1, 'Max. ' + y_axis + ' = ' + str(round(max(max_list), 2)), weight="bold")
    plt.text(90, min(min_list) + 0.1, 'Min. ' + y_axis + ' = ' + str(round(min(min_list), 2)), weight="bold")

    plt.legend(["Mean Value"], loc="upper right")
    plt.xlabel('Sequence #')
    plt.ylabel(y_axis)
    plt.grid()
    plt.savefig(config.OUTPUT_DIR+'figs/'+title+'.png')
    plt.show()

