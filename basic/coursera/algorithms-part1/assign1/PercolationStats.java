
/*
  The client of the homework
 */
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private int[] numSitesToPercolate;
    private int systemSize = -1;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("Size of percolation system and number of trials must be > 0");
        }

        // set the system size
        systemSize = n;

        // allocate memory for the 1d array
        numSitesToPercolate = new int[trials];

        for (int t = 0; t < trials; t++) { // the loop for Monte Carlo simulation
            // Initialize all sites to be blocked
            Percolation system = new Percolation(n);
            while (!system.percolates()) {

                // draw the site location from uniform distribution
                int row = StdRandom.uniform(0, n);
                int col = StdRandom.uniform(0, n);
                // open it
                system.open(row, col);
            }
            // StdOut.println("------------");
            // system.showGrid();
            // StdOut.println("------------");
            int numOpenedSites = system.numberOfOpenSites();
            numSitesToPercolate[t] = numOpenedSites;
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        // we divied the size after averging to have better numerical acc.
        double ret = StdStats.mean(numSitesToPercolate);
        ret /= (double) systemSize * systemSize;
        return ret;
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        double ret = StdStats.stddev(numSitesToPercolate);
        ret /= (double) systemSize * systemSize;
        return ret;
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        double trials = numSitesToPercolate.length;
        double ret = mean() - ((1.96 * stddev()) / Math.sqrt(trials));
        return ret;
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        double trials = numSitesToPercolate.length;
        double ret = mean() + ((1.96 * stddev()) / Math.sqrt(trials));
        return ret;
    }

    // test client (see below)
    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats sim = new PercolationStats(size, trials);

        double mean = sim.mean();
        double stddev = sim.stddev();
        double confLo = sim.confidenceLo();
        double confHi = sim.confidenceHi();

        // printout
        StdOut.printf("mean                    = %.8f\n", mean);
        StdOut.printf("stddev                  = %.8f\n", stddev);
        StdOut.printf("95%% confidence interval = [%.8f, %.8f]\n", confLo, confHi);
    }
}
