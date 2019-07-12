def Get_Time_Now(timestep = "%Y-%m-%d %H:%M:%S"):
	import time
	nowtime = time.strftime(timestep, time.localtime())
	return nowtime
