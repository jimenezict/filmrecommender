# filmrecommender
Another example code for recommendations based on distance algorithm for cheating in your Data Science homeworks

Thanks again to datasets of Kaggle: https://www.kaggle.com/c/movie/data, 

Get the training_ratings_for_kaggle_comp.csv and the movies.dat files and paste them on your local environment

For practising you have some parameters you can modify on the constant.py file:

NUM_OF_ROWS_RATING = 1000 -> don't overstress your computer getting so much values from the rating file
USER = int(2788) -> User Id we want to recommend to
RECOMMENDER_TYPE = 'D' -> By Now it is only distance, on the close future, also Pearson
ELEVATED = 2 -> Elevation factor for distance calculation -> 1 Manhattan, 2 Euclidian, ....

Code description will appear soon on www.blog.dataontheroad.com
