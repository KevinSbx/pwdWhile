# 密碼程式
# password = "a123456"
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確，印出"登陸成功!
# 如果不正確，印出"密碼錯誤，還有_次機會"

password = "a123456"
i = 3
while i > 0:
	i -= 1
	pwd = input("請輸入密碼: ")
	if pwd == password:
		print("登陸成功!") 
		break
	else:
		print("密碼錯誤")
		if i > 0:
			print("還有", i, "次機會")
		else:
			print("重複多次錯誤，帳號即將被鎖")