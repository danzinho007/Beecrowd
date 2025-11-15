cod1, num1, val1 = io.read("*n", "*n", "*n")
cod2, num2, val2 = io.read("*n", "*n", "*n")
total = num1 * val1 + num2 * val2
print(string.format("VALOR A PAGAR: R$ %.2f", total))