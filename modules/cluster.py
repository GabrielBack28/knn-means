from utils import classify

def find_cluster(means, items):
  clusters = [[] for i in range(len(means))]
  for item in items:
    index = classify(means, item)
    clusters[index].append(item)
  return clusters