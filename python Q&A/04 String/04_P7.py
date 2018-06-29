x = input().strip()
out = ""
for s in '0123456789':
    if s not in x:
        out += s + " "
if out == "":
    out = "No missing digits"
print(out.strip())
