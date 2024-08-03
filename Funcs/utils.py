from Setup import Setup
def visible(x, y):

	if(x > Setup.plane["px"] or x < Setup.plane["nx"] or y > Setup.plane["py"] or y < Setup.plane["ny"]):
		return False
	else: 
		return True


def map(input, input_start, input_end, output_start,output_end):
	return output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)


def mts(x, y):
	if(not visible(x,y)):
		return None
	else:
		rv = []
		rv.insert(0,int(map(y, plane["py"], plane["ny"], 0, screensize["y"])))
		rv.insert(0,int(map(x, plane["nx"], plane["px"], 0, screensize["x"])))
		return rv


