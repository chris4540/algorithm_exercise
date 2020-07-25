import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    // we use a 2d-array to represent the percolation grid
    private boolean[][] grid;

    // The grid size
    private int gridSize = -1;
    // the number of open sites
    private int numOpenSites = 0;

    //
    private WeightedQuickUnionUF disjointSet;
    private int virtualTopIdx = -1;
    private int virtualBottomIdx = -1;

    /*
        creates n-by-n grid, with all sites initially blocked
    */
    public Percolation(int n){
        if (n < 1){
            throw new IllegalArgumentException(
                "the size of the grid should be greater then 0");
        }

        this.gridSize = n;

        // initialize the grid with traditional nested for loop
        this.grid = new boolean[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                // Initialize all sites to be blocked
                this.grid[i][j] = false;
            }
        }

        // init. the disjointSet. plus two for 2 for the virtual top and bottom
        this.disjointSet = new WeightedQuickUnionUF(n*n+2);
        this.virtualTopIdx = 0;
        this.virtualBottomIdx = n*n+1;
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col){
        this.grid[row][col] = true;
        this.numOpenSites += 1;

        // get the index of the site representing in disjointSet
        int idx = convertToDisjointSetIdx(row, col);
        if (row == 0){
            // union the first row element with the virtual top
            this.disjointSet.union(this.virtualTopIdx, idx);
        }
        if (row == this.gridSize-1){
            // union the last row element with the virtual top
            this.disjointSet.union(this.virtualBottomIdx, idx);
        }

        // try to connect up, down, left, and right
        int[] shiftInRow = {0,  0, 1, -1};
        int[] shiftInCol = {1, -1, 0,  0};
        for (int i: shiftInRow){
            for (int j: shiftInCol){
                // check if out of boundary
                if (row+i < 0 || col+j < 0) continue;
                if (row+i >= gridSize || col+j >= gridSize) continue;

                if (this.isOpen(row+i, col+j)){
                    int neighborIdx = convertToDisjointSetIdx(row+i, col+j);
                    this.disjointSet.union(idx, neighborIdx);
                }
            }
        }
    }

    private int convertToDisjointSetIdx(int row, int col){
        // As the disjointSet has virtual top and bottom site, we need to convert
        // the index with this function
        // Example layout of 5-by-5 grid element for indexing in disjoint set
        //           0        <----- virtual top
        //   1   2   3   4   5
        //   6   7   8   9  10
        //  11  12  13  14  15
        //  16  17  18  19  20
        //  21  22  23  24  25
        //          26
        int ret = row * this.gridSize + col;
        ret += 1;
        return ret;
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col){
        return this.grid[row][col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col){
        // If the input site connected to the virtual top, then it is full

        // get the index of the site representing in disjointSet
        int idx = convertToDisjointSetIdx(row, col);
        if (disjointSet.find(virtualTopIdx) == disjointSet.find(idx)){
            return true;
        } else {
            return false;
        }
    }

    // returns the number of open sites
    public int numberOfOpenSites(){
        return this.numOpenSites;
    }

    /*
        Helper function to show the grid
     */
    public void showGrid(){
        int n = this.gridSize;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if (isOpen(i, j)){
                    System.out.print("O");
                } else{
                    System.out.print("X");
                }
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }

    // does the system percolate?
    public boolean percolates(){
        if (disjointSet.find(virtualTopIdx) == disjointSet.find(virtualBottomIdx)){
            return true;
        } else {
            return false;
        }
    }

    // test client (optional)
    public static void main(String[] args){
        int size = Integer.parseInt(args[0]);
        Percolation percolation = new Percolation(size);
        percolation.open(0, 2);
        percolation.open(3, 2);
        percolation.showGrid();

        System.out.format(
            "Is grid(3, 2) full? %b \n",
            percolation.isFull(3, 2));
        System.out.format(
            "Is grid(0, 2) full? %b \n",
            percolation.isFull(0, 2));
        System.out.println("Does the system percolate? " + percolation.percolates());
        System.out.println("--------------------------------------------");
        percolation.open(1, 2);
        percolation.open(2, 2);
        percolation.open(4, 2);
        percolation.open(3, 2);
        percolation.showGrid();
        System.out.println("Does the system percolate? " + percolation.percolates());
    }
}
