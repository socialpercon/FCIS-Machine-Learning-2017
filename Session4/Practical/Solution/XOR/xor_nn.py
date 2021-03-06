import tensorflow as tf
import matplotlib.pyplot as plt #we will use it to draw the learning curve after training the network

train_x = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
train_y = [[0], [1], [1], [0]]

INPUT_NEURONS = 2
HIDDEN_NEURONS = 3
OUTPUT_NEURONS = 1

NUM_OF_EPOCHS = 100000

"""(tf.float32, [None, 2]) specifies the datatype and the dimensions of the data.
#Since we don't know the number of the training data, we make it None which means it accepts any from the user.
#2 specifies that we have 2 input bits
"""
x = tf.placeholder(tf.float32, [None, 2])
y_target = tf.placeholder(tf.float32, [None, 1])

"""
1- Create the Input-to-hidden weights and bias matrices from the given figure.
They should be Variable datatype because they will be changed during the learning process
"""
input_hidden_weights = tf.Variable([[-0.99, 1.05, .19], [-0.43, -0.44, -0.30]]) #Init. from the given network
input_hidden_bias = tf.Variable(tf.ones([HIDDEN_NEURONS])) # The bias is one for each hidden neuron

"""
2- Get the values of the hidden layer by multiplying the features with the weight matrix [Input to Hidden feedforward]
Apply the hidden layer activation to the multiplication result
"""
hidden_neurons_values = tf.matmul(x, input_hidden_weights) + input_hidden_bias
hidden_activation_result = tf.nn.sigmoid(hidden_neurons_values)

"""
3- Create the hidden-to-output weights and bias matrices from the given figure.
They should be Variable datatype because they will be changed during the learning process
"""

hidden_output_weights = tf.Variable([[0.18], [1.11], [-0.26]])
hidden_output_bias = tf.Variable(tf.ones([1]))

"""
4- Get the values of the output layer by multiplying the hidden layer with the weight matrix [Hidden to Output feedforward]
Apply the output layer activation to the multiplication result
"""

hidden_output_value = tf.matmul(hidden_activation_result, hidden_output_weights) + hidden_output_bias
y_estimated = tf.nn.sigmoid(hidden_output_value)


"""
5- Calculate the mean squared error given your prediction and the actual output
"""

mean_squared_error = 0.5 * tf.reduce_sum((tf.square(y_estimated - y_target)))

train = tf.train.GradientDescentOptimizer(0.1).minimize(mean_squared_error)


"""
Initiate a Tensorflow graph and session variables
"""
session = tf.Session()
session.run(tf.initialize_all_variables())

errors = []
epochs = []

for i in range(0, NUM_OF_EPOCHS):
    session.run(train, feed_dict={x: train_x, y_target: train_y})

    if i % 10 == 0:
        print("Iteration number: ", i, "\n")
        error = session.run(mean_squared_error, feed_dict={x: train_x, y_target: train_y})
        print("Cost: ", error, "\n")
        errors.append(error)
        epochs.append(i)

        if error < 0.01:
            print("Input to hidden Weights",
              session.run(input_hidden_weights, feed_dict={x: train_x, y_target: train_y}))
            print("Input to hidden bias",
              session.run(input_hidden_bias, feed_dict={x: train_x, y_target: train_y}))
            print("Hidden to output weight",
              session.run(hidden_output_weights, feed_dict={x: train_x, y_target: train_y}))
            print("Hidden to output bias",
              session.run(hidden_output_bias, feed_dict={x: train_x, y_target: train_y}))

            plt.title("Learning Curve using mean squared error cost function")
            print("Cost: ", error, "\n")
            plt.xlabel("Number of Epochs")
            plt.ylabel("Cost")
            plt.plot(epochs, errors)
            plt.show()

            break