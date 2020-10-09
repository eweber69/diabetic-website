import jinja2
import pandas as pd
import matplotlib.pyplot as plt
import csv
from flask import Flask, render_template

# Instantiate a Flask app
app = Flask(__name__)


# Route and render template
@app.route('/')
def index():
    return render_template('index.html')


def graph():
    plt.figure(figsize=(9, 7))
    x = []
    y = []
    with open('readings.csv') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
    plt.subplot(2, 1, 1)
    plt.plot(x, y, marker='o')
    plt.xlabel('Time of Day')
    plt.ylabel('BGL Reading')
    plt.title('BGL Readings 1st of\nAugust')
    plt.xticks(range(1, 32))

    mpld3.show()