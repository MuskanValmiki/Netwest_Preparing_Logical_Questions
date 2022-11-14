//quere=It is first to first and last to last
class queue{
    constructor(){
        this.arr=[]
    }
    adding(element){
        this.arr.push(element)
    }
    removing(){
        this.arr.shift()
    }
    top(){
        return this.arr[0]
    }
    isEmpty(){
        this.arr.length==0
    }

}
let Queue=new queue
Queue.adding(45)
Queue.adding(98)
Queue.removing()
console.log(Queue)