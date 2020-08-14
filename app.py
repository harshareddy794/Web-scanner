from flask import Flask, render_template
from spyder import crawler

app = Flask(__name__)

@app.route('/')
def home():  
    return render_template('index.html')

@app.route('/portscanner')
def scan():
    return 'This is prot scanning page'

@app.route('/spyder')
def spyder():
    return render_template('spyder.html')
    # data=opt

@app.route('/spyder-result',methods = ['POST'])
def spyder_result():
       if request.method == 'POST':
           result = request.form
           return result

if __name__ == '__main__':
   app.run()