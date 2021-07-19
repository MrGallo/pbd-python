# Gender Game


Make a program which displays an appropriate name for a
person, using a combination of nested `if`s
and compound conditions. Ask the user for a gender, first name,
last name and age.


If the person is female and 20 or over, ask if she is married. If
so, display "Mrs." in front of her name. If not, display "Ms." in front
of her name. If the female is under 20, display her first and last
name.


If the person is male and 20 or over, display "Mr." in front of his
name. Otherwise, display his first and last name.


Note that asking a person if they are married should
*only* be done if they are female and 20 or older, which
means you will have a single `if` and
`else` nested inside one of your
`if` statements.


Also, did you know that with an `if` statement
(or `else`), the curly braces are
**optional** when there is only one statement inside?



```
What is your gender (M or F): F
First name: Kim
Last name: Kardashian
Age: 32 

Are you married, Kim (y or n)? y

Then I shall call you Mrs. Kardashian.

```

 



```
What is your gender (M or F): F
First name: Marisa
Last name: Tomei
Age: 48 

Are you married, Marisa (y or n)? n

Then I shall call you Ms. Tomei.

```

Notice that in the example below, we *never even ask the marriage
question*, because she is under 20 and so her marital status doesn't
change what we call her.



```
What is your gender (M or F): F
First name: Chloe
Last name: Moretz
Age: 16 

Then I shall call you Chloe Moretz.

```

 



```
What is your gender (M or F): M
First name: Daniel
Last name: Radcliffe
Age: 23  

Then I shall call you Mr. Radcliffe.

```

 



```
What is your gender (M or F): M
First name: Zachary
Last name: Gordon
Age: 15 

Then I shall call you Zachary Gordon.

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)