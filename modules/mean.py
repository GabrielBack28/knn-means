import sys
from random import uniform
from utils import classify

def find_col_min_max(items):
    number = len(items[0])
    min = [sys.maxsize for i in range(number)]
    max = [-sys.maxsize -1 for i in range(number)]
    for item in items:
      for f in range(len(item)):
        if (item[f] < min[f]):
          min[f] = item[f]
        if (item[f] > max[f]):
          max[f] = item[f]
    return min, max

def initialize_means(items, k, column_min, column_max):
  features_length = len(items[0])
  means = [[0 for i in range(features_length)] for j in range(k)]
  for mean in means:
    for position in range(len(mean)):
      mean[position] = uniform(column_min[position] + 1, column_max[position] - 1)
  return means

def update_mean(n, means, item):
  for i in range(len(means)):
    mean = means[i]
    mean = (mean * (n-1) + item[i]) / float(n)
    means[i] = round(mean, 3)
  return means

def calculate_means(k, items, maxIterations=100000):
  column_min, column_max = find_col_min_max(items)
  means = initialize_means(items, k, column_min, column_max)
  cluster_sizes = [0 for i in range(len(means))]
  belongs_to = [0 for i in range(len(items))]
  for e in range(maxIterations):
    no_change = True
    for i in range(len(items)):
      item = items[i]
      index = classify(means, item)
      cluster_sizes[index] += 1
      cluster_size = cluster_sizes[index]
      means[index] = update_mean(cluster_size, means[index], item)
      if(index != belongs_to[i]):
        no_change = False
      belongs_to[i] = index
    if (no_change):
      break
  return means