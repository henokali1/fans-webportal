def get_sec(file_name):
	try:
		full_file_name = '/etc/' + file_name + '.txt'
		with open(full_file_name) as f:
			sec = f.read().strip()
		return sec
	except:
		return '-1'