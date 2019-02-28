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
	public long insert('''+className+''' '''+xcamel(className)+''');
	public int delete(String id);
	public int deleteRange(String[] ids);
	public int update('''+className+''' '''+xcamel(className)+''');
	public '''+className+''' query(String id);
	public List<'''+className+'''> select(String userId, Map<String,Object> params);
	public PageMyBatis<'''+className+'''> search(String userId, PagingCriteria pagingCriteria);
	public int count(Map<String,Object> params);
	public int count4Or(Map<String,Object> params);
	public Integer maxValue(String fieldName);
}
'''

xoutput(path, className + "Service.java", template)