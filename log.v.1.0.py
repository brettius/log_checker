#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt


#User menu

def main():


    print('logb: enter "h" to view a list of commands')
    run_program = 'run'
    while run_program == 'run':
        user_input = get_user_input()
        if user_input == ('h'):
            help_menu()
        elif user_input == ('ls'):
            current_files()
        elif user_input == ('i'):
            open_a_log()
        elif user_input.lower() == ('q'):
            run_program == 'stop'
            break
        else:
            print('logb: command not found:',(user_input) + '.'+ ' Enter h for help')

#Perform scan

def scan_log(imported_log):
    print('logb Health Check:')
    print('\nERRORS\n')

    counted_errors = (error_count(imported_log, 'error'))
    counted_warnings = (error_count(imported_log, 'warning'))
    counted_warnings = (error_count(imported_log, 'critical'))

    print('\nTRACEBACK OBJECTS\n')

    counted_python_warnings = (python_error_count(imported_log, 'arithmeticerror'))
    counted_python_warnings = (python_error_count(imported_log, 'assertionerror'))
    counted_python_warnings = (python_error_count(imported_log, 'attributeerror'))

#Search log for common keywords

def error_count(imported_log, keyword):
    counted_keyword = 0
    for item in imported_log:
        if item.lower() == keyword:
            counted_keyword = counted_keyword + 1
    print(counted_keyword, ' ' ,keyword.upper() + 'S' )
    return keyword, counted_keyword

def python_error_count(imported_log, keyword):
    counted_keyword = 0
    for item in imported_log:
        if item.lower() == keyword:
            counted_keyword = counted_keyword + 1
        if counted_keyword > 0:
            print(counted_keyword, ' ' ,keyword.upper())
            return keyword, counted_keyword

#Open, get user input, print help menu

def open_a_log():
    select_file = input('Enter logname: ')
    if select_file != 0:
        try:
            infile = open(select_file, 'r')
            contents_of_file = infile.read()
            infile.close()
            processed_log = contents_of_file.split()
            print(processed_log)
            scanned_log = (scan_log(processed_log))

            return processed_log
        except:
            print('Log not found')

def get_user_input():
    user_input = input('logb:')
    return user_input

def help_menu():
    print('\nlogb usage:\n')
    print('   h:      help menu')
    print('   i:      import a log')
    print('   ls:     list files in directory')
    print('   q:      exit program\n')

def current_files():
    file_list = os.listdir()
    for file in file_list:
        print(file)

main()

#To do
#most_commonm()
#https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
#Then filer out out and or and the
