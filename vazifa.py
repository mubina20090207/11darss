# """1"""
# import asyncio

# async def numbers(password):
#     result = ''
#     i = 0
#     while i < len(password):
#         if not password[i].isdigit():
#             result += password[i]
#         i += 1
#     print(result)

# asyncio.run(numbers("pass123word"))

# """"2"""
# async def text(text):
#     result = ''
#     i = 0
#     while i < len(text) and i < 10:
#         result += text[i]
#         i += 1
#     print(result)

# asyncio.run(text("This is a long text example"))

# """3"""
# async def numbers(name):
#     result = ''
#     i = 0
#     while i < len(name):
#         if not name[i].isdigit():
#             result += name[i]
#         i += 1
#     print(result)

# asyncio.run(numbers("John123"))


# """4"""
# async def Text(text):
#     result = ''
#     i = 0
#     while i < len(text):
#         if text[i] != ' ':
#             result += text[i].lower()
#         i += 1
#     print(result)

# asyncio.run(Text("Hello World"))


# """5"""
# async def num(text):
#     vowels = 'aeiouAEIOU'
#     result = ''
#     i = 0
#     while i < len(text):
#         if text[i] in vowels:
#             result += text[i]
#         i += 1
#     print(result)

# asyncio.run(num("This is an example"))


# """6"""
# async def text(word):
#     result = ''
#     i = 0
#     while i < len(word):
#         if i < len(word) - 1 and word[i] == 'a' and word[i + 1] == 'b':
#             result += '#'
#             i += 1 
#         else:
#             result += word[i]
#         i += 1
#     print(result)

# asyncio.run(text("absolutely"))


# """7"""
# async def num(text):
#     if text.isdigit():
#         print(text[::-1])

# asyncio.run(num("123456"))


# """8"""
# async def text(word):
#     result = ''
#     middle_index = len(word) // 2
#     for i in range(len(word)):
#         if i != middle_index:
#             result += word[i]
#     print(result)

# asyncio.run(text("example"))

# """9"""
# async def num(name):
#     if name.endswith('a'):
#         print(name.lower())

# asyncio.run(num("Maria"))


# """10"""
# async def num(text):
#     result = ''
#     seen = set()
#     i = 0
#     while i < len(text):
#         if text[i] not in seen:
#             seen.add(text[i])
#             result += text[i]
#         i += 1
#     print(result)

# asyncio.run(num("banana"))


# """11"""
# async def num(word):
#     vowels = 'aeiouAEIOU'
#     if all(char in vowels for char in word):
#         print(word.upper())

# asyncio.run(num("aeiou"))
