package inge2.dataflow;

import java.lang.reflect.Array;

public class StackAr {

    /**
     * Capacidad por defecto de la pila.
     */
    //@ spec_public
    private final static int DEFAULT_CAPACITY = 10;

    /**
     * Arreglo que contiene los elementos de la pila.
     */
    //@ spec_public
    private final int[] elems;

    /**
     * Indice del tope de la pila.
     */
    //@ spec_public
    private int top = -1;

    //@ ensures this.elems.length == DEFAULT_CAPACITY;
    public StackAr() {
        this(DEFAULT_CAPACITY);
    }

    //@ requires capacity > 0;
    //@ ensures this.elems.length == capacity;
    //@ ensures top == -1;
    public StackAr(int capacity) {
        this.elems = new int[capacity];
    }

    //@ ensures \result == (this.top == -1);
    public boolean isEmpty() {
        return this.top == -1;
    }

    //@ requires this.top >= -1 && this.top < this.elems.length;
    //@ ensures \result == (this.top+1 == this.elems.length);
    public boolean isFull() {
        return this.top+1 == this.elems.length;
    }

    //@ requires this.top >= -1 && this.top < this.elems.length;
    //@ ensures \result == this.top + 1;
    public int size() {
        return this.top+1;
    }

    //@ requires this.top >= 0 && this.top < this.elems.length-1;
    //@ ensures this.top == \old(this.top) + 1;
    //@ ensures \forall int i; 0 <= i < this.top; this.elems[i] == \old(this.elems[i]);
    //@ ensures this.elems[this.top] == e;
    public void push(int e) {
        this.top++;
        this.elems[this.top] = e;
    }

    //@ requires this.top >= 0 && this.top < this.elems.length;
    //@ ensures this.top == \old(this.top) - 1;
    //@ ensures \forall int i; 0 <= i <= this.top; this.elems[i] == \old(this.elems[i]);
    //@ ensures \result == this.elems[\old(this.top)];
    public int pop() {
        int res = this.elems[this.top];
        this.top--;
        return res;
    }

    //@ requires this.top >= 0 && this.top < this.elems.length;
    //@ ensures \forall int i; 0 <= i <= this.top; this.elems[i] == \old(this.elems[i]);
    //@ ensures \result == this.elems[this.top];
    public int peek() {
        return this.elems[this.top];
    }
}

