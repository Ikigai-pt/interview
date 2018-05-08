package com.interview.questions.array;

import java.util.Scanner;
/**
 * Created by pthirunavukkarasu on 9/25/17.
 *
 */
public class LeftRotation {

    static int[] leftRotation(int[] a, int d) {
        // Complete this function
        int [] temp = a;
        for(int outer = 0; outer< d; outer++){
            int local = temp[0];
            // 5 1 2 3 4
            for(int i=0 ; i< temp.length-1; i++){

                temp[i]= temp[i+1];

            }

            temp[temp.length -1] = local;
        }
        return temp;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int d = in.nextInt();
        int[] a = new int[n];
        for(int a_i = 0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int[] result = leftRotation(a, d);
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i != result.length - 1 ? " " : ""));
        }
        System.out.println("");


        in.close();
    }
}
