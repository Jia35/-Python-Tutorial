# Python程式教學03

[[回首頁]](../README.md)<br/>

----
### format 格式化函數
為了輸出更加美觀，我們可以用format來把字串格式化。<br/>
```python
"{} {}".format("hello", "world") # 不設置指定位置，按默認順序
# 'hello world'
"{0} {1}".format("hello", "world") # 設置指定位置
# 'hello world'
```
數字格式化<br/>

| 數字    | 格式    | 輸出           | 描述                        |
| ------- | ------- | -------------- | --------------------------- |
| 3.14159 | {:.2f}  | ‘3.14’ | 保留小數點後兩位            |
| 2.71    | {:.0f}  | ‘3’    | 不帶小數(四捨五入)          |
| 5       | {:x<4d} | ‘5xxx’ | 數字補x (填充右邊, 寬度為4) |
| 5       | {:x>3d} | ‘xx5’  | 數字補x (填充左邊, 寬度為3) |
| 3       | {:3d}   | ‘&ensp;&ensp;3’  | 右對齊 (默認, 寬度為3)       |
| 3       | {:<3d}  | ‘3&ensp;&ensp;‘  | 左對齊 (寬度為3)             |
| 3       | {:^3d}  | ‘&ensp;3&ensp;’  | 中間對齊 (寬度為3)           |
<br/>

### 資料型別
#### 數字（Number）
#### 字串（String）
#### 布林值（Boolean）
#### 列表（List）
```python
x = [1, 2, 3, 4, 5, 6]

#index 從 0 開始
print(x[0])     #[1]
print(x[3])     #[4]

print(x[-1])    #[6]

#[起始 index, 結束 index 但不包含]
print(x[:3])    #[1, 2, 3]
print(x[3:])    #[4, 5, 6]
print(x[1:5])   #[2, 3, 4, 5]
print(x[0:-1])  #[1, 2, 3, 4, 5]
print(x[-1:-1]) #[]
```
動態增加元素:
* ```list.append(x)```: 把變數x塞到list的最後面
* ```list.insert(i, x)```: 把變數x塞到i這個位置上
* ```list.pop()```: 把list的最後一格丟掉
* ```list.pop(i)```: 把list的第i格丟掉
* ```list.remove(x)```: 會把第一個出現的變數x拿掉
* ```list.clear()```: 把list內的資料全部清光光
* ```list.sort()```: 把list內的資料由小到大排列

與常見函數的結合:
* ```max(list)```: 找出list中最大值
* ```min(list)```: 找出list中最小值
* ```sum(list)```: 找出list數字總和

#### 元組（Tuple）
Tuple 類似於 List，比較大差別在於宣告後不能修改。<br/>
```python
tuple1 = (1, 2, 3, 4, 5)
tuple1[0] = 9
# TypeError: 'tuple' object does not support item assignment
```

#### 字典（Dictionary）
字典存的資料是一個鍵(key)對應一個值(value)。<br/>
```python
dict1 = { 'Mark': 70, 'Jack': 40 }
print(dict1['Mark'])

print(dict1.keys())     # 所有鍵值組成的 list
print(dict1.values())   # 所有值組成的 list
print(dict1.items())    # 所有鍵值組成的 tuple of list
```
* ```dict={}```: 建立空的dict
* ```del dict[key]```: 刪除特定的key-value pari
* ```dict[key]=value```: 如果key不存在，會增加這組K-V；如果key已存在，會更新這組K-V

取出字典資料作法有兩種：
* ```dict[key]```: 這個做法相對不安全，key如果不存在的話就會出現KeyError。
* ```dict.get(key, default_value)```: 是比較安全的作法，如果key不存在的話就會回傳 default_value。
```python
dict1 = { 'Mark': 70, 'Jack': 40 }

print(dict1.get('Andy', "找不到"))
# 找不到
print(dict['Andy'])
#　TypeError: 'type' object is not subscriptable
```

#### 集合（Set）
set 是一組無序且沒有重複的元素。
```python
set1 = {'apple', 'orange', 'apple', 'banana'}
print(set1)
# {'orange', 'banana', 'apple'}
```
<br/>

### 函式（function）
函式是重複使用的程式區塊，有輸入輸出。在 Python 中我們會使用 def 來定義函式：
```python
def sum(x, y):
    return x + y

num = sum(1, 3)
print(num)      #4
```
<br/>
