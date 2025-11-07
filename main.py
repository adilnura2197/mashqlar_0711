#1-misol
for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        break

#2-misol
for i in range(100, 150):
    if i == 137:
        print("Parol topildi")
        break

#3-misol
sum = 0
for i in range(1, 10):
    sum += i
    if sum >= 20:
        break
print(sum)

#4-misol
k = 1
for i in range(1, 21):
    k *= i
    if k >= 10000:
        break
print(k)
