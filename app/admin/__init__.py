from flask import Blueprint

admin = Blueprint("admin", __name__, template_folder="admin_templates")

from .routes import dashboard