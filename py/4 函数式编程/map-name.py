def A2a(s):
    return s[0].upper()+s[1:].lower()
def normalize(s):
    return map(A2a,s)

L1 = ['adam', 'LISA', 'barT']
print(list(normalize(L1)))