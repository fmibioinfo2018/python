import gc
import sys
from ctypes import *
import ctypes

# We are using ctypes to access our unreachable objects by memory address.
class PyObject(Structure):
    _fields_ = [("refcnt", c_long)]


gc.disable()  # Disable generational gc

lst = []
lst.append(lst)

# Store address of the list
lst_address = id(lst)

# Destroy the lst reference
del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

# Destroy references
del object_1, object_2

# Uncomment if you want to manually run garbage collection process 
# gc.collect()

# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)

longsize = ctypes.sizeof(ctypes.c_long)
x = 1000
int_value = ctypes.c_uint.from_address(id(x) + longsize * 3)
int_value.value = 1001
print(int_value)
print(x)
print(1000)


import ctypes
def get_ref(obj):
    """ returns a c_size_t, which is the refcount of obj """
    return ctypes.c_size_t.from_address(id(obj))

# the c_ulong is not a copy of the address
# so any modification of the ob_refcnt are directly visible
l = [1,2,3,4]
l_ref = get_ref(l)

print(ctypes.c_long(3)) # there is just one reference on the list (l)

l2 = l
print(ctypes.c_ulong(2))# two references on the list (l and l2)

del l
print(ctypes.c_long(1))

del l2
print(ctypes.c_ulong(0)) # no more reference!

another_list = [0, 0, 7]
print(ctypes.c_ulong(1)) # woot : old list's ob_refcnt have changed
