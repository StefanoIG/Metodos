from scipy.optimize import linprog
from prettytable import PrettyTable
# Coeficientes de la función objetivo (negativos para maximizar)
c = [-375, -275, -475, -325]
# Coeficientes de las restricciones de horas de fabricación y acabado
A = [
    [2.5, 1.75, 2.75, 2],
    [3.5, 3, 3, 2]
]
b = [640, 960]
# Límites de las variables (cantidades no negativas)
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
# Resolver el problema de optimización lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds, x3_bounds], method='highs')
# Crear una tabla para mostrar los resultados
table = PrettyTable()
table.field_names = ["Parte", "Cantidad Óptima (unidades)"]
if result.success:
    table.add_row(["Parte a", f"{result.x[0]:.2f}"])
    table.add_row(["Parte b", f"{result.x[1]:.2f}"])
    table.add_row(["Parte c", f"{result.x[2]:.2f}"])
    table.add_row(["Parte d", f"{result.x[3]:.2f}"])
    table.add_row(["Utilidad máxima", f"${-result.fun:.2f}"])
else:
    table.add_row(["Resultado", "No se encontró una solución óptima."])
# Imprimir la tabla formateada
print(table)
