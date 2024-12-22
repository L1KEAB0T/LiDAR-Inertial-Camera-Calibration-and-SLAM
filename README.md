# LiDAR-Inertial-Camera-Calibration-and-SLAM

## 项目依赖

ubuntu20.04

ros-neotic

## 配置过程

1. livox_camera_calib的安装

   参考 [livox_camera_calib](https://github.com/hku-mars/livox_camera_calib) 或 [Livox Camera Calib 安装和配置指南-CSDN博客](https://blog.csdn.net/gitblog_07500/article/details/142235221)

2. r3live 的安装

   参考 [hku-mars/r3live: A Robust, Real-time, RGB-colored, LiDAR-Inertial-Visual tightly-coupled state Estimation and mapping package](https://github.com/hku-mars/r3live)

## 使用说明

[livox_camera_calib](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/tree/main/livox_camera_calib)下的[bag_img_calib.launch](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/blob/main/livox_camera_calib/launch/bag_img_calib.launch)实现了从rosbag中提取点云实现自动化标定的过程

需要修改config下的[bag_img_calib.yaml](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/blob/main/livox_camera_calib/config/bag_img_calib.yaml)来适配

[r3live](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/tree/main/r3live)下的 [r3live_bag.launch](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/blob/main/r3live/r3live/launch/r3live_bag.launch) 已经被修改，和原作者的r3live_bag.launch相比增加了从rosbag中实现自动化外参标定的过程，实现了从rosbag中自动化外参标定然后自动SLAM的过程

从rosbag的提取图像和点云的功能还未加入自动化中，请使用[bag2img.py](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/blob/main/bag2img.py)和[bag_cut.py](https://github.com/L1KEAB0T/LiDAR-Inertial-Camera-Calibration-and-SLAM/blob/main/bag_cut.py)做rosbag做简单的预处理



