package com.interview.questions.linkedlist;

import com.interview.questions.linkedlist.impl.LinkedListServiceImpl;

/**
 *
 * Created by pthirunavukkarasu on 9/27/17.
 */
public class LinkedListQns {

    private static LinkedListService linkedListService = new LinkedListServiceImpl();

    private static Node createMockLL(int size){
        Node head = new Node(1);
        Node root = head;
        for(int i =1; i<size; i++){
            Node newNode = new Node(i+1);
            head.next = newNode;
            head = newNode;
        }
        return root;
    }



    public static void main (String args[]){
        Node root = createMockLL(5);
        linkedListService.printLL(root);
        linkedListService.insertAtHead(root,9);
        linkedListService.insertAtTail(root, 0);

        System.out.println(" Insert Head and Tail-----");
        linkedListService.printLL(root);

        System.out.println(" Insert at 3 -----");
        linkedListService.printLL(
                linkedListService.insertAtNth(root,33,3));

        System.out.println(" Insert at 1 -----");
        linkedListService.printLL(
                linkedListService.insertAtNth(root,11,1));

        System.out.println(" Insert at 8-----");
        linkedListService.printLL(
                linkedListService.insertAtNth(root,88,8));

        System.out.println(" Delete at Beginning ------");
        linkedListService.printLL(
              linkedListService.deleteAtNth(root, 1));

        System.out.println(" Delete at 3 ------");
        linkedListService.printLL(
              linkedListService.deleteAtNth(root, 3));

        System.out.println(" Delete at End ------");
        linkedListService.printLL(
              linkedListService.deleteAtNth(root, 7));
    }
}
