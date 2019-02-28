template = '''
package '''+package+''';
 
import com.alibaba.fastjson.JSON;
import io.jsonwebtoken.Claims;
import kit.common.*;
import kit.common.annotation.RequestJsonParam;
import kit.common.BaseController;
import kit.common.QueryParamV2;
import kit.common.SearchKeyword;
import kit.common.QueryParam;
import kit.common.exception.OperationException;
import org.apache.commons.collections.MapUtils;
import org.apache.shiro.authz.annotation.RequiresPermissions;
import org.mybatis.pagination.dto.PageMyBatis;
import org.mybatis.pagination.dto.datatables.PagingCriteria;
import org.mybatis.pagination.dto.datatables.SearchField;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.HttpRequest;
import org.springframework.stereotype.Controller;
import org.springframework.util.StringUtils;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import java.sql.Timestamp;
import java.util.*;

import static kit.common.JsonResult.*;
'''+xfor(depends, lambda item:'''
import '''+item+'''.*;
''')+'''

@Controller
@RequestMapping(value = "'''+uri+'''")
public class '''+className+'''Controller extends BaseController
{
	@Autowired
	@Qualifier("'''+xcamel(className)+'''Service")
	'''+xpascal(className)+'''Service '''+xcamel(className)+'''Service;

	private static final Logger logger = LoggerFactory.getLogger('''+className+'''Controller.class);

	@ResponseBody 
	@RequestMapping(value="/add",method=RequestMethod.POST)
	public Map<String, Object> insert(@Valid @RequestBody '''+xpascal(className)+''' '''+xcamel(className)+''', Errors errors, HttpServletRequest request) throws TokenException {

		'''+xcamel(className)+'''.setId(null);
		try{
			long inserted = '''+xcamel(className)+'''Service.insert(request.getHeader("userId"), '''+xcamel(className)+''');
			return data(inserted);
		} catch (Exception ex){
			logger.error('''+xpascal(className)+''')
			logger.error(ex)
			return error('''+xpascal(className)+''');
		}
	}

	@ResponseBody
	@RequestMapping(value="/update",method=RequestMethod.POST)
	public Map<String, Object> update(@Valid @RequestBody '''+xpascal(className)+''' '''+xcamel(className)+''',Errors errors)
	{
		try{
			int updated = '''+xcamel(className)+'''Service.update('''+xcamel(className)+''');
			return data(updated);
		} catch (Exception ex){
			logger.error('''+xpascal(className)+''')
			logger.error(ex)
			return error('''+xpascal(className)+''');
		}
	}
	
	@ResponseBody
	@RequestMapping(value="/delete",method=RequestMethod.POST)
	public Map<String, Object> delete(@RequestJsonParam("id") String id) 
	{
		if (StringUtils.isEmpty(id)) {
			logger.error("id is empty!!!")
			return error("id is empty!!!");
		}
		try{
			int deleted = '''+xcamel(className)+'''Service.delete(id);
			return ok(deleted);
		} catch (Exception ex){
			logger.error(id)
			logger.error(ex)
			return error(id);
		}
	}

	@ResponseBody
	@RequestMapping(value="/delete-range",method=RequestMethod.POST)
	public Map<String, Object> deleteRange(@RequestJsonParam("ids") String[] ids) 
	{
		if(ids.length==0){
			logger.error("ids is empty!!!")
			return error("ids is empty!!!");
		}
		try{
			int deleted = '''+xcamel(className)+'''Service.deleteRange(ids);
			return ok(deleted);
		} catch (Exception ex){
			logger.error("[" + String.join(",", ids) + "]")
			logger.error(ex)
			return error("[" + String.join(",", ids) + "]");
		}
	}
	
	@ResponseBody
	@RequestMapping(value = "/query", method = RequestMethod.POST)
	public Map<String,Object> detail(@RequestJsonParam("id") String id) {
	
		'''+xpascal(className)+''' '''+xcamel(className)+''' = '''+xcamel(className)+'''Service.query(id);
		return data('''+xcamel(className)+''');
	}

	@ResponseBody
	@RequestMapping(value="/select",method=RequestMethod.POST)
	public Map<String,Object> queryListByPageFully(@RequestBody Map<String,Object> selectParam, HttpServletRequest request) throws TokenException {
		try {
			String userId = request.getHeader("userId");
			PageMyBatis<Project> pageMyBatis = '''+xcamel(className)+'''Service.search(userId, selectParam);
			return data(pageMyBatis);
		} catch(Exception e) {
			logger.error(new Gson().toJson(this).toString());
			logger.error(e);
			return error(new Gson().toJson(this).toString())
		}
		return null;
	}

	@ResponseBody
	@RequestMapping(value="/search",method=RequestMethod.POST)
	public Map<String,Object> queryListByPageFully(@RequestBody QueryParam queryParamV1, HttpServletRequest request) throws TokenException {
		QueryParamV2 queryParam = new QueryParamV2(queryParamV1);
		PagingCriteria pagingCriteria = fillPagingCriteria(queryParam.pageNum,queryParam.numPerPage,queryParam.searchKeywords,queryParam.orderField,queryParam.orderDirection);
		try {
			String userId = request.getHeader("userId");
			PageMyBatis<Project> pageMyBatis = '''+xcamel(className)+'''Service.search(userId, pagingCriteria);
			return data(pageMyBatis);
		} catch(Exception e) {
			logger.error(new Gson().toJson(this).toString());
			logger.error(e);
			return error(new Gson().toJson(this).toString())
		}
		return null;
	}
}
'''

xoutput(path, className + 'Controller.java', template)