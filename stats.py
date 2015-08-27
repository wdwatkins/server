def mean(vals):
	total = sum(vals)
	length = len(vals)
	return float(total)/length

def std(vals):
	n = len(vals)
	if n == 0:
		return 0.0
	mu = sum(vals)/n
	var = 0.0
	for val in vals:
		var = var + (val-mu)**2
	return (var/n)**0.5

#print mean([3,4])

