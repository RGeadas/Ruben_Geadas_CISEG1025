# Scenario
# We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition ‒ learn from your mistakes and draw your own conclusions.

# Try to:

# minimize the number of print() function invocations by inserting the \n sequence into the strings;
# make the arrow twice as large (but keep the proportions)
# duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
# remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists? 
# do the same with some of the parentheses;
# change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
# replace some of the quotes with apostrophes; watch what happens carefully.

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# minimize the number of print() function invocations by inserting the \n sequence into the strings;

print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")

# make the arrow twice as large (but keep the proportions)

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

# duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)

print("        *        " * 2)
print("       * *       " * 2)
print("      *   *      " * 2)
print("     *     *     " * 2)
print("    *       *    " * 2)
print("   *         *   " * 2)
print("  *           *  " * 2)
print(" *             * " * 2)
print("******     ******" * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *     *     " * 2)
print("     *******     " * 2)

# remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists? 
#R: Erro de syntax, o Python aponta o erro algures apos o local onde ele foi cometido, aponta erro pois o Python não sabe onde a string começa/termina

# do the same with some of the parentheses;
#R: De novo erro de syntax, pois tal como as aspas é necessario os parenteses para que a função funcione

# change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
#R: Python é case-sensitive logo gera um erro de NameError pois não reconhece o nome a não ser que seja criado anteriormente (apenas reconhece print())

# replace some of the quotes with apostrophes; watch what happens carefully.
#R: Não acontece nada mas apenas se os apostrofos forem utilizados em pares com outros apostrofos, não utilizar (aspa) " e depois (apostrofo) '