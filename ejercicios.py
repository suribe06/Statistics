import scipy.stats
import math

#ejercicio 1
n = 100
std_dev_ = 0.5
x_ = 20.4

x1 = scipy.stats.norm(x_, std_dev_/math.sqrt(n)).cdf(19.2)
x2 = 1 - scipy.stats.norm(x_, std_dev_/math.sqrt(n)).cdf(20.5)

ans = x1 + x2
print(ans)
print(f"{ans*100}%")

#ejercicio 2
n = 100
miu = 24
std_dev = 8
ans = 1 - scipy.stats.norm(miu, std_dev/math.sqrt(n)).cdf(25)
print(ans)
print(f"{ans*100}%")
