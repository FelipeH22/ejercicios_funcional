operacion = lambda a: [abs(x)%10 for x in a]
print("".join(map(str,operacion([125,459,784,888]))))