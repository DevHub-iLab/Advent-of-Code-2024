import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day14Pt2 {
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

        int elapsedTime = 2;
        while (true) {
            for (int i = 0; i < rows; i++) {
                Arrays.fill(grid[i], 0); // Use '.' for empty spaces
            }

            for (Robot robot : robots) {
                int newPy = robot.py + elapsedTime * robot.vy;
                int newPx = robot.px + elapsedTime * robot.vx;

                int row = ((newPy % rows) + rows) % rows;
                int col = ((newPx % cols) + cols) % cols;

                grid[row][col]++;
            }

            boolean allUnique = true;
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    if (grid[i][j] > 1) {
                        allUnique = false;
                        break;
                    }
                }
            }

            if (allUnique) {
                System.out.println(elapsedTime);
                for (int i = 0; i < rows; i++) {
                    for (int j = 0; j < cols; j++) {
                        System.out.print(grid[i][j] + " ");
                    }
                    System.out.println();
                }
                break;
            }

            elapsedTime++;
        }


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
