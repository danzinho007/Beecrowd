nome = io.read()
salarioFixo = tonumber(io.read())
vendas = tonumber(io.read())
total = salarioFixo + vendas * 0.15
print(string.format("TOTAL = R$ %.2f", total))