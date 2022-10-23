#ex 7: Bootstrap
import scipy.stats as sc
import random as rn
M = 1000
lsta = numpy.empty(M)
for i in np.arange(0,M):
    datm = rn.choices(population=dataB, k=500)
    a, loc, scale = sc.invgauss.fit(datm)
    lsta[i] = a

#percentile
pp025 = stats.scoreatpercentile(lsta,2.5)  
pp975 = stats.scoreatpercentile(lsta,97.5)

print("pp025 = " + str(pp025))
print("pp975 = " + str(pp975))


#Interprétation :

#Nous avons 95% de chance que la moyenne soit entre pp025 et pp975
