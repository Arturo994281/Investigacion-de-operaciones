import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Escritorio", lowBound=0, upBound=2000, cat='Integer')
x2 = pulp.LpVariable("Laptop", lowBound=0, upBound=4000, cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Ganancia_Total"

# 4. Restricciones
model += x1 +  x2 <= 60, "Procesadores"
model += 1 * x1 + 3 * x2 <= 100, "Horas"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Escritorio: {x1.varValue}")
print(f"Laptop: {x2.varValue}")
print(f"Ganancia total: ${pulp.value(model.objective)}")

#source .venv/bin/activate