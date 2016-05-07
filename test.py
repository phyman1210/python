# coding: utf-8
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

