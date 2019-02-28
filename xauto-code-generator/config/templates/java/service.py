template = '''
package '''+package+''';
 
import kit.common.exception.OperationException;
import org.apache.shiro.authc.DisabledAccountException;
import org.apache.shiro.authc.UnknownAccountException;
import org.mybatis.pagination.dto.PageMyBatis;
import org.mybatis.pagination.dto.datatables.PagingCriteria;
'''+xfor(depends, lambda item:''' 
import '''+item+'''.*;
''')+'''
import java.util.List;
import java.util.Map;
import java.util.Set;

public interface '''+className+'''Service {
	long insert('''+className+''' '''+xcamel(className)+''');
	int delete(String id);
	int update('''+className+''' '''+xcamel(className)+''');
	'''+className+''' query(String id);
	PageMyBatis<'''+className+'''> search(String userId, PagingCriteria pagingCriteria);
}
'''

xoutput(path, className + "Service.java", template)