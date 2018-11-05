
public class 修饰符 {
   private static int numInstances = 0;
   protected static int getCount() {
      return numInstances;
   }
 
   private static void addInstance() {
      numInstances++;
   }
 
   修饰符() {
      修饰符.addInstance();
   }
 
   public static void main(String[] arguments) {
      System.out.println("Starting with " +
      修饰符.getCount() + " instances");
      for (int i = 0; i < 500; ++i){
         new 修饰符();
          }
      System.out.println("Created " +
      修饰符.getCount() + " instances");
   }
}