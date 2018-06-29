# pattern = "].-[A]-...[B]-.-.[C].[E]"
fn = open(input().strip())
code = fn.readline().strip()
pattern = fn.readline().strip()
if code == 'T2M' :
    for text in fn :
        text = text.strip()
        morse = ''
        for e in text :
            j = pattern.rfind(']' + e + '[',0,len(pattern))
            if j == -1 :
                print('Invalid :', text)
                break
            k = pattern.rfind('[',0,j)
            morse += pattern[k+1:j] + ' '
        else:
            print(morse.strip())
elif code == 'M2T' :
    for morse in fn :
        morse = morse.strip() + ' '
        text = ''
        i1 = 0
        while i1 < len(morse):
            i2 = morse.find(' ',i1)
            s = '[' + morse[i1:i2] + ']'
            j = pattern.find(s)
            if j == -1 :
                print('Invalid :',morse.strip())
                break
            text += pattern[j+len(s)]
            i1 = i2 + 1
        else :
            print(text)
else :
    print('Invalid code')
fn.close()
