# 2025 - Day 5

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/5)

#### What are we asked to find?

How many of the available ingredient ids are fresh?

#### What do we know?

* We're give a list of id ranges, with ids falling within any of those ranges considered to be fresh
* We're give a list of ingredient ids to be compared to those ranges

#### What can we assume?


### Explore


### Plan

* Simply make Python ranges for each of the ranges
* Then for each id, start going through the ranges and stop at the first one that contains the ids
* If a matching range is found, then increment the count

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/5#part2)

#### What are we asked to find?

The count of all possible fresh ids

### Explore


### Plan (initial)

* Build a bit map based on the ranges
* Count the number of set bits to give the total number of fresh ids

> [!CAUTION]
> This method works for the sample data but fails with a memory error when used with the real data.

