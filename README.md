## PythonTeX Example

## Installation (windows)

TeX Live <http://www.tug.org/texlive/acquire-netinstall.html>

```
\texlive\2016\bin\win32\pythontex.exe
```

python3 <https://www.python.org/downloads/windows/>

```
pip install matplotlib   
pip install pygments  
```

## Usage

```
python.exe probability.py

pdflatex.exe -synctex=1 -interaction=nonstopmode BirthdayProblem.tex
pythontex.exe BirthdayProblem.tex
pdflatex.exe -synctex=1 -interaction=nonstopmode BirthdayProblem.tex
```

```
pdflatex.exe -synctex=1 -interaction=nonstopmode TrigonometricTable.tex
pythontex.exe TrigonometricTable.tex
pdflatex.exe -synctex=1 -interaction=nonstopmode TrigonometricTable.tex
```
# 
***

### in japanese
# 

### 誕生日問題
#### probability.py
n人の中に同じ誕生日の人がいない（つまり、n人の誕生日がすべて異なる）  
確率を求める関数 distinct_prob(n) を定義しています。  
n人の中に同じ誕生日の人がいる確率は 1 - distinct_prob(n) です。  
テレビのクイズ番組で、何度か出題されました。  
実行すると、1 - distinct_prob(n) ( n = 2, 3, ...,100 ) のグラフの pdf を作成し、表示します。xで終了。   
さらに、  
There are 40 persons in my class. The Birthday-Problem's probability is 0.891.  
と出力します。  
if __name__ == '__main__': 以下のコードは、他のプログラムから読み込まれたときは、実行されません。  
よく使う手です。  
このように、まず、python のプログラムを作成します。  

#### BirthdayProblem.tex
probability.py で定義した関数 distinct_prob をfrom probability import distinct_prob で読み込みます。  
授業クラスの人数を cnum に代入します。  
``` 
\py{'{:.03f}'.format(1-distinct_prob(cnum))} 
```
で cnum 人の中に同じ誕生日の人がいる確率を書き込みます。  
tex のコードのなかに、python のコードをすべて書き込む方法もありますが、    
python のコードをcopy, past する。  
初めの pdflatex で画像なしのエラーがでる。  
あまり自然ではありません。  
特別な事情がないのであれば、画像は事前に作成し、  
python のコードは、上記のように、import で取り込む。  
この場合は、この方法が best!  

### 三角比の表
#### TrigonometricTable.tex  
0 度から 90 度まで step 度刻みの「三角比の表」が作成できます。  
step=0.1 にすると、2段組10ページの表ができる。  
step=1.0 で小数点以下第4位表示にすると、 高校数学教科書によくある表ができます。  
近頃、このような「数表」も使いませんが、テスト時配布用としの利用価値はあります。  
```
print(r"{:4.1f}$^\circ$ & {:8.6f}  & {:8.6f} & {:8.6f}\\"
		.format(x10/10, math.sin(rad), math.cos(rad), math.tan(rad)))
```
のように、表(tabular)のコードを書き込んでいくだけです。   
one_page_print は、2段組み、左右半ページを作成する関数。    
マクロで書かれたものより、python の方が分かり易いと、思うのですが、如何でしょうか。  
※ math は標準ライブラリに含まれているので、pip でインスツールする必要はありません。    



