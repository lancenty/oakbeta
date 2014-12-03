__author__ = 'Lancent'

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)