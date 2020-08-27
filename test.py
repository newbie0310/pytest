import tensorflow as tf
tf.app.flags.DEFINE_string('gpus', None, 'gpus to use')
tf.app.flags.DEFINE_integer('batch_size', 5, 'batch size')

FLAGS = tf.app.flags.FLAGS

def main(_):
    print(FLAGS.gpus)
    print(FLAGS.batch_size)

if __name__=="__main__":
    tf.app.run()