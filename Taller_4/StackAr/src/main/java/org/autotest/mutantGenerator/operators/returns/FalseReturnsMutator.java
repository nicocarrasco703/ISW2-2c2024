package org.autotest.mutantGenerator.operators.returns;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtExpression;
import spoon.reflect.code.CtReturn;
import spoon.reflect.declaration.CtElement;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#FALSE_RETURNS
 *
 * Este operador reemplaza los valores de retorno de las funciones que devuelven booleano por false.
 */
public class FalseReturnsMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtReturn)) {
            return false;
        }

        CtReturn op = (CtReturn)candidate;
        String type = getReturnedExpressionType(op);
        List<String> targetTypes = Arrays.asList(
                "bool"
        );
        return targetTypes.contains(type);
    }

    @Override
    public void process(CtElement candidate) {
        CtReturn op = (CtReturn)candidate;
        op.setReturnedExpression(getEmptyValueForReturnExpression(op));
    }

    private static String getReturnedExpressionType(CtReturn op) {
        return op.getReturnedExpression().getType().toString();
    }

    private CtExpression getEmptyValueForReturnExpression(CtReturn op) {
        String returnType = getReturnedExpressionType(op);
        if (returnType.equals("bool")){
                return op.getFactory().Code().createLiteral(false);
        }
        return null;
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtReturn op = (CtReturn)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getReturnedExpression().toString() + " por " + getEmptyValueForReturnExpression(op).toString() +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
