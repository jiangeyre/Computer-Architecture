Bitwise Operations
------------------

12 == 0b1100


1100
1000
1011

1100
0110
0011

Really similar to Boolean operations, and or not


A  B      A & B  (and)
----------------
0  0        0
1  0        0
0  1        0
1  1        1

A  B      A | B (or)
----------------
0  0        0
1  0        1
0  1        1
1  1        1

A  B      A ^ B (exclusive-or, xor)
----------------
0  0        0
1  0        1
0  1        1
1  1        0


  11101001
& 00001111   AND-mask
----------
  00001001


  11101001
| 00001111
----------
  11101111


Shifting
--------
   vv 
11001010
   ^^

     vv
  11001010
& 00011000  Mask
----------
  00001000
     ^^

      vv
  00001000  Shift right by 3   x = x >> 3
  00000100
  00000010
  00000001
        ^^


Demo by analogy with base 10
----------------------------

  vv
123456
009900  Mask
------
003400

003400  Shift
000340
000034
    ^^

Demo with base 16
-----------------
Extract green channel from pixel

  RRGGBB
0xff7fff
0x00ff00
--------
0x007f00
0x00007f


Decimal
-------
Shifting multiplies/divides by 10, the base

     12
	120
   1200
	120
     12
      1


Binary
------
Shifting multiplies/divides by 2, the base

0b11000  = 24
0b01100  = 12
0b00110  = 6
0b00011  = 3

You can't use shift to multiply by 10. It is a base-2 operation, so it only
multiplies by 2 (or powers of 2).

But if you really wanted to, you could take advantage of the fact that:

x * 10 == x * 8 + x + x

or 

x * 10 == x * 8 + x * 2

which means

x * 10 == (x << 3) + (x << 1)

x = 12
r = (x << 3) + (x << 1)

print(r) # 120

A compiler will know which code to generate to make the program run quickest,
whether that's a MUL or a bunch of shifts and adds.


