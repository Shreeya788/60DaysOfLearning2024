import random
f= open('petnames.txt','r')
f_content = f.read()
f_content_list=f_content.split('\n')

print(random.choice(f_content_list))
f.close()