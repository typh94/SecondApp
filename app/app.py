from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  #  return 'Welcome to My First Flask Website!'
    return render_template('main/base.html')

@app.route('/about')
def about():
    return render_template('main/about.html')

@app.route('/contact')
def contact():
    return render_template('main/contact.html')
    
@app.route('/projects')
def projects():
    return render_template('main/projects.html')


if __name__ == '__main__':
#  app.run(host='127.0.0.1', port=5000)
    app.run(debug= True)
