import sys

foo = []

print(sys.getrefcount(foo))


def bar(a):
    print(sys.getrefcount(a))

bar(foo)
print(sys.getrefcount(foo))