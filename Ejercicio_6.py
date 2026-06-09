import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Estandar", lowBound=0, upBound=20, cat='Integer')
x2 = pulp.LpVariable("Premium", lowBound=0, upBound=60, cat='Integer')

# 3. Función Objetivo
model += 20 * x1 + 60 * x2, "Cumplir con la ley"

# 4. Restricciones
model += x1 * 1 +  x2 * 3 >= 15, "IOPS"
model += x1 * 2 +  x2 * 2 >= 14, "Disponibilidad"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Estandar: {x1.varValue}")
print(f"Premium: {x2.varValue}")
print(f"Cumplir con la ley: {pulp.value(model.objective)}")

#source .venv/bin/activate