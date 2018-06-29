heights = [int(e) for e in input().split()]
h = int(input())
heights.sort()

if h<min(heights):
    print('Too short')
elif h>max(heights):
    print('Too tall')
else:
    i = 0
    p = 100.0
    while i < len(heights):
        if heights[i] > h:
            p = i*100/len(heights)
            break
        else:
            i += 1
    print(str(p)+'th percentile')
