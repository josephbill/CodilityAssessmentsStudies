// Given a pointer to the head node of a linked list,
//  the task is to reverse the linked list.
//   We need to reverse the list by changing the links between nodes.

//pseudocode 
// 3 pointers on linked list 
// intialize previous node , current node (head) , next (NULL)
// iterate /loop through the linked list // inside loop 
// 

let head;
class Node {
    constructor(val){
        this.data = val;
        this.next = null;
    }
}

//function to reverse the list 
function reverse_list(node) {
    let prev = null;
    let current = node;
    let next = null;

    while (current != null){
        //swapping the variables for reversing the linked list 
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    node = prev;
    return node;

}


function printList(node) {
    while (node != null){
       // document.write(n.data + " ");
       console.log(node.data + "") 
       node = node.next;
    }
}


//test code 

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
//before reversal
printList(head);
head = reverse_list(head);
//after reversal 
printList(head);