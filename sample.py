import math
import os
import sys

# print(sys.version)
print(sys.executable)


def sayHello(who_to_greet):
    test = "test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(sayHello("World"))
print(sayHello("Uttam"))
