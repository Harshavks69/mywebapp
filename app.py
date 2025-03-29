from flask import Flask, render_template

app = Flask(__name__)  # No need for template_folder if using default 'templates'

@app.route('/')
def home():
    return render_template('index.html')  # Looks in templates/ automatically

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)