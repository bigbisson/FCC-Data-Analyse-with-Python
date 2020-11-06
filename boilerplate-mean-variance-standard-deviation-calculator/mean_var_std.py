import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")
  else:
    calculations = {}
    data = np.array(list).reshape(3,3)
    
    means = [np.mean(data,axis=0).tolist(),np.mean(data,axis=1).tolist(),np.mean(data)]
    varian = [np.var(data,axis=0).tolist(),np.var(data,axis=1).tolist(),np.var(data)]
    stds = [np.std(data,axis=0).tolist(),np.std(data,axis=1).tolist(),np.std(data)]
    maxs = [np.max(data,axis=0).tolist(),np.max(data,axis=1).tolist(),np.max(data)]
    mins = [np.min(data,axis=0).tolist(),np.min(data,axis=1).tolist(),np.min(data)]
    sums = [np.sum(data,axis=0).tolist(),np.sum(data,axis=1).tolist(),np.sum(data)]
    calculations = {'mean':means,'variance':varian,'standard deviation':stds,'max':maxs,'min':mins,'sum':sums}

    return calculations