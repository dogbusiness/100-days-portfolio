from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_gravatar import Gravatar

#
app = Flask(__name__)
Bootstrap(app)
gravatar = Gravatar(app, size=300, rating='pg', default='retro',
                    force_default=False, force_lower=False, use_ssl=False, base_url=None)

@app.route('/')
def home():
    return render_template("index.html")



if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(threaded=True, port=5000, debug=False)