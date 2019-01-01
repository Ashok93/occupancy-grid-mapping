# Occupancy Grid Mapping in Python - KITTI Dataset 

An occupancy grid mapping implemented in python using KITTI raw dataset - http://www.cvlibs.net/datasets/kitti/raw_data.php

### Dependencies
1. Pykitti - For reading and parsing the dataset from KITTI - https://github.com/utiasSTARS/pykitti
2. numpy
3. matplotlib
4. mayavi (if required for visualization)

Make sure to add the dataset downloaded from http://www.cvlibs.net/datasets/kitti/raw_data.php into a folder in the working directory. Please check and modify the `get_kitti_dataset` function in `main.py`.

Run `python main.py`

Used `bresenhan_nd.py` - the bresenhan algorithm from http://code.activestate.com/recipes/578112-bresenhams-line-algorithm-in-n-dimensions/