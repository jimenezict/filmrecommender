import DistanceCalculatorService as dc
import numpy as np
import pandas as pd
import constant

def __userpositionbyorder(pos):
    return allusers[pos]

def __userpositionbyid(id):
    return allusers.index(id)

def __getUserRecommendations(df_l, user):
    df_l = df_l.loc[df_l['user'] == user]
    return df_l

# Input: id according to the reference of users list, not the one on df order
# Output 1: array with the position of the columns with the minimum value excluding 0's (0 means itself
#   if it is on the diagonal or non similar value if it is not on the diagonal. The output is the position
#   inside the matrix
# Output 2: float value with the distance

def __getCloserUser(id):
    user_ini = __userpositionbyid(id)
    user_array = np.array(distanceMatrix[user_ini])
    ma = np.ma.masked_equal(user_array, 0.0, copy=False)
    return (np.where(user_array == ma.min())[0]), ma.min

# Similar as __getCloserUser but on the other way around
#   -> We want to evaluate if negative recommendation of farther users works as good recommendations for
#   the users

def __getFartherUser(id):
    user_ini = __userpositionbyid(id)
    user_array = np.array(distanceMatrix[user_ini])
    ma = np.ma.masked_equal(user_array, 0.0, copy=False)
    return (np.where(user_array == ma.max())[0]), ma.max

###############################################     MAIN    ###########################################################


def recommenderRunner():
    user1 = constant.USER
    n = constant.ELEVATED

    # Data Loading and distances matrix alculation
    sourceratings,allusers,pandaarray,pandacountarray = dc.getRatingFile()
    distanceMatrix = dc.generalDistanceMatrix(allusers,n)
    userpos1 = __userpositionbyid(user1)
    print('\nRecommending user: ' + str(user1) + ' equivalent to row ' + str(userpos1) + ' of the matrix \n')
    print('distanceMatrix :\n')
    print(distanceMatrix)
    print('----------------')
    closerusers = __getCloserUser(user1)[0]
    fartherusers = __getFartherUser(user1)[0]
    print('The closer/farther user position: ' + str(closerusers) + '/' + str(fartherusers))
    print('----------------')

    # Generating a dataframe with close/farther users ratings
    closerusersfilmsrating = pd.DataFrame()
    fartherusersfilmsrating = pd.DataFrame()

    print('----------------')
    print('Recommending by closer user and positive ratings')
    print('----------------')
    for userpos2 in closerusers:
        user2 = __userpositionbyorder(userpos2)
        commonfilms = pandaarray[userpos1][userpos2]
        print('Common Films between '+ str(user1) + ' and ' + str(user2) + ': ' + str(commonfilms) + ' to be excluded')
        print('----------------')
        user2films = __getUserRecommendations(sourceratings, user2)
        for filmtopop in commonfilms:
            user2films = user2films.drop(str(user2) + '_' + str(filmtopop))
        closerusersfilmsrating = pd.concat([closerusersfilmsrating,user2films])

    closerusersfilmsrating = closerusersfilmsrating.sort_values(by=['rating','movie'],ascending=False)
    print(closerusersfilmsrating.head(10))

    print('----------------')
    print('Recommending by farther user and negative ratings')
    print('----------------')

    for userpos2 in fartherusers:
        user2 = __userpositionbyorder(userpos2)
        commonfilms = pandaarray[userpos1][userpos2]
        print('Common Films between '+ str(user1) + ' and ' + str(user2) + ': ' + str(commonfilms) + ' to be excluded')
        print('----------------')
        user2films = __getUserRecommendations(sourceratings, user2)
        for filmtopop in commonfilms:
            user2films = user2films.drop(str(user2) + '_' + str(filmtopop))
        fartherusersfilmsrating = pd.concat([fartherusersfilmsrating,user2films])

    fartherusersfilmsrating = fartherusersfilmsrating.sort_values(by=['rating','movie'])
    print(fartherusersfilmsrating.head(10))