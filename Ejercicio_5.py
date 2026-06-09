import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras)
x1 = pulp.LpVariable("Backend", lowBound=0, upBound=6, cat='Integer')
x2 = pulp.LpVariable("Data_Worker", lowBound=0, upBound=7, cat='Integer')

# 3. Función Objetivo
model += 300 * x1 + 250 * x2, "Rendimiento_Total"

# 4. Restricciones
model += 2 * x1 + 1 * x2 <= 16, "Memoria_RAM"
model += 1 * x1 + 2 * x2 <= 17, "Almacenamiento_SSD"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contenedores Backend: {x1.varValue}")
print(f"Contenedores Data Worker: {x2.varValue}")
print(f"Rendimiento Maximo por Hora: ${pulp.value(model.objective)}")

#source .venv/bin/activate