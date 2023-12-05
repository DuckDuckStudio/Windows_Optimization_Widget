import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("请输入要生成的密码位数："))
password = generate_password(length)
print("生成的随机密码为：", password)