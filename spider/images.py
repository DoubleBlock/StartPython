from urllib import request

for i in range(1,):
        res= request.urlopen('https://img.onvshen.com:85/gallery/20590/13484/'+ str(i) + '.jpg')
        if res.status == 404:
            print('出错')
        else:
            data= res.read()

