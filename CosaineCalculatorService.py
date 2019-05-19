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
    return math.sqrt(sum)

def getRatingFile():
    df,allusers,pandaarray,pandacountarray = fr.DataSetBuilder()
    return df,list(allusers),pandaarray,pandacountarray

def filterRatesByUser(user,rates):
    rates_local = rates.loc[rates['user'] == user]
    ratesList = list(rates_local['rating'])
    return ratesList

def cartesianproduct(user1,user2,pandaarray,allusers, rates):
    range_of = pandaarray[allusers.index(user1)][allusers.index(user2)]
    sum = 0
    for movie in range_of:
        usr1_rating = rates.loc[str(user1) + '_' + str(movie), 'rating']
        usr2_rating = rates.loc[str(user2) + '_' + str(movie), 'rating']
        sum = sum + usr1_rating * usr2_rating
    return sum

def distanceCosaine(user1,user2,rates, pandaarray,allusers):
    denominador = getNorma(filterRatesByUser(user1,rates)) * getNorma(filterRatesByUser(user2,rates))
    numerador = cartesianproduct(user1, user2, pandaarray,allusers, rates)
    if(denominador == 0):
        denominador = 100000000
    return numerador/denominador

def generalDistanceMatrix(allusers,rates, pandaarray):
    matrix = []
    for user1 in allusers:
        row = []
        for user2 in allusers:
            row.append(distanceCosaine(user1,user2,rates,pandaarray,allusers))
        matrix.append(row)
    return(pd.DataFrame(matrix))
