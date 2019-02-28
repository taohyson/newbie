template = '''
package '''+package+''';
import java.sql.Date;
import java.sql.Time;
import java.util.Map;
import java.util.HashMap;
import java.sql.Timestamp;
import java.io.Serializable;
import kit.common.TypeConvert;
import org.hibernate.validator.constraints.*;
import javax.validation.constraints.*;
import kit.common.CombineKeysUtil;


/**
* 实体类 Project
*/
public class '''+className+''' implements Serializable{

	'''+xfor(fields, lambda item: '''
	private '''+item["type"]+''' '''+item["field"]+ ''';
	''')+'''

	'''+xfor(fields, lambda item: '''
	public '''+item["type"]+''' get'''+item["field"].capitalize()+'''() {
		return '''+item["field"]+''';
	}

	public void set'''+item["field"].capitalize()+'''('''+item["type"]+''' '''+item["field"] +''') {
		this.'''+item["field"] +''' = '''+item["field"] +''';
	}
	''')+'''
}
'''

xoutput(path, className + ".java", template)