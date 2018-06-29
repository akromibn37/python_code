import math
w = float(input())
h = float(input())
x = math.log10(w)*0.0188
mo = math.pow(w*h,1/2)/60
ha = 0.024265*math.pow(w,0.5378)*math.pow(h,0.3964)
bo = 0.0333*math.pow(w,0.6157-x)*math.pow(h,0.3)
print(mo)
print(ha)
print(bo)