numero = tonumber(io.read())
horas = tonumber(io.read())
valorHora = tonumber(io.read())
salario = horas * valorHora
print("NUMBER = " .. numero)
print(string.format("SALARY = U$ %.2f", salario))