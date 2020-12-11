import matplotlib as mpl
import matplotlib.pyplot as mplpp
from random import choice



def spiral(origin, radius, n):
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wintergreen", "xkcd:charcoal grey"]
    xList = 2 * [origin[0] + radius] + 2 * [origin[0] - radius] + [origin[0] + radius]
    yList = [origin[1] + radius] + 2 * [origin[1] - radius] + 2 * [origin[1] + radius]
    for _ in range(n):
        mplpp.plot(xList, yList, choice(colorList))
        for j in range(len(xList)-1):
            xList[j] = (xList[j] * 9 + xList[j+1]) / 10
            yList[j] = (yList[j] * 9 + yList[j+1]) / 10
        xList[-1] = xList[0]
        yList[-1] = yList[0]



spiral((10, 10), 10, int(input("Nombre de carrés : ")))

mplpp.axis("equal")
mplpp.show()