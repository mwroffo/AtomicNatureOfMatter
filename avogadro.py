import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.


def main():
    # 1. estimating D
    displacements = []
    n = 0
    while not stdio.isEmpty():
        n += 1
        displacements.append(stdio.readFloat() * 0.175 * 10.0 ** -6.0)
        # now displacements are in meters...
    D = 0.0
    # intialize D
    # then calculate D as variance of radial displacements in meters:
    for i in range(len(displacements)):
        D += displacements[i] * displacements[i]
    D /= (2 * n)

    # 2. estimating k
    T = 297.0
    eta = 9.135 * 10.0 ** -4.0
    rho = 0.5 * 10.0 ** -6.0
    k = (6.0 * math.pi * eta * rho * D) / (T)

    # 3. estimating Avogadro's number
    R = 8.31457
    N_A = R / k

    # print:
    stdio.writef('Boltzman = %.6e\n', k)
    stdio.writef('Avogadro = %.6e\n', N_A)

if __name__ == '__main__':
    main()
