# 2025 - Day 6

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/6)

#### What are we asked to find?

* The sum of the answers to the individual homework problems

#### What do we know?

* We're given a set of math problems
* The problems are laid out in columnar format with the operator at the bottom of a set of inputs

#### What can we assume?

* Looking at the input, it looks like the number of inputs for each operator is the same

### Explore


### Plan

* Read each line of the input, use split() to break into individual input
* For numerical inputs, put each row into an operands 
* For operators, put them into a separate list

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/6#part2)

#### What are we asked to find?

Same as before, but the interpretation of the data is now different

### Explore


### Plan

* Read each line as a string
* When we get to the operators, we'll use the operator positions to split the data rows because the operator is always in the first column of the applicable data set
