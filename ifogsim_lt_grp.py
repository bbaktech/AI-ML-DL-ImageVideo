# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:43:41 2023

@author: BBAK TECH
"""
import matplotlib.pyplot as plt
import numpy as np

species = ("16", "20", "24", "28","32","36","40")
penguin_means = {
    'EdgeWord Computation offloading': (13.642857142856146,13.642857142855938,13.64285714285583,13.642857142857393,13.64285714285892,13.642857142860109,13.64285714286106),
    'CloudWord Computation offloading': (220.7597209296328,224.55388757537463,484.5651494087837,643.4868869066469,746.7551644274467,817.4916492959798,868.0684134331592),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Latency (ms)')
ax.set_xlabel('Number of edge bins')
ax.set_title('Comparison of latency - Edge/fog computing v/s cloud computing')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left')
ax.set_ylim(0, 1000)

plt.show()
