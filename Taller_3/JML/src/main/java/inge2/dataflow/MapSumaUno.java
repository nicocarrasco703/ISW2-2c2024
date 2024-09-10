package inge2.dataflow;

public class MapSumaUno {

    // Suma uno a todos los elementos de un array.
    //@ requires \forall int i; 0 <= i < arr.length; arr[i] < Integer.MAX_VALUE;

    //@ ensures \forall int i; 0 <= i < arr.length; arr[i] == \old(arr[i]) + 1 ;
    public static void mapSumaUno(int[] arr) {
        //@ maintaining 0 <= i <= arr.length;
        //@ maintaining \forall int k; 0 <= k < i; arr[k] == \old(arr[k]) + 1 ;
        //@ maintaining \forall int k; i <= k < arr.length; arr[k] == \old(arr[k]);
        //@ loop_writes i, arr[*];
        //@ decreases arr.length -i;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] + 1;
        }
    }
}