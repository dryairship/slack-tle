from matplotlib import pyplot as plt
from typing import List

import datetime as dt
import grpc_server.util.codeforces_api as cf
from .graph_common import get_current_figure_as_file, plot_rating_bg, StrWrap

def _plot_rating(resp, mark='o', labels: List[str] = None):
    labels = [''] * len(resp) if labels is None else labels
    for rating_changes, label in zip(resp, labels):
        ratings, times = [], []
        for rating_change in rating_changes:
            ratings.append(rating_change.newRating)
            times.append(dt.datetime.fromtimestamp(rating_change.ratingUpdateTimeSeconds))

        plt.plot(times,
                 ratings,
                 linestyle='-',
                 marker=mark,
                 markersize=3,
                 markerfacecolor='white',
                 markeredgewidth=0.5,
                 label=label)

    plot_rating_bg(cf.RATED_RANKS)
    plt.gcf().autofmt_xdate()

async def get_rating_graph_file(*, handles):
    """Plots Codeforces rating graph for the handles provided."""
    resp = [await cf.user.rating(handle=handle) for handle in handles]

    if not any(resp):
        handles_str = ', '.join(f'`{handle}`' for handle in handles)
        if len(handles) == 1:
            message = f'User {handles_str} is not rated'
        else:
            message = f'None of the given users {handles_str} are rated'
        raise GraphCogError(message)

    plt.clf()
    _plot_rating(resp)
    current_ratings = [rating_changes[-1].newRating if rating_changes else 'Unrated' for rating_changes in resp]
    labels = [StrWrap(f'{handle} ({rating})') for handle, rating in zip(handles, current_ratings)]
    plt.legend(labels, loc='upper left')

    min_rating = 1100
    max_rating = 1800
    for rating_changes in resp:
        for rating in rating_changes:
            min_rating = min(min_rating, rating.newRating)
            max_rating = max(max_rating, rating.newRating)
    plt.ylim(min_rating - 100, max_rating + 200)

    return get_current_figure_as_file()
