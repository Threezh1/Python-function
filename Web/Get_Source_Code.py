def Get_Source_Code(URL, UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"):
	import requests
	from requests.packages import urllib3
	urllib3.disable_warnings()
	headers = {"User-Agent": UA}
	try:
		source_object = requests.get(URL, headers = header, timeout = 5, verify=False)
		source_content = source_object.content.decode("utf-8", "ignore")
	except:
		return None
	return source_content
