import re
import json
# from rules import root

def repeat(context, template):
	groups = template.split("<MacroRepeat>")
	for i in range(len(groups)):
		group = groups[i]
		tmpls = group.split("</MacroRepeat>")
		if tmpls[0][:4] != "len(":
			continue
		else:
			newtmpls = duplicate(context, tmpls[0])
			template = template.replace(tmpls[0], newtmpls)
	return template

def duplicate(ctx, tmpl):
	match = re.search(r'len\(.*', tmpl)
	if match:
		length = len(match.group(0))
		lenstr = tmpl[0:length - 1]
		size = eval(lenstr, {}, ctx)
		return copies(size, tmpl[length:])
	
def copies(size, tmpl):
	tmpls = ''
	for i in range(size):
		tmpls += tmpl.replace('[0]', '[' + str(i) + ']')
	return tmpls

def generate(context, template):
	template = template.replace('<MacroRepeat>', '');
	template = template.replace('</MacroRepeat>', '');

	template = template.replace('<Macro>', '\'\'\' + ')
	template = template.replace('</Macro>', ' + \'\'\'')

	template = template.replace('<MacroFunc>', '\'\'\' + eval(\'')
	template = template.replace('<MacroCtx>', '\', {}, ');
	template = template.replace('</MacroCtx>', '');
	template = template.replace('</MacroFunc>', ') + \'\'\'')
	return eval(template, {}, context)

root = json.loads(open('rules.json', 'r', encoding='UTF-8').read())
template = open('java.tmpl', 'r', encoding='UTF-8').read()
template = repeat(root, template)
res = generate(root, template)
if res:
	print(res)