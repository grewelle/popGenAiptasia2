import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    Infected = 100
    Uninfected = 900

    P_pop = Infected

    lamb = 5
    sampleEffort = .02

    props = []
    rhos = []
    P_test = 0

    for i in range(30):
        infTest = Infected*sampleEffort*lamb
        uninfTest = Uninfected*sampleEffort
        Infected -= infTest
        Uninfected -= uninfTest

        P_test += infTest
        rho = infTest/(uninfTest+infTest)

        props.append(P_test/P_pop)
        rhos.append(5**(5**rho))

    plt.plot(rhos, props)
    plt.show()



        



main()