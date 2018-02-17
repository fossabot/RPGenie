#!/usr/bin/env python

"""
RPGenie; a modular toolkit for developing RPG games in Python

RPGenie focuses on modularity and ease-of-use; not only can you add
functionality through the pre-defined classes, functions and mixins,
but you can also directly use any of them as base classes.

The toolkit is aiming to be fully compatible with Python versions 3.6 and up.
RPGenie is currently being maintained by {maintainer}.

All credit goes to the following people: {credits}
"""

__author__     = "Lari Liuhamo"
__copyright__  = f"Copyright 2017, {__author__}."
__credits__    = [__author__,]

__license__    = "GNU General Public License v3.0"
__version__    = "0.1.0"
__maintainer__ = __author__
__email__      = "lari.liuhamo+rpgenie@gmail.com"
__status__     = "alpha"

__doc__ = __doc__.format(
    maintainer = __maintainer__,
    credits = ", ".join(__credits__)
        if len(__credits__) > 1
        else __credits__[0]
            if __credits__
            else "None"
)
