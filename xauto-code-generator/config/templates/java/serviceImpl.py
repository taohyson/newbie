template = '''
package '''+package+''';
 
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.mybatis.pagination.dto.PageMyBatis;
import org.mybatis.pagination.dto.datatables.PagingCriteria;
'''+xfor(depends, lambda item:'''
import '''+item+'''.*;
''')+'''

import javax.management.openmbean.OpenDataException;
import java.sql.Timestamp;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@Service("'''+xcamel(className)+'''Service")
public class '''+className+'''ServiceImpl implements  '''+className+'''Service {
	@Autowired
	'''+className+'''Dao '''+xcamel(className)+'''Dao;

	@Override
    @Transactional
	public long insert('''+className+''' '''+xcamel(className)+'''){
		return this.'''+xcamel(className)+'''Dao.insert('''+xcamel(className)+''');
	}
	
	@Override
    @Transactional
	public int delete(String id){
		return this.'''+xcamel(className)+'''Dao.delete(id);
	}
	
	@Override
    @Transactional
	public int update('''+className+''' '''+xcamel(className)+'''){
		return this.'''+xcamel(className)+'''Dao.update('''+xcamel(className)+''');
	}

	@Override
	public '''+className+''' query(String id){
		return this.'''+xcamel(className)+'''Dao.query(id);
	}

	@Override
	public List<'''+className+'''> select(String userId, Map<String, Object> params){
		return this.'''+xcamel(className)+'''Dao.select(userId, params);
	}
	
	@Override
	public PageMyBatis<'''+className+'''> search(String userId, PagingCriteria pagingCriteria){
		return this.'''+xcamel(className)+'''Dao.queryListByPageFully(userId,pagingCriteria);
	}

	@Override
    @Transactional
	public int count(Map<String, Object> params){
		return this.'''+xcamel(className)+'''Dao.update(params);
	}

	@Override
    @Transactional
	public int countRange(Map<String, Object> params){
		return this.'''+xcamel(className)+'''Dao.countRange(params);
	}

	@Override
    @Transactional
	public Integer maxValue(String fieldName){
		return this.'''+xcamel(className)+'''Dao.maxValue(fieldName);
	}
}
'''

xoutput(path, className + 'ServiceImpl.java', template)