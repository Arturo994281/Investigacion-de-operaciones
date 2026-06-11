import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Ilustraciones", lowBound=0, upBound=40, cat='Integer')
x2 = pulp.LpVariable("Iconos", lowBound=0, upBound=20, cat='Integer')

# 3. Función Objetivo
model += 40 * x1 + 20 * x2, "Ganancia_Total"

# 4. Restricciones
model += x1 *2 +  x2 <= 12, "RAM"
model +=  x1 +  x2 <= 9, "VCPU"
model +=   x2 <= 8, "Iconos"
model +=   x1 <= 2, "Ilustraciones"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Ilustraciones: {x1.varValue}")
print(f"Iconos: {x2.varValue}")
print(f"Ganancia Máxima Diaria: ${pulp.value(model.objective)}")

#source .venv/bin/activate