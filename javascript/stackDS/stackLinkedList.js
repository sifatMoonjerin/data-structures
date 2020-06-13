class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack{
    constructor(){
        this.head = null;
        //this.count = 0;
    }

    _push = value => {
        //this.count++;
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
    }

    _pop = () => {
        if(!this.head){
            return undefined;
        }
        //this.count--;
        const temp = this.head.value;
        this.head = this.head.next;
        return temp;
    }

    _peek = () => {
        if(!this.head){
            return undefined;
        }
        return this.head.value;
    }
    
    _print = () => {
        let currentNode = this.head;
        while(currentNode){
            console.log(currentNode.value);
            currentNode = currentNode.next;
        }
    }
}

const stack = new Stack();
stack._push('one');
stack._push('two');
stack._push('three');
stack._print();
console.log('----------');
console.log(stack._pop());
console.log('----------');
stack._print();