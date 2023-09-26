let head; //head of the lists 

    /* Linked list Node.  This inner class is made  so that
       main() can access it */

class Node 
{
    constructor(d)
    {
        this.data = d;
        this.next = null;
    }
}

// now method to create a simple linked list with 3 nodes 
let firstnode  = new Node(1);
let secondnode = new Node(2);
let thirdnode = new Node(3);

   /* Three nodes have been allocated dynamically.
          We have references to these three blocks as head,  
          second and third
  
          llist.head        second              third
             |                |                  |
             |                |                  |
         +----+------+     +----+------+     +----+------+
         | 1  | null |     | 2  | null |     |  3 | null |
         +----+------+     +----+------+     +----+------+ */

// linking first node with the second node 
firstnode.next = secondnode;

        /*  Now next of the first Node refers to the second.  So they
            both are linked.
  
         llist.head        second              third
            |                |                  |
            |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  | null |     |  3 | null |
        +----+------+     +----+------+     +----+------+ */

//so linking second node with third node will simply entail 
secondnode.next = thirdnode;

  /*  Now next of the second Node refers to third.  So all three
            nodes are linked.
  
         llist.head        second              third
            |                |                  |
            |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  |  o-------->|  3 | null |
        +----+------+     +----+------+     +----+------+ */
        