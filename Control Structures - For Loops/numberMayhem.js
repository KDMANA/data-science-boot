/*
Use the let function to create a loop (20 to 0)
Create a for lop with an index  that starts at 19 and ends at -1. 
The loop should decrement by one each time through the loop.
Create a for loop with 
*/

// Countdown loop to display from 20 to 0
let count = 20;  // Start with the number 20
while (count >= 0) {  // Keep going until we reach 0
    console.log(count);  // Print the current number
    count--;  // Move to the next lower number
}

console.log('\n'); // New line for readability

// Output and display even numbers (1 to 20)
for (let i = 2; i <= 20; i += 2) {  // Start from 2, increase by 2, stop at 20
    console.log(i);  // Print each even number
}

console.log('\n'); // New line for readability

// Output the desired star pattern
for (let i = 1; i <= 5; i++) {  // Repeat 5 times
    let stars = "*".repeat(i);  // Create a string of asterisks based on the loop count
    console.log(stars);  // Print the current line of asterisks
}
