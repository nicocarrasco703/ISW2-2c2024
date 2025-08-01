package inge2.dataflow;

public class Absoluto {

    // Calcula el valor absoluto de un número entero.
    // Si el número es negativo, devuelve el opuesto.
    //
    //@ requires n > Integer.MIN_VALUE;
    //@ ensures \result >= 0;
    //@ ensures \result == n || \result  == -n;
    public static int valorAbsoluto(int n) {
        if (n < 0) {
            return -n;
        } else {
            return n;
        }
    }
}