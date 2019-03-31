import json
from pprint import pprint

import pymongo

from utils import get_meta_hashtags, get_hashtags_from_meta

myclient = pymongo.MongoClient("mongodb://localhost:32769/")
mydb = myclient["ocupa2"]
mycol = mydb["posts"]


def heading_panel():
    with open('icons.json') as f:
        icons = json.load(f)
    html = """<div class="row">"""
    print(icons)
    for meta in get_meta_hashtags():
        html += heading_panel_single(str(len(get_hashtags_from_meta(meta))) + ' hashtags', icons[meta], meta)
    html += "</div>"
    return html


def heading_panel_single(number, icon, title):
    html = """
    <div class="col-lg-3 col-md-6">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <div class="row">
                    <div class="col-xs-3">
                        <i class="%s fa-5x"></i>
                    </div>
                    <div class="col-xs-9 text-right">
                        <div class="huge">%s</div>
                        <div>%s</div>
                    </div>
                </div>
            </div>
            <a href="%s">
                <div class="panel-footer">
                    <span class="pull-left">View Details</span>
                    <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                </div>
            </a>
        </div>
    </div>""" % (icon, title, number, 'meta-' + title)
    return html


def meta_hashtags():
    html = ""
    for meta in get_meta_hashtags():
        html += "<li><a href=\"/meta-" + meta + "\">" + meta + "</a></li>\n"
    return html


def generate_top_ranking_table():
    html = """<thead>
                        <tr>
                            <th>User</th>
                            <th>Followers</th>
                            <th>Media count</th>
                        </tr>
                        </thead>"""
    query = {'user': 1, '_id': 0}
    users = list(mycol.find({}, query).distinct('user'))
    print(users)
    users = sorted(users, key=lambda k: k['followerCount'], reverse=True)
    for user in users:
        html += '<tr><td>' + str(user['username']) + '</td><td>' + str(user['followerCount']) + '</td><td>' + str(
            user['mediaCount']) + '</td><tr>'

    return html


def generate_hashtag_ranking_table(hashtag):
    html = """<thead>
                         <tr>
                             <th>User</th>
                             <th>Followers</th>
                             <th>Media count</th>
                         </tr>
                         </thead>"""
    query = {'user': 1, '_id': 0}
    users = list(mycol.find({'hashtags': hashtag}, query).distinct('user'))
    users = sorted(users, key=lambda k: k['followerCount'], reverse=True)
    for user in users:
        html += '<tr><td>' + str(user['username']) + '</td><td>' + str(user['followerCount']) + '</td><td>' + str(
            user['mediaCount']) + '</td><tr>'

    return html
