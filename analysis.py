import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import math

def write_pdf(fname, figures):
    doc = PdfPages(fname)
    for fig in figures:
        fig.savefig(doc, format='pdf')
    doc.close()

def plot_tumor_history(csv_file="tumor_history.csv"):
    df = pd.read_csv(csv_file, header=None)
    fig = plt.figure()
    plt.plot(df)
    plt.xlabel('Time in days')
    plt.ylabel('Tumor cell ammount')
    plt.title('Tumor cell growth over time in days')

    return fig

def gompertz(t, N_max, b, c):
    inside = math.exp(-c * t)
    outside = math.exp(-b * inside)

    return N_max * outside

def gompertz_plot(N_max, b, c, max_steps):
    gompertz_values = [gompertz(t, N_max, b, c) for t in range(max_steps)]
    df = pd.DataFrame(gompertz_values, columns=['tumor_size'])
    fig = plt.figure()
    plt.plot(df)
    plt.xlabel('Time in days')
    plt.ylabel('Tumor cell ammount')

    return fig



def comparing_plots():
    plot_tumor_h = plot_tumor_history(csv_file="tumor_history.csv")
    # temp values for now.
    plot_tumor_g = gompertz_plot(N_max=1, b=1, c=1, max_steps=100)
    write_pdf("tumor_analysis.pdf", [plot_tumor_h, gompertz_plot])