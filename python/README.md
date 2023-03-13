# Python

## Text wrap

The `textwrap` module provides two convenient function: `wrap()` and `fill()`

[`textwrap.wrap()`](https://docs.python.org/2/library/textwrap.html#textwrap.wrap)

The `wrap()` function wraps a single paragraph in text (a string) so that every line is width characters long at most.

It returns a list of output lines

```python
import textwrap

string = "This is a very very very very long string."
print(textwrap.wrap(string, 8))
```

[`textwrap.fill()`](https://docs.python.org/2/library/textwrap.html#textwrap.fill)

The `fill()` function wraps a single parahraph in text and returns a single string, string containing the wrapped paragraph

```python
import textwrap

string = "This is a very very very very long string."
print(textwrap.fill(string, 8))
```

## Introduction to Sets

A set is an unordered collections of elements without duplicate entries.

When printed, iterated or converted into a squence, its elements will appear in an arbitary order.

### Example

```python
print(set())
# set([])

print(set('YusrilArzaqi'))
# {'i', 's', 'r', 'u', 'l', 'A', 'a', 'Y', 'q', 'z'}

print(set([1, 2, 1, 2, 3, 4, 5, 6, 0, 9, 12, 22, 3]))
# {0, 1, 2, 3, 4, 5, 6, 9, 12, 22}

print(set(1, 2, 3, 4, 5, 5))
# {1, 2, 3, 4, 5}

print(set(set(['Y', 'u', 's', 'r', 'i', 'l', 'A', 'r', 'z', 'a', 'q', 'i'])))
# {'i', 's', 'r', 'u', 'l', 'A', 'a', 'Y', 'q', 'z'}

print(set({'Yusril': 'LINUX', 'Arzaqi': 420}))
# {'Yusril', 'Arzaqi'}

print(set(enumerate(['Y', 'u', 's', 'r', 'i', 'l', 'A', 'r', 'z', 'a', 'q', 'i'])))
# {(9, 'a'), (5, 'l'), (1, 'u'), (4, 'i'), (3, 'r'), (6, 'A'), (7, 'r'), (11, 'i'), (8, 'z'), (2, 's'), (10, 'q'), (0, 'Y')}
```

Basically, sets are used for membership testing and eliminating duplicate entries.

### Task

Now, let's use our knowledge of sets and help Mickey.

Ms.Gabriel Williams is a botany professor at District Collage. One day, she
asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse

Formula used:

$Average = \frac{Sum of Distinct Heights}{Total Number of Distinct Heights}$

### Function Description

Average has the following parameter

- `int` `arr`: an array of integers

### returns

- `float`: the resulting float value rounded to 3 places after the decimal

### Input Format

The first line contain the integer $N$, the size of $arr$.

The second line contain the $N$ space-sepaarated integers, $arr[i]$

### Explanation

Here, `set([154, 161, 167, 170, 171, 174, 178, 182])` is the set containing the distinct heights.
Using `sum()` and `len()` function, we can compute the average.

$Average = \frac{1355}{8}   = 169.375$

## Symmetric Difference

### Concept

If the inputs given on one line separated by a characters (the delimiter), use `split()` to get separated values in the form of a list.
The delimiter is space (ascii 32) by default.
To specify that comma is the delimiter, use `string.split(',')`.
For this challenge, and in general on HackerRank, space will be the delimiter.

### Usage

```python
a = input()
# 5 4 3 2
lis = a.split()
print(lis)
# ['5', '4', '3', '2']
```

If the list values are all integer types, use the `map()` method to convert all the strings to integers.

### Creating Sets

```python
myset = {1, 2} # Directly assigning values to a set
myset = set() # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print(myset)
# {'a', 'b'}
```

### Modifying Sets

Using the `add()` function:

```python
myset = set('a', 'b')
myset.add('c')
print(myset)
# {'a', 'b', 'c'}
myset.add('a') # As 'a' already exists in the set, nothing happends
myset.add((5,4))
print(myset)
# {'a', 'c', 'b', (5,4)}
```

---

Using the `update()` function:

```python
myset.update([1, 2, 3, 4]) # update() only works for iterable objects
print(myset)
# {1, 2, 3, 4, 5, 'b', (5, 4), 'c', 'a'}

myset.update({1, 7, 8})
print(myset)
# {1, 2, 3, 4, 5, 7, 8, 'a', (5, 4), 'c', 'b'}

myset.update({1, 6}, [5, 13])
# {1, 2, 3, 4, 5, 6, 7, 8, (5, 4), 13, 'c', 'b', 'a'}
```

### Removing Items

Both the `discard()` and `remove()` functions take a single value as an argument and removes that value from the set.
If that value is not present, `discard()` does nothing, but `remove()` will raise a `KeyError` exception.

```python
myset.discard(10)
print(myset) # nothing happends
# {1, 2, 3, 4, 5, 6, 7, 8, 'c', (5, 4), 13, 'b', 'a'}

myset.remove(13)
print(myset)
# {1, 2, 3, 4, 5, 6, 7, 8, 'c', (5, 4), 'a', 'b'}
```

### Common Set operations

Using `union()`, `intersection()`, and `difference()` functions.

```python
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

print(a.union(b)) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}

print(a.intersection(b)) # Values which exist in a and b
# {2, 4}

print({9, 5}) # Values which exist in a but not in b
# {9, 5}
```

---

The `uinion()` and `intersection()` function are symmetric methods:

```python
print(a.union(b) == b.union(a))
# True

print(a.intersection(b) == b.intersection(a))
# True

print(a.difference(b) == b.difference(a))
# False
```

These [other built-in data structures in Python](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-4--built-in-data-structures-strings-lists-tuples-dictionaries-mutability) are also useful.

### Task

Given $2$ sets of integers, $M$ and $N$, print their symmetric difference in asscending order.
The term symmetric difference indicates those values that exist in either $M$ or $N$ but do not exists in both.

### Input Format

The first line of input contains an integer, $M$.

The second line contains $M$ space-separated integers.

The third line contains an integer, $N$.

The fourth line contains $N$ space-separated integers.

### Output Format

Output the symmetric difference integers in ascending order, one per line.

## No Ideal

There is an array of $n$ integers. There are also $2$ **disjoint sets**, $A$ and $B$, each containing $m$ integers.
You like all the integers in set $A$ and dislike all the integers in set $B$.
Your initial happiness is $0$.
For each $i$ integer in the array, if $i \in A$, you add $1$ to your happiness.
If $i \in B$, you add -1 to your happiness.
Otherwise, your happiness does not change.
Output your final happiness at the end.

**Note:** Since $A$ and $B$ are sets, they have no repeated elements.
However, the array might contain duplicate elements.

### Input Format

- The first line contains integers $n$ and $m$ separated by a space.
- The second line contains $n$ integers, the elements of the array.
- The third and fourth lines contain $m$ integers, $A$ and $B$, respectively.

### Output Format

Output a single integer, your total happiness.

### Explanation

You gain $1$ unit of happiness for elements $3$ and $1$ in set $A$.
You lose $1$ unit for $5$ in set $B$.
The element $7$ in set $B$ does not exist in the array so it is not included in the calculation.

Hence, the total happiness is $2 - 1 = 1$

##
