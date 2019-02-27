import re
from rules import root

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
	

res = repeat(root, open('java.tmpl', 'r', encoding='UTF-8').read())
print(res)