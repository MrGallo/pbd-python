# Vowel Capitalization


Open a file specified by the user. Read in each line from the file,
one at a time. Then use square-brackets and an index (`[i]`) and a loop to process that line one character at a time.

If the character is a consonant, simply display it as-is on the screen.
If the character is a lower-case vowel (a,e,i,o,u), display it as a
CAPITAL LETTER instead. This is going to take some `if`
statements.

Name your program `137_vowel_capitalization.py`

You can try the sample input file `vowels.txt` to see what your
program does. You could also test it on any other file you like.


* [vowels.txt](examples/vowels.txt)

Original `voewls.txt`:
```
Old McDonald had a farm; e-i-e-i-o.  (And don't forget 'u'.)
aBCDeFGHiJKLMNoPQRSTuVWXYZ
^bcd^fgh^jklmn^pqrst^vwxyz
```

What your program should do
---------------------------

```
Open which file: vowels.txt

Old McDOnAld hAd A fArm; E-I-E-I-O.  (And dOn't fOrgEt 'U'.)
ABCDEFGHIJKLMNOPQRSTUVWXYZ
^bcd^fgh^jklmn^pqrst^vwxyz
```

```
Open which file: letter.txt

+---------------------------------------------------------+
|                                                    #### |
|                                                    #### |
|                                                    #### |
|                                                         |
|                                                         |
|                              BIll GAtEs                 |
|                              101 MIcrOsOft WAy          |
|                              REdmOnd, WA 78641          |
|                                                         |
+---------------------------------------------------------+

```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)