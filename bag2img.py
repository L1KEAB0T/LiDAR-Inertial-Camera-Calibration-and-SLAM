# coding:utf-8
#!/usr/bin/python
# Extract images from a bag file.

import rospy
import rosbag
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import os

output_path = '/mnt/d/multi_source_slam/image/'  # 替换为保存图像的目录路径
frame_interval = 10  # 提取图像的帧间隔

# 初始化 ROS 节点
rospy.init_node('image_extractor', anonymous=True)

class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        frame_count = 0
        if not os.path.exists(output_path):  # 确保保存图像的路径存在
            os.makedirs(output_path)

        with rosbag.Bag('/mnt/d/multi_source_slam/test5.bag', 'r') as bag:  # 要读取的bag文件路径
            for topic, msg, t in bag.read_messages():
                #print("Reading topic: {} at time {}".format(topic, t.to_sec()))
                if topic == "/camera/color/image_raw/compressed":  # 图像的topic
                    if frame_count % frame_interval == 0:  # 每隔frame_interval帧提取一次
                        try:
                            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding='passthrough')
                        except CvBridgeError as e:
                            print(e)
                        filename = "{}.jpg".format(t.to_nsec())  # 使用时间戳作为文件名
                        save_path = output_path + filename
                        cv2.imwrite(save_path, cv_image)  # 保存图像
                        print("Saved image: {}".format(save_path))
                    frame_count += 1

if __name__ == '__main__':
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
