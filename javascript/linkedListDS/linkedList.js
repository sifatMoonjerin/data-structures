class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
    }

    _insert = (value, currentNode = this.head) => {
        if(this.head === null){
            this.head = new Node(value);
        } else if(currentNode === null){
            return new Node(value);
        } else{
            currentNode.next = this._insert(value, currentNode.next)
            return currentNode
        }
    }

    _print = (currentNode = this.head) => {
        if(currentNode === null){
            return;
        } 
        console.log(currentNode.value);
        this._print(currentNode.next);
    }
}

const linkedList = new LinkedList();

linkedList._insert(10);
linkedList._insert(9);
linkedList._insert(8);
linkedList._insert(7);
linkedList._insert(6);
linkedList._insert(5);
linkedList._insert(4);
linkedList._insert(3);
linkedList._insert(2);
linkedList._insert(1);
linkedList._print()