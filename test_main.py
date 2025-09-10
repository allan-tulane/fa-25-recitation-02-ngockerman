from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(16, 2, 2) == 80
	assert simple_work_calc(9, 3, 3) == 27
	assert simple_work_calc(64, 2, 2) == 448

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(16, 2, 2, lambda n: n) == 80
	assert work_calc(27, 2, 3, lambda n: n) == 65 
	assert work_calc(10, 2, 3, lambda n: 1) == 7


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
	work_fn1 = lambda n: simple_work_calc(n, a=2, b=2)
	work_fn2 = lambda n: work_calc(n, a=2, b=2, f=lambda x: 1)

	# create work_fn1
	# create work_fn2
	res = compare_work(work_fn1, work_fn2)

	print(res)

	
def test_compare_span():
	# TODO
	span_fn1 = lambda n: span_calc(n, a=2, b=2, f=lambda x: x)
	span_fn2 = lambda n: span_calc(n, a=2, b=2, f=lambda x: 1)

	res = compare_span(span_fn1, span_fn2)
