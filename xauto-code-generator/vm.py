import importlib

def expand(array, sample):
	res = ''
	for i in range(len(array)):
		res += sample(array[i])
	return res

def generate(ruleFile, templateFile):
	module = importlib.import_module(ruleFile)
	if module is None:
		return ''
	rules = module.rules
	template = open(templateFile, 'r', encoding='UTF-8').read()
	return eval(template, {"expand": expand}, rules)

if __name__ == '__main__':
	print(generate('rules', 'temp.py'))