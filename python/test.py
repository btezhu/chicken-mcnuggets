from src import max_nuggets

tests = {
	(6, 9, 20): 43,
	(7, 11, 17): 37,
	(9, 18, 32): 247
}

for test in tests:
	assert max_nuggets(*test) == tests[test],\
		"Failed test: " + ', '.join(map(str, test)) + " -> " + str(tests[test]) + "."