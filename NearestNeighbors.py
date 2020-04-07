import csv
import math

sum_height = 0.0
sum_weight = 0.0
with open('train.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    num_lines = 0

    training_list = []
    for row in reader:
        if num_lines != 0:
           inner_list = [row[1][0:len(row[1])], float(row[2][0:len(row[2])]), float(row[3])]
           training_list.append(inner_list)
           sum_height += float(row[2][0:len(row[2])])
           sum_weight += float(row[3])

        num_lines += 1

with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    num_lines = 0

    test_list = []
    for row in reader:
       if num_lines != 0:
           inner_list = [row[1][0:len(row[1])], float(row[2][0:len(row[2])]), float(row[3])]
           test_list.append(inner_list)

       num_lines += 1

test_index = 0
num_wrong = 0.0
std_test_index = 0
std_num_wrong = 0.0
mean_height = sum_height / len(training_list)
mean_weight = sum_weight / len(training_list)
stdev_height = math.sqrt(sum([((x[1] - mean_height) ** 2) for x in training_list]) / len(training_list))
stdev_weight = math.sqrt(sum([((x[2] - mean_weight) ** 2) for x in training_list]) / len(training_list))

std_test_list = []
std_training_list = []
for i in range(len(training_list)):
    std_training_list.append([training_list[i][0],(training_list[i][1] - mean_height) / stdev_height,(training_list[i][2] - mean_weight) / stdev_weight])
for i in range(len(test_list)):
    std_test_list.append([test_list[i][0],(test_list[i][1] - mean_height) / stdev_height,(test_list[i][2] - mean_weight) / stdev_weight])


for point in std_test_list:
    dist = []

    for data in std_training_list:
        dist.append(math.sqrt((point[1] - data[1]) ** 2 + (point[2] - data[2]) ** 2))

    min = dist[0]
    min_index = 0
    index = 0
    correct = False

    for i in dist:
        if i < min:
            min = i
            min_index = index
        index += 1

    if std_training_list[min_index][0] == point[0]:
        correct = True
    else:
        std_num_wrong += 1.0
    std_test_index += 1


for point in test_list:
    dist = []

    for data in training_list:
        dist.append(math.sqrt((point[1] - data[1]) ** 2 + (point[2] - data[2]) ** 2))

    min = dist[0]
    min_index = 0
    index = 0
    correct = False

    for i in dist:
        if i < min:
            min = i
            min_index = index
        index += 1

    if training_list[min_index][0] == point[0]:
        correct = True
    else:
        num_wrong += 1.0
    test_index += 1

error = num_wrong / len(test_list)
std_error = std_num_wrong / len(std_test_list)
print('Error: {} || Standardized Error: {}'.format(error, std_error))
