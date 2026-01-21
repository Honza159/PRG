f0, f1 = 0,1
print(f"F0 = {f0}")
for i in range(1, 21):
    print(f"F{i} = {f1}")
    f0, f1 = f1, f0 + f1