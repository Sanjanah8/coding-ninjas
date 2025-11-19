from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    result=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==s:
                pair=[min(arr[i],arr[j]),max(arr[i],arr[j])]
                result.append(pair)
    result.sort(key=lambda x: (x[0],x[1]))
    return result
