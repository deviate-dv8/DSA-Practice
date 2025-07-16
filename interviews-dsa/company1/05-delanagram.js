// 5) Two strings are said to be anagrams of each other if they both contain the same characters with the same counts/frequencies.
// e.g.
// UPSET and SETUP are anagrams
// FRUITS and BASKET are not anagrams
// UPSET and PUSEEEEEET are not anagrams

// From the last example, if we delete 5 E's from PUSEEEEEET, we will get PUSET, which is an anagram of UPSET.

// Define a function/method named DELANAGRAM that accepts two string arguments and prints the minimum total number of characters that can be deleted so that the two strings are anagrams of each other.

// Sample:
// DELANAGRAM("BREAD", "GRIDDLE")
// Output:
// 6
// Explanation:
// Delete B and A in BREAD
// Delete G, I, D and L in GRIDDLE
// You'll get RED and RDE which are anagrams of each other
// Total deleted: 2 + 4 = 6

// Sample:
// DELANAGRAM("SETUP", "UPSET")
// Output:
// 0
// Explanation:
// No need to delete, since they are already anagrams

// Sample:
// DELANAGRAM("XYZ", "ABC")
// Output:
// 6
// Explanation:
// "" and "" are anagrams of each other

function DELANAGRAM(str1, str2) {
  let charFreq1 = {};
  for (let char of str1) {
    charFreq1[char] = 0;
  }
  for (let char of str1) {
    charFreq1[char] += 1;
  }
  let charFreq2 = {};
  for (let char of str2) {
    charFreq1[char] = 0;
  }
  for (let char of str2) {
    charFreq1[char] += 1;
  }
  const str1sorted = Object.entries(str1)
    .map((arr) => arr[1])
    .sort();
  const str2sorted = Object.entries(str2)
    .map((arr) => arr[1])
    .sort();
  // checks if the char from str1 from char2, removes it from str1 and str2 respectively
  for (let i = 0; i < str1sorted.len; i++) {
    if (str2sorted.includes(str1sorted[i])) {
      str1sorted.shift(1, i);
    }
  }
  // checks if the char from str2 from char1, removes it from str2 and str1 respectively

  // count the remaining length of the both arrays, and that will be the result of the DEANAGRAM it takes to be ANAGRAM
}
DELANAGRAM("UPSETA", "SETUP");
