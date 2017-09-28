package com.interview.questions.linkedlist.impl;

import com.interview.questions.linkedlist.LinkedListService;
import com.interview.questions.linkedlist.Node;

/**
 * Created by pthirunavukkarasu on 9/27/17.
 *
 */
public class LinkedListServiceImpl implements LinkedListService {

    @Override public Node insertAtHead(Node head, int data) {
        Node temp = new Node(data);
        temp.next = head;
        return temp;
    }

    @Override public Node insertAtTail(Node head, int data) {
        if(head == null )
            head = new Node(data);
        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = new Node(data);
        return head;
    }

    @Override public Node insertAtNth(Node head, int data, int position) {
        Node node = head;
        if (position == 1){
            node = new Node(data);
            node.next = head;
            return node;
        }
        else {
            while(--position > 1){
                node = node.next;
            }
            Node i = node.next;
            node.next = new Node(data);
            node.next.next = i;
            return head;
        }
    }

    @Override public void printLL(Node node) {
        while(node != null){
            System.out.println(node.data);
            node = node.next;
        }
    }
}
