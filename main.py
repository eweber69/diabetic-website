from flask import Flask, render_template
import matplotlib.pyplot as plt
import csv
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Instantiate a Flask app
app = Flask(__name__)


# Route and render template
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/week')
def past_week():
    return render_template('week.html')


@app.route('/History')
def history():
    return render_template('History.html')


def six_august():
    x = []
    y = []
    with open('2020-08-06.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            y.append(float(row[2]))
            x.append(float(row[1]))
    plt.plot(x, y)
    plt.xlabel('Time of Day')
    plt.ylabel('BGL Reading')
    plt.title('BGL Readings 6th of\nAugust')
    plt.gcf().autofmt_xdate()
    plt.show()


def seven_august():
    x = []
    y = []
    with open('2020-08-07.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            y.append(float(row[1]))
            x.append(float(row[0]))
    plt.plot(x, y)
    plt.xlabel('Time of Day')
    plt.ylabel('BGL Reading')
    plt.title('BGL Readings 7th of\nAugust')
    plt.gcf().autofmt_xdate()
    plt.show()


six_august()
seven_august()
