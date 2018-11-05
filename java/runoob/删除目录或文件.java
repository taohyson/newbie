
import java.io.File;
 
public class 删除目录或文件 {
    public static void main(String args[]) {
        // 这里修改为自己的测试目录
        File folder = new File("e:/runoob");
        deleteFolder(folder);
    }
 
    // 删除文件及目录
    public static void deleteFolder(File folder) {
        File[] files = folder.listFiles();
        if (files != null) {
            for (File f : files) {
                if (f.isDirectory()) {
                    deleteFolder(f);
                } else {
                    f.delete();
                }
            }
        }
        folder.delete();
    }
}