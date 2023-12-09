import pulp
from prettytable import PrettyTable
# Crea el problema de maximización
prob = pulp.LpProblem("Maximizar Utilidades", pulp.LpMaximize)
# Variables de decisión
x1 = pulp.LpVariable('x1', lowBound=0)  # Cantidad de Producto 1
x2 = pulp.LpVariable('x2', lowBound=0)  # Cantidad de Producto 2
x3 = pulp.LpVariable('x3', lowBound=0)  # Cantidad de Producto 3
# Función objetivo
prob += 30 * x1 + 30 * x2 + 35 * x3, "Utilidad Total"
# Restricciones
prob += 6 * x1 + 4 * x2 + 13 * x3 <= 3000, "Materia Prima"
prob += 0.05 * x1 + 0.1 * x2 + 0.2 * x3 <= 55, "Tiempo de Producción"
# Resuelve el problema
prob.solve()
# Crear una tabla para mostrar los resultados
tabla_resultados = PrettyTable()
tabla_resultados.field_names = ["Variable", "Valor óptimo"]
tabla_resultados.add_row(["Estado", pulp.LpStatus[prob.status]])
tabla_resultados.add_row(["Cantidad de Producto 1 (kg)", pulp.value(x1)])
tabla_resultados.add_row(["Cantidad de Producto 2 (kg)", pulp.value(x2)])
tabla_resultados.add_row(["Cantidad de Producto 3 (kg)", pulp.value(x3)])
tabla_resultados.add_row(["Utilidad Total ($)", pulp.value(prob.objective)])
# Imprimir la tabla de resultados
print(tabla_resultados)
