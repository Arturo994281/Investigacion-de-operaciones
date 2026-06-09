import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Personajes", lowBound=0, upBound=80, cat='Integer')
x2 = pulp.LpVariable("Escenarios", lowBound=0, upBound=60, cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Maximizar valor total aportado esta semana"

# 4. Restricciones
model += x1 * 2 +  x2 * 1 <= 12, "GPU"
model += x1 * 1 +  x2 * 2 <= 14, "VRAM"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Personajes: {x1.varValue}")
print(f"Escenarios: {x2.varValue}")
print(f"Valor total aportado esta semana: {pulp.value(model.objective)}")

#source .venv/bin/activate