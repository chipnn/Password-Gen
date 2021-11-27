import random

lower="qwertyuiopasdfghjklzxcvbnm"
uper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
gen=lower+uper+number
length=16
generate="".join(random.sample(gen,length))
print(generate)