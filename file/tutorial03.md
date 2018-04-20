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

#### 元組（Tuple）
Tuple 類似於 List，比較大差別在於宣告後不能修改。<br/>
#### 字典（Dictionary）
字典存的資料是一個鍵(key)對應一個值(value)。<br/>
```python
dict1 = { 'Mark': 70, 'Jack': 40 }
print(dict1['Mark'])

print(dict1.keys())     # 所有鍵值組成的 list
print(dict1.values())   # 所有值組成的 list
print(dict1.items())    # 所有鍵值組成的 tuple of list
```

#### 集合（Set）
<br/>
### 函式（function）
函式是重複使用的程式區塊，有輸入輸出。在 Python 中我們會使用 def 來定義函式：
```python
def sum(x, y):
    return x + y

num = sum(1, 3)
print(num)      #4
```

### File(文件)
