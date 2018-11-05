
public class 虚方法 {
   public static void main(String [] args) {
      虚方法Salary s = new 虚方法Salary("员工 A", "北京", 3, 3600.00);
      虚方法Employee e = new 虚方法Salary("员工 B", "上海", 2, 2400.00);
      System.out.println("使用 虚方法Salary 的引用调用 mailCheck -- ");
      s.mailCheck();
      System.out.println("\n使用 虚方法Employee 的引用调用 mailCheck--");
      e.mailCheck();
    }
}