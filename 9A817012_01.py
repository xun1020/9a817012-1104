def print_diamond(num):
    if num % 2 == 0:
        num += 1

# for i in range(i的初始值,i的上限,i每次加多少)
    for i in range(1, num + 1, 2):
        spaces = (num - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(num - 2, 0, -2):
        spaces = (num - i) // 2
        print(" " * spaces + "*" * i)

num = int(input("請輸入星星數量: "))

print_diamond(num)
