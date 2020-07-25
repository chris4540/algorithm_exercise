import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdOut;
import java.util.Scanner;

public class Percolation {

    // we use a 2d-array to represent the percolation grid
    private boolean[][] grid;

    // The grid size
    final private int gridWidth;
    // the number of open sites
    private int numOpenSites;

    //
    final private WeightedQuickUnionUF disjointSet;
    final private int virtualTopIdx;
    final private int virtualBottomIdx;

    // // memorize if the system has percolated.
    // private boolean hasPercolated = false;

    /*
     * creates n-by-n grid, with all sites initially blocked
     */
    public Percolation(int n) {
        if (n < 1) {
            throw new IllegalArgumentException("the size of the grid should be greater then 0");
        }

        this.gridWidth = n;
        this.numOpenSites = 0;
        // this.hasPercolated = false;

        // initialize the grid with traditional nested for loop
        this.grid = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Initialize all sites to be blocked
                this.grid[i][j] = false;
            }
        }

        // init. the disjointSet. plus two for 2 for the virtual top and bottom
        this.disjointSet = new WeightedQuickUnionUF(n * n + 2);
        this.virtualTopIdx = 0;
        this.virtualBottomIdx = n * n + 1;
    }

    // opens the site (row, col) if it is not open already
    // Notes: row, col ~ [1...n]
    public void open(int row, int col) {
        validateInput(row, col);

        // if the site is already opened, just return
        if (this.grid[row - 1][col - 1]) {
            return;
        }
        // open the site
        this.grid[row - 1][col - 1] = true;
        this.numOpenSites += 1;

        // get the index of the site representing in disjointSet
        int idx = convertToDisjointSetIdx(row, col);
        if (row == 1) {
            // union the first row element with the virtual top
            this.disjointSet.union(this.virtualTopIdx, idx);
        }

        // check if the system has percolated. If so, stop connecting the bottom
        // row to the virtual bottom to prevent backwash
        //
        if (row == this.gridWidth && !this.percolates()) {
            // union the last row element with the virtual top
            this.disjointSet.union(this.virtualBottomIdx, idx);
        }

        // try to connect up, down, left, and right
        int[] shiftInRow = { 0, 0, 1, -1 };
        int[] shiftInCol = { 1, -1, 0, 0 };
        int nShift = Math.min(shiftInRow.length, shiftInCol.length);
        for (int s = 0; s < nShift; s++) {
            int i = shiftInRow[s];
            int j = shiftInCol[s];
            // check if out of boundaries
            if (row + i < 1 || col + j < 1)
                continue;
            if (row + i > gridWidth || col + j > gridWidth)
                continue;

            if (this.isOpen(row + i, col + j)) {
                int neighborIdx = convertToDisjointSetIdx(row + i, col + j);
                this.disjointSet.union(neighborIdx, idx);
            }
        }
    }

    private int convertToDisjointSetIdx(int row, int col) {
        // As the disjointSet has virtual top and bottom site, we need to convert
        // the index with this function
        // Example layout of 5-by-5 grid element for indexing in disjoint set
        // 0 <----- virtual top
        // 1 2 3 4 5
        // 6 7 8 9 10
        // 11 12 13 14 15
        // 16 17 18 19 20
        // 21 22 23 24 25
        // 26
        int ret = (row - 1) * this.gridWidth + col;
        return ret;
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        validateInput(row, col);
        return this.grid[row - 1][col - 1];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        validateInput(row, col);
        // If the input site connected to the virtual top, then it is full

        // get the index of the site representing in disjointSet
        int idx = convertToDisjointSetIdx(row, col);
        if (disjointSet.find(virtualTopIdx) == disjointSet.find(idx)) {
            return true;
        }
        return false;
    }

    private void validateInput(int row, int col){
        if (row < 1 || row > this.gridWidth){
            throw new IllegalArgumentException(
                String.format("The row input should in between 1 and %d.",
                this.gridWidth));
        }
        if (col < 1 || col > this.gridWidth){
            throw new IllegalArgumentException(
                String.format("The col input should in between 1 and %d.",
                this.gridWidth));
        }
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return this.numOpenSites;
    }

    // does the system percolate?
    public boolean percolates() {
        if (disjointSet.find(virtualTopIdx) == disjointSet.find(virtualBottomIdx)) {
            // this.hasPercolated = true;
            return true;
        }
        return false;
    }

    // /*
    // * Helper function to show the grid
    // */
    private void showGrid() {
        int n = this.gridWidth;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (isOpen(i, j)) {
                    System.out.print("O");
                } else {
                    System.out.print("X");
                }
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }

    // test client (optional)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = Integer.parseInt(sc.nextLine().trim());
        Percolation sys = new Percolation(size);

        while (sc.hasNextLine()){
            // StdOut.println(sc.nextLine().trim());
            String tokens[] = sc.nextLine().trim().split(" ");

            int row = Integer.parseInt(tokens[0]);
            int col = Integer.parseInt(tokens[1]);
            sys.open(row, col);
            sys.showGrid();
            StdOut.printf("isFull(%d, %d) = %b\n", row, col, sys.isFull(row, col));
        }
        sc.close();
    }
}
