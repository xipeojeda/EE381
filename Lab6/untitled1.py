import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import matplotlib.lines as mlines


def main():

    n = 15      # 15 times
    N = 10000   # repetition of the experiment


    throws = []
    throws = np.zeros(n)
    state1 = np.zeros(n)
    state2 = np.zeros(n)
    state3 = np.zeros(n)

    for j in range(N):

        for i in range(n):

            if i == 0:
                initialThrow = nsideddie([0.25, 0, 0.75])
                throws[i] = initialThrow

            if initialThrow == 1:
                initialThrow = nsideddie([0.5, 0.25, 0.25])
                throws[i] = initialThrow
                state1[i] += 1

            elif initialThrow == 2:
                initialThrow = nsideddie([0.25, 0.125, 0.625])
                throws[i] = initialThrow
                state2[i] += 1

            elif initialThrow == 3:
                initialThrow = nsideddie([0.33, 0.67, 0])
                throws[i] = initialThrow
                state3[i] += 1

        if j == 0:
            graph(throws)

    for i in range(n):
        state1[i] = state1[i]/N
        state2[i] = state2[i]/N
        state3[i] = state3[i]/N

    graphProb(state1, state2, state3)


    # for the calculated grpah

    intialMatrix = np.matrix([0.25, 0, 0.75])
    transitionMatrix = np.matrix([[0.5, 0.25, 0.25], [0.25, 0.125, 0.625], [0.33, 0.67, 0]])

    Y = np.zeros((n, 3))
    Y[0, :] = intialMatrix

    for i in range(0, n-1):
        Y[i+1, :] = np.matmul(Y[i, :], transitionMatrix)

    plt.figure()
    nv = np.linspace(0, n, num=n)
    plt.plot(nv, Y[:, 0], 'r:', marker='o')
    plt.plot(nv, Y[:, 1], 'b:', marker='o')
    plt.plot(nv, Y[:, 2], 'g:', marker='o')
    plt.title('Calculated 3 state Markov Chain')
    plt.xlabel('steps')
    plt.ylabel('states')
    l1 = mlines.Line2D([], [], color='red', marker='.', label='state 1', markersize=15)
    l2 = mlines.Line2D([], [], color='blue', marker='.', label='state 2', markersize=15)
    l3 = mlines.Line2D([], [], color='green', marker='.', label='state 3', markersize=15)
    plt.legend(handles=[l1, l2, l3])
    plt.show()

def graphProb(p1, p2, p3):
    plt.scatter(np.arange(len(p1)), p1, color='r', edgecolors='r')
    plt.scatter(np.arange(len(p2)), p2, color='b', edgecolors='b')
    plt.scatter(np.arange(len(p3)), p3, color='g', edgecolors='g')
    plt.xticks(np.arange(len(p1)), np.arange(1, len(p1) + 1))
    plt.plot(p1, 'r:')
    plt.plot(p2, 'b:')
    plt.plot(p3, 'g:')
    plt.ylabel('Probabilities of the different states in each step')
    plt.xlabel('steps')
    plt.title('Simulated state prob. graph')

    l1 = mlines.Line2D([], [], color='red', marker='.', label='state 1', markersize=15)
    l2 = mlines.Line2D([], [], color='blue', marker='.', label='state 2', markersize=15)
    l3 = mlines.Line2D([], [], color='green', marker='.', label='state 3', markersize=15)

    plt.legend(handles=[l1, l2, l3])
    plt.show()

def graph(throws):

    plt.yticks([1, 2, 3])
    plt.scatter(np.arange(len(throws)), throws, color='r', edgecolors='b')
    plt.xticks(np.arange(len(throws)), np.arange(1, len(throws) + 1))
    plt.plot(throws, 'b:')
    plt.ylabel('states')
    plt.xlabel('steps')
    plt.title('Simulated run')
    plt.show()


def nsideddie(p):
    n = len(p)  # length of the array p tell us the
                # how many sides the die has

    cs = np.cumsum(p)
    cp = np.append(0, cs)

    r = np.random.rand()
    for k in range(0, n):

        if r > cp[k] and r <= cp[k + 1]:
            d = k + 1

    return d


main()