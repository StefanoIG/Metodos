import pulp
from prettytable import PrettyTable
# Crear el problema de maximización
prob = pulp.LpProblem("Maximize Function", pulp.LpMaximize)
# Definir las variables
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')
# Función objetivo
prob += 6 * x + 8 * y, "Z"
# Restricciones
prob += 5 * x + 2 * y <= 40, "Restricción 1"
prob += 6 * x + 6 * y <= 60, "Restricción 2"
prob += 2 * x + 4 * y <= 32, "Restricción 3"
prob += x >= 0, "Restricción x >= 0"
prob += y >= 0, "Restricción y >= 0"
# Resolver el problema
prob.solve()
# Crear una tabla para mostrar los resultados
tabla_resultados = PrettyTable()
tabla_resultados.field_names = ["Variable", "Valor óptimo"]
tabla_resultados.add_row(["Valor óptimo de x", pulp.value(x)])
tabla_resultados.add_row(["Valor óptimo de y", pulp.value(y)])
tabla_resultados.add_row(["Valor óptimo de la función objetivo (Z)", pulp.value(prob.objective)])
# Imprimir la tabla de resultados
print(tabla_resultados)
