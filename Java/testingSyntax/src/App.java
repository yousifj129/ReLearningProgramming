
import java.util.Random;
import java.util.Vector;


public class App {

    public static void main(String[] args) throws Exception {
        Vector<Integer> v = new Vector<>();
        Random rand = new Random();
        for (int i = 0; i < 10; i++) {
           v.add(rand.nextInt(0,100)); 
        }
        System.out.println(v);
    }
}
