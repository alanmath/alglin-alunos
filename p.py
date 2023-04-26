import math

p = 0.763
N = 11

# Função para calcular o coeficiente binomial
def binomial_coef(n, k):
    return math.comb(n, k)

# Função para calcular a probabilidade de X=x
def binomial_prob(x):
    return binomial_coef(N, x) * pow(p, x) * pow(1-p, N-x)

# Calcular a entropia
entropy = 0
for x in range(N+1):
    px = binomial_prob(x)
    if px > 0:
        entropy -= px * math.log2(px)

print("Entropia em base 2:", entropy)

import scipy.stats as stats
print(stats.entropy([1/13]*13, base=2))


print(math.log2(1/13))
