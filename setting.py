import json

class Setting:

	def __init__(self, setting_file):
		setting = json.load(open(setting_file))
		for key, val in setting:
			self.__dict__[key] = val
