import os
import random
import sys

random.seed(90210)

diagnoses = ['MEL', 'NV', 'BCC', 'AK', 'BKL', 'DF', 'VASC', 'SCC', 'UNK']


def my_algorithm(image):
    return [random.random() for _ in range(len(diagnoses))]


if not os.path.exists('/images'):
    print('The directory /images does not exist, did you forget to mount it?', file=sys.stderr)
    sys.exit(1)

# print headers
print(','.join(['image'] + diagnoses))

# print scores for each image
for input_file in os.listdir('/images'):
    if input_file.endswith('.jpg'):
        scores = my_algorithm(input_file)
        print(','.join([input_file.replace('.jpg', '')] + [str(x) for x in scores]))
