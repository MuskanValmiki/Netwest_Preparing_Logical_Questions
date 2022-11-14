//stack =It is first is last and last is first like if 
// we have plates so we want to take last plate so we 
// have to remove first then we can take last plate.

class Stack{
    constructor(){
        this.arr=[]
    }
    adding(element){
        this.arr.push(element)
    }
    removing(){
        this.arr.pop()
    }
    top(){
        this.isEmpty ? console.log("Stack is empty"):this.arr[arr.length-1]
    }
    isEmpty(){
        this.arr.length==0
    }
}
let stack=new Stack 
stack.adding(45)
stack.adding(98)
stack.removing()
console.log(stack)



