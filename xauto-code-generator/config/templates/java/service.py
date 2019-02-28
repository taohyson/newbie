template = '''
package '''+package+''';
 
import kit.common.exception.OperationException;
import org.apache.shiro.authc.DisabledAccountException;
import org.apache.shiro.authc.UnknownAccountException;
import org.mybatis.pagination.dto.PageMyBatis;
import org.mybatis.pagination.dto.datatables.PagingCriteria;
import '''+beanpackage+'''.*;
import java.util.List;
import java.util.Map;
import java.util.Set;
public interface '''+className+'''Service {
	long insert'''+className+'''('''+className+''' '''+className+''');
	int delete'''+className+'''ById(String token);
	int update'''+className+'''('''+className+''' '''+className+''');
	'''+className+''' get'''+className+'''ById(String token);
	'''+className+''' get'''+className+'''FullyById(String token);
	PageMyBatis<'''+className+'''> query'''+className+'''ListByPageFully(PagingCriteria pagingCriteria);
	List<'''+className+'''> query'''+className+'''List();
	List<'''+className+'''> query'''+className+'''ListFully();
}
'''

xoutput(path, className + "Service.java", template)