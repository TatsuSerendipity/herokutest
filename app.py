from flask import Flask, render_template, request
from model import RHR_scraping

app = Flask(__name__)


@app.route('/')
def top():
    return render_template('expect.html')


@app.route('/', methods=['POST'])
def expect():
    data = RHR_scraping.scraip(request.form['number'])
    return render_template('result.html', data=data, racenum=request.form['number'])


if __name__ == '__main__':
    app.run()
