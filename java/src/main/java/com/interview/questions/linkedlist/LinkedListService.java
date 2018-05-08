package com.interview.questions.linkedlist;

/**
 * Created by pthirunavukkarasu on 9/27/17.
 *
 */
public interface LinkedListService {
    Node insertAtHead(Node head, int data);
    Node insertAtTail(Node head, int data);
    Node insertAtNth(Node head, int data, int position);
    void printLL(Node head);
    Node deleteAtNth(Node head, int position);
}
