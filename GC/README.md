# Garbage collection (GC)
## Memory management
Unlike many other languages, Python does not necessarily release the memory back to the Operating System. Instead, it has a specialized object allocator for small objects (smaller or equal to 512 bytes), which keeps some chunks of already allocated memory for further use in future. The amount of memory that Python holds depending on the usage patterns, in some cases all allocated memory is never released.

Therefore, if a long-running Python process takes more memory over time, it does not necessarily mean that you have memory leaks. If you are interested in Python's memory model, consider reading my article on memory management.

## Garbage collection algorithms
Standard CPython's garbage collector has two components, the reference counting collector and the generational garbage collector, known as gc module.

The reference counting algorithm is incredibly efficient and straightforward, but it cannot detect reference cycles. That is why Python has a supplemental algorithm called generational cyclic GC, that deals with reference cycles.

The reference counting is fundamental to Python and can't be disabled, whereas the cyclic GC is optional and can be used manually.

Detaild information:
- [gc module](https://docs.python.org/3.6/library/gc.html) 
- [source code](https://github.com/python/cpython/blob/master/Modules/gcmodule.c) 
- [Tracing References](https://pymotw.com/3/gc/)
- [Python Garbage Collector Implementations CPython, PyPy and GaS](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)

## Reference counting
Reference counting is a simple technique in which objects are deallocated when there is no reference to them in a program.

Every variable in Python is a reference (a pointer) to an object and not the actual value itself. For example, the assignment statement just adds a new reference to the right-hand side.

To keep track of references every object (even integer) has an extra field called reference count that is increased or decreased when a pointer to the object is copied or deleted. See Objects, Types and Reference Counts section, for a detailed explanation.

## GC reference cycles
Instead of trying to find all reachable objects it tries to find unreachable objects. This is much safer because if the algorithm fails we are no worse off than with no garbage collection (except for the time and space wasted).
Since we are still using reference counting, the garbage collector only has to find reference cycles. The reference counting will handle freeing other types of garbage. First we observe that reference cycles can only be created by container objects. These are objects which can hold references to other objects. In Python lists, dictionaries, instances, classes, and tuples are all examples of container objects. Integers and strings are not containers. With this observation we realize that non-container objects can be ignored for the purposes of garbage collection. This is a useful optimization because things like integers and strings should be fast and small.

Our idea now is to keep track of all container objects. There are several ways that this can be done but one of the best is using doubly linked lists with the link fields inside the objects structure. This allows objects to be quickly inserted and removed from the set as well as not requiring extra memory allocations. When a container is created it is inserted into this set and when deleted it is removed.

Now that we have access to all the container objects, how to we find reference cycles? First we add another field to container objects in addition to the two link pointers. We will call this field gc_refs. Here are the steps to find reference cycles:

For each container object, set gc_refs equal to the object's reference count.
For each container object, find which container objects it references and decrement the referenced container's gc_refs field.
All container objects that now have a gc_refs field greater than one are referenced from outside the set of container objects. We cannot free these objects so we move them to a different set.
Any objects referenced from the objects moved also cannot be freed. We move them and all the objects reachable from them too.
Objects left in our original set are referenced only by objects within that set (ie. they are inaccessible from Python and are garbage). We can now go about freeing these objects.
[Full document link](http://arctrix.com/nas/python/gc/)

