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

    ul = htmll.xpath('//ul[@role="table"]/li')
    # //*[@id="Body react-aria-4"]/div/div/div/div/ul

    for li in ul:
        arr = []
        arr.append(indx)
        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[2]/div[1]/div/div/a/div/span/div
        a1 = li.xpath('./div[1]/div/div/a/div/span/div/text()')
        # //ul[@role="table"]/li[2]/div[2]/div/div/div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount"]/text()
        a2 = li.xpath('./div[2]/div/div/div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount"]/text()')

        a3 = li.xpath(
            './div[3]/div/span/text()')
        a4 = li.xpath(
            './div[4]/div/div/div/span/text()')
        a5 = li.xpath(
            './div[5]/div/div/a/span/text()')
        a6 = li.xpath(
            './div[6]/div/span/text()')
        a7 = li.xpath(
            './div[7]/div/text()')
        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[10]/div[7]/div

        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[10]/div[6]/div/span
        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[2]/div[5]/div/div/a/span

        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[2]/div[4]/div/div/div/span

        arr.append(''.join(a1))
        arr.append(''.join(a2))
        arr.append(''.join(a3))
        arr.append(''.join(a4))
        arr.append(''.join(a5))
        arr.append(''.join(a6))
        arr.append(''.join(a7))
        print(arr)
        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[2]/div[3]/div/span
        # //*[@id="Body react-aria-4"]/div/div/div/div/ul/li[2]/div[2]/div/div/div[2]
        allarr.append(arr)
    #


    # //*[@id="main"]/div/div/div[1]/div[2]/div[2]/div/div/button/div/i/text()

    # //ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[2]/a/div/span/text()
    return allarr

    # return arr


if __name__ == '__main__':
    allarr2 = []
    # bidmadeinfo4inj166.html
    filename = "bid"
    lb = "家居"
    for ii in range(1 , 500):
        for j in range(0,5):
            try:
                # 1inj183.html
                arr = getdata('./info2html/'+ "bidinfo"+str(j)+"inj" + str(ii) +'.html' , str(ii))
                allarr2.extend(arr)
            except Exception as e :
                print("------------****" , e)
                continue

    print(len(allarr2))
    kk = [';'.join(i2) for i2 in allarr2]
    kk = list(set(kk))
    print(len(kk))
    # print(kk)
    bb = []
    for i3 in kk:
        # print(i)
        b =i3.split(";")
        bb.append(b)
    allarr2 = bb
    name = ["index","Offer","Unit Price","USD Unit Price","Floor Difference","From","Expiration","Received"]
    test = pandas.DataFrame(columns=name, data=allarr2)
    test.to_csv("./csv/aa0519v2" + filename + '2.csv', encoding='utf-8')

