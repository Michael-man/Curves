import numpy as np
from matplotlib import pyplot as plt
import time


def bezier_curve_3(xpoints, ypoints, nTimes=1000):
    ret_x = []
    ret_y = []
    for i in np.arange(0, nTimes + 1):
        t = i / nTimes
        x = (1 - t) ** 3 * xpoints[0] + 3.0 * t * (1 - t) ** 2 * xpoints[1] + 3.0 * (t) ** 2 * (1 - t) * xpoints[
            2] + t ** 3 * xpoints[3]
        ret_x.append(x)
        y = (1 - t) ** 3 * ypoints[0] + 3.0 * t * (1 - t) ** 2 * ypoints[1] + 3.0 * (t) ** 2 * (1 - t) * ypoints[
            2] + t ** 3 * ypoints[3]
        ret_y.append(y)
    return ret_x, ret_y

def temp_curve_3(x, y, nTimes=1000):
    dx_0 = (x[1] - x[0]) * 2 / nTimes
    dy_0 = (y[1] - y[0]) * 2 / nTimes

    tdx = (x[2] - 2 * x[1] + x[0]) * 2 / nTimes ** 2
    tdy = (y[2] - 2 * y[1] + y[0]) * 2 / nTimes ** 2

    tddx = (x[3] - 3 * (x[2] - x[1]) - x[0]) * 2 / nTimes ** 3
    tddy = (y[3] - 3 * (y[2] - y[1]) - y[0]) * 2 / nTimes ** 3

    M_0 = x[0]
    N_0 = y[0]

    TM = (x[1] - x[0]) / nTimes  # TMS
    TN = (y[1] - y[0]) / nTimes  # TNS

    ret_x = []
    ret_y = []
    ret_x.append(M_0)
    ret_y.append(N_0)
    C = nTimes

    atdx = tdx / 2
    atdy = tdy / 2

    atddx = tddx / 2
    atddy = tddy / 2
    for i in np.arange(1.0, C+1):
        M_0 += dx_0 + atdx
        N_0 += dy_0 + atdy

        atdx += tdx
        atdy += tdy

        TM += tdx + atddx
        TN += tdy + atddy

        atddx += tddx
        atddy += tddy

        M = M_0 + (i * (TM))
        N = N_0 + (i * (TN))

        ret_x.append(M)
        ret_y.append(N)
    return ret_x, ret_y

xpoints = [-6.0000000001, -4.00000000011, -0.000000000111, -0.0000000001111]
ypoints = [-5.0000000001, 3.00000000011, 0.000000000111, -4.0000000001111]

plt.rcParams["figure.figsize"] = (10, 10)
plt.axis([-8, 2, 2, -8])

plt.plot(xpoints, ypoints, "b")

loop_times = 1000
proc_times = 1000

start = time.time()
for i in np.arange(loop_times):
    X, Y = bezier_curve_3(xpoints, ypoints, nTimes=proc_times)

end = time.time()
plt.plot(X, Y, "k")
print("Bezier_3 time : ", end - start, "(start : ", start, " end : ", end)

start = time.time()
for i in np.arange(loop_times):
    X, Y = temp_curve_3(xpoints, ypoints, nTimes=proc_times)

end = time.time()
plt.plot(X, Y, "m")
print("temp_3 time : ", end - start, "(start : ", start, " end : ", end)

plt.show()
