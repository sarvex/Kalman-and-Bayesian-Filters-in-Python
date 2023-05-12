from __future__ import print_function
import io
import nbformat
import sys


def remove_formatting(nb):
    cells = nb['cells']
    for i in range (len(cells)):
        if (
            'source' in cells[i].keys()
            and cells[i]['source'][:16] == '#format the book'
        ):
            del cells[i]
            return


def remove_links(nb):
    c = nb['cells']
    for i in range (len(c)):
        if (
            'source' in c[i].keys()
            and c[i]['source'][:19] == '[Table of Contents]'
        ):
            del c[i]
            return


def remove_links_add_appendix(nb):
    c = nb['cells']
    for i in range (len(c)):
        if (
            'source' in c[i].keys()
            and c[i]['source'][:19] == '[Table of Contents]'
        ):
            c[i]['source'] = '\\appendix'
            return
