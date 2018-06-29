import java.util.Scanner;

public class A {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int n = 100;
    int[] d = new int[n];
    for (int i = 0; i < n; i++) d[i] = kb.nextInt();
    System.out.println(1+f(d,0,0,false,0));
  }
  public static int f(int[] d, int c, int s, boolean b, int m) {
    if (s == d.length - 1) return m;
    if (b && d[s + 1] >= d[s]) return f(d, c + 1, s + 1, true, Math.max(c + 1, m));
    if (b && d[s + 1] < d[s]) return f(d, 0, s + 1, false, m);
    if (!b && d[s + 1] >= d[s]) return f(d, 1, s + 1, true, m);
    return f(d, 0, s + 1, false, m);
  }
 }
