dust = 70

if dust < 150 :
    print('매우나쁨')
elif 80 < dust <= 150 :
    print('나쁨')
elif 30 < dust <= 80 :
    print('보통')
else : 
    print('좋음')

# 순서대로 내려가면서 실행되기 때문에 코드는 주의해서 작성