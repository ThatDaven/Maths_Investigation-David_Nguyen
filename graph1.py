from numbergen import *
from matplotlib import pyplot as plt
lst = [
  170.11,169.39,176.69,178.1,172.7,184.9,175.03,176.32,170.95,168.55,168.25,181.62,171.61,164.03,181.88,157.07,170.53,168.47,179.99,166.68,176.26,165.37,171.03,152.77,168.69,173.94,177.78,181.89,161.16,172.77,157.56,176.74,182.63,153.48,164.48,191.72,155.57,169.55,161.72,162.14,172.73,157.34,175.78,175.19,172.22,153.34,153.22,159.07,164.91,173.81,166.42,171.85,154.69,168.82,157.64,191.2,174.71,162.46,174.12,173.55,161.58,161.77,170.53,167.35,169.03,169.14,182.91,174.78,160.27,181.55,182.48,158.28,151.82,189.6,166.26,174.81,164.79,177.7,170.23,182.8,161.36,180.13,163.9,186,165.69,171.35,152.62,153.7,173.89,188.85,142.43,175.78,168.2,168.43,193.56,176.58,163.15,149.16,195.1,163.07,173.56,174.36,153.28,163.01,186.29,154.66,167.68,152.76,161.35,159.29,168.44,169.77,160.62,176.52,172.77,165.18,168.27,176.2,188.96,172.52,175,161.11,165.76,171.56,153.63,173.66,173.92,151.01,173.78,163.56,185.9,175.52,174.45,172.46,163.57,169.4,179.33,172.69,176.81,165.76,167.71,165.84,165.73,173.2,180.48,163.59,180.68,179.78,173.09,175.94,182.14,188.48,172.24,163.59,162.88,180.08,166.19,158.43,165.75,185.09,173.99,145.13,164.84,172.58,167.35,182.12,162.52,156.71,161.02,164.51,183.42,180.29,166.24,163.25,166.93,181.27,164.1,165.72,159.93,189.46,181.09,157.05,166.99,181.66,169.01,172.57,160.65,164.3,172.18,172.65,159.67,187.07,167.16,170.46,182.24,168.83,159.84,164.93,166.61,171.99,176.92,166.43,165.17,169.91,172.48,156.93,156.26,153.28,169.15,164.15,179.54,165.55,166.27,173.46,164.7,150.46,165.3,173.55,176.74,183.85,182.48,172.56,169.04,174.55,165.48,150.62,158.62,177.2,174.48,172.01,151.64,176.22,181.57,190.45,173.37,147.94,179.95,175.59,176.66,185.24,161.02,195.11,162.18,164.25,152.32,174.63,163.02,164.78,175.33,166.31,169.91,170.55,184.44,166.84,174.33,165.51,168.83,174.66,160.83,164.32,154.16,176.79,171.79,140.74,185.82,171.47,161.1,161.42,171.35,170.5,169.77,180.56,153.43,156.22,178.71,174.38,161.45,165.74,166.8,165.56,186.72,161.67,176.4,191.16,156.35,179.36,171.78,157.47,153.39,177.24,174.45,175.9,181.8,175.87,160.87,158.92,160.26,170.13,169.02,155.29,167.95,156.93,157.99,175.91,172.47,172.55,180.32,160.29,178.55,165.79,162.15,166.31,191.96,183.63,155.73,171.5,174.83,157.15,176.72,159.34,173.46,174.96,166.43,163.31,159.2,174.79,163.52,187.71,178.39,165.34,170.47,164.2,172.61,164.27,159.34,172.39,173.83,160.04,173.54,165.96,162.78,186.59,158.01,145.78,178.03,157.01,167.44,178.13,177.59,164.53,155.45,191.67,168.35,156.16,169.3,165.97,149.68,188.71,192.77,168.67,157.11,187.74,179.5,169.06,145.88,177.03,161.72,181.79,160.57,193.48,159.21,171.61,164.45,171.03,175.91,171.9,155.95,166.16,189.9,178.96,188.76,173.81,185.64,179.47,174.3,176.65,172.15,180.82,167.71,177.1,169.7,151.01,173.44,171.62,163.67,166.59,167.36,169.55,173.46,159.67,174.21,166.71,171.14,171.12,176.21,167.91,176.56,176.87,184.3,168.56,158.29,173.59,177.29,158.98,173.21,156.14,169.76,177.57,158.41,148.14,174,184.34,178.66,153.4,176.64,173.71,162.43,177.9,162.61,174.26,170.24,137.19,200.41,181.1,177.13,184.6,164.49,180.7,169.21,175.28,186.82,181.78,172.02,173.74,145.35,175.21,156.11,169.16,193.27,160.01,167.54,177.06,164.16,175.65,180.08,168.26,169.45,166.75,168.51,176.43,174.13,174.89,166.82,184.23,164.16,171.94,171.61,167.48,184.68,174.32,166.09,164.77,170.13,166.11,161.85,174.8,188.3,192.79,184.88,177.58,164.69,169.25,186.7,175.36,172.58,188.5,185.95,143.01,171.22,172.3,183.48,149.69,179.28,186.71,162.24,185.32,173.03,174.75,165.77,168.52,177.53,168.2,161.27,165.67,170.58,169.14,166.69,176.71,167.72,168.8,178.87,173.14,177.09,150.55,180.7,158.12,178,165.33,171.87,160.61,166.54,156.7,188.7,164.06,186.05,149.24,174.5,175.03,175.63,187.96,169.68,173.68,173.56,161.32,172.71,156.39,183.87,180.82,180.89,184.86,158.27,157.21,177.37,176.4,181.98,147.9,162.02,176.87,169.35,190.16,165.61,174,182.19,156.26,170.93,180.43,167.36,168.26,175.71,161.3,183.25,146.43,185.22,168.88,175.17,157.57,172.79,176.65,171.85,167.22,168.3,177.25,186.94,180.95,179.25,167.28,174.48,181.76,163.34,176.2,173.43,173.69,159.43,173.39,176.84,150.17,165.35,172.94,171.9,160.71,184.91,184.85,172.66,181.24,167.88,160.25,177.74,183.8,163.28,166.19,173.81,187.5,171.83,174.25,172.43,178.54,172.91,169.39,162.87,173.69,164.78,162.1,173.67,168.1,157.28,181.64,168.84,184.96,164.3,180.91,163.2,175.57,173.02,174.53,172.52,175.53,185.12,173.55,178.17,163.73,174.87,159.74,173.55,175.35,169.71,188.01,174.86,158.85,179.67,179.45,182.29,168.71,173.68,174.14,176.31,168.23,164.87,184.34,167.18,178.86,177.78,161.96,190.27,179.11,171.94,176.67,157.32,168.02,163.45,174.98,168.2,168.26,161.97,169.24,174.48,167.8,181.7,179.22,189.03,159.07,177.69,165.75,167.6,185.28,143.44,173.96,175.9,196.79,171.88,157.58,173.89,173.85,161.29,183.75,161.44,162.73,178.56,169.66,158.27,176.17,175.46,157,179.15,163.88,156.88,180.99,183.94,156.99,168.76,173.5,177.69,169.39,165.65,173.77,173.76,179.97,170.93,191.29,174.66,145.72,154.87,174.15,172.06,177.85,172.47,162.31,175.99,168.07,192.3,162.94,174.26,164.25,163.66,163.67,177.65,159.02,161.53,163.69,155.7,175.17,157.15,163.34,188.9,176.55,162.88,167.76,178.49,161.92,168.92,164.52,172.39,178.45,176.67,158.68,180.03,160.42,173.6,175.63,163.75,175.77,160.65,167.42,178.8,167.35,167.7,153.8,167.76,165.96,178.75,158.17,158.68,151.27,161.5,160.6,188.89,170.57,158.08,165.83,181.75,175.34,171.81,163.77,169.64,174.21,171.84,182.26,158.9,152.12,147.61,159.49,164.74,173.11,164.32,188.34,166.68,146.86,179.07,176.75,175.64,150.71,185.77,177.48,156.33,164.99,181.45,164.35,167.05,169.93,160.8,175.25,172.76,180.12,158.5,169.44,175.45,176.47,178.09,169.76,187.79,163.96,175.19,156.77,161.34,174.81,177.13,171.42,181.38,162.87,188.04,167.19,182.43,169.08,164.86,165.17,161.33,175.96,175.86,165.72,171.01,175.09,176,172.31,165.26,151.59,178.28,182.76,167.24,165.82,152.19,152.71,174.95,177.71,173.8,186.2,150.36,169.81,176.21,184.36,171.74,172.39,167.75,176.94,173.12,162.58,179.62,167.75,165.75,187.26,174.82,165.37,183.79,165.01,158.68,164.12,179.61,178.75,166.34,158.02,187.16,177.87,172.01,170.09,170.23,179.24,181.15,156,167.65,169.77,183.87,175.92,175.44,170.73,181.03,158.72,180.29,166.02,174.18,162.7,176.7,161.21,186.72,147.91,160.12,174.1,175.46,161.25,197.55,165.16,163.47,153.02,168.51,177.55,155.73,169.77,165.71,168.27,187.36,181.58,165.84,158.23,154.6,194.87,172.59,186.06,179.65,163.65,147.5,170.9,173.98,180.97,175.88,166.51,159.47,175.55,164.4,174.17,165.36,173.29,177.13,170.81,157.94,166.27,170.89,176.02,174.7,182.61,160.95,170.78,181.99,177.61,174.1,186.4,174.45,166.74,160.87,149.75,163.28,185.59,173.74,165.8,175.33,172.63,183.98,151.18,185.38,164.05,169.5,174.81,165.89,181.55,182.68,161.93,158.73,161.67,178.96,169.64,175.15,158.68,154.39,156.78,178.84,177.72,171.22,173.13,175.51,150.28,175.11,168.16,180.13,155.07,162.17,178.53,165.72,172.33,167.23,167.06,169.7,160.96,183.23,172.19,185.25,183.87,184.71,171.23,154.95,179.99,145.98,184.05,174.91,174.43,171.22,172.4,168.1,177.67,165.32,172.77,177.28,172.21,169.01,180.96,161.41,169.2,173.4,146.1,184.42,161.54,155.5,155.13,146.31,153.75,155.98,178.87,164.81,161.77,159.57,176.87,165.54,158.89,162.2,174.81,188.89,184.5,166.62,156.61,158.37,172.36,159.05,148.13,181.61,186.53,150.18,165.24,185.07,182.36,175.81,188.78,171.84,174.03,185.44,156.2,174.14,163.68,165.49,183.8,169.96,178.86,167.86,181.61,184.29,173.95,175.48,160.13,164.96,184.77,160.26,181.09,178.25,150.41,166.89,185.69,181.75,154.65,192.01,168.52,168.51,182.76,155.62,161.75,162.26,170.7,161.65,152.33,172.13,164.95,175.28,168.51,169.27,171.4,172.29,177.53,154.5,156.32,183.39,180.63,178.34,178.57,167.31,164.74,178.12,171.32,186.22,176.14,169.58,177.49,183.34,183.29,177.44,163.7,173.59,158.06,160.33,173.56,180.66,155.45,166.33,175.41,179.61,167.74,167.82,160.69,164.28,174.18,180.86,183.16,166.47,189.14,153.46,173.92,160.4,171.61,154.33,191.98,173.67,184.35,164.32,185.27,176.05,151.38,164.27,171.92,168.03,181.89,158.04,159.39,168.67,164.21,178.04,170.44,184.1,152.76,171.42,178.67,178.61,169.01,170.27,199.86,189.12,181.62,164.8,157.95,172.07,182.7,156.42,176.43,168.44,176.1,171.97,176.02,180.6,173.18,162.48,191.44,152.05,170.27,183.47,170.57,184.71,167.47,168.21,172.3,170.31,163.88,151.92,179.87,170.19,174.69,152.19,165.1,175.51,172.56,187.45,166.45,179.75,169.06,177.31,161.83,186.11,169.79,182.16,168.09,175.92,174.21,166.13,182.74,171.72,180.51,168.13,149.26,181.66,165.28,179.83,153.38,161.17,165.68,198.77,165.85,169.55,174.19,175.02,183.99,160.88,171.9,172.91,158.48,167.59,174.66,168.49,172.69,186,165.31,170.1,173.88,183.84,183.91,179.33,188.3,154.47,170.66,146.38,168.81,170.34,180.38,184.95,156.05,175.09,156.14,172.36,169.47,159.99,179.48,156.15,165.08,180.97,169.38,184.3,167.05,164.06,171.83,188.66,185.31,159.58,177.72,170.82,154.54,156.71,158.17,171.27,176.28,180.59,192.71,155.46,169.7,178.83,175.64,170.69,179.06,176.82,170.14,170.73,166.6,168.26,167.71,166.34,186.3,171.92,175.7,179.59,166.7,178.02,172.65,180.61,164.11,159.13,174.32,157.98,165.05,172.4,163.69,172.38,164.71,167.66,144.37,170.92,139.5,150.35,175.79,158.27,168.76,172.26,179.59,163.79,171.38,162.01,165.91,179.23,159.68,181.08,172.28,173.87,172.22,169.81,185.94,154.53,168.34,162.53,168.46,174.89,169.32,146.8,154.32,160.42,178.87,161.17,166.46,168.69,187.34,176.87,176.67,178.19,167.42,160.98,184.62,167.71,176.59,168.52,146.38,178.71,181.55,166.27,174.86,168.03,187.12,165.13,184.31,177.22,172.15,158.49,172.66,187.31,161.77,159.05,164.98,162.18,161.05,171.97,173.4,167.46,162.08,171.79,190.18,166.39,153.41,161.68,170.46,165.06,168.85,163.62,174.45,180.36,167.14,157.83,170.7,151.12,168.36,168.28,159.98,179.26,164.73,169.13,175.34,168.06,146.68,161.24,177.22,156.83,181.16,177.04,191.45,174.74,182.65,164.53,182.3,166.57,165.36,163.32,167.49,178.99,166,174.33,175.85,164.97,142.63,183.09,180.31,169.15,161.54,166.21,181.92,176.57,182.04,176.61,194.65,176.62,160.27,181.56,170.74,178.99,170.01,160.88,167.68,179.86,163.42,164.94,169.81,138.95,163.47,162.71,172.83,177,191.13,172.93,157.01,167.12,174.39,182.22,173.1,160.49,157.39,153.34,155.13,167.92,150.29,177.51,164.32,157.79,176.95,169.01,153.99,173.14,168.6,192.36,173.81,159,164,164.68,181.06,162.4,155.46,171.08,175.67,166.39,173.47,178.25,175.54,175.96,159.08,153.63,166.55,160.99,164.73,179.11,159.13,165.12,162.89,159.42,161.52,178.88,182.92,183.18,163.59,156.7,180.06,159.25,169.08,160.05,169.52,178.55,168.44,163.19,161.44,167.86,168.72,176.78,160.18,170.21,172.07,188.23,173.14,170.69,174.55,168.14,174.45,171.06,161.96,173.26,179.8,164.09,175.5,173.8,148.02,156.92,162.12,174.03,158.06,164.75,178.48,180,182.96,169.15,169.24,190.86,158.2,163.8,175.12,177.21,181.74,166.85,167.07,163.08,186.07,172.85,167.61,174.2,183.59,181.27,164.46,175.47,186.72,183.07,153.64,173.7,177.08,153.94,182.23,154.57,179.49,160.12,171.26,169,156.75,187.22,162.66,164.94,173.52,167.03,164.66,156.16,166.83,184.36,174.26,166.73,179.43,172.74,171.89,181.94,152.95,174.69,174.2,145.59,162.03,181.98,171.22,146.98,170.62,179.24,153.56,186.14,163.19,161.96,167.69,164.34,176.42,168.48,179.89,167.79,168,172.34,160.62,176.96,167.77,154.59,166.74,161.79,180.72,171.58,155.15,166.86,177.74,157.36,157.12,164.65,181.07,158.19,178.25,167.74,168.8,185.57,170.93,172.64,184.54,161.92,173.54,155.89,164.81,180.21,164.76,166.34,174.21,184.74,169.93,163.61,191.78,192.29,164.29,162.91,166.86,163.26,165.86,165.47,167.5,176.01,159.52,147.44,194.8,181.53,166.38,163.71,172.73,185.65,160.34,167.33,150.67,172.36,181.12,177.05,174.61,175.26,174.17,179.31,171.52,167.2,190.56,160.12,158.13,170.75,191.56,171.56,180.1,182.18,173.48,184.33,177.58,178.66,174.23,167.8,169.52,155.48,153.05,173.46,191.43,167.09,158.88,184.35,154.91,162.98,152.24,167.37,161.49,176.03,178.45,156.06,171.98,179.54,168.44,167.44,172.03,171.7,179.97,154.48,182.62,165.49,166.74,179.8,167.36,160.03,168.86,146.74,170.78,164.65,162.68,161.09,177.64,174.6,181.39,159.49,174.36,182.26,188.57,147.27,146.63,170.04,174.95,160.38,179.4,161.34,170.58,183.97,167.21,185.84,158.11,170.14,181.82,170.48,165.55,165.14,161.21,168.49,176.37,162.88,175.4,179.8,179.93,164.52,170.04,164.93,179.77,176.41,172.1,175.42,168.81,159.12,162.6,179.14,178.91,164.67,182.49,163.65,172.3,177.02,180.94,180.4,180.87,166.66,140.09,160.11,165.41,178.26,151.57,176.04,150,167.11,159.23,165.89,171.64,171.7,169.01,166.36,170.31,177.34,182.88,166.18,173.57,191.57,173.12,167.14,171.66,155.15,163.69,183.3,170.84,173.49,168.67,149.34,166.99,164.67,193.94,183.94,164.76,174.81,167.71,168.33,176.31,178.92,174.51,166.74,166.52,179.06,174.63,181.68,175.54,164.66,177.46,171.71,151.42,161.72,176.26,149.8,163.92,184.02,165.4,178.56,179.84,177.55,167.18,163.35,165.42,171.61,158.62,166.28,178.71,165.41,163.04,167.8,191.3,174.94,179.28,181.56,174.26,178.88,173.02,159.15,161.94,174.08,176.2,186.39,159.1,173.23,172.16,164.02,151.46,184.84,167.14,170.12,159.56,175.57,179.82,183.34,153.35,158.95,178.04,166.96,171.52,176.39,167.95,175.85,166.44,162.97,154.05,173.25,158.96,154.79,174.47,169.07,175.77,153.41,160.27,174.36,166.93,163.06,158.76,166.16,170.04,171.67,165.93,170.6,189.5,170.75,173.04,171.16,174.41,179.54,180.54,147.66,161.14,155.53,170.42,158.58,182.85,185.39,162.33,155.53,167.19,160.59,166.77,174.34,175.88,174.75,177.58,183.84,171.94,173.58,180.99,168.22,177.41,155.06,157.92,171.06,164.52,160.11,181.66,184.79,181.22,172.93,152.01,177.1,173.87,171.76,180.44,158.12,165.01,177.84,173.05,170.21,178.07,183.9,173.52,160.36,155.25,156.9,180.05,166.2,179.08,149.96,166.54,174.66,167.73,185.91,176.16,170.01,163.05,165.18,177.87,189.14,161.36,171.15,173.47,149.61,166.92,165.28,173.47,181.97,178.05,172.84,174.77,149.62,149.19,167.69,162.26,183,163.37,158.75,192.17,151.26,170.92,164.17,164.24,190.68,173.57,177.21,163.95,166.62,160.78,164.43,173.48,157.19,150.9,171.1,181.79,157.47,157.44,180.7,174.56,174.7,188.6,164.59,177.52,159.31,168.63,178.95,169.77
]

def flatten(x):
    result = []
    for i in x:
        if hasattr(i, "__iter__") and not isinstance(i, str):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

def graph_samp1():
  totallst = []
  sample_means = []
  sampsize = int(input('How many samples from list: '))
  size = int(input('How many samples of samples: '))
  for i in range(1, size):
    totallst.append(sample_pick(lst, sampsize))
 
########## Graph making
  totallst = flatten(totallst)
  plt.title(f"Histogram with {size} sample means.")
  plt.hist(totallst, 10)
  plt.show()
