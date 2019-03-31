#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory, redirect
import jinja2.exceptions
from markupsafe import Markup

from generated_html import heading_panel, meta_hashtags, generate_top_ranking_table, generate_hashtag_ranking_table
from plotly_graphs import create_plot, graph_posts_per_hashtag, get_statistics_graph
from utils import add_usage

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


if __name__ == '__main__':
    app.run()
