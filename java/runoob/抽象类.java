
public class 抽象类
{
   public static void main(String [] args)
   {
      /* 以下是不允许的，会引发错误 */
      // 抽象类Employee e = new 抽象类Employee("George W.", "Houston, TX", 43);
 
      // System.out.println("\n Call mailCheck using 抽象类Employee reference--");
      // e.mailCheck();

      抽象类Salary s = new 抽象类Salary("Mohd Mohtashim", "Ambehta, UP", 3, 3600.00);
      抽象类Employee e = new 抽象类Salary("John Adams", "Boston, MA", 2, 2400.00);
 
      System.out.println("Call mailCheck using 抽象类Salary reference --");
      s.mailCheck();
 
      System.out.println("\n Call mailCheck using 抽象类Employee reference--");
      e.mailCheck();
    }
}