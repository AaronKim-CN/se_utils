# -*- coding: utf-8 -*-
import pandas as pd

def mergetwofile(file1, file2, outputfile):
    data1 = pd.read_csv(file1,dtype=str)
    data2 = pd.read_csv(file2,dtype=str)

    out = data1.append(data2)
    out.to_csv(outputfile, index=False)
    

if __name__ == '__main__' :

    folder = '/pass/'
    file1 = folder + 'file0.csv'
    file2 = folder + 'file1.csv'
    output = folder + 'output.csv'
    
    mergetwofile(file1, file2, output)
