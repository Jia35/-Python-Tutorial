# Python程式教學04

[[回首頁]](../README.md)<br/>

----
### File(文件)
#### 開啟檔案
```python f = open('檔案', '模式') ```<br/>
| 模式 | 意思                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 讀取(檔案需存在)                                             |
| w    | 新建檔案寫入(檔案可不存在，若存在則清空)                     |
| a    | 資料附加到舊檔案後面(游標指在EOF)                            |
| r+   | 讀取舊資料並寫入(檔案需存在且游標指在開頭)                   |
| w+   | 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增) |
| a+   | 資料附加到舊檔案後面(游標指在EOF)，可讀取資料                |
| b    | 二進位模式                                                   |

#### 讀取文件內容
```python f.read(size) ``` - 讀取size字串長度進來，若不填則讀取整份文件<br/>
```python f.readline() ``` - 讀取一行,最後面會加上一個 \n<br/>
```python f.readlines() ``` - 傳回一list ，每一行文字最後面會加上一個 \n 為一個list的資料項<br/>
#### 寫入檔案
```python f.write(string) ``` - 寫入檔案，並回傳寫入的string長度<br/>
#### 游標位置
```python f.seek(位移的bit數) ```<br/>
可指定從哪邊開始<br/>
```python f.seek(位移的bit數,0) ``` - 從文件開頭開始<br/>
```python f.seek(位移的bit數,1) ``` - 從目前游標位置開始<br/>
```python f.seek(位移的bit數,2) ``` - 從目前文件結尾開始<br/>
#### 關閉檔案
```python f.close() ```<br/>
簡單範例<br/>
```python 
f = open('123.txt', 'r+')
print(f.read())

f.write("string")

f.close()
```
123.txt檔案內容`<br/>
<img src="./image/tutorial05_image01.png"  alt="tutorial05_image01.png" width="40%"/><br>
<img src="./image/tutorial05_image02.png"  alt="tutorial05_image02.png" width="80%"/><br>
<br/>

<br/>

模組 from 陳述
視窗
