import os
import importlib
import util

def generate(ruleFile):
	module = importlib.import_module(ruleFile)
	if module is None:
		return
	contexts = module.contexts
	for language, context in contexts.items():
		templates = context.get("templates")
		if templates:
			for item in templates: 
				template = open('config\\templates\\' + language +'\\' + item.get("template"), 'r', encoding='UTF-8').read()
				context.update(item.get("context"))
				print(ruleFile)
				print(item.get("template"))
				exec(template, util.__dict__, context)
	return

def walk():
	for fpath,dirs,fs in os.walk('config'):
		for f in fs:
			if f[-3:] == ".py":
				generate('config.' + f[:-3])
		break
	return

if __name__ == '__main__':
	# generate('config.user')
	walk()