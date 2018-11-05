
import java.io.File;
 
public class 创建目录 {
    public static void main(String args[]) {
        String dirname = "e:/runoob/java/test/create/dir";
        File d = new File(dirname);
        // 现在创建目录
        d.mkdirs();
    }
}