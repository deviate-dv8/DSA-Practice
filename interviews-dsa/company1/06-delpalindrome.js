// 6) A string is said to be a palindrome if it reads the same forwards and backwards. e.g. KAYAK, RACECAR
// BAYABAS is not a palindrome, but if we delete the last 2 letters, we will get BAYAB, which is a palindrome.
// Define a function DELPALINDROME that accepts a string argument S and prints out the minimum number of characters that can be deleted to make the string a palindrome.

// Sample:
// DELPALINDROME("BARYABAS")
// Output:
// 3
// Explanation:
// Delete R, and the last 2 letters AS to get BAYAB
// (or Delete Y and the last 2 letters AS to get BARAB)

// Sample:
// DELPALINDROME("RACECAR")
// Output:
// 0
// Explanation:
// Already a palindrome

// Sample:
// DELPALINDROME("COLA")
// Output:
// 3
// Explanation:
// Delete any 3 letters to get a 1-character string, which by definition, is a palindrome.
