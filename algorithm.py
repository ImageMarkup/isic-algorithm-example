import os
import random

random.seed(90210)

diseases = ['MEL', 'NV', 'BCC', 'AKIEC', 'BKL', 'DF', 'VASC']


def my_algorithm(image):
    return [random.random() for _ in range(len(diseases))]


# print headers
print(','.join(['image'] + diseases))

# print scores for each image
for input_file in os.listdir('/images'):
    scores = my_algorithm(input_file)
    print(','.join([input_file] + [str(x) for x in scores]))
