x=input("enter your string: ")
words=x.split()
y=[]
for w in words:
    z=''
    for ch in w:        
        if ch.casefold() in 'aeiou':
            z+=ch
    if len(w)==len(z):
        y.append(z)
for w in words:
    z=''
    for ch in w:        
        if ch.casefold() in 'aeiou':
            pass
        else:            
            z+=ch
    if len(z)>1:
        y.append(z)    
print(' '.join(y))
            
        
