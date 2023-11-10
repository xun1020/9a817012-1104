# 輸入學號、姓名、國文、數學、電腦成績
sid = input("請輸入您的學號: ")
sname = input("請輸入您的姓名: ")
fchina = float(input("請輸入您的國文成績: "))
fmath = float(input("請輸入您的數學成績: "))
finfo = float(input("請輸入您的電腦成績: "))
output = "-" * 50

print("{}".format(output))

# 計算總分和平均
total_score = fchina + fmath + finfo
average_score = total_score / 3

# 顯示各科成績、總分和平均
print(f"{sname} ({sid})同學您好:\n以下是您的各科成績與分數評定\n")
print(f"國文成績: {fchina}/數學成績: {fmath}/電腦成績: {finfo}")
print(f"總分:{round(total_score, 2)}/平均: {round(average_score, 2)}")

print("{}".format(output))

# 檢查是否合格
if average_score > 60:
    print("成績判定:合格")
else:
    print("成績判定:不合格")
