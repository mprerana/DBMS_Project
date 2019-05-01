import pandas as pd
import random
import numpy
from nltk.corpus import stopwords
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

stops = set(stopwords.words("english"))


def get_len_min_max_mean(lst):
    total = len(lst)
    avgl = lst.mean()
    return total, avgl


def get_most_frequent(n, lst):
    wordcount = list(pd.Series(' '.join(lst).split()).value_counts()[:n].keys())
    return wordcount


def get_most_important(n, lst):
    tfidf = TfidfVectorizer(stop_words='english', max_features=n)
    tf = tfidf.fit_transform(lst)
    feature_array = tfidf.get_feature_names()
    return list(feature_array)


def get_stats_for_df(dataF, col='tweet'):
    reviews, avg = get_len_min_max_mean(dataF['text length'])  # send to django
    dataF = dataF.drop_duplicates(subset=[col])
    wc = get_most_important(50, dataF[col])  # send to django
    df_stats = {'count': reviews, 'avg_text_len': avg, 'freq_words': wc}
    return dict(df_stats)


def get_stats(complete, name):
    complete = complete.dropna()
    print(complete['party'].nunique)
    complete['text length'] = complete['tweet'].apply(len)
    opp_party = complete[complete['party'] != name]
    party = complete[complete['party'] == name]
    mvdf = party.copy()
    mvpdf = mvdf[mvdf['polarity'] == 'p']
    mvndf = mvdf[mvdf['polarity'] == 'n']
    pos_stats = get_stats_for_df(mvpdf)
    neg_stats = get_stats_for_df(mvndf)
    print(opp_party.head())
    print(len(opp_party))
    opp_pos = len(opp_party[opp_party['polarity'] == 'p'])
    opp_neg = len(opp_party[opp_party['polarity'] == 'n'])
    opp_name = list(opp_party['party'])[0]
    pos_hash = list(mvpdf['hashtag'].unique())
    neg_hash = list(mvndf['hashtag'].unique())
    return pos_stats, neg_stats, opp_pos, opp_neg, opp_name, pos_hash, neg_hash
