#!/usr/bin/env python
# a bar plot with errorbars
import sys
import numpy as np
import matplotlib.pyplot as plt

import parse

def byName(parsed, name):
    return np.array( parsed[name])

parsed = parse.byFileName("data.csv")
lengths = parsed['length']
safe = byName(parsed,'safe')
unsafe = byName(parsed,'unsafe')
semisafe = byName(parsed,'semi_safe')


safe /= unsafe
semisafe /= unsafe
unsafe /= unsafe

N = len(lengths)
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()

safe_rects = ax.bar(ind+width*0, safe, width, color='r')
unsafe_rects = ax.bar(ind+width*1, unsafe, width, color='b')
semisafe_rects = ax.bar(ind+width*2, semisafe, width, color='g')

def head( l ): return l[0]
legend_items= map( head, [ safe_rects, unsafe_rects, semisafe_rects ] )

# add some text for labels, title and axes ticks
t = np.arange(0.01, 20, 0.1)
ax.set_ylabel('Times slower than the unchecked version')
ax.set_xlabel('Length of Vector')
#ax.set_yscale('log')
ax.set_title('')
ax.set_xticks(ind+width)
ax.set_xticklabels( lengths )

ax.legend( legend_items, ('safe',
                          'unsafe',
                          'semi_safe'),
                          loc=1)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
#map( autolabel, [safe_rects,unsafe_rects,semisafe_rects])

_dpi = 1600
plt.savefig( "graph.pdf", dpi=_dpi, format="pdf")
#plt.savefig( "ep_graph.svg", dpi=_dpi, format="svg")
#plt.savefig( "ep_graph.png", dpi=_dpi, format="png")

if '-q' not in sys.argv[1:]:
    plt.show()
