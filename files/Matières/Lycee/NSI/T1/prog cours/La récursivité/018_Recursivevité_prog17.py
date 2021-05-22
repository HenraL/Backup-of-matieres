def fact_term(n,acc):
    if n>0:
        return fact_term(n-1,acc*n)
    else:
        return acc

print(fact_term(4,1))
print(fact_term(3,4))
print(fact_term(2,12))
print(fact_term(1,24))
print(fact_term(0,24))