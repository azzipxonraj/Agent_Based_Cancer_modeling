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


def overlay_plot(csv_file, N_max, b, c, max_steps):
    df = pd.read_csv(csv_file, header=None)
    gompertz_values = [gompertz(t, N_max, b, c) for t in range(max_steps)]

    fig = plt.figure()
    plt.plot(df, label='Tumor cell growth - simulation')
    plt.plot(gompertz_values, label='Tumor cell growth - Gompertz prediction')
    plt.legend()
    plt.xlabel('Time in days')
    plt.ylabel('Tumor cell amount')
    plt.title('Simulatie vs Gompertz-model')

    return fig


def comparing_plots(N_max, b, c, max_steps):
    plot_tumor_h = plot_tumor_history(csv_file="tumor_history.csv")
    # temp values for now.
    plot_tumor_g = gompertz_plot(N_max=N_max, b=b, c=c, max_steps=max_steps)
    overlay_p = overlay_plot("tumor_history.csv", N_max=N_max, b=b, c=c, max_steps=max_steps)
    write_pdf("tumor_analysis.pdf", [plot_tumor_h, plot_tumor_g, overlay_p])