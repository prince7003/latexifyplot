import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import math

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f','--figure', help='Figure to generate ("xy", None for all)', type=str, default=None)
parser.add_argument('-l','--latex', help='Produce output for LaTex docs', type=int, default=1)
args = parser.parse_args()


def latexify(fig_width=None, fig_height=None):
  if args.latex:
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    fig_width_pt = 397.48499   # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27  # Convert pt to inch

    if fig_width is None:
        fig_width = fig_width_pt*inches_per_pt

    if fig_height is None:
        golden_mean = (math.sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height +
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {
      'backend': 'ps',
      #'text.latex.preamble': ['\usepackage{gensymb}'],
      'axes.labelsize': 8, # fontsize for x and y labels (was 10)
      'axes.titlesize': 8,
      'font.size':       8, # was 10
      'legend.fontsize': 8, # was 10
      'xtick.labelsize': 8,
      'ytick.labelsize': 8,
      'text.usetex': True,
      'figure.figsize': [fig_width,fig_height],
      'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)