# Criptografia

N = int(input())
for _ in range(N):
    lin = input()
    chars = []
    for i in lin:
        chars.append(i)
    for i in range(len(chars)):
        id = ord(chars[i])
        if (65 <= id <= 90) or (97 <= id <= 122):
            id += 3
            chars[i] = chr(id)
    chars.reverse()
    for i in range(len(chars) // 2, len(chars)):
        id = ord(chars[i])
        id -= 1
        chars[i] = chr(id)
    print("".join(chars))