import java.util.Scanner;

public class A {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int n = kb.nextInt();
    int[] d = new int[n];
    for (int i = 0; i < n; i++) d[i] = kb.nextInt();
    System.out.println(isASorted(d) || isDSorted(d));
  }
  public static boolean isASorted(int[] d) {
    return isASorted(d, d.length);
  }
  private static boolean isASorted(int[] d, int n) {
    if (n <= 1) return true;
    if (d[n - 2] > d[n - 1]) return false;
    return isASorted(d, n - 1);
  }
  public static boolean isDSorted(int[] d) {
    return isDSorted(d, d.length);
  }
  private static boolean isDSorted(int[] d, int n) {
    if (n <= 1) return true;
    if (d[n - 2] < d[n - 1]) return false;
    return isDSorted(d, n - 1);
  }
}
