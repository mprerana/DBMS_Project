import pandas as pd

a = pd.read_csv("movies.csv")
b = pd.read_csv("movie_reviews.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='title')
c=pd.read_csv("movie_genre.csv")
c=c.dropna(axis=1)
merged1=merged.merge(c,on='title')
d=pd.read_csv("movies_dir.csv")
d=d.dropna(axis=1)
merged2=merged1.merge(d,on='title')
merged2.to_csv("output.csv", index=False)