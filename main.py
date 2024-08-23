from flask import Flask, render_template, url_for






app = Flask(__name__)
app.config['SECRET_KEY'] = 'VHHS'



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/club')
def club():
    return render_template("club.html")

@app.route('/vend')
def vend():
    return render_template("vend.html")


@app.route('/gwc')
def gwc():
    return render_template("gwc.html")

@app.route('/xp')
def xp():
    return render_template("xp.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/exec')
def exec():
    return render_template("exec.html")

@app.route('/steam')
def steam():
    return render_template("steam.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)