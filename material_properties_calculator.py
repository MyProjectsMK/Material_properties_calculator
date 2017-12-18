import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import os
from pandas import DataFrame


# input check-up functions

def file_is_empty(path):
    return os.stat(path).st_size == 0

def file_is_empty_check(path):
    while file_is_empty(path) == True:
        if path == "input_known_temperatures.txt":
            print "\nERROR: input_known_temperatures.txt file is empty! Please insert values into input_known_temperatures.txt file. \n"
        else:
            print "\nERROR: input_known_parameter_values.txt file is empty! Please insert values into input_known_parameter_values.txt file. \n"
        ready_status = raw_input("When you are ready, press [Y] \n")
        while ready_status != 'y' and ready_status != 'Y':
            ready_status = raw_input("\nWhen you are ready, press [Y] \n")

def file_if_numbers(known_values, path):
    a = 1
    while a == 1:
        known_values = np.array([line.strip() for line in open(path, 'r')])
        for i in known_values:
            while True:
                try:
                    int(i)
                    a = 0
                    break
                except ValueError:
                    try:
                        float(i)
                        a = 0
                        break
                    except ValueError:
                        if path == "input_known_temperatures.txt":
                            print "\nERROR: There are not only numbers in the input_known_temperatures.txt file! Please correct your input. \n"
                        else:
                            print "\nERROR: There are not only numbers in the input_known_parameter_values.txt file! Please correct your input. \n"
                        ready_status = raw_input("When you are ready, press [Y] \n")
                        while ready_status != 'y' and ready_status != 'Y':
                            ready_status = raw_input("\nWhen you are ready, press [Y] \n")
                        a = 1
                        break

            if a == 1:
                break

def file_length(path1, path2):
    count1 = len(open(path1, 'rU').readlines())
    count2 = len(open(path2, 'rU').readlines())
    while count1 != count2:
        if count1 > count2:
            print "\nERROR: The number of values in the input files are not equal! There are more values in the input_known_temperatures.txt file. Please correct your input.\n"
            ready_status = raw_input("When you are ready, press [Y] \n")
            while ready_status != 'y' and ready_status != 'Y':
                ready_status = raw_input("\nWhen you are ready, press [Y] \n")
            count1 = len(open(path1, 'rU').readlines())
            count2 = len(open(path2, 'rU').readlines())
        else:
            print "\nERROR: The number of values in the input files are not equal! There are more values in the input_known_parameter_values.txt file. Please correct your input.\n"
            ready_status = raw_input("When you are ready, press [Y] \n")
            while ready_status != 'y' and ready_status != 'Y':
                ready_status = raw_input("\nWhen you are ready, press [Y] \n")
            count1 = len(open(path1, 'rU').readlines())
            count2 = len(open(path2, 'rU').readlines())

def monotonic(x):
    dx = np.diff(x)
    return np.all(dx > 0)

def file_if_temperatures_grow(path):
    a = 1
    while a == 1:
        temperatures = np.array([line.strip() for line in open(path, 'r')])
        temporary_list = [float(i) for i in temperatures]
        if monotonic(temporary_list) == False:
            print "\nERROR: Temperatures in the input_known_temperatures.txt file don't have the growth trend. Please correct your input. \n"
            ready_status = raw_input("When you are ready, press [Y] \n")
            while ready_status != 'y' and ready_status != 'Y':
                ready_status = raw_input("\nWhen you are ready, press [Y] \n")
        else:
            a = 0


# main body beginning

first_line = "\n Solids and fluids parameters calculator"
print first_line
underlining = len(first_line) * "=" + "\n"
print underlining
print "Please insert known values of solid/fluid parameter into input_known_parameter_values.txt file and values of temperatures corresponding to them into input_known_temperatures.txt file. \n"
ready_status = raw_input("When you are ready, press [Y] \n")
while ready_status != 'y' and ready_status != 'Y':
    ready_status = raw_input("\nWhen you are ready, press [Y] \n")


# known values check-up

file_is_empty_check("input_known_temperatures.txt")
file_is_empty_check("input_known_parameter_values.txt")

known_temperatures = []
file_if_numbers(known_temperatures, "input_known_temperatures.txt")

known_parameter_values = []
file_if_numbers(known_parameter_values, "input_known_parameter_values.txt")

file_length("input_known_temperatures.txt", "input_known_parameter_values.txt")

file_if_temperatures_grow("input_known_temperatures.txt")

known_temperatures = np.array([line.strip() for line in open("input_known_temperatures.txt", 'r')])
known_temperatures_list = [i for i in known_temperatures]

known_parameter_values = np.array([line.strip() for line in open("input_known_parameter_values.txt", 'r')])
known_parameter_values_list = [j for j in known_parameter_values]


# reading minimal temperature: disabled for Converge use

"""min_temperature = 0
while True:
    min_temperature = raw_input("\nPlease insert minimal temperature for which you want to calculate solid/fluid parameter value: \n")
    try:
        int(min_temperature)
        break
    except ValueError:
         try:
            float(min_temperature)
            break
         except ValueError:
            print "\nThis is not a number!" """


# reading maximal temperature which is a number divisible by 10: enabled for Converge use

max_temperature = 0
while True:
    max_temperature = raw_input("\nPlease insert maximal temperature for which you want to calculate solid/fluid parameter value. Temperature value must be a positive integer divisible by 10:\n")
    try:
        int(max_temperature)
        if int(max_temperature) > 0 and int(max_temperature) % 10 == 0:
            break
        else:
            print "\nThis is not a positive integer divisible by 10!"
            continue
    except ValueError:
        print "\nThis is not a positive integer divisible by 10!"


# reading maximal temperature which is any real number: disabled for Converge use

"""max_temperature = 0
while True:
    max_temperature = raw_input("\nPlease insert maximal temperature for which you want to calculate solid/fluid parameter value: \n")
    try:
        int(max_temperature)
        if int(max_temperature) > int(min_temperature):
            break
        else:
            print "\nMaximal temperature is lower than or equal to minimal temperature!"
            continue
    except ValueError:
         try:
            float(max_temperature)
            if float(max_temperature) > float(min_temperature):
                break
            else:
                print "\nMaximal temperature is lower than or equal to minimal temperature!"
                continue
         except ValueError:
            print "\nThis is not a number!" """


# reading the number of points: disabled for Converge use

"""points_number = 0
while True:
    points_number = raw_input("\nPlease insert a number of points for which you want to calculate solid/fluid parameter values: \n")
    try:
        int(points_number)
        if int(points_number) > 0:
            break
        else:
            print "\nThis is not a positive integer!"
            continue
    except ValueError:
        print "\nThis is not an integer!" """


# positions to inter/extrapolate when a temperature step is equal to 10: enabled for Converge use

points_number = int(max_temperature)/10
x = range(0,int(max_temperature)+10, 10)


# positions to inter/extrapolate which are any real numbers in the specified range: disabled for Converge use

"""x = np.linspace(float(min_temperature), float(max_temperature), num=points_number, endpoint=True)"""


# interpolation/extrapolation, printing graphs and saving results to output file

ready_status = 0
while ready_status != 'y' and ready_status != 'Y' and ready_status != 'n' and ready_status != 'N':
    ready_status = raw_input("\nDo you want to take a look of a comparison of the results obtained with different types of spline? [Y]\[N]\n")

order = 0
if ready_status == 'y' or ready_status == 'Y':
    plt.figure()
    plt.plot(known_temperatures_list, known_parameter_values_list, 'o')
    for order_number in range(1, 4):
        s = InterpolatedUnivariateSpline(known_temperatures_list, known_parameter_values_list, k=order_number)
        y = s(x)
        plt.plot(x, y)
    plt.legend(['data', 'linear', 'quadratic', 'cubic'], loc='best')
    print "\nWhen you are ready, close the graph to continue."
    plt.show()

    while True:
        print "\nWhat type of a spline would you like to use to interpolate/extrapolate values of solid/fluid parameter? \n"
        order = raw_input(" [1] linear \n [2] quadratic \n [3] cubic \n\n")
        if order == '1' or order == '2' or order == '3':
            break
        else:
            print "\nChoose again the type of the spline."

    plt.figure()
    plt.plot(known_temperatures_list, known_parameter_values_list, 'o')
    s = InterpolatedUnivariateSpline(known_temperatures_list, known_parameter_values_list, k=order)
    y = s(x)
    y_list = [s(i) for i in x]
    df = DataFrame({'Temperature': x, 'Parameter': y_list})
    df.to_excel('output_calculated_values.xlsx', sheet_name='Parameter1', index=False, columns=['Temperature', 'Parameter'])
    plt.plot(x, y)
    plt.legend(['data', 'parameter values'], loc='best')
    print "\nResults have been saved to the output_calculated_values.xlsx file.\n"
    print "Close the graph and press ENTER to exit the calculator."
    plt.show()
    closeInput = raw_input()

if ready_status == 'n' or ready_status == 'N':
    while True:
        print "\nWhat type of a spline would you like to use to interpolate/extrapolate values of solid/fluid parameter? \n"
        order = raw_input(" [1] linear \n [2] quadratic \n [3] cubic \n\n")
        if order == '1' or order == '2' or order == '3':
            break
        else:
            print "\nChoose again the type of the spline."

    plt.figure()
    plt.plot(known_temperatures_list, known_parameter_values_list, 'o')
    s = InterpolatedUnivariateSpline(known_temperatures_list, known_parameter_values_list, k=order)
    y = s(x)
    y_list = [s(i) for i in x]
    df = DataFrame({'Temperature': x, 'Parameter': y_list})
    df.to_excel('output_calculated_values.xlsx', sheet_name='Parameter1', index=False, columns=['Temperature', 'Parameter'])
    plt.plot(x, y)
    plt.legend(['data', 'parameter values'], loc='best')
    print "\nResults have been saved to the output_calculated_values.xlsx file.\n"
    print "Close the graph and press ENTER to exit the calculator."
    plt.show()
    closeInput = raw_input()
