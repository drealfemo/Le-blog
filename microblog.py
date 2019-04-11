from app import create_app, db
from app.models import User, Post

app = create_app()

# shell context function to make database available in flask shell environment
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
