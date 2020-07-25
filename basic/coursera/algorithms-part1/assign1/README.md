# Algorithm and application with disjoint-set data structure

[Wiki](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

## **Specification**

Here is the programming 
assignment [specification](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php) 
that describes the assignment requirements.

Be sure that your code conforms to the prescribed APIs: each program must be in 
the "default" package (i.e., no **package** statements) and include only the 
public methods and constructors specified (extra private methods are fine). 
Note that **algs4.jar** uses a "named" package, so you must use 
an **import** statement to access a class in **algs4.jar**.

## **Web Submission**

Submit a zip file named **percolation.zip** that contains only the two source 
files **Percolation.java** and **PercolationStats.java**.

## **Assessment Report**

Here is some information to help you interpret the assessment report. See 
the [Assessment 
Guide](https://www.coursera.org/learn/algorithms-part1/resources/R2mre) for 
more details.

- *Compilation*: we compile your .java files using a Java 8 compiler. Any error 
or warning messages are displayed and usually signify a major defect in your 
code. If your program does not compile, no further tests are performed.
- API: we check that your code exactly matches the prescribed API (no extra 
methods and no missing methods). If it does not, no further tests are performed.
- *Bugs*: we run [SpotbBugs](https://spotbugs.github.io/) to check for common 
bug patterns in Java programs. A warning message strongly suggests a bug in 
your code but occasionally there are false positives. Here is a summary 
of [bug 
descriptions](https://spotbugs.readthedocs.io/en/latest/bugDescriptions.html), 
which you can use to help decode warning messages.
- *Style*: we run [Checkstyle](http://checkstyle.sourceforge.net/) to 
    automatically checks the style of your Java programs. Here is a list of 
    available [Checkstyle checks](http://checkstyle.sourceforge.net/checks.html), 
    which you can use to help decode any warning messages.
- *Correctness*: we perform a battery of unit tests to check that your code 
    meets the specifications.
- *Memory*: we determine the amount of memory according to the 64-bit memory 
    cost model from lecture.
- *Timing*: we measure the running time and count the number of elementary 
    operations.

## **Personalized Feedback**

In addition to the autograder feedback (available for free via Coursera 
platform), you can pay to have a teaching assistant read and provide 
personalized feedback on your submission 
at [https://mooc.codepost.io](https://mooc.codepost.io/).


## **Backwashing**
After the system has percolated, my PercolationVisualizer colors in light blue
all sites connected to open sites on the bottom (in addition to those connected
to open sites on the top). Is this “backwash” acceptable?
> No, this is likely a bug in Percolation. It is only a minor deduction 
> (because it impacts only the visualizer and not the experiment to estimate 
> the percolation threshold), so don’t go crazy trying to get this detail.
> However, many students consider this to be the most challenging and 
> creative part of the assignment (especially if you limit yourself to one 
> union–find object).

How to visualize backwashing
```bash
java-algs4 PercolationVisualizer  inputs/input10.txt
```
