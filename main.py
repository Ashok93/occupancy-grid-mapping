import itertools
import numpy as np
import os
import pykitti

from occupancy_grid import Map
from plot_utils import plot2D_scatter, plot3D_scatter, mayavi_viz3D
from bresenhan_nd import bresenhamline

use_mayavi = False

def get_kitti_dataset():
    # Change this to the directory where you store KITTI data
    curr_dir_path = os.getcwd()
    basedir = curr_dir_path + '/kitti_data'

    # Specify the dataset to load
    date = '2011_09_26'
    drive = '0001'

    # Load the data. Optionally, specify the frame range to load.
    # dataset = pykitti.raw(basedir, date, drive)
    dataset = pykitti.raw(basedir, date, drive)

    return dataset


if __name__ == "__main__":

    dataset = get_kitti_dataset()
    velo_pts = list(dataset.velo)
    point_imu = np.array([0,0,0,1])
    vehicle_pts = [o.T_w_imu.dot(point_imu) for o in dataset.oxts]
    env_map = Map(500,500, resolution=1)

    # Mayavi Visualization
    if use_mayavi:
        point_w = [o.T_w_imu.dot(point_imu) for o in dataset.oxts]
        mayavi_viz3D(velo_pts, point_w)

    for idx, velo_pt in enumerate(velo_pts):
        # Adding some offset as some velo pts are in negative. This offset is applied to every pt.
        veh_pt = vehicle_pts[idx] + 200
        velo_pt = veh_pt + velo_pt

        env_map.set_vehicle_pose(veh_pt)
        # plot2D_scatter(velo_pt, veh_pt)

        print("Processing point cloud data... \n")
        for pt in velo_pt[::50]:
            if (pt < 300).all():
                env_map.update_log_odds(pt[1], pt[0], occupied=True)
                start_pt = np.array([[int(veh_pt[0]), int(veh_pt[1])]])
                end_pt = np.array([[int(pt[0]), int(pt[1])]])
                bresenham_path = bresenhamline(start_pt, end_pt, max_iter=-1)

                for bres_pt in bresenham_path:
                    env_map.update_log_odds(bres_pt[1], bres_pt[0], occupied=False)

    env_map.visualize()