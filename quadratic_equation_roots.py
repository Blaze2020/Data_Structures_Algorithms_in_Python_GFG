# Quadratic Equation Roots
# BasicAccuracy: 12.78%Submissions: 100k+Points: 1
# Given a quadratic equation in the form ax2 + bx + c. Find its roots.

# Note: Return the maximum root followed by the minimum root.

# Example 1:

# Input:
# a = 1
# b = -2
# c = 1
# Output: 1 1
# Explanation:
# Roots of equation x2-2x+1 are 1 and 1.

from math import floor, sqrt


def quadraticRoots(a, b, c):
    d = (b*b)-(4*a*c)
  # print("D value:", d)
    roots = []
    if d > 0:
        roots.append(floor((-b+sqrt(d))//(2*a)))
        roots.append(floor((-b-sqrt(d))//(2*a)))
        if roots[0] < roots[1]:
            temp = roots[0]
            roots[0] = roots[1]
            roots[1] = temp
    # print(roots)
        return roots
    elif d == 0:
        roots.append(-b//(2*a))
        roots.append(-b//(2*a))
        return roots
    elif d < 0:
        roots.append(-1)
        return roots


if __name__ == "__main__":
    print(quadraticRoots(1, -2, 1))
