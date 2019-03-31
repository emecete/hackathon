import plotly
import plotly.graph_objs as go
import pymongo
import pandas as pd
import numpy as np
import json
from collections import Counter

from utils import get_hashtags_from_meta

myclient = pymongo.MongoClient("mongodb://localhost:32769/")
mydb = myclient["ocupa2"]


def create_plot():
    trace1 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[0, 2, 3, 5],
        fill='tozeroy'
    )
    trace2 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[3, 5, 1, 7],
        fill='tonexty'
    )
    data = [trace1, trace2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def graph_posts_per_hashtag(meta):
    mycol = mydb["posts"]
    hashtags = get_hashtags_from_meta(meta)
    y = []
    for hashtag in hashtags:
        hashtag = hashtag.replace('#', '')
        y.append(len(list(mycol.find({'hashtags': hashtag}))))
    print(hashtags)
    data = [go.Bar(
        x=hashtags,
        y=y
    )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def get_statistics_graph():
    mycol = mydb["usage"]
    query = {'date': 1, '_id': 0}
    dates = list(mycol.find({}, query))
    dates_list = []
    for date in dates:
        dates_list.append(date['date'])
    counts = Counter(dates_list)
    trace1 = go.Scatter(
        x=list((count[0] for count in counts)),
        y=list((count[1] for count in counts)),
        fill='tozeroy'
    )
    data = [trace1]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
