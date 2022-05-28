from lxml import etree
import pandas


def getdata(name , indx):
    f = open(name, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    f.close()
    htmll = etree.HTML(text)

    arr = []
    allarr = []
    arr.append(indx)
    name = htmll.xpath('//div[@role="gridcell"]//div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX"]/text()')
    pric = htmll.xpath(
        '//div[@role="gridcell"]//div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount"]')
    token = htmll.xpath(
        '//div[@role="gridcell"]//div[@class="AssetCardFooter--name"]/text()')
    if len(name) > 6:
        print(len(name))
    for k,n in enumerate(name):
        arr = []
        arr.append(indx)
        arr.append(n)
        if len(pric) > k:
            p = pric[k].xpath("./text()")
            arr.append(" ".join(p))
        else:
            arr.append("")
        if len(token) > k:
            arr.append(token[k])
        else:
            arr.append("")

        allarr.append(arr)



    # //*[@id="main"]/div/div/div[1]/div[2]/div[2]/div/div/button/div/i/text()

    # //ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[2]/a/div/span/text()
    return allarr

    # return arr


if __name__ == '__main__':
    allarr2 = []
    filename = "collectionInfo"
    lb = "家居"


    for i2 in range(5, 500):
            try:
                arr = getdata('./info2html/'+ "aa1info1inj" + str(i2) +'.html' , str(i2))
                allarr2.extend(arr)
            except Exception as e :
                print("------------****" , e)
                continue
    print(len(allarr2))
    kk = [";".join(i) for i in allarr2]
    kk = list(set(kk))
    print(len(kk))
    # print(kk)
    bb = []
    for i in kk:
        # print(i)
        b =i.split(";")
        bb.append(b)
    allarr2 = bb


    name = ["indx" , "name","pric","token"]
    test = pandas.DataFrame(columns=name, data=allarr2)
    test.to_csv("./csv/aa0519v2" + filename + '2.csv', encoding='utf-8')
