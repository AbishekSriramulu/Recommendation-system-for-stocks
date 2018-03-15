import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

style.use('ggplot')
def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['AAP'].plot()
    #plt.show()
    df_corr = df.corr()
    data = df_corr.values
    fig = plt.figure()
    ax= fig.add_subplot(1,1,1)
    heatmap = ax.pcolor(data, cmap= plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor= False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor= False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    colum_labels = df_corr.columns
    row_labels = df_corr.index
    ax.set_xticklabels(colum_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.savefig("correlations.png", dpi = (300))
    plt.show()

visualize_data()