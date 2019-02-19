import FileReaders as fr
import math
import pandas as pd

df = []
allusers = []
pandaarray  = []
pandacountarray = []

def getRatingFile():

    df,allusers,pandaarray,pandacountarray = fr.DataSetBuilder()

    print('Array of matching films:')
    print(pandaarray)
    print('-------------------')
    print('Count of matching films:')
    print(pandacountarray)
    print('-------------------')
    print(allusers)
    print('-------------------')

    return df,list(allusers),pandaarray,pandacountarray


def distanceExponential(pwd,user1,user2):
    sum = 0
    for movie in pandaarray[allusers.index(user1)][allusers.index(user2)]:
        usr1_rating = df.loc[str(user1) + '_' + str(movie), 'rating']
        usr2_rating = df.loc[str(user2) + '_' + str(movie), 'rating']
        sum = sum + abs(usr1_rating - usr2_rating)**pwd
    return round(math.pow(sum,1/pwd),2)

def manhattanSingle(user1,user2):
    return distanceExponential(1,user1,user2)

df,allusers,pandaarray,pandacountarray = getRatingFile()

def manhattanMatrix(allusers):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            row.append(distanceExponential(1,user1,user2))
        matrix.append(row)
    print(pd.DataFrame(matrix))

def euclidianMatrix(allusers):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            row.append(distanceExponential(2,user1,user2))
        matrix.append(row)
    print(pd.DataFrame(matrix))

def generalDistanceMatrix(allusers,n):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            row.append(distanceExponential(n,user1,user2))
        matrix.append(row)
    print(pd.DataFrame(matrix))

generalDistanceMatrix(allusers,5)