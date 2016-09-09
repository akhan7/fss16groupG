def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'


# Part 1
do_twice(print_spam)


# Part 2
def do_twice(f, v):
    f(v)
    f(v)


# Part 3
def print_twice(par):
    print par
    print par


# Part 4
do_twice(print_twice, 'spam1')


# Part 5
def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


do_four(print_twice, 'spam2')
