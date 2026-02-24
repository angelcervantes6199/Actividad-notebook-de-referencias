import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int a = 5;
        int b = a;   // copia el valor 5
        a = 10;
        System.out.println(b); // 5
        System.out.println(a); // 10
    }
}
