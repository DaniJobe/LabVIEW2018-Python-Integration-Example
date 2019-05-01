from datetime import date
from typing import Any

def HelloWorld(Name):
    return ('Hello '+ Name + '!')

def Add(a, b):
    return a+b

def CalculateDaysSince(event):
    delta = date.today() - date(event[2],event[1]+1,event[0])
    return delta.days

def DataType(item: Any):
    return str(type(item))

def getValueForKey(keyValuePairs, key): 
    return (dict(keyValuePairs).get(key))

def maxAndMin(array):
    return (max(array), min(array))
