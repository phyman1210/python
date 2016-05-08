# coding: utf-8
# ↑日本語を入力するために必要
# コメント
# リスト:データが並んだもの
# タブル:データが並んだもの(変更ができない)
# セット:データが並んだもの(重複を許さない)
# 辞書:キーとバリューがペアになっているもの

msg = "hello world"
print msg

# 演算子
# + - * / // % **

print 10 / 3.0	
print 10 // 3
print 2 ** 3

# 日本語入力
# 'hello'
# u'こんにちは
# +:接続、*:リピート
# エスケープ / これを使えばいい感じにエスケープできる

print 'hello' + ' world'
print u'無駄' * 10
print '''<html lang="ja">
<body>
</body>
</html>'''

# 文字数:len
# 検索:find
# 切り出し:[]

s = 'abcdefghij'
print len(s)
print s.find('b')
print s.find('x')
print s[2]
print s[2:len(s)-1]


# 文字列
# 数値(int, float) <> 文字列(str)
print 5 + int('5')
age = 10
print 'I am ' + str(age) + ' years old!!' 


# リスト
sales = [255, 100, 350, 300]
print len(sales)
print sales[2]
sales[2] += 200
print sales[2]
print 100 in sales
print 150 in sales
print sales
list1 = range(3, 20, 3)
print list1

sales.sort()
print sales
sales.reverse()
print sales

d = '2016/1/1'
print d.split('/')
e = d.split('/')
print '-'.join(e)

a = (2, 5, 8) # タプル(tuple)(丸括弧)
print len(a)
b = a * 3
print b
c = list(b)
print c

# セット
g = set([1, 2, 3, 4, 3, 2])
print g
h = set([1, 2, 6, 7, 8])
print g - h # 差集合
print g | h # 和集合
print g & h # 掛けあわせ集合
print g ^ h # どちらかにしかない集合

# 辞書
sales = {'takeshi':100, 'tsuyoshi': 200}
sales['takeshi'] *= 3
print sales
print 'takeshi' in sales

print sales.keys()
print sales.values()
print sales.items()

# 文字列にデータを入れる
i = 10
j = 3.1415
k = 'takeshi'
l = {'tsuyoshi':100, 'chie':300}
print 'age: %d' % i
print 'age: %5d' % i
print 'age: %05d' % i
print 'price: %f' % j
print 'price: %.2f' % j
print 'name: %s' % k
print 'sales: %(tsuyoshi)d' %l
print '%d and %.2f' % (i, j)


# 条件分岐
score = 10
if score > 50:
	print str(score) + ' bigger then 50'
elif score == 50:
	print 'same score as 50'
else:
	print str(score) + ' less then 50'

# 省略形条件の書き方
print 'Good' if score > 30 else 'NG'

# ループ文
indicators = range(1, 10, 2)
print indicators
sum = 0
for indicator in indicators:
	sum += indicator
else:
	print sum

# breakを含むループ文
for i in range(10):
	print i
	if i == 3:
		break

# 辞書を使ったループ文 -> iterkeys, itervalues, iteritems
for key, value in l.iteritems():
	print 'key: %s value: %d' %(key, value)
for key in l.iterkeys():
	print 'key: %s' %key
for value in l.itervalues():
	print 'value: %d' %value

# whileを使ったループ文
n = 0
while n < 10:
	if n == 3:
		n += 1
		# continue
		break
	print n
	n += 1
else:
	print 'end'

# 関数
def hello():
	print 'hello!!'
hello()

def hello1(name, num = 3):
	print 'hello %s! ' %name * num
hello1('takeshi')
hello1('takeshi', 4)

def hello1(name, num = 3):
	return 'hello %s! ' %name * num
s = hello1('takeshi')
print s

# 変数のスコープ -> 関数内で定義した変数名は、関数名でのみ有効になる
# pass -> 関数内にpassを書くと、何もしないことを宣言することができる(何に使うのか分からないww)

# map -> リストの中の変数を関数に通す
def double(x):
	return x * x
print map(double, [2, 4, 8])
# mapと無名関数
print map(lambda x: x * x, [2, 4, 8])

# オブジェクト(変数と関数をまとめたもの)
# クラス:オブジェクトの設計図
# インスタンス:クラスを実体化したもの
class User(object):
	def __init__(self, name): # この辺りまでは決まり文句
		self.name = name
	def greet(self):
		print 'my name is %s' % self.name
bob = User('Bob')
tom = User('tom')
print bob.name
bob.greet()
tom.greet()

# クラスを継承する
class SuperUser(User):
	def shout(self):
		print 'my name is super %s' % self.name
alice = SuperUser('alice')
alice.greet()
alice.shout()

# モジュールを使う
# python documentにたくさん用意されているので、importして使う
import math, random
print math.ceil(5.2)
for i in range(5):
	print i
	print random.random()

from datetime import date
print date.today()