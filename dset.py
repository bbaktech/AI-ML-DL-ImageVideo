import tensorflow as tf

x = tf.linspace(10, 20,2)
x = tf.cast(x, tf.float32)
print("x values:")
print (x)

def f(x):
    y = x**2 + 2*x - 5
    return y

print("y values :")
print (f(x))

batch_size = 1
dataset = tf.data.Dataset.from_tensor_slices((x, f(x)))
for element in dataset.as_numpy_iterator():
    print(element)

#find how it shuffle
dataset = dataset.shuffle(buffer_size=x.shape[0]).batch(batch_size)
for element in dataset.as_numpy_iterator():
    print(element)

w_q = tf.Variable([1.0,2.0,5.0])
w_l = tf.Variable(2.0)
b = tf.Variable(5.0)

with tf.GradientTape() as tape:
  grades = w_q[0] * (x**2) + w_q[1] * x + w_q[2]

# dy = 2x * dx
dy_dx = tape.gradient(grades, w_q)
print (dy_dx)
