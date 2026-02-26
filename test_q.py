from q import *
import pytest

def test_is_empty():
	q = Queue()
	assert q.is_empty()

def test_add():
	q = Queue()
	q.add("Felicity")
	assert q.head.data == "Felicity"
	q.add("Robert")
	assert q.head.data == "Felicity"
	next_node = q.head.next
	assert next_node.data == "Robert"

def test_pop_left():
	q = Queue()
	q.add("Felicity")
	assert q.head.data == "Felicity"
	q.add("Robert")
	
