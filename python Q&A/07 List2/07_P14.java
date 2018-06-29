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
      for (int j = 0; j < c; j++) {
        int s = d[i][j];
        boolean minInRow = true, maxInCol = true;
        for (int ii = 0; ii < r; ii++) {
          if (d[ii][j] > s) maxInCol = false;
        }
        for (int jj = 0; jj < c; jj++) {
          if (d[i][jj] < s) minInRow = false;
        }
        if (minInRow && maxInCol) {
          System.out.println(s);
          return;
        }
      }
    }
    System.out.println(-1);
  }
}
