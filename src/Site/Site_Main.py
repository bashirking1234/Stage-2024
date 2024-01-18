#Site_Main Copyright (C) 2023 Tom van der Greft
import os
from flask import Flask, render_template, request, send_file, url_for
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)
global real
global bagging
global poisson
global decisio

@app.route("/")
@app.route("/Homepage.html")
def homePage():
    """
    Geeft een render template van de homepagina
    """
    return render_template("Homepage.html")


@app.route("/Posterpage.html")
def uitlegPage():
    """
    Geeft een render template van de uitlegpagina
    """
    return render_template("Posterpage.html")

@app.route('/Downloads.html')
def downloadpage():

    return render_template("Downloads.html")

@app.route('/Documentation.html')
def documentpage():

    return render_template("Documentation.html")


@app.route('/Voorspellers.html')
def upload_file():
    """
    Functie om een excel bestand in te lezen, werkt met alle formatten van excel
    """
    return render_template("Voorspellers.html")

@app.route("/Resultaatpage.html", methods=['GET', 'POST'])
def plot():
    global real
    global bagging
    global poisson
    global decision

    if request.form.get('action1') == 'Werkelijkheid Aan/Uit':
        real = not real

    elif request.form.get('action2') == 'Bagging Aan/Uit':
        bagging = not bagging

    elif request.form.get('action3') == 'Poisson Aan/Uit':
        poisson = not poisson

    elif request.form.get('action4') == 'Decision Tree Aan/Uit':
        decision = not decision

    elif request.form.get('action5') == 'Reset grafiek':
        real, bagging, poisson, decision = True, True, True, True

    else:
        real, bagging, poisson, decision = True, True, True, True

    create_figure()
    return render_template('Resultaatpage.html',
                           url='/static/images/new_plot.png')

@app.route("/Aboutpage.html")
def about():

    return render_template('Aboutpage.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Geeft een render template van de 404 pagina als
    er iets mis gaat met het laden van een pagina
    """
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def generate(length):
    i = 0
    blank_list = []
    while i < length:
        blank_list.append(0)
        i+=1
    return blank_list
def create_figure():

    global real
    global bagging
    global poisson
    global decision
    data_pathname = "Data/Site_Data_Top_3_2.0.0.xlsx"

    df = pd.read_excel(data_pathname)

    x1 = df.iloc[:, 1]
    x2 = df.iloc[:, 2]
    x3 = df.iloc[:, 3]
    x4 = df.iloc[:, 4]
    x5 = df.iloc[:, 5]
    x6 = df.iloc[:, 6]
    x7 = df.iloc[:, 7]
    x8 = df.iloc[:, 8]
    y = df.iloc[:, 0]

    if not real:
        x1 = generate(len(x1))
        x5 = generate(len(x1))
    if not bagging:
        x2 = generate(len(x1))
        x6 = generate(len(x1))
    if not poisson:
        x3 = generate(len(x1))
        x7 = generate(len(x1))
    if not decision:
        x4 = generate(len(x1))
        x8 = generate(len(x1))

    ind = np.arange(5)

    # set width of bar
    barWidth = 0.25


    # Set position of bar on X axis
    br1 = np.arange(len(x1))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br58 = [x + (barWidth/2) for x in br2]


    # Make the plot
    fig, ax1 = plt.subplots(figsize=(32, 16))

    ax1.set_xlabel('Predictiedatum', fontweight='bold', fontsize=15)
    ax1.set_ylabel('Aantal nieuwe Covid-19 gevallen', fontweight='bold',
                   fontsize=15)
    ax1.set_xticks([r + barWidth for r in range(len(x1))], y, rotation = 45)
    ax1.tick_params(axis='y', labelcolor='black')


    ax1.bar(br1, x1, color='#96CA5A', width=barWidth,
            edgecolor='grey', label='Werkelijkheid')
    ax1.bar(br2, x2, color='#F1CB43', width=barWidth,
            edgecolor='grey', label='Predictie Bagging regressor')
    ax1.bar(br3, x3, color='#54A1E5', width=barWidth,
            edgecolor='grey', label='Predictie Poisson regressor')
    ax1.bar(br4, x4, color='#DF2A25', width=barWidth,
            edgecolor='grey', label='Predictie Decision Tree regressor')
    ax1.legend(loc='upper left')
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Logaritmisch aantal nieuwe Covid-19 gevallen',
                   fontweight='bold', fontsize=15)
    ax2.set_ylim(0, 6)

    ax2.plot(br58, x5, color='#96CA5A', label='Werkelijkheid Logaritmisch')
    ax2.plot(br58, x6, color='#F1CB43', label='Predictie Logaritmisch Bagging regressor')
    ax2.plot(br58, x7, color='#54A1E5', label='Predictie Logaritmisch Poisson regressor')
    ax2.plot(br58, x8, color='#DF2A25', label='Predictie Logaritmisch Decision Tree regressor')

    ax2.legend(loc='upper right')

    ax2.tick_params(axis='y', labelcolor='black')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped


    os.remove('static/images/new_plot.png')
    plt.savefig('static/images/new_plot.png')
    plt.close()

@app.route('/download_data')
def download_data():
    path = 'static/data/01-02-2023_main_covid_19_dataset.xlsx'
    return send_file(path, as_attachment=True)

@app.route('/download_git')
def download_git():
    path = 'static/data/Gitea.zip'
    return send_file(path, as_attachment=True)

@app.route('/download_drive')
def download_drive():
    path = 'static/data/OneDrive.zip'
    return send_file(path, as_attachment=True)



if __name__ == '__main__':
    real, bagging, poisson, decision = True, True, True, True
    app.run(host="0.0.0.0")
    #{{ url_for("homePage") }}
