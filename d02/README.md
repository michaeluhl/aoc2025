# 2025 - Day 2

## Part 1

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/2)

#### What are we asked to find?

* The sum of all invalid ids

#### What do we know?

* Product id ranges are separated by commas
* The first id and last id in a range are separated by dashes
* Valid ids don't have leading zeros
* Invalid ids consist of a repeated sub-pattern

#### What can we assume?


### Explore

* It's really tempting to want to try some sort of regex solution on this, but you still have to generate ids to test that way - and I'm pretty sure that the point is not to brute force this.

### Plan

* My naive approach is:
  * Take the first and last ids of each range:
    * Taking the ids as strings, split each in two
    * Make a range out of the first halves and a second out of the second halves
    * For each value in the first range, test if it's in the second range
* Thinking about this more, I don't think this plan works.  I don't want to have to check each value, because I'm sure that part 2 will rule out brute force solutions... need to think about whether there's a better way...

## Part 2

### Define the Problem

The text of the problem is available [here](https://adventofcode.com/2025/day/2#part2)

#### What are we asked to find?

* The sum of invalid ids

### Explore

* This time invalid ids are ones that consist exclusively of repeated units - but these units can be as short as a single digit.

### Plan

