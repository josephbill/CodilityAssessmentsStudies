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
    //the variables here represent the node pointers
    let prev = null;
    let current = node;
    let next = null;

    while (current != null){
        //this process happens to each node 
        //swapping the variables for reversing the linked list 
        //1234 
        // 1 is the head //4 is the tail 
        // output should be 4 is the head and 1 is the tail
        //swapping the pointers 
        next = current.next;  // to save the intial pointer of start node //next here in iteration: is 2
        current.next = prev; // this line makes current.next which is at node 1 , change its pointer to prev. i.e reversed direction //because prev. at this equal to null 
        //updating the pointers 
        prev = current; // previous pointer now stores the active node i.e. 1 in first iteration // updating its location in node it was null now its the active node 
        current = next; // current is assigned the next pointer which is the next node in list : so that iteration goes on 
    }
    node = prev; //so node equals to the previous node / pointer ->which is current 
    return node; //output

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


//more here 
//https://www.youtube.com/watch?v=S9kMVEUg-x4