import sqlalchemy
import pandas as pd
import numpy as np
import sys

logged_in_user = sys.argv[1]

def recc_result(logged_in_user):
    # constants required to connect to the database
    USERNAME = 'root'
    PASS = 'root'
    HOST = 'localhost'
    PORT = 3306
    DATABASE = 'project'

    # connect to the database
    con_string = f'mysql+pymysql://{USERNAME}:{PASS}@{HOST}:{PORT}/{DATABASE}'
    engine = sqlalchemy.create_engine(con_string)


    # a similarity function
    def sim(v1, v2):
        mean = lambda x: sum(x) / len(x)
        
        u1 = v1 - 5
        u2 = v2 - 5
        
        num = sum(u1 * u2)
        denom = (sum(u1 ** 2) * sum(u2 ** 2)) ** 0.5
        
        return num / denom


    # read neceessary tables into pandas
    books = pd.read_sql_table("Books", engine, columns=["ASIN", "Title", "Author", "Category"])
    books.ASIN = books.ASIN.astype(str)
    ratings = pd.read_sql_table("Ratings", engine) # finish this

    # get rating vector of currently logged in user
    req_user = ratings.loc[ratings.UserID == logged_in_user, :]
    semi_sparse_req = pd.merge(req_user, books, how='outer', on='ASIN')[['UserID', 'ASIN', 'Rating']]
    semi_sparse_req.UserID = semi_sparse_req.UserID.fillna(value=logged_in_user)
    semi_sparse_req.Rating = semi_sparse_req.Rating.fillna(value=0)
    semi_sparse_req.Rating = semi_sparse_req.Rating - 2.5
    semi_sparse_req = semi_sparse_req.sort_values('ASIN')
    logged_in_ratings = semi_sparse_req.Ratings.values

    # join userid with userid
    similarity_df = pd.DataFrame(columns=["user1", "user2", "similarity"])

    for user in np.unique(ratings.UserID.values):
        second_user = ratings.loc[ratings.UserID == user, :]
        semi_sparse = pd.merge(second_user, books, on='ASIN', how='outer')[['UserID', 'ASIN', 'Rating']]
        semi_sparse.UserID = semi_sparse.UserID.fillna(value=user)
        semi_sparse.Rating = semi_sparse.Rating.fillna(value=0)
        semi_sparse.Rating = semi_sparse.Rating - 2.5
        semi_sparse = semi_sparse.sort_values('ASIN')
        second_ratings = semi_sparse.Ratings.values

        user1 = logged_in_user
        user2 = user

        similarity_df.loc[similarity_df.shape[0], :] = (user1, user2, sim(logged_in_ratings, second_ratings) * (1 - np.random.random()))

    top_common_users = similarity_df.sort_values('similarity', ascending=False).iloc[1:, :]['user2'][0:3].values
    final_recs = []
    for user in top_common_users:
        final_recs.extend(ratings.loc[ratings.UserID == user, ['Rating', 'ASIN']].sort_values('Rating', ascending=False).iloc[0:3, 1].values)

    print(','.join(final_recs))


if __name__ == "__main__":
	recc_result(sys.argv[1])
