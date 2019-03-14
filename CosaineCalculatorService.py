import FilesReader as fr
import math
import pandas as pd

df = []
allusers = []
pandaarray  = []
pandacountarray = []

# ratingArray - [0,5] Example: ratingArray = 3,2,4,1
def getNorma(ratingArray):
    sum = 0
    for rateuser in ratingArray:
        sum = sum + rateuser**2
    return sum


def getRatingFile():
    print('estudiando para mejorar')
    df,allusers,pandaarray,pandacountarray = fr.DataSetBuilder()
    return df,list(allusers),pandaarray,pandacountarray

def generalDistanceMatrix(allusers,n):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            ##row.append(distanceExponential(n,user1,user2))
            ## TO BE IMPLEMENTED
            print("null")
    return "null"

getNorma([1,2,3,4,5])