import sys
import math
from random import shuffle

def read_file_data(filePath):
  file = open(filePath, 'r')
  lines = file.read().splitlines()
  file.close()
  items = []

  for i in range(1, len(lines)):
    line = lines[i].split(',')
    item_features = []
    for j in range(len(line)-1):
      feature_value = float(line[j])
      item_features.append(feature_value)
    items.append(item_features)

  shuffle(items)

  return items

def calculate_euclidean_distance(x, y):
  sum = 0
  for position in range(len(x)):
    sum += math.pow(x[position]-y[position], 2)
  return math.sqrt(sum)

def classify(means, item):
  min_distance = sys.maxsize
  index = -1
  for meanIndex in range(len(means)):
    distance = calculate_euclidean_distance(item, means[meanIndex])
    if (distance < min_distance):
      min_distance = distance
      index = meanIndex
  return index