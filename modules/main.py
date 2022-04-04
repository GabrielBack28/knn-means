# Gabriel Back
import os
from utils import read_file_data
from cluster import find_cluster
from mean import calculate_means

currentDir = os.path.dirname(__file__)
filePath = os.path.join(currentDir, 'dataset.txt')
items = read_file_data(filePath)

means = calculate_means(3, items)
clusters = find_cluster(means, items)

def generic_print(text, genericItem):
  for i in range(len(genericItem)):
    print(f"{text} {str(i)}: {str(genericItem[i])}")

print("################## Items ##################")
generic_print('Item', items)
print()

print('################## Means ##################')
generic_print('Mean', means)
print()

print('################## Clusters ##################')
for i in range(len(clusters)):
    print(f"Cluster {str(i)}:")
    for j in range(len(clusters[i])):
      print(f"Item {str(j)}: {str(clusters[i][j])}")
    print()