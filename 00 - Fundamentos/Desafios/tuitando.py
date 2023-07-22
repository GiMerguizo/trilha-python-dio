T = str(input("Tweet: "))
carc = len(T)
print(f"Quantidade de caracteres: {carc}")

if carc > 140:
    print('MUTE')
else:
    print('TWEET')