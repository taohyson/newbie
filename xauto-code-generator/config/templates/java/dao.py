template = '''
package '''+package+''';

import java.util.List;
import java.util.Map;
import org.apache.ibatis.annotations.Param;
import org.mybatis.pagination.dto.PageMyBatis;
import org.mybatis.pagination.dto.datatables.PagingCriteria;
import kit.common.*;
import org.apache.ibatis.annotations.Mapper;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.HashMap;
import java.util.Map;
'''+xfor(depends, lambda item:''' 
import '''+item+'''.*;
''')+'''
/**
* 映射接口类 '''+package+'''.'''+className+'''Dao
*/
@Mapper
@CommonDataBase
public interface '''+className+'''Dao {
	public long insert('''+className+''' '''+xcamel(className)+''');
	public int delete(@Param(value="id") String id);
	public int deleteRange(String [] ids);
	public int update('''+className+''' '''+className+''');
	public '''+className+''' query(@Param(value="id") String id);
	public PageMyBatis<'''+className+'''> select(@Param(value="userId") String userId, Map<String,Object> params);
	public PageMyBatis<'''+className+'''> search(@Param(value="userId") String userId, PagingCriteria pagingCriteria);
	public int count(Map<String,Object> params);
	public int countRange(Map<String,Object> params);
	public Integer maxValue(@Param("fieldName") String fieldName);
}
'''

xoutput(path, className + "Dao.java", template)