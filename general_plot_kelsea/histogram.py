import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def make_histogram(data, title, xlabel, ylabel):
    n, bins, patches = plt.hist(data, bins='auto')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()