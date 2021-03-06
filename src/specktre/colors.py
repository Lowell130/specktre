# -*- encoding: utf-8 -*-
"""Generate random colors between two other colors."""

import collections
import random
import warnings

RGBColor = collections.namedtuple('RGBColor', ['red', 'green', 'blue'])


def Color(*args, **kwargs):
    warnings.warn('Color is deprecated, use RGBColor instead.',
                  DeprecationWarning)
    return RGBColor(*args, **kwargs)


def random_color(start, end):
    d_red = (start.red - end.red)
    d_green = (start.green - end.green)
    d_blue = (start.blue - end.blue)
    while True:
        chosen_d = random.uniform(0, 1)
        yield Color(
            start.red - int(d_red * chosen_d),
            start.green - int(d_green * chosen_d),
            start.blue - int(d_blue * chosen_d)
        )
