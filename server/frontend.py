from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

front = Blueprint('frontend', __name__, template_folder="templates")
