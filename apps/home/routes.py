# -*- encoding: utf-8 -*-

from apps.home import blueprint
from flask import render_template, redirect, request, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound

#@login_required 각 함수마다 존재하였으나, 로그인 기능 업앨 예정

@blueprint.route('/')
def route_default():
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/index')
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


