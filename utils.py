import functools, colorama, time, datetime

colorama.init()

PLUGINS = dict()

current_date = datetime.datetime.now()
formatted_current_date = current_date.strftime('%Y-%m-%d  %H:%M:%S')

colors = {
	'end': '\033[0m',
	'red': '\033[31m',
	'green': '\033[32m',
	'yellow': '\033[33m',
	'blue': '\033[34m',
	'purple': '\033[35m',
	'cyan': '\033[36m',
	'gray': '\033[37m'
}

def convert_to_int(value):
	return int(value) if isinstance(value, str) else value

def timer(func):
	"""Print the runtime of the decorated function"""
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()
		value = func(*args, **kwargs)
		end_time = time.perf_counter()
		run_time = end_time - start_time
		print(f"Finished {func.__name__}() in {run_time:.4f} secs")
		return value
	return wrapper_timer

def debug(func):
	"""Print the function signature and return value"""
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		print(f"\nCalling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		print(f"{func.__name__}() returned {repr(value)}")
		return value
	return wrapper_debug

def slow_down(func):
	"""Sleep 1 second before calling the function"""
	@functools.wraps(func)
	def wrapper_slow_down(*args, **kwargs):
		time.sleep(1)
		return func(*args, **kwargs)
	return wrapper_slow_down

def register(func):
	"""Register a function as a plug-in"""
	PLUGINS[func.__name__] = func
	return func