



from lxml import etree

import pandas




def getdata(name , lb):
    # htmll = etree.parse(name, etree.HTMLParser())
    f = open(name, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    f.close()

    # encode_type = chardet.detect(text)
    # text = text.decode(encode_type['encoding'])
    htmll = etree.HTML(text)

    # # /html/body/div[15]/button[1]/div/div/div/div/div/div/div/div[2]
    aa = htmll.xpath('//div[@role="listitem"]')
    # print(aa)
    # /html/body/div[17]/button[1]/div/div/div/div/div/div/div/div[2]/span[1]/div/a
    # print("----ffsf")
    allarr = []
    for a in aa:
        arr = []
        # a1 = a.xpath('./button/div/div[1]/div/a/@href')
        # button/div/div[2]/div/div/div/div[2]/span[2]/a/div..name
        a2 = a.xpath('./button/div/div[2]/div/div/div/div[2]/span[2]/a/div/text()')
        # /div/div[3]/div/div[2]/span/div/div...pri
        a3 = a.xpath('./button/div/div[3]/div/div[2]/span/div/div/text()')
        # /div/div[4]/p/div--q
        a4 = a.xpath('./button/div/div[4]/div/text()')
        print(a4)
        # a5 = a.xpath('./button/div/div[5]/div/a/@href')
        # url
        a6 = a.xpath('./button/div/div[6]/div/a/@href')
        #
        a7 = a.xpath('./button/div/div[7]/div/a/text()')

        arr.append(''.join(a2))
        arr.append(''.join(a3))
        arr.append(''.join(a4))
        arr.append(''.join(a6))
        arr.append(''.join(a7))
        # print(arr)
        # assets      = a.xpath('./span/a/@href')
        # collection  = a.xpath('./span/div/a/@href')
        # if len(assets) > 0:
        #     arr.append(assets[0])
        # else:
        #     arr.append("")
        #
        # if len(collection) > 0:
        #     arr.append(collection[0])
        # else:
        #     arr.append("")
        allarr.append(arr)



    return allarr

    # return arr


if __name__ == '__main__':
    allarr = []
    filename = "a2list"
    lb = "家居"
    for i in range(0 , 2000):
        try:
            # print("______"+ str(i))
            arr = getdata('../html/'+ filename + str(i) +'.html' , lb)
            # print(arr)
            # arr.append(lb)
            # print(arr)
            allarr.extend(arr)
            # print(len(allarr))
            if i%25 == 24:
                print("---")
                print(i)
                kkk = [";".join(i) for i in allarr]
                kkk = list(set(kkk))
                print(len(kkk))
        except Exception as e :
            # print("------------****" , e)
            if i%25 == 24:
                print("---")
                print(i)
                kkk = [";".join(i) for i in allarr]
                kkk = list(set(kkk))
                print(len(kkk))
            continue

    print(len(allarr))
    kk = [";".join(i) for i in allarr]
    kk = list(set(kk))
    print(len(kk))
    # print(kk)
    bb = []
    for i in kk:
        # print(i)
        b =i.split(";")
        bb.append(b)
    name = ['name' , "price" , "qu" , "url" , "time"]
    test = pandas.DataFrame(columns=name, data=bb)
    test.to_csv("./csv/aa0518v2" + filename + '2.csv', encoding='utf-8')

