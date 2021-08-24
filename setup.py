from app import create_app, db
from app.models import User
from dotenv import load_dotenv
import os

load_dotenv()
app = create_app(os.getenv("FLASK_ENV"))


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
