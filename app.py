from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except:
        abort(404, description="About page template not found")

@app.route('/services')
def services():
    try:
        return render_template('services.html')
    except:
        abort(404, description="Services page template not found")

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)