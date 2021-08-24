from flask import Blueprint

usr = Blueprint("usr", __name__, template_folder="usr_templates")

from .routes import home
from .routes.auth import auth