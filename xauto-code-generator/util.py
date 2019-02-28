import os

def xif(item, tempCtrl):
    if item:
    	return tempCtrl(item)
    else:
    	return ''

def xfor(array, tempCtrl):
    res = ''
    if array:
	    for i in range(len(array)):
	        res += tempCtrl(array[i])
    return res

def xoutput(srcDir, srcFile, srcCode):
	if not os.path.exists(srcDir):
		os.makedirs(srcDir)
	open(srcDir + srcFile, 'w', encoding='UTF-8').write(srcCode)


if __name__ == '__main__':
	java = {
		"package": "com.autoai.app",
		"class": "User",
		"fields": [
			{
				"type": "String",
				"field": "name"
			},
			{
				"type": "int",
				"field": "age"
			}
		],
		"templates": [
			{
				"template": "bean.py",
				"path": "src/main/java/com/autoai/app/bean/"
			},
			{
				"template": "dao.py",
				"path": "src/main/java/com/autoai/app/dao/"
			},
			{
				"template": "interface.py",
				"path": "src/main/java/com/autoai/app/interface/"
			},
			{
				"template": "service.py",
				"path": "src/main/java/com/autoai/app/service/"
			},
			{
				"template": "serviceImp.py",
				"path": "src/main/java/com/autoai/app/service/imp/"
			}
		],
	}
	mysql = {
		"table": "t_user",
		"columns": [
			{
				"type": "String",
				"column": "id"
			},
			{
				"type": "int",
				"column": "name"
			}
		]
	}
	srccode = xfor(java["fields"], lambda item:'''
	    public static ''' + item["type"] + ''' get''' + item["field"].capitalize() + '''{
	        String ret = "";
	        return ret;
	    }
	    ''')
	xoutput('testDir/', 'xfor.java', srccode)
	srccode = xif(mysql.get("table"), lambda item:'''
	    DROP TABLE IF EXISTS `''' + item + '''`;
	    ''')
	xoutput('testDir/', 'xif.sql', srccode)