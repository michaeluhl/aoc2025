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

* After pursuing this a little more, the answer is to consider this as a system of [Diophantine_equations](https://en.wikipedia.org/wiki/Diophantine_equation) (linear equations with integer coefficients and integer solutions - exactly what we need, since we have to push the buttons whole numbers of times).  A particular solution can be found by decomposing the coefficient matrix into [Smith Normal Form](https://en.wikipedia.org/wiki/Smith_normal_form).

* The process of producing the Smith Normal Form gives two matrices, $U$ and $V$ such that, $A_{SNF} = U A V$; the Wikipedia article refers to $A_{SNF}$ as $B$.
  Further, the article refers to $U b$ (as I write it here) as $D$.

* The original system can thus be re-written as:

$$
U A V V^{-1} x = U b
$$

  or 

$$
B V^{-1} x = D
$$

* $B$ is only non-zero on the diagonal - and even then, only some of the entries are non-zero - we can rewrite this as:

$$
V^{-1} x = \left[d_1/b_{1,1} ... d_k/b_{k,k} h_{k+1} ... h_n\right]^T
$$

  where $k$ is the index of the last non-zero entry in the diagonal of $B$ and $h_{k+1}$ thru $h_n$ are arbitrary integers.
  We'll call this vector $y$

$$
V^{-1} x = y
$$

* It follows, then, that

$$
x = V y
$$

* All my troubles come in determining the appropriate values of $h_{k+1}$ through ${h_n}$, as these are what's needed to answer the ultimate question for each machine - what's the sum of the number of time each button must be pushed to get right joltage.
  We need to determine the right values of these free variables ($h_i$) in order to minimize $x$ while keeping all values non-negative.

* We can see the effect of each free variable by looking at:

$$
V \left[ d_1/b_{1,1} ... d_k/b_{k,k} 1 ... 0 \right]^T - x
$$

* We set each $h_i$ individually to $1$, calculate the product with $V$ and subtract $x$.
  This shows us how each $h_i$ affects the solution vector.

* We can make a matrix out of these vectors...

$$
Y = \left[ y_{k+1}^T ... y_n^T \right]
$$

* Then we can consider the system:

$$
Y h \le x
$$

  where all $h_i \ge 0$

* From what I gather this is a [linear pogramming](https://en.wikipedia.org/wiki/Linear_programming) problem, but really this doesn't help much.

* Instead we can go through each row of $Y$ and $x$ and look for rows in $Y$ that have only one non-zero value.
  If we find any of those, they can be use to set constraints on the values of $h$

* What took me a long time was realizing that we can also add rows with within $Y$ to look for combinations that give us a single non-zero value, and then use those results to set constraints as well.

* This last piece allowed me to obtain solutions in reasonable times.

### Plan

