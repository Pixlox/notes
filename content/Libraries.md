#software-engineering/y11 

---
### Random
---
Python's random library implements psuedo-random number generators for a variety of uses. One of the most common is randint.

```python
random.randint(a, b)
```
Return a random integer N such that a <= N <= b. Alias for rand range (a, b+1).

```python
random.choice(seq)
```
Choice returns a random item from a list.

### Importing library
---
In a program, you have to import the library before you can use it.

```python
import random
r == random.randint(1, 10)

import random as rng
r = rng.randint(1, 10)
```

You can also give the imported library a new name; this may be useful to prevent confusion, or just to reduce the amount of space required.

```python
from random import randint as rng

r = rng(1, 10)
```
If you only need to use specific modules, these can be imported directly (and renamed if you wish) rather than adding the entire library.

### Psuedorandom
---
A pseudorandom sequence of numbers is one that appears to be statistically random, despite having been produced by a completely deterministic and repeatable process.

In Python, random uses a random float uniformly in the half-open range `0.0 <= X < 1.0`. Python uses the Mersenne Twister as the core generator. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.

This is good enough for our purposes, but definitely not good enough for sensitive things like cryptography and generating security tokens'


### Datetime structure
---
To store date data digitally, a specific moment in time (called an epoch) is chosen and dates are calculated as the number of seconds before/after that epoch. The Unix epoch is 01/01/1970 00:00:00 UTC.

Python's time library has the modules `time()`, which returns the number of seconds since the Unix epoch, and `time_ns()`, which returns the number of nanoseconds since epoch.