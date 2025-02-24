import numpy as np
import matplotlib.pyplot as plt

def main():

    

    a = .0003
    b = .1
    c = 0.01
    t=0.001
    lam = 2
    lam2 = 5
    rhos = []
    logCFRs = []
    sampleTimes = [20, 25, 30, 35, 40, 45]

    for sampleTime in sampleTimes:
        Susc = [999]
        Susc_test = [0]
        Inf = [1]
        Inf_test = [0]
        Recov = [0]
        Dead = [0]
        single_suscTest = [0]
        single_infTest = [0]
        single_dead = [0]
        
        gen = np.linspace(0,100,101)

        for g in range(100):

            Susc.append(Susc[g]-a*Susc[g]*Inf[g]-t*Susc[g])
            Susc_test.append(Susc_test[g]+t*Susc[g]-a*Susc_test[g]*Inf[g])
            Inf.append(Inf[g]+a*(Susc[g]+Susc_test[g])*Inf[g]-b*Inf[g]-lam*t*Inf[g])
            Inf_test.append(Inf_test[g]+lam*t*Inf[g]-b*Inf_test[g])
            Recov.append(Recov[g]+b*(1-c)*(Inf[g]+Inf_test[g]))
            Dead.append(Dead[g]+b*c*(Inf[g]+Inf_test[g]))
            single_suscTest.append(single_suscTest[g]+t*(Susc[g]+Recov[g]))
            single_infTest.append(single_infTest[g]+lam*t*Inf[g])
            #single_dead.append(lam*t*c*(Inf_test[g]+Inf[g]))
            single_dead.append(single_dead[g]+lam2*t*(Dead[g]-single_dead[g]))

        
        rhos.append(single_infTest[sampleTime]/(single_infTest[sampleTime]+single_suscTest[sampleTime]))
        logCFRs.append(np.log(single_dead[sampleTime]/single_infTest[sampleTime]))
        #logCFRs.append(Dead[sampleTime]/single_infTest[sampleTime])
        #plt.plot(gen, single_infTest)
        #plt.plot(gen, single_suscTest)
        plt.plot(gen, single_dead)
        plt.show()

    #print(rhos)
    #print(logCFRs)
    plt.plot(rhos, logCFRs)
    plt.show()
    coefficients = np.polyfit(rhos, logCFRs, 1)
    print(coefficients[0])
    print(np.exp(coefficients[1]))

    #print('IFR=', Dead[sampleTime]/(Inf[sampleTime]+Inf_test[sampleTime]+Recov[sampleTime]+Dead[sampleTime]))


    """lamb = 3

    startDead = [[Dead[40]], [Dead[40]], [Dead[40]], [Dead[40]], [Dead[40]]]
    startInfected = [[999-Susc[40]], [999-Susc[40]], [999-Susc[40]], [999-Susc[40]], [999-Susc[40]]]
    startFree = [[Susc[40]+Recov[40]], [Susc[40]+Recov[40]], [Susc[40]+Recov[40]], [Susc[40]+Recov[40]], [Susc[40]+Recov[40]]]

    logCFR = []
    CFR = []
    rho = []

    for effort in range(5):

        for rounds in range(100):
            startInfected[effort].append(startInfected[effort][rounds]*(1-lamb*(effort+.1)/1000))
            startFree[effort].append(startFree[effort][rounds]*(1-(effort+.1)/1000))

        deaths = startDead[effort][0]
        print(deaths)
        cases = startInfected[effort][0]-startInfected[effort][-1]
        tests = startInfected[effort][0]-startInfected[effort][-1] + startFree[effort][0]-startFree[effort][-1]

        logCFR.append(np.log(deaths/cases))
        CFR.append(deaths/cases)
        rho.append(cases/tests)

    plt.scatter(rho, logCFR)
    plt.show()
    coefficients = np.polyfit(rho, logCFR, 1)
    print(np.exp(coefficients[1]))

    print('IFR=', deaths/startInfected[0][0])"""

    






main()