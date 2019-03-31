#!/usr/bin/env python
import os

import PIL
from flask import Flask, url_for, render_template, send_from_directory, redirect, request, make_response
import jinja2.exceptions
from markupsafe import Markup
import urllib.request
from generated_html import heading_panel
import matplotlib.pyplot as plt
import numpy as np

from generated_html import heading_panel, meta_hashtags, generate_top_ranking_table, generate_hashtag_ranking_table
from plotly_graphs import create_plot, graph_posts_per_hashtag, get_statistics_graph
from utils import add_usage

from hackaton.porsche.conv_porsche import classify

app = Flask(__name__)


@app.route('/')
def index():
    """
    API main page
    :return: html 'index.html' from templates folder to be shown in the browser
    """
    add_usage()  # Registers new connection
    return render_template('index.html', hashtag_li=Markup(meta_hashtags()), heading_panel=Markup(heading_panel()))


@app.route('/app_metrics')
def metrics():
    return render_template('app_metrics.html', hashtag_li=Markup(meta_hashtags()), plot=get_statistics_graph())


@app.route('/meta-<hashtag>')
def meta(hashtag):
    return render_template('meta.html', title=hashtag, hashtag_li=Markup(meta_hashtags()),
                           plot=graph_posts_per_hashtag(hashtag),
                           hashtag_ranking_table=Markup(generate_hashtag_ranking_table(hashtag)))


@app.route('/<pagename>')
def admin(pagename):
    if pagename == 'index':
        return redirect('/')
    else:
        return render_template(pagename + '.html', hashtag_li=Markup(meta_hashtags()))


@app.route('/rankings')
def rankings():
    """
    API rankings page, where it will be shown different influencers rankings
    :return: html 'rankings.html' from templates folder to be shown in the browser
    """
    return render_template('rankings.html',
                           main_ranking_table=Markup(generate_top_ranking_table()), hashtag_li=Markup(meta_hashtags()))


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)


@app.errorhandler(404)
def not_found(e):
    return '<strong>Page Not Found!</strong>', 404


@app.route('/classifier', methods=['POST'])
def classifier():
    # getting image
    URL = request.form['URL']
    urllib.request.urlretrieve(URL, "img.jpg")
    img = PIL.Image.open('img.jpg')
    # resizing image
    img = img.resize((612, 612), PIL.Image.ANTIALIAS)
    img = np.array(img)
    # remove temporal image file
    os.remove("img.jpg")
    result = classify(img)
    #result = "It is a Porsche!!"
    content = Markup('<div class="card" style="width:100px"><img class="card-img-top" src= ' + URL + ' alt="Card '
                     'image"  width="550" height="550"><div class="card-body"><h3 class="card-title">' + result + '</h3></div></div>')
    return make_response(
        render_template('porsche_classifier.html', content=content))


if __name__ == '__main__':
    app.run()
