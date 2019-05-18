import DistanceCalculatorService as dc
import CosaineCalculatorService as cc
import numpy as np
import pandas as pd
import constant

class RecommendarByDistances:

    def __init__(self):
        n = constant.ELEVATED
        if (constant.RECOMMENDER_TYPE == 'D'):
            self.sourceratings, self.allusers, self.pandaarray, self.pandacountarray = dc.getRatingFile()
            self.distanceMatrix = dc.generalDistanceMatrix(self.allusers, n)
        elif (constant.RECOMMENDER_TYPE == 'C'):
            self.sourceratings, self.allusers, self.pandaarray, self.pandacountarray = cc.getRatingFile()
     #       self.distanceMatrix = cc.generalDistanceMatrix(self.allusers, n)
        else:
            print("Not valid type of recommender")
#
    def __userpositionbyorder(self,pos):
        return self.allusers[pos]

    def __userpositionbyid(self,id):
        return self.allusers.index(id)

    def __getUserRecommendations(self,df_l, user):
        df_l = df_l.loc[df_l['user'] == user]
        return df_l

    # Input: id according to the reference of users list, not the one on df order
    # Output 1: array with the position of the columns with the minimum value excluding 0's (0 means itself
    #   if it is on the diagonal or non similar value if it is not on the diagonal. The output is the position
    #   inside the matrix
    # Output 2: float value with the distance

    def __getCloserUser(self,id):
        user_ini = self.__userpositionbyid(id)
        user_array = np.array(self.distanceMatrix[user_ini])
        ma = np.ma.masked_equal(user_array, 0.0, copy=False)
        return (np.where(user_array == ma.min())[0]), ma.min

    # Similar as __getCloserUser but on the other way around
    #   -> We want to evaluate if negative recommendation of farther users works as good recommendations for
    #   the users

    def __getFartherUser(self,id):
        user_ini = self.__userpositionbyid(id)
        user_array = np.array(self.distanceMatrix[user_ini])
        ma = np.ma.masked_equal(user_array, 0.0, copy=False)
        return (np.where(user_array == ma.max())[0]), ma.max

    def runner(self):

        user1 = constant.USER

        userpos1 = self.__userpositionbyid(user1)
        closerusers = self.__getCloserUser(user1)[0]
        fartherusers = self.__getFartherUser(user1)[0]

        # Generating a dataframe with close/farther users ratings
        closerusersfilmsrating = pd.DataFrame()
        fartherusersfilmsrating = pd.DataFrame()

        for userpos2 in closerusers:
            user2 = self.__userpositionbyorder(userpos2)
            commonfilms = self.pandaarray[userpos1][userpos2]
            user2films = self.__getUserRecommendations(self.sourceratings, user2)
            for filmtopop in commonfilms:
                user2films = user2films.drop(str(user2) + '_' + str(filmtopop))
            closerusersfilmsrating = pd.concat([closerusersfilmsrating,user2films])

        closerusersfilmsrating = closerusersfilmsrating.sort_values(by=['rating','movie'],ascending=False)

        for userpos2 in fartherusers:
            user2 = self.__userpositionbyorder(userpos2)
            commonfilms = self.pandaarray[userpos1][userpos2]
            user2films = self.__getUserRecommendations(self.sourceratings, user2)
            for filmtopop in commonfilms:
                user2films = user2films.drop(str(user2) + '_' + str(filmtopop))
            fartherusersfilmsrating = pd.concat([fartherusersfilmsrating,user2films])

        fartherusersfilmsrating = fartherusersfilmsrating.sort_values(by=['rating','movie'])

        return closerusersfilmsrating.head(10),fartherusersfilmsrating.head(10)