# 2025 - Day 1

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/1)

#### What are we asked to find?

* The password to open a safe

#### What do we know?

* The safe has a dial has 100 positions (0 through 99)
* The dial starts at 50
* The combination is the number of times that dial points at zero during the rotation sequence
* The dial can be rotated left or right

#### What can we assume?


### Explore

* Seems simple enough application of the modulo

### Plan

* For every Left rotation, subtract the number of clicks from the current value
* For every right rotation, add the number of clicks from the current value
* After each instruction, calculate the modulo 100
* If the dial is at zero, then increment the count of times the dial has been at zero

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/1#part2)

#### What are we asked to find?

* Not just when the dial stops at zero, but also zero crossings

### Explore


### Plan

* Break all dial moves down into mutliple moves where no single move exceeds 100
* Count all zero crossings and times where the dial is left at zero
