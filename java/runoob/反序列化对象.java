
import java.io.*;
 
public class 反序列化对象
{
   public static void main(String [] args)
   {
      序列化对象Employee e = null;
      try
      {
         FileInputStream fileIn = new FileInputStream("employee.ser");
         ObjectInputStream in = new ObjectInputStream(fileIn);
         e = (序列化对象Employee) in.readObject();
         in.close();
         fileIn.close();
      }catch(IOException i)
      {
         i.printStackTrace();
         return;
      }catch(ClassNotFoundException c)
      {
         System.out.println("序列化对象Employee class not found");
         c.printStackTrace();
         return;
      }
      System.out.println("Deserialized 序列化对象Employee...");
      System.out.println("Name: " + e.name);
      System.out.println("Address: " + e.address);
      System.out.println("SSN: " + e.SSN);
      System.out.println("Number: " + e.number);
    }
}