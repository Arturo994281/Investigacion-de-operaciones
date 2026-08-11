import math
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print('Advertencia: matplotlib no está disponible. La gráfica se omitirá.')
import numpy as np

def resolver_eoq(D, S, H, C, dias_laborables, lead_time):

    # Calcular EOQ
    Q_optimo = math.sqrt((2 * D * S) / H)

    # Numero de pedidos al año
    N_pedidos = D / Q_optimo

    # Tiempo entre pedidos
    tiempo_entre_pedidos = dias_laborables / N_pedidos

    # Demanda diaria
    demanda_diaria = D / dias_laborables

    # Punto de reorden
    rop = demanda_diaria * lead_time

    # Costos
    costo_compra = D * C
    costo_ordenar = (D / Q_optimo) * S
    costo_mantener = (Q_optimo / 2) * H
    costo_total = costo_compra + costo_ordenar + costo_mantener

    # Mostrar resultados
    print("=== RESULTADOS DEL MODELO EOQ ===")
    print(f"Lote Óptimo de Pedido (EOQ): {Q_optimo:.2f} unidades")
    print(f"Número de pedidos al año: {N_pedidos:.2f} órdenes")
    print(f"Tiempo entre pedidos: {tiempo_entre_pedidos:.2f} días laborables")
    print(f"Demanda diaria: {demanda_diaria:.2f} unidades")
    print(f"Punto de Reorden (ROP): {rop:.2f} unidades")
    print("-" * 40)
    print(f"Costo Anual de Ordenar: ${costo_ordenar:,.2f} USD")
    print(f"Costo Anual de Mantener: ${costo_mantener:,.2f} USD")
    print(f"Costo Anual de Compra: ${costo_compra:,.2f} USD")
    print(f"Costo Total Anual: ${costo_total:,.2f} USD")

    return Q_optimo, rop, tiempo_entre_pedidos


# Datos del ejercicio
D = 12000          # Demanda anual
S = 200            # Costo por orden
H = 4              # Costo de mantener una unidad al año
C = 50             # Costo por unidad
dias_lab = 240     # Días laborables al año
L = 6              # Lead Time en días


# Resolver modelo EOQ
Q_opt, rop_val, t_ciclo = resolver_eoq(
    D, S, H, C, dias_lab, L
)


# -----------------------------
# SIMULACIÓN DEL INVENTARIO
# -----------------------------

num_ciclos = 3

tiempo = np.linspace(
    0,
    num_ciclos * t_ciclo,
    500
)

inventario = []

for t in tiempo:

    tiempo_en_ciclo = t % t_ciclo

    inv = Q_opt - (
        (D / dias_lab) * tiempo_en_ciclo
    )

    inventario.append(inv)


# -----------------------------
# GRÁFICA
# -----------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    tiempo,
    inventario,
    color='navy',
    lw=2,
    label='Nivel de inventario'
)

plt.axhline(
    y=rop_val,
    color='red',
    linestyle='--',
    label=f'ROP = {rop_val:.0f} unidades'
)

plt.axhline(
    y=0,
    color='black',
    linewidth=0.8
)

plt.title('Simulación de Inventario: Modelo EOQ')
plt.xlabel('Días Laborables')
plt.ylabel('Unidades en Almacén')

plt.grid(
    True,
    linestyle=':',
    alpha=0.6
)

plt.legend()
plt.tight_layout()
plt.show()