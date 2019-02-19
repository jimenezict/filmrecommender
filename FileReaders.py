import pandas as pd

ratingsfilename='training_ratings_for_kaggle_comp.csv'
numrows = 5000

def __readfile(name, numrows):
    return pd.read_csv(name, nrows=numrows, index_col='id')

def __getUserRecommendations(df_l, user):
    df_l = df_l.loc[df_l['user'] == user]
    return df_l['movie']

def __getAllUsers(df_l):
    return df_l.user.unique()

def allUserStatistics(df_l):
    for user in __getAllUsers(df_l):
        __getUserRecommendations(df_l,user)

def matchingFilms(df_l, user1, user2):
    list1 = __getUserRecommendations(df_l, user1)
    list2 = __getUserRecommendations(df_l, user2)
    ret_list = []
    for film1 in list1:
        for film2 in list2:
            if (str(film1) == str(film2)):
                ret_list.append(film1)
    return ret_list

def __matchingFilmsByUser(df_l, user):
    retarray = []
    for userinlist in __getAllUsers(df_l):
        if(user != userinlist):
            retarray.append(matchingFilms(df_l, user, userinlist))
        else:
            retarray.append([])
    return retarray

def __matchingCountFilmsByUser(df_l, user):
    retarray = []
    for userinlist in __getAllUsers(df_l):
            retarray.append(matchingFilms(df_l, user, userinlist).__len__())
    return retarray

def DataSetBuilder():
    df = __readfile(ratingsfilename, numrows)
    rawarray = []
    countfilm = []
    for user in __getAllUsers(df):
        rawarray.append(__matchingFilmsByUser(df, user))
        countfilm.append(__matchingCountFilmsByUser(df, user))
    return df,__getAllUsers(df),rawarray,countfilm