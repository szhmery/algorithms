import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline


T = np.array([1, 2, 3 ,4, 5, 6, 7])
power1 = np.array([1.3, 2.0, 1.8, 1.7, 2.1, 2.0, 1.9])
power2 = np.array([13, 8.0, 1.8, 9.7, 5.1, 3.0, 9.9])

power3 = np.array([86.3, 46.0, 89.8, 45.7, 33.1, 11.0, 12.9])

power4 = np.array([111.3, 46.0, 89.8, 45.7, 33.1, 11.0, 12.9])

power5 = np.array([567.3, 46.0, 89.8, 45.7, 33.1, 11.0, 12.9])

power6 = np.array([4455.3, 46.0, 89.8, 45.7, 33.1, 11.0, 12.9])

power7 = np.array([86.3, 46.0, 5555.8, 45.7, 33.1, 11.0, 12.9])

power8 = np.array([86.3, 46.0, 34577.8, 45.7, 33.1, 11.0, 12.9])
# plt.plot(T,power)
# plt.show()


#axis1 = fig.add_subplot(211)
xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max
#print(xnew)
spl = make_interp_spline(T, power1, k=3) #BSpline object
power_smooth = spl(xnew)
#print(power_smooth)

fig=plt.figure(figsize=(20,20))
plt.subplot(2,2,1)
n, bins, patches = plt.hist(power2, 1000, density=True, cumulative=True, label="aaa",
                                histtype='step')
n, bins, patches = plt.hist(power3, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')




#axis1.minorticks_on()
#axis1.set(title="plot1")
#plt.plot(xnew,power_smooth)
#plt.show()


#axis1.plot(range(10))
#axis2 = fig.add_subplot(212)
plt.subplot(2,2,2)
n, bins, patches = plt.hist(power2, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')
n, bins, patches = plt.hist(power3, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')

#axis2.minorticks_on()
#axis2.set(title="plot2")
#axis3 = fig.add_subplot(311)
plt.subplot(2,2,3)
n, bins, patches = plt.hist(power4, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')
n, bins, patches = plt.hist(power5, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')
#axis3.minorticks_on()
#axis3.set(title="plot3")
#axis4 = fig.add_subplot(321)
plt.subplot(2,2,4)
n, bins, patches = plt.hist(power6, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')
n, bins, patches = plt.hist(power7, 1000, density=True, cumulative=True, label="aaa",
                            histtype='step')
#axis4.minorticks_on()
#axis4.set(title="plot4")

fig.tight_layout()
fig.savefig('multipleplots.pdf')