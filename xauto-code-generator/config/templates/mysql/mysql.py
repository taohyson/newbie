template='''
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="'''+package+'''.'''+className+'''Dao">
    <select id="query" resultType="'''+beanpackage+'''.'''+className+'''">
        select '''+xforargs(columns, table, lambda item,tableName:tableName+'''.'''+item.get("column")+''' as '''+item.get("field")+''',''')[:-1]+'''
        '''+xfor(references, lambda reference:xforargs(reference.get("columns"), reference.get("table"), lambda column,table:''','''+table+'''.'''+column.get("column")+''' as '''+column.get("field")))+'''
        from '''+table+xforargs(references, table, lambda reference, table:'''
        left join '''+reference.get("table")+''' on ('''+xforargs(reference.get("ons"), table, lambda condition, table:table+'''.'''+condition.get("on")+''' = '''+reference.get("table")+'''.'''+condition.get("oned")+''' and ''')[:-5]+''')''')+'''
        WHERE '''+table+'''.ID = #{id}
        limit 1
    </select>
    <select id="select" resultType="'''+beanpackage+'''.'''+className+'''">
        select '''+xforargs(columns, table, lambda item,tableName:tableName+'''.'''+item.get("column")+''' as '''+item.get("field")+''',''')[:-1]+'''
        '''+xfor(references, lambda reference:xforargs(reference.get("columns"), reference.get("table"), lambda column,table:''','''+table+'''.'''+column.get("column")+''' as '''+column.get("field")))+'''
        from '''+table+xforargs(references, table, lambda reference, table:'''
        left join '''+reference.get("table")+''' on ('''+xforargs(reference.get("ons"), table, lambda condition, table:table+'''.'''+condition.get("on")+''' = '''+reference.get("table")+'''.'''+condition.get("oned")+''' and ''')[:-5]+''')''')+'''
    </select>
    <select id="search" resultType="'''+beanpackage+'''.'''+className+'''">
        <choose>
            <when test="userId != null">
                select '''+xforargs(columns, table, lambda item,tableName:tableName+'''.'''+item.get("column")+''' as '''+item.get("field")+''',''')[:-1]+'''
                '''+xfor(references, lambda reference:xforargs(reference.get("columns"), reference.get("table"), lambda column,table:''','''+table+'''.'''+column.get("column")+''' as '''+column.get("field")))+'''
                from '''+table+xforargs(references, table, lambda reference, table:'''
                left join '''+reference.get("table")+''' on ('''+xforargs(reference.get("ons"), table, lambda condition, table:table+'''.'''+condition.get("on")+''' = '''+reference.get("table")+'''.'''+condition.get("oned")+''' and ''')[:-5]+''')''')+'''
                <!--where PROJECT_ACCESS0.USER_ID = #{userId}-->
            </when>
            <otherwise>
                select '''+xforargs(columns, table, lambda item,tableName:tableName+'''.'''+item.get("column")+''' as '''+item.get("field")+''',''')[:-1]+'''
                '''+xfor(references, lambda reference:xforargs(reference.get("columns"), reference.get("table"), lambda column,table:''','''+table+'''.'''+column.get("column")+''' as '''+column.get("field")))+'''
                from '''+table+xforargs(references, table, lambda reference, table:'''
                left join '''+reference.get("table")+''' on ('''+xforargs(reference.get("ons"), table, lambda condition, table:table+'''.'''+condition.get("on")+''' = '''+reference.get("table")+'''.'''+condition.get("oned")+''' and ''')[:-5]+''')''')+'''
            </otherwise>
        </choose>
    </select>
    <select id="count" resultType="int">
        select count(*) from '''+table+''';
    </select>
    <select id="count" resultType="int" parameterType="java.util.Map">
        select count(*) from '''+table+'''
        <where>
            '''+xforargs(columns, table, lambda item, table:'''
            <choose>
                <when test="'''+item.get("field")+''' == 'nil'">
                    AND ('''+table+'''.'''+item.get("column")+''' is null)
                </when>
                <when test="'''+item.get("field")+''' != null">
                    AND ('''+table+'''.'''+item.get("column")+''' = #{'''+item.get("field")+'''})
                </when>
                <otherwise></otherwise>
            </choose>
            ''')+'''
        </where>

    </select>
    <select id="countRange" resultType="int" parameterType="java.util.Map">
        select count(*) from '''+table+'''
        <where>
            '''+xforargs(columns, table, lambda item, table:'''
            <choose>
                <when test="'''+item.get("field")+''' == 'nil'">
                    AND ('''+table+'''.'''+item.get("column")+''' is null)
                </when>
                <when test="'''+item.get("field")+''' != null">
                    AND ('''+table+'''.'''+item.get("column")+''' = #{'''+item.get("field")+'''})
                </when>
                <otherwise></otherwise>
            </choose>
            ''')+'''
        </where>

    </select>
    <select id="maxValue" resultType="Integer">
        select max(${fieldName}) from '''+table+'''
    </select>

    <insert id="insert" parameterType="'''+beanpackage+'''.'''+className+'''">
        insert into '''+table+''' (
        '''+xfor(columns, lambda item:item.get("column")+''',''')[:-1]+'''
        )
        values(
        '''+xfor(columns, lambda item:'''#{'''+item.get("field")+'''},''')[:-1]+'''
        )
    </insert>
    <delete id="delete">
        delete from '''+table+''' where '''+table+'''.id = #{id}
    </delete>
    <delete id="deleteRange">
        delete from '''+table+''' where '''+table+'''.id in #{ids}
    </delete>
    <delete id="deleteIf" parameterType="java.util.Map">
        delete from '''+table+'''
        <where>
            '''+xforargs(columns, table, lambda item, table:'''
            <choose>
                <when test="'''+item.get("field")+''' == 'nil'">
                    AND ('''+table+'''.'''+item.get("column")+''' is null)
                </when>
                <when test="'''+item.get("field")+''' != null">
                    AND ('''+table+'''.'''+item.get("column")+''' = #{'''+item.get("field")+'''})
                </when>
                <otherwise></otherwise>
            </choose>
            ''')+'''
        </where>
    </delete>
    <update id="update" parameterType="'''+beanpackage+'''.'''+className+'''">
        update '''+table+''' set
        '''+xfor(columns, lambda item:item.get("column")+'''=#{'''+item.get("field")+'''},''')[:-1]+'''
        where '''+table+'''.id = #{id}
    </update>
</mapper>
'''

xoutput(path, className+'Dao.xml', template)