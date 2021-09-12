text1 = input("Text By Human > ").lower() # Text by human
text2 = input("Text By Machine > ").lower() # Text by machine
sdi = 0
for word in text1.split():
    if word not in text2:
        sdi += 1

print(f"Your WER is : {sdi/len(text1.split())}")
