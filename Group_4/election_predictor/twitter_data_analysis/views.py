from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .location_dataanalysis import get_stats_for_location
from .data_analysis import get_stats
import pandas as pd
from authentication.models import Usertype, Party
from django.http import HttpResponse, HttpResponseRedirect
import uuid
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def stats(request):
    usertype = Usertype.objects.get(user_id=request.user.pk)
    if usertype.is_party:
        profile = Party.objects.get(party__user_id=usertype.pk)
        if profile.name == 'bjp' or profile.name == 'congress':
            temp = profile.credit_amount
            bal = float(temp) - float(200)
            if float(bal) >= 0:
                name = profile.name
                complete = pd.read_csv(os.path.join(os.path.join(BASE_DIR, 'tweets'), 'cleaned_political_tweets.csv'))
                #print(complete.head())
                pos_stats, neg_stats, opp_pos_count, opp_neg_count, opp_name, pos_hash, neg_hash = get_stats(complete,name)  # send to django
                pos_avg_len = pos_stats['avg_text_len']
                neg_avg_len = neg_stats['avg_text_len']
                party_pos_count = pos_stats['count']
                party_neg_count = neg_stats['count']
                g1_y = [party_pos_count, party_neg_count]
                p = 'p'
                n = 'n'
                g1_x = [p, n]
                g2_y = [party_pos_count, opp_pos_count]
                g2_x = [name, opp_name]
                g3_y = [party_neg_count, opp_neg_count]
                g3_x = [name, opp_name]
                g4_y = [party_pos_count + party_neg_count, opp_pos_count + opp_neg_count]
                g4_x = [name, opp_name]
                pos_words = pos_stats['freq_words']
                neg_words = neg_stats['freq_words']
                lead = party_pos_count - party_neg_count - opp_pos_count + opp_neg_count
                context = {'g1_x': g1_x, 'g1_y': g1_y, 'g2_x': g2_x, 'g2_y': g2_y, 'g3_x': g3_x, 'g3_y': g3_y, 'g4_x': g4_x,
                           'g4_y': g4_y, 'pos_avg_lev': pos_avg_len,
                           'profile': profile, 'neg_avg_len': neg_avg_len, 'pos_words': pos_words,
                           'neg_words': neg_words,
                           'pos_hash': pos_hash, 'neg_hash': neg_hash, 'lead':lead}
                profile.credit_amount = bal
                profile.save()
                return render(request, 'twitter_data_analysis/stats.html', context)
            else:
                return render(request, 'party/data_analysis.html',
                              {'profile': profile, 'error': 'You don\'t have enough credits'})
        else:
            return render(request, 'party/data_analysis.html', {'profile': profile, 'error': 'Your party name is bjp or congress'})


def polarity_analysis_location(request, location=None):
    if location:
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_party:
            profile = Party.objects.get(party__user_id=usertype.pk)
            if profile.credit_amount > 50:
                stats, hashtags, personalities, values = get_stats_for_location(location)
                count = stats['count']
                avg_len = stats['avg_text_len']
                words = stats['freq_words']
                profile.credit_amount = profile.credit_amount - 50
                profile.save()
                mylist = zip(personalities,values)
                return render(request, 'twitter_data_analysis/location_stats.html', {'hashtags': hashtags, 'count':count,'avg_len':avg_len,'words':words,'mylist':mylist})
            else:
                return render(request, 'party/data_analysis.html',
                              {'profile': profile, 'error': 'You don\'t have enough credits'})
