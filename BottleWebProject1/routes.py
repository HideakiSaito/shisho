"""
Routes and views for the bottle application.
"""

from bottle import route, view,template
from datetime import datetime

@route('/hello/<name>')
def hello(name):
  return template("hello {{name}} <div>{{year}}<div>",
                  name=name,
                  year=datetime.now().year)

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    a=1
    b=2
    if (a == 2):
      hogehoge ="true"
    else:
      hogehoge="false"
    return dict(
        year=datetime.now().year,
        hogehoge=hogehoge
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
