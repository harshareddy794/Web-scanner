from flask import Flask, render_template, request
from lib.port_scanner import scanner
from lib.spyder import crawler

app = Flask(__name__)

@app.route('/')
def home():  
    return render_template('index.html')

@app.route('/portscanner')
def port():
    return render_template('ports.html')

@app.route('/port-result',methods = ['POST'])
def port_result():
       if request.method == 'POST':
            form_data = request.form
            opt=scanner(form_data['url'])
            return render_template('ports.html',data=opt)


@app.route('/spyder')
def spyder():
    return render_template('spyder.html')

@app.route('/spyder-result',methods = ['POST'])
def spyder_result():
       if request.method == 'POST':
            form_data = request.form
            opt=crawler(form_data['url'])
            return render_template('spyder.html',data=opt)
if __name__ == '__main__':
   app.run()