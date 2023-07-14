income = 25000
name = "Johannes Hirschbeck"

if income < 10000:
    taxes = 0.4*income
elif 10000<income<30000:
    taxes = 0.55*income
elif 30000<income<70000:
    taxes = 0.75*income
elif income > 70000:
    taxes = 0.82*income

print(f"Der Steuerzahler {name} muss für das laufende Jahr {taxes} Dublonen dem Steueramt bezahlen.")
capital = 600000

if capital < 100000:
    taxes += 0.05*capital
elif 100000<capital<500000:
    taxes += 0.08*capital
elif 500000<capital<1000000:
    taxes += 0.13*capital
elif capital > 1000000:
    taxes += 0.21*capital

print(f"Der Steuerzahler {name} muss für das laufende Jahr {taxes} Dublonen dem Steueramt bezahlen.")
