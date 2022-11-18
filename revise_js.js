// let,var and const is for declare variable 
// let we are re assign but not re declare
// var we are re assign also and re declare also
// const we are not re assign and re declare
// for adding element in array we use push function
// for removing we use pop method
// shif will remove first element of array
// unshift will add the element in starting array
// there is five loop 1.for loop 2.while loop 3.do while loop 4.for in loop 5.for off loop.

// print 1 to 10 even number
for (let i=0;i<11;i++){
    if (i%2==0){
        console.log(i)
    }
}

// print 1 to 10 table
for (let i=1;i<11;i++){
    console.log(2+"*"+i+"="+2*i)
}

// create a length converter function 
var readlineSync = require('readline-sync');
length=readlineSync.questionInt("enter the length of kilometer")
console.log(length*1000+" meter")

// 