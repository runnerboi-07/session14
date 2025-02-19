from china import cook as china_cook # python first checks current directory for China
from senegal import cook as senegal_cook # can rename functions while importing
try:
    from romania import cook as romania_cook
except ModuleNotFoundError: # can be different import errors, e.g. the function does not exist in the module
    print("sorry, there is no cook in Romania")
from china import * # bulk import
import china as prc

from latam.cuba import cook as cuba_cook
from latam.peru import cook as peru_cook
from latam.mexico.jalisco import cook as jalisco_cook
from latam.mexico.yucatan import cook as yucatan_cook

# import sys
# import pandas

print("hello world")
def greet():
    print("hello from Segoland")

def cook():
    print("We are making cochinillo")

senegal_cook()
china_cook()
cook()
print(hello)
print(prc.hello)

cuba_cook()
peru_cook()
yucatan_cook()
jalisco_cook()