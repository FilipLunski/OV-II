from pulp import *

# Vytvoření problému
prob = LpProblem("Vícekriteriální optimalizace", LpMinimize)

# Definice proměnných
x1 = LpVariable("x1", lowBound=0)               # Počet vyrobených jednotek produktu A
x2 = LpVariable("x2", lowBound=0)               # Počet vyrobených jednotek produktu B
d1_minus = LpVariable("d1_minus", lowBound=0)   # Negativní odchylky od cíle zisku
d2_minus = LpVariable("d2_minus", lowBound=0)   # Negativní odchylky od cíle výroby produktu A
d3_minus = LpVariable("d3_minus", lowBound=0)   # Negativní odchylky od cíle výroby produktu B

# Cílová funkce
prob += d1_minus + d2_minus + d3_minus, "Cílová funkce"

# Omezení
prob += 5*x1 + 10*x2 <= 300, "Omezení pracovních hodin"
prob += 2*x1 + 3*x2 <= 120, "Omezení surovin"
# Cíle
prob += 100*x1 + 200*x2 + d1_minus  == 8000, "Cíl zisku"
prob += x1 + d2_minus >= 30, "Cíl výroby produktu A"
prob += x2 + d3_minus >= 20, "Cíl výroby produktu B"

# Řešení problému
prob.solve()

# Výpis výsledků
print("Status:", LpStatus[prob.status])
print("Optimální hodnota cílové funkce:", value(prob.objective))
print("\nDosažený zisk:", 100*value(x1) + 200*value(x2))
print("d1_minus =", value(d1_minus))
print("\nx1 =", value(x1))
print("d2_minus =", value(d2_minus))
print("\nx2 =", value(x2))
print("d3_minus =", value(d3_minus))
print("\nPracovní hodiny:", 5*value(x1) + 10*value(x2))
print("Spotřeba surovin:", 2*value(x1) + 3*value(x2))