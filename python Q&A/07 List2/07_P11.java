
import java.util.Scanner;

public class BBB {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int nc = kb.nextInt();
    int ns = kb.nextInt();
    String[][] g = new String[nc][ns];
    for (int i = 0; i < nc; i++) {
      for (int j = 0; j < ns; j++) {
        g[i][j] = kb.next().trim();
      }
    }
    String G = "A B+B C+C D+D F ";
    double[] P = { 4, 3.5, 3, 2.5, 2, 1.5, 1, 0 };
    double[] cgpa = new double[nc];
    for (int i = 0; i < nc; i++) {
      double s = 0;
      int n = 0;
      for (int j = 0; j < ns; j++) {
        if (!g[i][j].equals("X")) {
          s += P[G.indexOf((g[i][j] + " ").substring(0, 2)) / 2];
          n++;
        }
      }
      cgpa[i] = s / n;
    }
    for (int i = 0; i < nc; i++) {
      System.out.printf("%4.2f\n", cgpa[i]);
    }
  }
}
