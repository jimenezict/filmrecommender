import FilesReader as fr
import math
import pandas as pd

df = []
allusers = []
pandaarray  = []
pandacountarray = []

def generalDistanceMatrix(allusers,n):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            ##row.append(distanceExponential(n,user1,user2))
            ## TO BE IMPLEMENTED
        matrix.append(row)
    return(pd.DataFrame(matrix))