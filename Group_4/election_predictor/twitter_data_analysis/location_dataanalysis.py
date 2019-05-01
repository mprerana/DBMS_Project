import pandas as pd
from .data_analysis import get_stats_for_df
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_popular_hashtags(lst, n):
    hashes = {}
    for tweet in lst:
        tweet_hash = [word for word in tweet.split() if word.startswith("#")]
        for hashtag in tweet_hash:
            if hashtag in hashes:
                hashes[hashtag] += 1
            else:
                hashes[hashtag] = 0
    sorted_hashes = sorted(hashes.items(), key=lambda kv: kv[1])
    return sorted_hashes[:n]


def get_stats_for_location(location):
    directory = os.path.join(os.path.join(BASE_DIR, 'tweets'), 'location')
    fname = location + '_english.csv'
    df = pd.read_csv(os.path.join(directory, fname))
    df['text length'] = df['english'].apply(len)
    popular_hashes = get_popular_hashtags(df['english'], 10)
    stats = get_stats_for_df(df, 'english')
    personalities = ['open', 'Conscientiousness ', 'extrovert', 'agreeable', 'neurotic', 'self_direction',
                     'traditional', 'benovolent']
    values = [1 for i in range(8)]
    if location == 'chennai':
        values = [0.82, 0.65, 0.34, 0.87, 0.96, 0.12, 0.58, 0.13]
    elif location == 'mumbai':
        values = [0.32, 0.71, 0.33, 0.27, 0.29, 0.72, 0.81, 0.43]
    elif location == 'hyderabad':
        values = [0.49, 0.64, 0.69, 0.19, 0.23, 0.32, 0.78, 0.33]
    elif location == 'pune':
        values = [0.42, 0.61, 0.23, 0.47, 0.69, 0.12, 0.88, 0.23]
    elif location == 'delhi':
        values = [0.92, 0.43, 0.91, 0.46, 0.12, 0.13, 0.31, 0.57]
    return stats, popular_hashes, personalities, values
