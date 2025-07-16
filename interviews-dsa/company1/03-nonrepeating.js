// 3) Define a function/method named NONREPEATING that accepts a string argument s, and prints the first non-repeated character in the string argument. You may use any data structure you find appropriate.
// If all characters appear more than once in the string, print "IS A GIANT NUT"
// Example:
// Sample call:
// NONREPEATING("PARTICIPATE")
// Output:
// R
// Sample:
// NONREPEATING("COCONUT")
// Output:
// N
// Input:
// NONREPEATING("COCONUTNUT")
// Output:
// IS A GIANT NUT
function NONREPEATING(s) {
  let charFreq = {};
  for (let char of s) {
    charFreq[char] = 0;
  }
  for (let char of s) {
    charFreq[char] += 1;
  }
  charFreqArr = Object.values(charFreq);
  isAllRepeating = true;

  for (const freq of charFreqArr) {
    if (freq < 2) {
      isAllRepeating = false;
    }
  }
  const entries = Object.entries(charFreq);
  const filteredChar = entries.filter((arr) => arr[1] == 1);
  if (isAllRepeating) {
    console.log("IS A GIANT NUT");
  } else {
    console.log(filteredChar[0][0]);
  }

  // const mapResult = Object.values(charFreq).map()
}

NONREPEATING("COCONUTNUT");
