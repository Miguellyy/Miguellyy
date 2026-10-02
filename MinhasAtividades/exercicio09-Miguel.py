nums = int(input("Quantos numeros você deseja printar?: "))
count1 = 0
count2 = 1
fib = 0

while fib <= nums:
    print(count1)
    if fib == (nums - 1):
        break
    print(count2)
    if fib == (nums - 2):
        break
    count1 = count1 + count2
    count2 = count1 + count2
    fib = fib + 2