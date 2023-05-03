# ****************************
# if __name__ == '__main__'
# ****************************

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets 'special variables', one of which is __name__
# then Python will execute the code found within __main__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

print(__name__)

import modules

print(modules.__name__)

# We are checking if this module is being run directly, the result is we are running this module directly

if __name__ == '__main__':
    print("running this module directly")

else:
    print("running this module indirectly")
