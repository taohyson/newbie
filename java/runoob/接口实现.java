
public class 接口实现 implements 接口{
 
   public void eat(){
      System.out.println("Mammal eats");
   }
 
   public void travel(){
      System.out.println("Mammal travels");
   } 
 
   public int noOfLegs(){
      return 0;
   }
 
   public static void main(String args[]){
      接口实现 m = new 接口实现();
      m.eat();
      m.travel();
   }
}