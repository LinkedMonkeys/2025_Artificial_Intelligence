import random
import copy


# Applies the hypothesis function to the point, given the weights.
def h(weights, data_point):
    new_data_point = [1] + data_point
    # new_data_point = copy.copy(data_point)
    # new_data_point.insert(0, 1) # Add a data item to match w_0.
    dot_product = 0
    for i in range(len(weights)):
        dot_product += weights[i]*float(new_data_point[i])

    return 1 if dot_product>=0 else 0

# Adjusts the weights if currently a bad prediction (matches classification).
def adjust_weights(weights, data_point, classification):
    new_data_point = [1] + data_point
    alpha = .1
    prediction = h(weights, data_point)
    # TODO: Do we need this if?
    if not(prediction==1 and classification==data_point[-1] or prediction==0 and classification!=data_point[-1]):
        y = 1 if classification==data_point[-1] else 0 # Is this data point what we are looking for?
        for i in range(len(weights)):
            weights[i] = weights[i] + alpha * (y - prediction) * float(new_data_point[i])

def train(weights, training_data, classification):
    for data_point in training_data:
        adjust_weights(weights, data_point, classification)

def run_test_data(weights, test, classification):
    correct_count = 0
    for data_point in test:
        prediction = h(weights, data_point)
        if prediction==1 and classification==data_point[-1] or prediction==0 and classification!=data_point[-1]:
            correct_count += 1
    print(correct_count)

#########################################################
with open('training.txt', 'r') as file:
    training = [line.strip().split(',') for line in file]

with open('test.txt', 'r') as file:
    test = [line.strip().split(',') for line in file]

weights = []
for i in range(len(training[0])):
    weights.append(random.uniform(-10, 10))

# classification = 'Iris-setosa'
# classification = 'Iris-versicolor'
classification = 'Iris-virginica'

train(weights, training, classification)

run_test_data(weights, test, classification)
