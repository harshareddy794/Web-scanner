from flask import Flask, render_template
from spyder import crawler
app = Flask(__name__)

@app.route('/')
def home():  
    return crawler('https://www.sathyabama.ac.in')

@app.route('/portscanner')
def scan():
    return 'This is prot scanning page'

@app.route('/spyder')
def spyder():
    return 'This is web spyder page'

if __name__ == '__main__':
   app.run()