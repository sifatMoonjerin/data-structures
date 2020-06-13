class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.head = null;
        this.tail = null;
    }

    _enqueue = value => {
        const newNode = new Node(value);
        if(!this.tail){
            this.head = newNode;
        } else{
            this.tail.next = newNode;
        }
        this.tail = newNode;
    }

    _dequeue = () => {
        if(!this.head){
            return undefined;
        } else if(!this.head.next){
            const temp = this.head.value;
            this.head = null;
            this.tail = null;
            return temp;
        } else{
            const temp = this.head.value;
            this.head = this.head.next;
            return temp;
        }
    }

    _print = () => {
        let currentNode = this.head;
        while(currentNode){
            console.log(currentNode.value);
            currentNode = currentNode.next;
        }
    }
}

const queue = new Queue();
queue._enqueue('one');
queue._enqueue('two');
queue._enqueue('three');
queue._print();
console.log('----------');
console.log(queue._dequeue());
console.log('----------');
queue._print();
