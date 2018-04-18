# Python程式教學01

[[回首頁]](../README.md)<br/>

----
## 什麼是程式語言?

人類與電腦溝通的語言稱為程式語言。<br>
電腦除了可以上網、放音樂、看影片、遊戲，還可以做更多事情:<br>
* 下棋。例如：AlphaGo 圍棋程式
* 無人駕駛汽車，又稱電腦駕駛汽車
* 掃地機器人

要做到以上功能，必須給電腦一堆指令寫一連串指令存於文件（稱程式碼），形成一個程式，這過程稱撰寫程式，而所用的指令稱程式語言<br>

例如你想讓一台搭載電腦的機器人幫你上街去買菜。
* (X)嘿，電腦，請幫我去市場買顆高麗菜回來
* (O)出門後直走一百公尺後左轉<br>繼續走遇到第二個紅綠燈後停下<br>超市應該就在你的右手邊<br>進門後往最裡面的區域走<br>
<br>

## Python

<img src="./python-logo.png"  alt="python logo" width="600"/><br>
* 活躍的社群
* 開放源始碼
* 傑出的設計哲學
* 眾多的第三方資源
* 跨平台
* 被廣泛地使用
<br>

### 安裝Python

[https://goo.gl/YKsmr3](https://goo.gl/YKsmr3)
<br>

### 第一個程式

顯示Hello World<br>
```python
print(‘Hello World’)
```
<br>

### 變數

變數定義的規則：<br>
* 變量命名時，只能是字母、數字或是_下劃線的任意組合
* 變量命名時，第一個字符不能是數字
* 大小寫是不同的
* 關鍵字不能聲明為變量名

O ---> Abd、i、out01、apple_phone<br>
X ---> 101dogs、for<br>
<br>

### 資料型別

**數字（Number）**		->整數(int)、浮點數(float)<br>
      a = 123<br>
      b = 99.9<br>
**字串（String）**<br>
      str1 = ‘Hello’<br>
      str2 = “你好”<br>
**布林值（Boolean）**	->True、False<br>
      Boo = True<br>

程式語言分成靜態語言與動態語言:<br>
C、C++與Java屬於靜態語言，變數在執行前需要宣告資料型別，變數宣告了資料型別後就不能更改成其他型別；<br>
Python屬於動態語言，執行時才決定資料型別，不需要事先宣告變數的資料型別。<br>
<br>

### 註解

單行註解用『#』字<br>
多行註解用『'''』三個單引號或是用『"""』三個雙引號<br>
<br>

### 運算子

|     |     |      |      |     |            |
| --- | --- | ---- | ---- | --- | ---------- |
| +   | 加  | *    | 乘   | /   | 除         |
| -   | 減  | \*\* | 次方 | //  | 除(取整數) |
|     |     |      |      | %   | 取餘數     |

用括號刮起來的部分優先計算<br>
延伸：a=a+1  ==>  a+=1<br>

|     |          |     |          |     |        |
| --- | -------- | --- | -------- | --- | ------ |
| >   | 大於     | <   | 小於     | ==  | 等於   |
| >=  | 大於等於 | <=  | 小於等於 | !=  | 不等於 |

```AND```-->當全部都為1(True)時輸出1(True)，否則為0(false)<br>
```OR```-->當至少一個為1(True)時輸出1(True)，否則為0(false)<br>
```NOT```-->輸出相反(輸入1->輸出0)<br>
<br>

### 字串運算

```python
Str1 = ‘Hello’
Str2 = ‘World’
Str3 = ‘’‘Hello
World’’’

Str4 = Str1+ Str2   # Str4=‘HelloWorld’
Str5 = Str1*3       # Str5=’HelloHelloHello’
Str6 = Str1[1]      # Str6=’e’
Str7 = Str1[1:4]    # Str7=’ell’
```

```python
給使用者輸入
A = input()
B = input(‘請輸入:’)
```
<br>

### if…elif…else條件判斷

如果…否則如果…否則…
```python
a=7
if a > 10:
	print("a大於10")
elif a > 5: 
	print("a大於5")
else:
	print("a不大於5")
```
<br>

### for…in循環

```python
for x in range(10):		# 0...9不含10
	print(x)
[0,1,2,3,4,5,6,7,8,9]
for x in 'Python':
	print(x)
```

