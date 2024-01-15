import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import math

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f','--figure', help='Figure to generate ("xy", None for all)', type=str, default=None)
parser.add_argument('-l','--latex', help='Produce output for LaTex docs', type=int, default=1)
args = parser.parse_args()

SPINE_COLOR = 'gray'

def format_axes(ax):
  if args.latex:
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

  return ax