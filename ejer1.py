import pulp
from prettytable import PrettyTable
# Crear el problema de maximización
prob = pulp.LpProblem("Maximize Utility", pulp.LpMaximize)
# Definir las variables
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')
# Función objetivo
prob += 45 * x + 20 * y, "Z"
# Restricciones
prob += 20 * x + 5 * y <= 9500, "Materia prima"
prob += 0.04 * x + 0.12 * y <= 40, "Tiempo de producción"
prob += x + y <= 550, "Almacenamiento"
# Resolver el problema
prob.solve()
# Crear una tabla para mostrar los resultados
tabla_resultados = PrettyTable()
tabla_resultados.field_names = ["Variable", "Valor óptimo"]
tabla_resultados.add_row(["Cantidad de A a producir", pulp.value(x)])
tabla_resultados.add_row(["Cantidad de B a producir", pulp.value(y)])
tabla_resultados.add_row(["Utilidad máxima", pulp.value(prob.objective)])
# Imprimir la tabla de resultados
print(tabla_resultados)
