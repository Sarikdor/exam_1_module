def persist(num):
    a = 1
 
    while num > 0:
        digit = num % 10
        mult = mult * digit
        num = num // 10
    return num
print(persist(999))
    