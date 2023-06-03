import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]

import tensorflow as tf
x = tf.linspace(-8, 8, 101)
x = tf.cast(x, tf.float32)

def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[101])

def plot_preds(x, y, model, title):
  plt.figure()
  plt.plot(x, y, '.', label='Data')
  plt.plot(x, f(x), label='Ground truth')
  plt.plot(x, model(x),'.', label='Predictions')
  plt.title(title)
  plt.legend()
  plt.show()

# new_model = tf.keras.Sequential()
# new_model.add()
# new_model.load_weights('new_model.h5')

new_model = tf.keras.models.load_model("my_model")

plot_preds(x, y, new_model, 'After Training: Keras')

plt.legend()
plt.show()
