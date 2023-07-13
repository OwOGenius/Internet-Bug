#抓取 PTT八卦板網頁原始碼(HTLM)
import urllib.request as req
def getData(url):
    #建立一個Request物件，附加 Request Headers 的資訊
    request= req.Request(url, headers={
    'cookie':'over18=1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
})
    with req.urlopen(request) as response:   
        date=response.read().decode('utf-8')
    #解析原始碼，取得每篇文章標題
    import bs4
    root=bs4.BeautifulSoup(date, 'html.parser')#讓BS協助解析HTML格式文件
    titles=root.find_all('div', class_="title")#尋找所有 class="title"的div標籤
    print(titles)
    for title in titles:
        if title.a != None:#如果標題包含 a 標籤(沒有被刪除)，印出來
            print(title.a.string)
    #抓取下一列連結
    nextLink=root.find('a', string='‹ 上頁')#找到內容是 ‹ 上頁 的 a 標籤
    return nextLink['href']
#抓取一個頁面標題
pageURL='https://www.ptt.cc/bbs/Gossiping/index.html'
count=0
while count<5:
    pageURL='https://www.ptt.cc'+getData(pageURL)
    count+=1
