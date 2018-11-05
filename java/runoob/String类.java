
public class String类{
   public static void main(String args[]){
      char[] helloArray = { 'r', 'u', 'n', 'o', 'o', 'b'};
      String helloString = new String(helloArray);  
      System.out.println( helloString );
      System.out.println( "菜鸟教程网址长度 : " + helloString.length() );
      String string1 = "菜鸟教程网址：";     
      System.out.println("1、" + string1 + "www.runoob.com");  
      float floatVar = -9.5f;
      int intVar = -38;
      String stringVar = "zx\n123456;";
      System.out.printf("浮点型变量的值为 " +
              "%f, 整型变量的值为 " +
              " %d, 字符串变量的值为 " +
              "is %s", floatVar, intVar, stringVar);
   }
}