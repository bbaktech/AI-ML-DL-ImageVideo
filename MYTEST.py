import tensorflow as tf
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]
x = tf.linspace(-2, 2,201)
x = tf.cast(x, tf.float32)
print("x values:")
print (x)

def f(x):
  y = x**2 + 2*x
  return y

#error is found randomly added to y
p = tf.random.normal(shape=[201])
print("y ERROR values:")
print (p)

print("y values :")
print (f(x))

y = f(x) + p
print("y values added with error:")
print (y)

learning_rate = 0.01
w_q = tf.Variable([4.3870,1.4291])

print ("w_q")
print (w_q)

epochs = 10
for epoch in range(epochs):
    print ("epoch")
    print (epoch)

    y_pred = w_q[0] * (x**2) + w_q[1] * x
    print ("y predect")
    print (y_pred)

    sqr_v = tf.square(y_pred - y)
    mse_v = tf.reduce_mean(sqr_v)

    print ("MSE:")
    print (mse_v)

    with tf.GradientTape() as tape:
        batch_loss = tf.reduce_mean(tf.square( (w_q[0] * (x**2) + w_q[1] * x) - y))

    grads = tape.gradient(batch_loss, w_q)

    # print ("lr *grads")
    # print (learning_rate*grads)
    w_q.assign(learning_rate*grads)

    print ("w_q")
    print (w_q)

def plot_preds(x, y, f, yp, title):
  plt.figure()
  plt.plot(x, y, '.', label='Data')
  plt.plot(x, f(x), label='Ground truth')
  plt.plot(x, yp, label='Predictions')
  plt.title(title)
  plt.legend()
  plt.show()

plot_preds(x, y, f, y_pred, "after learning")
