s = 'yobobozbobobobbobbobobobobobbobbobobobobbyoa'

 
term = 'bob'

print list(enumerate(s))
print sum(1 for i, j in enumerate(s) if s[i:i+len(term)] == term)



