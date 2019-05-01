
from nltk.stem.snowball import SnowballStemmer
from sklearn.externals import joblib
from nltk.corpus import stopwords
import pickle
from autocorrect import spell
import re
import os

DIR = os.path.dirname(__file__)
mov_loca = os.path.join(DIR, 'movie.pickle')

stemmer = SnowballStemmer("english")
mov = pickle.load(open(mov_loca, 'rb'))
stops = set(stopwords.words("english"))


def truncate_multiples(word):
    l = list(word)  # convert to list
    prev = ''
    count = 0
    out = ''
    for i in range(len(l)):
        if l[i] is prev:
            count += 1
            if count > 2:
                count -= 1
            else:
                out = out + l[i]
        else:
            out = out + l[i]
            prev = l[i]
            count = 1
    return out


def cleantext(string):
    text = string.lower()
    text = text.replace("e-mail", "email")
    text = text.replace(" v ", " very ")
    text = text.replace(" r ", ' are ')
    text = re.sub(r"&", ' and ', text)
    text = re.sub(r"[^a-z0-9]+", ' ', text)
    text = re.sub(r"\s+", ' ', text)
    text = text.split()
    text = [truncate_multiples(w) for w in text]
    text = [spell(w) for w in text]
    text = [w for w in text if not w in stops and len(w) >= 2]
    stems = []
    for word in text:
        word = stemmer.stem(word)
        if word != "":
            stems.append(word)
    stemmed = " ".join(stems)
    return stemmed
