package org.autotest.mutantGenerator.operators.constants;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtLiteral;
import spoon.reflect.declaration.CtElement;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#EXPERIMENTAL_CRCR
 *
 * Este operador reemplaza los valores de las constantes por -1.
 */
public class MinusOneConstantMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtLiteral)) {
            return false;
        }

        CtLiteral op = (CtLiteral)candidate;
        String type = getLiteralType(op);
        List<String> targetTypes = Arrays.asList(
            "int"
        );

        if (!targetTypes.contains(type)) {
            return false;
        }

        String parentNodeCode = op.getParent().toString();
        // No usamos op.getValue().toString() para obtener el valor del literal sino que miramos el parent porque
        // Spoon separa los literales negativos en dos nodos: el operador de negación y el literal.
        if (parentNodeCode.contains("-1")) {
            // Para evitar generar mutantes inválidos, ignoramos los literales que ya son -1, ya que produciría "--1"
            return false;
        }

        return true;
    }

    @Override
    public void process(CtElement candidate) {
        CtLiteral op = (CtLiteral)candidate;
        op.setValue(op.getFactory().Code().createLiteral(-1));
    }

    private static String getLiteralType(CtLiteral op) {
        return op.getType().toString();
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtLiteral op = (CtLiteral)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getValue().toString() + " por -1" +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
