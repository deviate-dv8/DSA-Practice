// 1) Define a function/method named F that accepts a positive integer argument N.
// The function should print numbers 1 to N, each in a new line but with the following rules:
// If the number is divisible by 3, print "EDI" instead of the number.
// If the number is divisible by 5, print "WOW" instead of the number.
// If the number is divisible by both 3 and 5, print "EDIWOW" instead of the number.
// Example:
// Sample call:
// F(17)
// Output:
// 1
// 2
// EDI
// 4
// WOW
// EDI
// 7
// 8
// EDI
// WOW
// 11
// EDI
// 13
// 14
// EDIWOW
// 16
// 17
function F(num) {
  for (let i = 1; i <= num; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log("EDIWOW");
    } else if (i % 3 == 0) {
      console.log("EDI");
    } else if (i % 5 == 0) {
      console.log("WOW");
    } else {
      console.log(i);
    }
  }
}

sample_num = 17;
F(sample_num);
