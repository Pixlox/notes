#software-engineering/y11 

### Binary
---
Binary is a base-2 number system which uses the digits 0 and 1. To convert from decimal to binary, the value should be broken up into powers of 2. For example:

27<sub>10</sub> = 16 + 8 + 2 + 1

Then consider all the possible powers of 2. For each, if they were used, place a 1 in that column. Otherwise, a 0. 

Therefore in the above example: 

27<sub>10</sub> = 11011<sub>2</sub>

To convert a binary value back to decimal, identify which powers of two are assigned a 1, and add the values of these together. For example:

101101<sub>2</sub> = 2<sup>5</sup> + 2<sup>3</sup> + 2<sup>2</sup> + 2<sup>0</sup> = 32 + 8 + 4 + 1 = 45<sub>10</sub>


### Hexadecimal
---
Hexadecimal is a base 16 number system, using the digits 0-9 and the letters A-F. This means it can represent the values 0-15 with one character each. The process for converting to and from hexadecimal is the same, except that now we need to consider how many of each power of 16 there are. For example:

64<sub>10</sub> = 4 x 16

Therefore 64<sub>10</sub> = 4 x 16<sup>1</sup> + 0 x 16<sup>0</sup> = 40<sub>16</sub>

Converting from hexadecimal to decimal requires each power of 16 to be multiplied by its coefficient, with these added together. For example:

A4F<sub>16</sub> = A x 16<sup>2</sup> + 4 x 16<sup>1</sup> + F x 16<sup>0</sup>

