import json 
import csv

def flat(file_path):
    flat={}

    def flat_file(x, flat_key=""):
        if type(x) is dict:
            for current_key in x:
                flat_file(x[current_key],flat_key + current_key + '_' )
        elif type(x) is list:
            i = 0
            for elem in x:
                flat_file(elem, flat_key + str(i) + '_')
            i += 1 
        else:
            flat[flat_key[:-1]] = x 
            