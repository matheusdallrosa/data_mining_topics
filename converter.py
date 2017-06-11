import sys

import numpy as np
from sklearn import tree

reputation = {'"home"':1,'"reputation"':2,'"course"':3,'"other"':4}

def convert_float(data):
    if type(data) == float or type(data) == int: return data
    if data in reputation: return reputation[data]
    if data == '"U"' or data == '"T"' or data == '"no"' or data == '"F"' or data == '"GP"' or data == '"LE3"': return 0
    if data == '"R"' or data == '"A"' or data == '"yes"' or data == '"M"' or data == '"MS"' or data == '"GT3"': return 1    
    
    if data == '"at_home"': return 0
    if data == '"services"': return 1
    if data == '"health"': return 2
    if data == '"teacher"': return 3
    
    if data == '"other"': return 7
    if data == '"mother"': return 0
    if data == '"father"': return 1
    return data

for row in sys.stdin:
    info = row.split(';')
    new_line = ""
    for i in range(0,30):
        new_line += str(convert_float(info[i]))+";"        
    new_line += info[30].split('"')[1]+";"
    new_line += info[31].split('"')[1]+";"
    final_grade = int(info[32].split('\n')[0])
    if final_grade <= 3: new_line += "1"
    elif final_grade <= 7: new_line += "2"
    elif final_grade <= 13: new_line += "3"
    elif final_grade <= 17: new_line += "4"
    elif final_grade <= 20: new_line += "5"
    print(new_line)