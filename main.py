import math
import sys

from methods import secant, fixed_point_iteration, fixed_point_iteration_system

f1 = lambda x: 3 * x ** 3 + 4.5 * x ** 2 - 2.3 * x - 3
f2 = lambda x: 2.1 * math.exp(x) + x ** 2 - 4.2 * x - 3.5
f3 = lambda x: 7 / x - 2.1 * x ** 2 + 3 * x + 2

f4 = lambda x, y: 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3
f5 = lambda x, y: 0.2 * x ** 2 + y - 0.1 * x * y - 0.7

f1_der = lambda x: 9 * x ** 2 + 9 * x - 2.3
f2_der = lambda x: 2.1 * math.exp(x) + 2 * x - 4.2
f3_der = lambda x: -7 / x ** 2 - 2.1 * 2 * x + 3

f4_x = lambda x, y: 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2
f5_y = lambda x, y: 0.7 - 0.2 * x ** 2 - 0.1 * x * y

f4_der_x = lambda x: -0.2 * x
f5_der_x = lambda x, y: -0.4 * x + 0.1 * y

f4_der_y = lambda y: -0.4 * y
f5_der_y = lambda x: 0.1 * x

functions = {1: f1, 2: f2, 3: f3}
functions_der = {1: f1_der, 2: f2_der, 3: f3_der}
systems = {1: [f4_x, f5_y]}
methods = {1: secant, 2: fixed_point_iteration}
methods_for_systems = {1: fixed_point_iteration_system}


def main():
    args = sys.argv[1:]
    if len(args) != 0:
        input_filepath = args[0]
        input_file = open(input_filepath, "r")
        process_file_input(input_file)
    else:
        process_console_input()


def process_file_input(file):
    func_or_system = int(file.readline())
    if func_or_system == 1:  # Function
        function_num = int(file.readline())
        function = functions[function_num]
        function_der = functions_der[function_num]
        method = methods[int(file.readline())]
        if method is secant:
            x1 = float(file.readline())
            x2 = float(file.readline())
        elif method is fixed_point_iteration:
            start_point = float(file.readline())
    elif func_or_system == 2:  # System
        system = systems[int(file.readline())]
        method = methods_for_systems[int(file.readline())]
        if method is fixed_point_iteration_system:
            x = float(file.readline())
            y = float(file.readline())

    accuracy = float(file.readline())

    if method is secant:
        secant(function, x1, x2, accuracy)
    elif method is fixed_point_iteration:
        fixed_point_iteration(function, function_der, start_point, accuracy)
    elif method is fixed_point_iteration_system:
        fixed_point_iteration_system(system[0], f4_der_x, f4_der_y, system[1], f5_der_x, f5_der_y, x, y, accuracy)

def process_console_input():
    print("1) Functions")
    print("2) Systems")
    print("Enter 1 or 2:")
    func_or_system = int(input())

    if func_or_system == 1:  # Function
        print("1) 3x^3+4.5x^2-2.3x-3=0")
        print("2) 2.1e^x+x^2-4.2x-3.5=0")
        print("3) 7/x-2.1x^2+3x+2=0")
        print("Choose function: ")
        function_num = int(input())
        function = functions[function_num]
        function_der = functions_der[function_num]

        print("1) Secant")
        print("2) Fixed Point Iteration")
        print("Choose method: ")
        method = methods[int(input())]

        if method is secant:
            print("Enter point x1: ")
            x1 = float(input())
            print("Enter point x2: ")
            x2 = float(input())
        elif method is fixed_point_iteration:
            print("Enter start point: ")
            start_point = float(input())

    elif func_or_system == 2:  # System
        print("1) 0.1x^2+x+0.2y^2-0.3=0\n   0.2x^2+y-0.1xy-0.7=0")
        system = systems[int(input())]
        print("1) Fixed Point Iteration")
        print("Choose method: ")
        method = methods_for_systems[int(input())]
        if method is fixed_point_iteration_system:
            print("Enter x: ")
            x = float(input())
            print("Enter y: ")
            y = float(input())

    print("Enter accuracy: ")
    accuracy = float(input())

    if method is secant:
        secant(function, x1, x2, accuracy)
    elif method is fixed_point_iteration:
        fixed_point_iteration(function, function_der, start_point, accuracy)
    elif method is fixed_point_iteration_system:
        # f1, f1_der_x, f1_der_y, f2, f2_der_x, f2_der_y, x, y, e
        # system[0], , , system[1], , x, y, accuracy
        fixed_point_iteration_system(system[0], f4_der_x, f4_der_y, system[1], f5_der_x, f5_der_y, x, y, accuracy)


main()