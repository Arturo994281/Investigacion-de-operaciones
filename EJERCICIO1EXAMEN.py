import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Basico", lowBound=0, upBound=30, cat='Integer')
x2 = pulp.LpVariable("Avanzado", lowBound=0, upBound=50, cat='Integer')

# 3. Función Objetivo
model += 30 * x1 + 50 * x2, "Ganancia_Total"

# 4. Restricciones
model += x1 + 2 * x2 <= 16, "RAM"
model += 3 * x1 + 2 * x2 <= 24, "VCPU"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Basico: {x1.varValue}")
print(f"Avanzado: {x2.varValue}")
print(f"Ganancia Máxima Diaria: ${pulp.value(model.objective)}")

#source .venv/bin/activate