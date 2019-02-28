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
					"depends": [
					],
					"path": "src/main/java/com/autoai/app/bean/"
				}
			},
			{
				"template": "dao.py",
				"context": {
					"package": "com.autoai.app.dao",
					"depends": [
						"com.autoai.app.bean"
					],
					"path": "src/main/java/com/autoai/app/dao/"
				}
			},
			{
				"template": "controller.py",
				"context": {
					"package": "com.autoai.app.controller",
					"depends": [
						"com.autoai.app.bean",
						"com.autoai.app.service"
					],
					"uri": "api/",
					"path": "src/main/java/com/autoai/app/controller/"
				}
			},
			{
				"template": "service.py",
				"context": {
					"package": "com.autoai.app.service",
					"depends": [
						"com.autoai.app.bean"
					],
					"path": "src/main/java/com/autoai/app/service/"
				}
			},
			{
				"template": "serviceImpl.py",
				"context": {
					"package": "com.autoai.app.service.impl",
					"depends": [
						"com.autoai.app.bean",
						"com.autoai.app.service",
						"com.autoai.app.dao",
					],
					"path": "src/main/java/com/autoai/app/service/impl/"
				}
			}
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