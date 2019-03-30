#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory
import jinja2.exceptions
from markupsafe import Markup

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.route('/rankings')
def rankings():
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
