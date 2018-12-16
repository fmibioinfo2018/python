import sys
import gc
from ctypes import *
import ctypes

longsize = ctypes.sizeof(ctypes.c_long)
x = 1000
int_value = ctypes.c_uint.from_address(id(x) + longsize * 3)
int_value.value = 1001

print(int_value)
print(x)
print(1000)