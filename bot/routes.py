from bot import app
# from bot import models

@app.route("/")
def main():
    return 'models.User.query.get(1).username'