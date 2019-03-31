import json

from utils import get_meta_hashtags


def heading_panel():
    with open('icons.json') as f:
        icons = json.load(f)
    html = """<div class="row">"""
    print(icons)
    for meta in get_meta_hashtags():
        meta = meta.replace('hashtags_', '')
        html += heading_panel_single('15', icons[meta], meta)
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
            <a href="#">
                <div class="panel-footer">
                    <span class="pull-left">View Details</span>
                    <span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                </div>
            </a>
        </div>
    </div>""" % (icon, title, number)
    return html
