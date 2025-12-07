# 2025 - Day 7

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/7)

#### What are we asked to find?

* The number of times that the tachyon beam is split

#### What do we know?

* The beam always moves downward
* The beam starts immediately below "S"
* When a beam intersects a splitter, a new beam is initiated immediately to the left and right of the splitter
* When splitters are located with only one space between them, only one resultant beam is created in the space between them.

#### What can we assume?


### Explore

* Looking at the input, I don't think that part 2 can ask about beams going sideways, so I'm going to guess that part 2 is going to have something to do with beam strength and build accordingly.

### Plan

* Read the file into a 2d array

* When building the array convert:
  * empty spaces to zeros
  * Source to 100
  * splitters to -1

* Intialize the split count to zero

* Loop over the rows in the array:
  * If a value greater than zero is encountered:
    * Take that value as `beamstren`
    * Examine the space immediately below it in the next row.
      * If the value in that space is zero, set that space to `beamstren`
      * If the value in that space is less than zero, add half of `beamstren` to the positions immediately to the left and right of that space.  Increment the split count
      * Otherwise, add `beamstren` to the value in that space

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/7#part2)

#### What are we asked to find?

* The total number of unique paths that a tachyon could take

### Explore

* This isn't really where I thought that part 2 would go, so I don't know that the machinery that I set up really helps to address the description
* For a second I thought that it could - I thought that I could look at the beam strenths at the bottom and from that determine how many ways you could get to that position, but since I'm only halving the strength at splitters I don't think this works.
* There might be a way though - if I revise the algorithm such I get rid of the halving, and just sum overlapping values...

### Plan

* Start with a strength of 1 rather than 100
* Don't halve at splitters
* The answer should just be the sum of the values at the bottom

