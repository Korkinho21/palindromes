# Palindromes

This code shows two ways to detect palindromes. First one, an imperative way -by force-, the other one is completely declarative.

1st One: palindrome func
  This func gets a string (s) as a parameter. A palindrome should have at least 3 caracters to be legible, 
  but somebody could just enter a string like: s = 'aa', and it also would be considered as a palindrome -even though it is meaningless.
  
  Long story short, palindrome func compares every character of the string to its contrary [1st/last; 2nd/last -1; and so forth]
  If the comparisons succeeded, s will be considered a palindrome and a True value will be returned.
  
2nd one: palindrome2 func
  This func also gets a string s and deals with it in a -way- more intelligent way.
  
  By comparing a string to its inverse the programme knows wether it is a palindrome or not. If the statement is True, then s is 
  a palindrome.
  
Example:
By running the current code you get
    
    True
    True
    
As the string s introduced was s = 'otto', which is a palindrome. Both methods work.
