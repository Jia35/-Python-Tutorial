## Python 題目測試~

[[回首頁]](../README.md)<br/>

----
1. 寫個字串連接，並讓使用者輸入兩個字串，輸出字串連接結果。<br/>
<img src="./image/problem011.png" width = "80%" alt="problem011"/><br/>

2. 產生字三角形(1)由小到大；(2)由大到小；(3)由使用者輸入數字<br/>
<img src="./image/problem021.png" width = "80%" alt="problem021"/><br/>
<img src="./image/problem022.png" width = "80%" alt="problem022"/><br/>

3. 做一個簡單的加法，讓使用者輸入A跟B，結果輸出A+B。<br/>
<img src="./image/problem031.png" width = "80%" alt="problem031"/><br/>

4. 延續上一題，如果結果大於等於100，則輸出’總和大於等於100’；<br/>
如果結果大於等於10但不到100，則輸出’總和大於等於10’；<br/>
如果結果小於10，則輸出’總和小於10’。<br/>
<img src="./image/problem041.png" width = "80%" alt="problem041"/><br/>

5. 輸入數字num，利用for迴圈計算1加至num的總和。<br/>
<img src="./image/problem051.png" width = "80%" alt="problem051"/><br/>

6. 輸入一個整數num，while迴圈判斷累加到多少會超過num。<br/>
(ex:num=4  1+2+3=6  6超過num)<br/>
<img src="./image/problem061.png" width = "80%" alt="problem061"/><br/>

7. 判斷是不是閏年。是的話輸出”閏年”；不是的話輸出”平年”。<br/>
(提示:西元年被4整除且不被100整除，或被400整除者即為閏年)<br/>
<img src="./image/problem071.png" width = "80%" alt="problem071"/><br/>

8. 簡單的計算機，第一步讓使用者輸入想要做的符號運算，比如「+, -, *, /」，第二步讓使用者輸入'整數1'和'整數2'，最後讓這兩個整數進行運算。<br/>
如果輸入的運算符號不是「+, -, *, /」，便輸出「錯誤」。<br/>
<img src="./image/problem081.png" width = "80%" alt="problem081"/><br/>

9. 使用for迴圈顯示出99乘法表。<br/>
(提示:可以用format 格式化函數美化)<br/>
<img src="./image/problem091.png" width = "80%" alt="problem091"/><br/>

10. 鉛筆一支 5 元，一打 50 元。小明需要幫班上每位同學買一枝鉛筆，請問要多少錢？<br/>
(鉛筆數量一定等於班上的人數)使用者輸入班級人數。<br/>
<img src="./image/problem101.png" width = "80%" alt="problem101"/><br/>

11. 使用者可一直輸入數字，直到輸入0則停止輸入，並輸出排序後的結果。<br/>
(提示:排序可用list.sort())<br/>
<img src="./image/problem111.png" width = "80%" alt="problem111"/><br/>

12. 輸入三筆數字，如果可以排成三角形輸出’O’，否則輸出’X’。<br/>
(如需排序可用list.sort())<br/>
<img src="./image/problem121.png" width = "80%" alt="problem121"/><br/>

13. 列印出所有的“水仙花數”，所謂“水仙花數”是指一個三位元數，其各位數字立方和等於該數本身。<br/>
   例如：153是一個“水仙花數”，因為153=1的三次方＋5的三次方＋3的三次方。<br/>
   (利用for迴圈控制100-999的數，每個數分解出個位，十位，百位。)<br/>
<img src="./image/problem131.png" width = "80%" alt="problem131"/><br/>

14. 一球從100米高度自由落下，每次落地後反跳回原高度的一半；再落下，求它在第10次落地時，共經過多少米？第10次反彈多高？<br/>
<img src="./image/problem141.png" width = "80%" alt="problem141"/><br/>

15. 3025這個數字有個巧合，如果你將這數字看成字串，將其分為兩半(30和25)，則其和平方(30+25)^2 = 3025<br/>
又變成原來的數字了。<br/>
你的題目是找出這種類似的巧合數字出來，你的程式要讀取一個位數(2、4、6、或8)，然後找出該位數的所有類似巧合的數字。<br/>
例如4位數，從0000到9999。請注意，0也要算在內，也就是說0001也等於(00+01)^2，也是4位數中的巧合數。<br/>
<img src="./image/problem151.png" width = "80%" alt="problem151"/><br/>

16. 斐波那契數列<br/>
Fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……<br/>
<img src="./image/problem161.png" width = "20%" alt="problem161"/><br/>
顯示前10個斐波那契數列<br/>
<img src="./image/problem162.png" width = "80%" alt="problem162"/><br/>

17. 從鍵盤輸入一個字串，將小寫字母全部轉換成大寫字母，然後輸出到一個“test.txt”中保存。<br/>
<img src="./image/problem171.png" width = "80%" alt="problem171"/><br/>
<img src="./image/problem172.png" width = "40%" alt="problem172"/><br/>

18. 有一個"problem.txt"檔案內有一長串亂碼，請從亂碼中找出英文字母，包括大小寫。<br/>
<img src="./image/problem181.png" width = "80%" alt="problem181"/><br/>

19. ISBN(International Standard Book Number)是一種世界共通的書籍編碼方法，世界上任何一本書籍之出版，皆有著唯一的一組ISBN碼。此碼由十個位數組成，每一位數可以為0~9的任何一個數字，或者為X，代表此位數為10。<br/>
試寫出一個程式來判斷所輸入的ISBN碼是否為合法的。<br/>
其判斷方法如下，首先，將此ISBN碼的十個位數分開，自左而右依次為第一位數，第二位數至第十位數，接著進行第一次的累加，使得第二位數成為第一位數到第二位數的和，第三位數為第一位數到第三位數的累加和，第十位數為第一位數到第十位數的累加和；進行完第一次的累加和後，接著再依照相同之方法進行第二次的累加動作，我們稱此時最後所求得之累加和為此ISBN碼之識別碼，倘若此識別碼為11的倍數，則此ISBN碼為合法的，故請輸出YES，反之請輸出NO。<br/>

| 函數         |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISBN碼       | 0   | 1   | 3   | 1   | 6   | 2   | 9   | 5   | 9   | X   |
| 第一次累加和 | 0   | 1   | 4   | 5   | 11  | 13  | 22  | 27  | 36  | 46  |
| 第二次累加和 | 0   | 1   | 5   | 10  | 21  | 34  | 56  | 83  | 119 | 165 |

經由計算可得其識別碼為165，乃是11之倍數，故此為一合法之ISBN碼，因此應該要輸出YES於螢幕上。<br/>

<br/>
