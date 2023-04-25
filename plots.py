from constants import *
import matplotlib.pylab as plt
from matplotlib.offsetbox import (OffsetImage,AnnotationBbox)

def offset_image(coord, name, ax, img):
    im = OffsetImage(img, zoom=0.2)
    im.image.axes = ax

    ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -12.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)

def plot_histogram():
    fig, ax = plt.subplots()
    fig.set_facecolor("#4d4d4dff")
    ax.set_facecolor("#4d4d4dff")
    ax.grid(True)

    monospace_font = {'fontname':'monospace'}
    plt.title('El Manzano', **monospace_font)
    
    y1 = [t['needs_id'] for t in taxa]
    y2 = [t['casual'] for t in taxa]
    y3 = [t['research_grade'] for t in taxa]

    x = range(len(taxa))
    img = [plt.imread(t['icon_path']) for t in taxa]

    ax.bar(x, y1, width=0.5,align="center", color='#bd7064ff')
    ax.bar(x, y2, width=0.5,align="center", bottom=y1, color='#6ca86cff')
    ax.bar(x, y3, width=0.5,align="center", bottom=y2, color='#4db54dff')

    for i, c in enumerate(taxa):
        offset_image(i, c, ax, img[i])
        
    plt.savefig('nat-data.pdf')  
    plt.show()
    return