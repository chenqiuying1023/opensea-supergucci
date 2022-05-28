from lxml import etree
import pandas


def getdata(name , indx):
    allarr = []
    f = open(name, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    f.close()
    htmll = etree.HTML(text)

    arr = []
    arr.append(indx)
    name = htmll.xpath('//div[@class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 gbiTQT jYqxGr"]/div/text()')
    time = htmll.xpath(
        '//div[@class="AccountHeaderreact__MainContainer-sc-1omadrn-2 etqLOL"]/span/text()')
    coll = htmll.xpath(
        '//ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[1]/a/div/span/text()')
    crea = htmll.xpath(
        '//ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[2]/a/div/span/text()')
    favc = htmll.xpath(
        '//ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[3]/a/div/span/text()')
    snss = htmll.xpath(
        '//*[@id="main"]/div/div/div[1]/div[2]/div[2]/div/div/button/div/i/text()')
    arr.append(' '.join(name))
    arr.append(' '.join(time))
    arr.append(' '.join(coll))
    arr.append(' '.join(crea))
    arr.append(' '.join(favc))
    arr.append(' '.join(snss))
    print(arr)
    # //*[@id="main"]/div/div/div[1]/div[2]/div[2]/div/div/button/div/i/text()
    allarr.append(arr)
    # //ul[@class="Blockreact__Block-sc-1xf18x6-0 Menureact__MenuBase-sc-1j0z9gq-1 AccountPageNavbarreact__StyledNavbar-sc-10ky4m4-0 elqhCm dlHLLo jZKuuO"]/li[2]/a/div/span/text()
    return allarr

    # return arr


if __name__ == '__main__':
    allarr2 = []
    filename = "collect-creat-fav"
    lb = "家居"
    for i in range(1 , 500):
        for j in range(1 , 2):
            try:
                arr2 = getdata('./info2html/'+ "aa1info" +str(j)+ "inj" + str(i) +'.html' , i)
                allarr2.extend(arr2)
            except Exception as e :
                print("------------****" , e)
                continue
    name = ["index","name","time","coll","crea","favc","snss"]
    test = pandas.DataFrame(columns=name, data=allarr2)
    test.to_csv("./csv/aa0519v2" + filename + '2.csv', encoding='utf-8')

