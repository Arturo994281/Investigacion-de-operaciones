import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Inspeccion Basica", lowBound=0, upBound=2, cat='Integer')
x2 = pulp.LpVariable("Inspeccion Profunda", lowBound=0, upBound=5, cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "Seguridad total"

# 4. Restricciones
model += x1 * 1 +  x2 * 3 <= 18, "Firewall"
model += x1 +  x2 <= 8, "RAM"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Inspeccion Basica: {x1.varValue}")
print(f"Inspeccion Profunda: {x2.varValue}")
print(f"Seguridad total: {pulp.value(model.objective)}")

#source .venv/bin/activate