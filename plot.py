import matplotlib.pyplot as plt
import numpy as np
import pickle

def plot():
    with open("times_pypy3.pkl", "rb") as f:
        pypy = pickle.load(f)
    with open("times_python3.pkl", "rb") as f:
        python = pickle.load(f)
    labels = np.arange(1, 26, 0.5)
    fig, ax = plt.subplots()
    ax.plot(labels, pypy, 'b', labels, python, 'r')
    #ax.plot(np.arange(1, 26, 0.5), python)
    #ax.set_yscale('log')
    #plt.show()
    plt.savefig("times.png")

if __name__ == "__main__":
    plot()