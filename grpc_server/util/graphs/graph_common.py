import os
import io
import time

from matplotlib import pyplot as plt

from grpc_server import constants


# String wrapper to avoid the underscore behavior in legends
#
# In legends, matplotlib ignores labels that begin with _
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
# However, this check is only done for actual string objects.
class StrWrap:
    def __init__(self, s):
        self.string = s
    def __str__(self):
        return self.string

def get_current_figure_as_file():
    filename = f'tempplot_{time.time()}.png'
    filepath = os.path.join(constants.TEMP_DIR, filename)
    plt.savefig(filepath, facecolor=plt.gca().get_facecolor(), bbox_inches='tight', pad_inches=0.25)
    return f'{constants.HOST_NAME}/temp/{filename}'

def plot_rating_bg(ranks):
    ymin, ymax = plt.gca().get_ylim()
    bgcolor = plt.gca().get_facecolor()
    for rank in ranks:
        plt.axhspan(rank.low, rank.high, facecolor=rank.color_graph, alpha=0.8, edgecolor=bgcolor, linewidth=0.5)

    locs, labels = plt.xticks()
    for loc in locs:
        plt.axvline(loc, color=bgcolor, linewidth=0.5)
    plt.ylim(ymin, ymax)
