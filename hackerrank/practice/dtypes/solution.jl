i =  4
d = 4.0
s = "HackerRank"

# Declare second integer, double, and String variables.
x = 0
y = 0.0
z = ""
# Read and save an integer, double, and String to your variables.
# Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
x = parse(typeof(x), readline())
y = parse(typeof(y), readline())
z = readline()
# Print the sum of both integer variables on a new line.
x = x + i
# Print the sum of the double variables on a new line.
y = y + d
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
z = string(s, " ", z)

println(x)
println(y)
println(z)
