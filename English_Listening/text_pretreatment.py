from os import replace
f = open(r'C:\Users\陈柏诚大帅B\Desktop\English Listening\keywords_list.txt','r',encoding='utf-8')
text=f.read()
while '；' in text:
    text=text.replace("；",' ')
print(text)
f = open(r'C:\Users\陈柏诚大帅B\Desktop\English Listening\keywords_list.txt','w')
f.write(text)
f.close()