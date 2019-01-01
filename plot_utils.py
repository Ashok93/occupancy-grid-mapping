import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot2D_scatter(velo_pts, veh_pt):
    print("Vehicle Pose \n" + str(veh_pt))
    fig = plt.figure(1)
    plt.axis('equal')
    plt.scatter(velo_pts[:,0], velo_pts[:,1],c='m',s=10,edgecolors='none')
    plt.scatter(veh_pt[0], veh_pt[1], s=20)
    plt.show()

def plot3D_scatter(velo_pts, veh_pt):
    velo_range = range(0, velo_pts.shape[0], 300)
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(velo_pts[velo_range,0], velo_pts[velo_range,1],velo_pts[velo_range,2],c='m',s=10,edgecolors='none')
    ax.scatter(veh_pt[0], veh_pt[1], veh_pt[2], s=20)
    plt.show()

def mayavi_viz3D(velo_pts, veh_pts):
    from mayavi import mlab
    velo_data = velo_pts
    point_w = veh_pts
    
    velo = velo_data[0]
    old_pose = point_w[0]
    x = old_pose[0]
    y = old_pose[1]
    z = old_pose[2]

    plt_point_cloud = mlab.points3d(
        velo[:, 0],   # x
        velo[:, 1],   # y
        velo[:, 2],   # z
        mode="point", # How to render each point {'point', 'sphere' , 'cube' }
        colormap='spectral',  # 'bone', 'copper',
        scale_factor=100,     # scale of the points
        line_width=10,        # Scale of the line, if any
    )

    mlab.axes(xlabel='x', ylabel='y', zlabel='z',ranges=(0,10000,0,10000,0,22),nb_labels=10)

    plt_vehicle = mlab.points3d(
        x,   # x
        y,   # y
        z,   # z
        mode="sphere", # How to render each point {'point', 'sphere' , 'cube' }
        colormap='copper',  # 'bone', 'copper',
        scale_factor=10,     # scale of the points
        line_width=5,        # Scale of the line, if any
    )

    @mlab.animate(delay = 300)
    def anim(old_pose):
        for idx in range(len(velo_data)):
            new_pose = point_w[idx]
            x = new_pose[0]
            y = new_pose[1]
            z = new_pose[2]
            velo = velo_data[idx] + new_pose
            plt_point_cloud.mlab_source.reset(x=velo[:, 0], y=velo[:, 1], z=velo[:, 2])
            plt_vehicle.mlab_source.reset(x=x, y=y, z=z)
            old_pose = new_pose
            yield

    anim(old_pose)
    mlab.show()

