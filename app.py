from flask import render_template
from zuku import app

from zuku import login_manager
from zuku.Models.Accounts import Accounts


@login_manager.user_loader
def load_user(user_id):
    return Accounts.query.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)


