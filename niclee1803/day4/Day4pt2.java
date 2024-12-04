import java.util.Scanner;

public class Day4pt2 {
    static boolean checkXMasShape(char[][] grid, int i, int j) {
        // Center must be 'A'
        if (grid[i][j] != 'A') return false;

        // M - S
        // - A -
        // M - S
        if (grid[i-1][j-1] == 'M' && grid[i+1][j+1] == 'S' &&
                grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M') {
            return true;
        }

        // S - S
        // - A -
        // M - M
        if (grid[i-1][j-1] == 'S' && grid[i+1][j+1] == 'M' &&
                grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M') {
            return true;
        }

        // M - M
        // - A -
        // S - S
        if (grid[i-1][j-1] == 'M' && grid[i+1][j+1] == 'S' &&
                grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S') {
            return true;
        }

        // S - M
        // - A -
        // s - M
        if (grid[i-1][j-1] == 'S' && grid[i+1][j+1] == 'M' &&
                grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S') {
            return true;
        }

        return false;
    }


    static int countXMasShapes(char[][] grid) {
        int count = 0;
        int m = grid.length;
        int n = grid[0].length;


        // For each center
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (checkXMasShape(grid, i, j)) {
                    count++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder inputStringBuilder = new StringBuilder();

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            if (line.equals("done")) break; // done to signify end of input
            inputStringBuilder.append(line).append("\n");
        }

        String[] lines = inputStringBuilder.toString().split("\n");
        int rows = lines.length;
        int cols = lines[0].length();

        char[][] charGrid = new char[rows][cols];

        // put input into char array form
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                charGrid[i][j] = lines[i].charAt(j);
            }
        }

        int count = countXMasShapes(charGrid);

        System.out.println(count);
    }
}
