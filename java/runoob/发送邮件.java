
import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;
 
public class 发送邮件
{
   public static void main(String [] args)
   {   
      // 获取系统属性
      Properties properties = System.getProperties();
      // 设置邮件服务器
      properties.setProperty("mail.smtp.host", "localhost");
      // 获取默认session对象
      Session session = Session.getDefaultInstance(properties);
 
      try{
         // 创建默认的 MimeMessage 对象
         MimeMessage message = new MimeMessage(session);
 
	     // 发件人电子邮箱
         message.setFrom(new InternetAddress("zhujiwan888@gmail.com"));
 
	     // 收件人电子邮箱
         message.addRecipient(Message.RecipientType.TO, new InternetAddress("541885431@qq.com"));
 
         // Set Subject: 头部头字段
         message.setSubject("This is the Subject Line!");
 
         // 设置消息体
         message.setText("This is actual message");
 
         // 发送消息
         Transport.send(message);
         System.out.println("Sent message successfully....");
      }catch (Exception mex) {
         mex.printStackTrace();
      }
   }
}