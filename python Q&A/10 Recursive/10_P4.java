import java.util.Scanner;

public class A {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int a = kb.nextInt();
    int k = kb.nextInt();
    int m = kb.nextInt();
    System.out.println(powmod(a, k, m));
  }
  static int powmod(int a, int k, int m) {
    if (k == 0) return 1;
    int p = powmod(a, k / 2, m);
    p = (p * p) % m;
    if (k % 2 == 1) p = (a * p) % m;
    return p;    
  }
}
