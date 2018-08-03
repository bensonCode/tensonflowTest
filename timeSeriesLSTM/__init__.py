import tensorflow as tf
import time
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

now = time.ctime(int(time.time()))
print(str(now))