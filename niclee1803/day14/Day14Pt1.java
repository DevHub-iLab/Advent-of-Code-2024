import java.util.ArrayList;
import java.util.Scanner;

public class Day14Pt1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line;
        ArrayList<Robot> robots = new ArrayList<>();

        while (true) {
            line = scanner.nextLine().trim();

            if (line.equalsIgnoreCase("done")) {
                break; // Stop processing if "done" is entered
            }
            line = line.replace("p=", "").replace("v=", "");
            String[] parts = line.split(" ");

            String[] position = parts[0].split(",");
            String[] velocity = parts[1].split(",");

            int px = Integer.parseInt(position[0]);
            int py = Integer.parseInt(position[1]);
            int vx = Integer.parseInt(velocity[0]);
            int vy = Integer.parseInt(velocity[1]);

            robots.add(new Robot(px, py, vx, vy));
        }


        int rows = 103;
        int cols = 101;
        int[][] grid = new int[rows][cols];

        for (Robot robot : robots) {
            int row = (robot.py + 100 * robot.vy);
            int col = (robot.px + 100 * robot.vx);

            // normalise
            row = (row % rows + rows) % rows;
            col = (col % cols + cols) % cols;

            grid[row][col]++;
        }

        int q1 = 0;
        int q2 = 0;
        int q3 = 0;
        int q4 = 0;

        // Quadrant 1
        for (int i = 0; i < rows / 2; i++) {
            for (int j = 0; j < cols / 2; j++) {
                q1 += grid[i][j];
            }
        }

        // Quadrant 2
        for (int i = 0; i < rows / 2; i++) {
            for (int j = cols / 2 + 1; j < cols; j++) {
                q2 += grid[i][j];
            }
        }

        // Quadrant 3
        for (int i = rows / 2 + 1; i < rows; i++) {
            for (int j = 0; j < cols / 2; j++) {
                q3 += grid[i][j];
            }
        }

        // Quadrant 4
        for (int i = rows / 2 + 1; i < rows; i++) {
            for (int j = cols / 2 + 1; j < cols; j++) {
                q4 += grid[i][j];
            }
        }

        long safetyFactor = (long) q1 * q2 * q3 * q4;
        System.out.println(safetyFactor);

    }

    static class Robot {
        int px;
        int py;
        int vx;
        int vy;

        public Robot(int px, int py, int vx, int vy) {
            this.px = px;
            this.py = py;
            this.vx = vx;
            this.vy = vy;
        }
    }

}
