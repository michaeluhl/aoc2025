# 2025 - Day 11

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/11)

#### What are we asked to find?

The number of different paths between "you" and the output

#### What do we know?

* We're given a list of connection

#### What can we assume?


### Explore



### Plan

* Build a graph
* Walk the graph

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/11#part2)

#### What are we asked to find?

* The number of paths from svr->{fft&dac}->out

### Explore


### Plan

* Tried a bunch of different things, but made a caching tracer, with arbitrary start/stop nodes
* Then searched for the paths to the end starting at dac and fft.  fft took too long, so I assumed that all paths went from dac->out (seems like a reasonable assumption since part 1 didn't have loops, and you can't have arbitrary ordering without the potential for loops)
* Then searched for paths from fft->dac
* Then searched for paths from svr->fft
* Then just took the product of the results

