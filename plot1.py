import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]

import tensorflow as tf
x = tf.linspace(-2, 2, 201)
x = tf.cast(x, tf.float32)
print (x)
def f(x):
  y = x**2 + 2*x - 5
  return y

y = f(x) + tf.random.normal(shape=[201])

z = tf.linspace(-4, 4, 401)
z = tf.cast(z, tf.float32)
z1 = f(z)+ tf.random.normal(shape=[401])

plt.plot(x, y, '.', label='Data')
plt.plot(x, f(x), label='Ground truth')
plt.legend()
plt.show()

def plot_preds(x, y, model, title):
  plt.figure()
  plt.plot(x, y, '.', label='Data2')
  plt.plot(x, f(x), label='Ground truth')
  plt.plot(x, model(x), label='Predictions')
  plt.title(title)
  plt.legend()
  plt.show()


# new_model = tf.keras.Sequential([
#     tf.keras.layers.Lambda(lambda x: tf.stack([x, x**2], axis=1)),
#     tf.keras.layers.Dense(units=1, kernel_initializer=tf.random.normal)])

new_model = tf.keras.Sequential()
new_model.add(tf.keras.layers.Lambda(lambda x: tf.stack([x, x**2],axis=1)))
new_model.add(tf.keras.layers.Dense(units=1, kernel_initializer=tf.random.normal))

new_model.compile(
    loss=tf.keras.losses.MSE,
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01))

history = new_model.fit(x, y,
                        epochs=100,
                        batch_size=32,
                        verbose=2)

new_model.save('my_model2')

plot_preds(x, y, new_model, 'After Training: Keras')

plt.plot(z, f(z), label='Ground truth')
plt.plot(z, z1,'.', label='New Distribution')
plt.plot(z, new_model(z), label='Predictions')
plt.legend()
plt.show()
