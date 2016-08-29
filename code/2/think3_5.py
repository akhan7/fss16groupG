def define_row():
	return '+ - - - - '

def define_column():
	return '/         '

# Part 1
print 'Part 1'
def print_row(f):
	print f() + f() + '+'

def print_column(f):
	print f() + f() + '/'
	print f() + f() + '/'
	print f() + f() + '/'
	print f() + f() + '/'

print_row(define_row)
print_column(define_column)
print_row(define_row)
print_column(define_column)
print_row(define_row)


# Part 2
print 'Part 2'
def print_row_4(f):
	print f() + f() + f() + f() + '+'

def print_column_4(f):
	print f() + f() + f() + f() + '/'
	print f() + f() + f() + f() + '/'
	print f() + f() + f() + f() + '/'
	print f() + f() + f() + f() + '/'

print_row_4(define_row)
print_column_4(define_column)
print_row_4(define_row)
print_column_4(define_column)
print_row_4(define_row)
print_column_4(define_column)
print_row_4(define_row)
print_column_4(define_column)
print_row_4(define_row)