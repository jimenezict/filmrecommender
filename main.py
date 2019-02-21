import RecommenderByDistances as r
import constant
import pandas as pd

pmovies = pd.read_csv(constant.MOVIE_FILE, sep="::",names = ["movie", "title", "Tags"],index_col='movie')

if(constant.RECOMMENDER_TYPE == 'D'):
    recommender = r.RecommendarByDistances()

closerusersfilmsrating,fartherusersfilmsrating = recommender.runner()
merged = pd.merge(closerusersfilmsrating,pmovies,on='movie',how='inner')

for index, row in merged.iterrows():
    print(str(row['user']) + ' recommends you the film ' + row['title'] + ' with a rating of ' + str(row['rating']))