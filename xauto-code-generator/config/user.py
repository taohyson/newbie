contexts = {
	"java": {
		"className": "User",
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
				"context": {
					"package": "com.autoai.app.bean",
					"path": "src/main/java/com/autoai/app/bean/"
				}
			},
			# {
			# 	"template": "dao.py",
			# 	"context": {
			# 		"package": "com.autoai.app.dao",
			# 		"path": "src/main/java/com/autoai/app/dao/"
			# 	}
			# },
			# {
			# 	"template": "interface.py",
			# 	"context": {
			# 		"package": "com.autoai.app.interface",
			# 		"path": "src/main/java/com/autoai/app/interface/"
			# 	}
			# },
			{
				"template": "service.py",
				"context": {
					"package": "com.autoai.app.service",
					"beanpackage": "com.autoai.app.bean",
					"path": "src/main/java/com/autoai/app/service/"
				}
			},
			# {
			# 	"template": "serviceImp.py",
			# 	"context": {
			# 		"package": "com.autoai.app.service.iml",
			# 		"path": "src/main/java/com/autoai/app/service/imp/"
			# 	}
			# }
		]
	},
	"mysql": {
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
		],
		"templates": [
			# {
			# 	"template": "mysql.py",
			# 	"path": "src/main/resource/com/autoai/app/"
			# }
		]
	}
}