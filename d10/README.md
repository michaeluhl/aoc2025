# 2025 - Day 10

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/10)

#### What are we asked to find?

The fewest number of button pushes to initialize all of the machines

#### What do we know?

* Each machine has a series of lights
* The lights must be set to a certain configuration in order to initialize the machine
* Each machine also has a series of buttons
  * Each button will toggle a set of lights
  * Lights are zero-indexed in the button definitions

#### What can we assume?


### Explore

* Here's what I'm thinking:  * The sequence of button pushes doesn't matter
  * Pushing a button an even number of times is the same as pushing it zero times
  * Pushing a button any odd number of times is the same as pushing it onces

* Based on this, I think that we can just progressively combine buttons until we find a sequence that works
* I think that it makes the most sense to do a sort of breadth first search (e.g., button 1 with button 2, button 2 with button 3, button 3 with button 4, ...)
* Cache results

### Plan


## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/10#part2)

#### What are we asked to find?


### Explore

* I think that I might be able to get the solution as:

$$
\left(A^T A\right) x = A^T b
$$

$$
x = \left(A^T A\right)^{-1} A^T b
$$

* Playing around here, the problem is that because there can be multiple solutions (we have more variables than equations) you're not guaranteed to get the lowest solution - your also not guaranteed to get an integer solution.
* You can obtain the right solution from $x + N @ y$ where $N$ is an orthogonal basis for the null space of $A$ and $y$ is a vector scaling those components.  But, I don't know how to choose $y$ without knowing the particular solution that is being sought.
* So, I'm not sure that this is a fruitful avenue

* I'm wondering if i can do something like what was done for part 1, but instead start with desired counter values and subtracting each wiring sequence
  * This works... for the sample data
  * It appears to be unusably slow for the full data.  Even running for 30 minutes it doesn't obtain the solution for the first row of the real data

### Plan

