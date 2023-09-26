// here we will print the contents of a linked lists 
let head; //head of lists 

 /* Linked list Node.  This inner class is made  so that
       main() can access it */
       class Node {
        constructor(val) {
            this.data = val;
            this.next = null;
        }
    }

/* This function prints contents of linked list starting from head */

function printList() {
    let n  = head_node;
    while (n != null){
       // document.write(n.data + " ");
       console.log(n.data + "") 
       n = n.next;
    }
}

    /* method to create a simple linked list with 3 nodes*/
      
      
        /* Start with the empty list. */
        
  
        var head_node = new Node(1);
        var second_node = new Node(2);
        var third_node = new Node(3);
  
        head_node.next = second_node; // Link first node with the second node
        second_node.next = third_node; // Link second node with the third node
printList();

// sample question
//User function Template for javascript
// printing items in a linked list on a single line. 
/*LINKED LIST NODE

class Node {
  constructor(x){
    this.data = x;
    this.next = null;
  }
}
*/


// /**
//  * @param {Node} head
// */

// class Solution {
//     display(head){
//       //code here
//          let n  = head;
//          let x = [];
//       while (n != null){
//           // document.write(n.data + " ");
//           //console.log(n.data)
//           x.push(n.data)
//           n = n.next;
//       }
//       console.log(...x);
//     }
//   }
  
