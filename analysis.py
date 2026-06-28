import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
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

def gompertz(max_steps, N_max, c):
    volumes = [1] # we start with 1 since the simulation always starts with 1 tumor cell
    current_V = 1

    for _ in range(max_steps - 1):
        if current_V <= 0:
            dVdt = 0
        else:
            # De formule: dV/dt = a * V * ln(Vmax / (V))
            dVdt = c * current_V * math.log(N_max / current_V)

        # Euler integratie: tel de groei van deze dag op bij het huidige volume
        current_V = current_V + dVdt
        volumes.append(current_V)

    return volumes

def gompertz_plot(N_max, c, max_steps):
    gompertz_values = gompertz(max_steps, N_max, c)
    df = pd.DataFrame(gompertz_values, columns=['tumor_size'])
    fig = plt.figure()
    plt.plot(df)
    plt.xlabel('Time in days')
    plt.ylabel('Tumor cell ammount')

    return fig


def overlay_plot(csv_file, N_max, c, max_steps):
    df = pd.read_csv(csv_file, header=None)
    gompertz_values = gompertz(max_steps, N_max, c)

    fig = plt.figure()
    plt.plot(df, label='Tumor cell growth - simulation')
    plt.plot(gompertz_values, label='Tumor cell growth - Gompertz prediction')
    plt.legend()
    plt.xlabel('Time in days')
    plt.ylabel('Tumor cell amount')
    plt.title('Simulatie vs Gompertz-model')

    return fig


def comparing_plots(N_max, c, max_steps):
    plot_tumor_h = plot_tumor_history(csv_file="tumor_history.csv")
    # temp values for now.
    plot_tumor_g = gompertz_plot(N_max=N_max, c=c, max_steps=max_steps)
    overlay_p = overlay_plot("tumor_history.csv", N_max=N_max, c=c, max_steps=max_steps)
    write_pdf("tumor_analysis.pdf", [plot_tumor_h, plot_tumor_g, overlay_p])