def File_Enumeration(directory, prefix=None, postfix=None):
	file_list = []
	directory = os.path.normpath(directory)
	for parent, dirnames, filenames in os.walk(directory):
		for filename in filenames:
			if postfix:
				if filename.endswith(postfix):
					file_list.append(os.path.join(parent, filename))
			elif prefix:
				if filename.startswith(prefix):
					file_list.append(os.path.join(parent, filename))
			else:
				file_list.append(os.path.join(parent, filename))		
	return file_list
