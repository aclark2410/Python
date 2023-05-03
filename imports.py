# How to import modules from another file

import modules as mod

mod.hello()

mod.bye()

# An alternative way of doing this 

from modules import hello, bye

hello()

bye()

# To import all of the modules from a file 

from modules import *

hello()
bye()

