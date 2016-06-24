from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

front = Blueprint('frontend', __name__, template_folder="templates")

@front.route('/')
def hello_world():
	return render_template('index.html')

@front.route('/team/<int:number>')
def team(number):
	return render_template('team.html', number=number)
