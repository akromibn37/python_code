# pattern = "[A].-[B]-...[C]-.-.[E].["
fn = open(input().strip())
code = fn.readline().strip()
pattern = fn.readline().strip()
if code == 'T2M' :
    for text in fn :
        text = text.strip()
        morse = ''
        for e in text :
            j = pattern.find('[' + e + ']')
            if j == -1 :
                print('Invalid :', text)
                break
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        else:
            print(morse.strip())
elif code == 'M2T' :
    for morse in fn :
        morse = morse.strip() + ' '
        text = ''
        i1 = 0
        while i1 < len(morse):
            i2 = morse.find(' ',i1)
            j = pattern.find(']' + morse[i1:i2] + '[')
            if j == -1 :
                print('Invalid :',morse.strip())
                break
            text += pattern[j-1]
            i1 = i2 + 1
        else :
            print(text)
else :
    print('Invalid code')
fn.close()
