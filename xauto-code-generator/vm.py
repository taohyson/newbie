import re
import json

def precompile(context, template):
	groups = template.split("<MacroRepeat>")
	for i in range(len(groups)):
		group = groups[i]
		samples = group.split("</MacroRepeat>")
		sample = samples[0]
		if sample[:4] == "len(":
			sampleSet = repeat(context, sample)
			if sampleSet:
				template = template.replace(sample, sampleSet)
			else:
				continue
		else:
			continue
	return template

def repeat(ctx, tmpl):
	match = re.search(r'len\(.*', tmpl)
	if match:
		length = len(match.group(0))
		lenstr = tmpl[0:length - 1]
		size = eval(lenstr, {}, ctx)
		return copies(size, tmpl[length:])
	else:
		return

def copies(size, tmpl):
	tmplSet = ''
	for i in range(size):
		tmplSet += tmpl.replace('[0]', '[' + str(i) + ']')
	return tmplSet

def compile(context, template):
	templated = template.replace('<MacroRepeat>', '');
	templated = templated.replace('</MacroRepeat>', '');

	templated = templated.replace('<Macro>', '\'\'\' + ')
	templated = templated.replace('</Macro>', ' + \'\'\'')

	templated = templated.replace('<MacroFunc>', '\'\'\' + eval(\'')
	templated = templated.replace('<MacroCtx>', '\', {}, ');
	templated = templated.replace('</MacroCtx>', '');
	templated = templated.replace('</MacroFunc>', ') + \'\'\'')
	return eval(templated, {}, context)

def generate(ruleFile, templateFile):
	rules = json.loads(open(ruleFile, 'r', encoding='UTF-8').read())
	template = open(templateFile, 'r', encoding='UTF-8').read()
	templated = precompile(rules, template)
	return compile(rules, templated)

if __name__ == '__main__':
	print(generate('rules.json', 'java.tmpl'))