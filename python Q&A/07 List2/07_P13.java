import java.util.Scanner;

public class AAA {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int r = kb.nextInt();
    int c = kb.nextInt();
    int[][] d = new int[r][c];
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        d[i][j] = kb.nextInt();
      }
    }
    for (int i = 0; i < r; i++) {
      boolean found = false;
      for (int ii = i+1; !found && ii < r; ii++) {
        if (i == ii) continue;
        boolean same = true;
        for (int j = 0; same && j < c; j++) {
          same = (d[i][j] == d[ii][j]);
        }
        if (same) found = true;
        if (found) {
          System.out.println(i + 1);
          for (int j = 0; j < c; j++) {
            System.out.print(d[i][j] + " ");
          }
          System.out.println();
          System.out.println(ii + 1);
          for (int j = 0; j < c; j++) {
            System.out.print(d[i][j] + " ");
          }
          System.out.println();
        }
      }
    }
  }
}
