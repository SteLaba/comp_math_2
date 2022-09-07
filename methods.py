from math import fabs, sqrt
import sympy as sym

from draw import draw


def secant(f, x1, x2, accuracy):
    print("---------------------------------------------------")
    print("%-10s %-10s %-10s %-10s %-10s" % ("x1", "x2", "f(x1)", "f(x2)", "|f(x1)-f(x2)|"))
    diff = fabs(x2 - x1)
    print("%-10.4f %-10.4f %-10.4f %-10.4f %-10.4f" % (x1, x2, f(x1), f(x2), diff))
    iters = 0
    while diff > accuracy:
        x_new = x2 - (x2 - x1) / (f(x2) - f(x1)) * f(x2)
        x1 = x2
        x2 = x_new
        iters += 1
        diff = fabs(x2 - x1)
        print("%-10.4f %-10.4f %-10.4f %-10.4f %-10.4f" % (x1, x2, f(x1), f(x2), diff))
    print("---------------------------------------------------")
    print(f"x = {x2}")
    print(f"f(x)= {f(x2)}")
    print(f"Accuracy: {diff}")
    print(f"Iterations: {iters}")
    draw(f, int(min(x1, x2) - 1), int(max(x1, x2) + 1))


def fixed_point_iteration(f, f_der, x0, e):
    print("---------------------------------------------------")
    print("%-10s %-10s" % ("x", "f(x)"))
    x = x0
    l = -1 / f_der(x0)
    print("%-10.4f %-10.4f" % (x, f(x)))
    iters = 0
    while fabs(f(x)) > e:
        x0 = x
        x = x0 + l * f(x0)
        iters += 1
        print("%-10.4f %-10.4f" % (x, f(x)))
    print("---------------------------------------------------")
    print(f"x = {x}")
    print(f"f(x)= {f(x)}")
    print(f"Accuracy: {fabs(x - x0)}")
    print(f"Iterations: {iters}")
    draw(f, int(min(x0, x) - 1), int(max(x0, x) + 1))


def fixed_point_iteration_system(f1, f1_der_x, f1_der_y, f2, f2_der_x, f2_der_y, x, y, e):
    print("---------------------------------------------------")
    print("%-10s %-10s %-10s %-10s %-10s %-10s" % ("x", "y", "f1(x, y)", "f2(x, y)", "acc_x", "acc_y"))
    print("%-10.4f %-10.4f %-10.4f %-10.4f %-10.4f %-10.4f" % (x, y, f1(x, y), f2(x, y), x, y))
    sum_der_x = f1_der_x(x) + f1_der_y(y)
    sum_der_y = f2_der_x(x, y) + f2_der_y(y)

    r_x = 0
    r_y = 0

    if sum_der_x < 1 and sum_der_y < 1:
        condition = True
        while condition:
            temp_x = f1(x, y)
            temp_y = f2(x, y)

            condition = fabs(temp_x - x) > e and fabs(temp_y - y) > e

            r_x = fabs(x - temp_x)
            r_y = fabs(y - temp_y)

            x = temp_x
            y = temp_y
            print("%-10.4f %-10.4f %-10.4f %-10.4f %-10.4f %-10.4f" % (x, y, f1(x, y), f2(x, y), r_x, r_y))
        print("---------------------------------------------------")
        print(f"x = {x}, y = {y}")
        print(f"f1(x, y) = {f1(x, y)}, f2(x, y) = {f2(x, y)}")

    else:
        print("Convergence condition has not been met.")

    return 0
