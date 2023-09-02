import tensorflow as tf
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = [9, 6]
x = tf.linspace(-2, 2,201)
x = tf.cast(x, tf.float32)
print("x values:")
#print (x)

def f(x):
  y = x**2 + 2*x - 5
  return y

#error is found randomly added to y
p = tf.random.normal(shape=[201])
print("y ERROR values:")
#print (p)

print("y values :")
#print (f(x))

y = f(x) + p
print("y values added with error:")
#print (y)

plt.plot(x.numpy(), y.numpy(), '.', label='Data')
plt.plot(x, f(x), label='Ground truth')
plt.legend();
plt.show()

class Model(tf.Module):

  def __init__(self):
    # Randomly generate weight and bias terms
    rand_init = tf.random.uniform(shape=[3], minval=0., maxval=5., seed=22)
    # Initialize model parameters
    self.w_q = tf.Variable(rand_init[0])
    self.w_l = tf.Variable(rand_init[1])
    self.b = tf.Variable(rand_init[2])

  @tf.function
  def __call__(self, x):
    # Quadratic Model : quadratic_weight * x^2 + linear_weight * x + bias
    return self.w_q * (x**2) + self.w_l * x + self.b

quad_model = Model()
print ("iNITIAL VALUES OF WATCH VARIABLES")
# print (quad_model.w_q)
# print (quad_model.w_l)
# print (quad_model.b)
print (quad_model.variables)
print (quad_model(40))
print ("--------")
def plot_preds(x, y, f, model, title):
  plt.figure()
  plt.plot(x, y, '.', label='Data')
  plt.plot(x, f(x), label='Ground truth')
  plt.plot(x, model(x), label='Predictions')
  plt.title(title)
  plt.legend()
  plt.show()

plot_preds(x, y, f, quad_model, 'Before training')

def mse_loss(y_pred, y):
  return tf.reduce_mean(tf.square(y_pred - y))

batch_size = 60
#x is actual x-vlaiues and y = f(x) + error
dataset = tf.data.Dataset.from_tensor_slices((x, y))
#print (dataset)
#it shuffle list of 32 items -- there will be 7 lists
dataset = dataset.shuffle(buffer_size=x.shape[0]).batch(batch_size)
#print (dataset)

# Set training parameters
epochs = 100
# we need to understand what is learning rate
learning_rate = 0.01
losses = []

# Format training loop
#epoch loop runs 100 times - each times it uses 201 items (32*7 - 23)
for epoch in range(epochs):

#grade printed 7 times- this is 7times loop
  for x_batch, y_batch in dataset:
    with tf.GradientTape() as tape:
      #x_batch has 32 x values and y_batch has corresponding 32 y values+err
      #batch_loss = mse_loss(quad_model(x_batch), y_batch)
      batch_loss = tf.reduce_mean(tf.square(quad_model(x_batch) - y_batch))
    # Update parameters with respect to the gradient calculations
    # x_batch and y_batch has 32 items
    # you need to understand this
    grads = tape.gradient(batch_loss, quad_model.variables)
    print ("grades")
    print (grads)
    print("learning_rate*g")
    #there are three variables in grade - a,b,c
    for g,v in zip(grads, quad_model.variables):
      print(learning_rate*g)
      v.assign_sub(learning_rate*g)

    print ("variables")
    print (quad_model.variables)
  # Keep track of model loss per epoch
  loss = mse_loss(quad_model(x), y)
  losses.append(loss)
  print(f'Mean squared error for step {epoch}: {loss.numpy():0.3f}')

#after training modal is it posible to print modal variable .. save  modal
print ("FINAL VALUES OF WATCH VARIABLES")
print (quad_model.w_q)
print (quad_model.w_l)
print (quad_model.b)
print (quad_model.variables)
print (quad_model(40))
print ("--------")

# Plot model results
print("\n")
plt.plot(range(epochs), losses)
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error (MSE)")
plt.title('MSE loss vs training iterations')

plot_preds(x, y, f, quad_model, 'After training')
