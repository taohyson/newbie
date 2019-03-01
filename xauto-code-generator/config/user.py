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
		"className": "User",
		"table": "t_user",
		"columns": [
			{
				"column": "id",
				"type": "bigint(20) NOT NULL",
				"field": "id"
			},
			{
				"column": "name",
				"type": "varchar(255) DEFAULT NULL",
				"field": "name"
			},
			{
				"column": "age",
				"type": "nt(11) DEFAULT NULL",
				"field": "age"
			}
		],
		"primary-key": [
			"id"
		],
		"references": [
			{
				"table": "t_order",
				"ons":[
					{
						"on": "id",
						"oned": "userId"
					}
				],
				"columns": [
					{
						"column": "id",
						"field": "orderId"
					},
					{
						"column": "name",
						"field": "orderName"
					}
				],
			}
		],
		"templates": [
			{
				"template": "mysql.py",
				"context": {
					"package": "com.autoai.app.dao",
					"beanpackage": "com.autoai.app.bean",
					"path": "src/main/resource/com/autoai/app/"
				}
			}
		]
	}
}