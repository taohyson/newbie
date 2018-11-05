abstract class Caravan{
   private double price;
   private String model;
   private String year;
   public abstract void goFast(); //抽象方法
   public abstract void changeColor();
}

public abstract class abstract修饰符{
    abstract void m(); //抽象方法
}
 
class SubClass extends abstract修饰符{
     //实现抽象方法
      void m(){
          // .........
      }
}