from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

rest = Blueprint('RESTful', __name__, template_folder='templates')
