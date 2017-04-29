'''
Created on Apr 27, 2017

@author: chewysano
'''

from flask import Flask, render_template
from ui.web.pageconfig import countries


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', countries=countries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)