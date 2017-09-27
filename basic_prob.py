# https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/basic-probability-models-and-rules/tutorial/

from __future__ import division

if __name__ == "__main__":
    pmb = float(input())
    pab = float(input())
    p1 = float(input())

    prs = p1 * ((pmb * (1 - pab)) + ((1 - pmb) * pab))

    print("%.6f" % prs)
