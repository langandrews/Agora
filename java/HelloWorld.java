import java.io.PrintWriter;

//Simple Hello World test program
public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        System.out.println("Hello, World!");

        try {
            PrintWriter pw = new PrintWriter("/home/Agora/logs/java_try.log", "UTF-8");
            pw.println("HelloWorld ran");
            pw.close();
        } catch (Exception e) {
            System.out.println("Error in running HelloWorld");
        }
    }
}
