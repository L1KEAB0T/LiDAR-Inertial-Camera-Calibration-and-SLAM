import rosbag
from rospy import Time

# 打开原始 bag 文件和目标 bag 文件
input_bag = rosbag.Bag('test5.bag', 'r')
output_bag = rosbag.Bag('output.bag', 'w')

# 获取 bag 文件的起始时间
start_time = input_bag.get_start_time()

# 设置时间截取点为 4 秒（相对于 bag 文件的起始时间）
end_time = start_time + 4.0

# 遍历消息
for topic, msg, t in input_bag.read_messages():
    if t.to_sec() <= end_time:
        output_bag.write(topic, msg, t)
    else:
        break

input_bag.close()
output_bag.close()

print("Bag file processing complete!")
