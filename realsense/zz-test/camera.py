import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import json

o3d.t.io.RealSenseSensor.list_devices()

config_filename = "camera_config.json"
bag_filename = "zz_test.bag"

with open(config_filename) as cf:
    rs_cfg = o3d.t.io.RealSenseSensorConfig(json.load(cf))

rs = o3d.t.io.RealSenseSensor()
rs.init_sensor(rs_cfg, 0, bag_filename)
rs.start_capture(True)  # true: start recording with capture
for fid in range(150):
    im_rgbd = rs.capture_frame(True, True)  # wait for frames and align them
    # process im_rgbd.depth and im_rgbd.color

rs.stop_capture()

