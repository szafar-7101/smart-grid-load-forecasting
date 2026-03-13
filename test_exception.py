import sys
from smartgrid.exception.exception import SmartGridException


try:
    a = 10 / 0
except Exception as e:
    raise SmartGridException(e, sys)