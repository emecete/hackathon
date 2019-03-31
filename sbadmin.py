#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory, redirect
import jinja2.exceptions
from markupsafe import Markup

from generated_html import heading_panel

app = Flask(__name__)


@app.route('/')
def index():
    """
    API main page
    :return: html 'index.html' from templates folder to be shown in the browser
    """
    return render_template('index.html', heading_panel=Markup(heading_panel()))


@app.route('/<pagename>')
def admin(pagename):
    if pagename == 'index':
        return redirect('/')
    else:
        return render_template(pagename + '.html')


@app.route('/rankings')
def rankings():
    """
    API rankings page, where it will be shown different influencers rankings
    :return: html 'rankings.html' from templates folder to be shown in the browser
    """
    return render_template('rankings.html',
                           main_ranking_table=Markup("""
                            <thead>
                        <tr>
                            <th>#</th>
                            <th>User</th>
                            <th>Followers</th>
                            <th>Total likes</th>
                        </tr>
                        </thead>"""))


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.route('/test')
def test():
    return '<strong>It\'s Alive!</strong>'


@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)


@app.errorhandler(404)
def not_found(e):
    return '<strong>Page Not Found!</strong>', 404


if __name__ == '__main__':
    app.run()
