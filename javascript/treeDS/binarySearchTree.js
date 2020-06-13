class Node{
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BST{
    constructor(){
        this.root = null;
    }

    _insert = (value, currentNode = this.root) => {
        if(this.root === null){
            this.root = new Node(value);
        } else if(currentNode === null){
            currentNode = new Node(value);
        } else if(value > currentNode.value){
            currentNode.right = this._insert(value, currentNode.right);
        } else if(value < currentNode.value){
            currentNode.left = this._insert(value, currentNode.left);
        }
        return currentNode;
    }

    _search = (value, currentNode = this.root) => {
        if(currentNode === null){
            return false;
        } else if(currentNode.value === value){
            return true;
        } else if(value > currentNode.value){
            return this._search(value, currentNode.right);
        } else{
            return this._search(value, currentNode.left);
        }
    }
}

const bst = new BST();
bst._insert(15);
bst._insert(20);
bst._insert(10);
bst._insert(12);
bst._insert(4);
bst._insert(25);
bst._insert(3);
bst._insert(18);


console.log(bst._search(18));