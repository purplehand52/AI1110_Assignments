import theo_func as t

pe_values = t.prob_err()

print("P{e|0}:", pe_values[0])
print("P{e|1}:", pe_values[1])
print("P{e}:", pe_values[2])
