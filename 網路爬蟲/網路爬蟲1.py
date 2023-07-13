#抓取 巴哈warthunder網頁原始碼(HTLM)
import urllib.request as req
url = 'https://forum.gamer.com.tw/B.php?bsn=20947'
#建立一個Request物件，附加 Request Headers 的資訊
request= req.Request(url, headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
})
with req.urlopen(request) as response:   
    data=response.read().decode('utf-8')
#解析原始碼，取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, 'html.parser')#讓BS協助解析HTML格式文件
titles=root.find_all('div', class_="b-list__tile")#尋找所有 class="b-list__tile"的div標籤
print(titles)
for title in titles:#如果標題包含 p 標籤(沒有被刪除)，印出來
    if title.p != None:
        print(title.p.string)