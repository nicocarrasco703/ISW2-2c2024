package inge2.dataflow.zeroanalysis;

import javax.print.DocFlavor;

/**
 * This enum represents the possible values of the zero analysis for a variable.
 */
public enum ZeroAbstractValue {

    /**
     * We don't have information about the variable.
     */
    BOTTOM("bottom"),

    /**
     * The variable is not zero.
     */
    NOT_ZERO("not-zero"),

    /**
     * The variable is zero.
     */
    ZERO("zero"),

    /**
     * The variable may be (or not) zero.
     */
    MAYBE_ZERO("maybe-zero");

    /**
     * The name of the ZeroAbstractValue.
     */
    private final String name;

    @Override
    public String toString() {
        return this.name;
    }

    ZeroAbstractValue(String name) {
        this.name = name;
    }

    /**
     * Returns the result of the division between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the division.
     */

    /*
     *  El metodo divideBy realiza la operacion division entre dos valores abstractos, segun el reticulado definido
     * revisando los casos posibles y devolviendo el posible valor luego de aplicar la operacion
     * */
    public ZeroAbstractValue divideBy(ZeroAbstractValue another) {
        if(another == BOTTOM || another == ZERO){
            return BOTTOM;
        }
        if(another == MAYBE_ZERO){
            if(this==BOTTOM){
                return BOTTOM;
            }
            return MAYBE_ZERO;
        }
        if(another == NOT_ZERO){
            if(this==ZERO){
                return ZERO;
            }
            if(this==BOTTOM){
                return BOTTOM;
            }
            return MAYBE_ZERO;
        }

        throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the addition between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the addition.
     */

    /*
     *  El metodo add realiza la operacion suma entre dos valores abstractos, segun el reticulado definido
     * revisando los casos posibles y devolviendo el posible valor luego de aplicar la operacion
     * */
    public ZeroAbstractValue add(ZeroAbstractValue another) {
        if(this == BOTTOM){
            return BOTTOM;
        }
        if(this == ZERO){
            return another;
        }
        if(this == MAYBE_ZERO){
            if(another==BOTTOM){
                return BOTTOM;
            }
            return MAYBE_ZERO;
        }
        if(this == NOT_ZERO){
            if(another==BOTTOM){
                return BOTTOM;
            }
            if(another==NOT_ZERO || another==MAYBE_ZERO){
                return MAYBE_ZERO;
            }
            if(another==ZERO){
                return NOT_ZERO;
            }
        }

        throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the multiplication between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the multiplication.
     */

    /*
     *  El metodo multiplyBy realiza la operacion producto entre dos valores abstractos, segun el reticulado definido
     * revisando los casos posibles y devolviendo el posible valor luego de aplicar la operacion
     * */
    public ZeroAbstractValue multiplyBy(ZeroAbstractValue another) {
        if(this == BOTTOM){
            return BOTTOM;
        }
        if(this == ZERO){
            if(another==BOTTOM){
                return BOTTOM;
            }
            return ZERO;
        }
        if(this == MAYBE_ZERO){
            if(another==NOT_ZERO){
                return MAYBE_ZERO;
            }
            return another;
        }
        if(this == NOT_ZERO){
            return another;
        }

        throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the subtraction between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the subtraction.
     */
    /*
     *  El metodo subtract realiza la operacion resta entre dos valores abstractos, segun el reticulado definido
     * revisando los casos posibles y devolviendo el posible valor luego de aplicar la operacion
     * */
    public ZeroAbstractValue subtract(ZeroAbstractValue another) {
        if(this == BOTTOM){
            return BOTTOM;
        }
        if(this == ZERO){
            return another;
        }
        if(this == MAYBE_ZERO){
            if(another==BOTTOM){
                return BOTTOM;
            }
            return MAYBE_ZERO;
        }
        if(this == NOT_ZERO){
            if(another==BOTTOM){
                return BOTTOM;
            }
            if(another==ZERO){
                return NOT_ZERO;
            }
            return MAYBE_ZERO;
        }

        throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the merge between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the merge.
     */
    /*
     * El metodo merge realiza la Union entre dos valores, según el reticulado definido y
     * el tipo de analisis MAY
     * */
    public ZeroAbstractValue merge(ZeroAbstractValue another) {
        if(this == BOTTOM){
            return another;
        }
        if(this == ZERO){
            if(another==BOTTOM || another==ZERO){
                return ZERO;
            }
            return MAYBE_ZERO;
        }
        if(this == MAYBE_ZERO){
            return MAYBE_ZERO;
        }
        if(this == NOT_ZERO){
            if(another==BOTTOM || another==NOT_ZERO){
                return NOT_ZERO;
            }
            return MAYBE_ZERO;
        }

        throw new UnsupportedOperationException();
    }

}
