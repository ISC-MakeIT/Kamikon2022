from django.db import models
from django.utils import timezone

# Create your models here.

#ユーザーテーブル
class Users(models.Model) :
    userid = models.CharField(primary_key=True, max_length=100)#ユーザーid 主キー
    usertype = models.BooleanField()#教師だったらFalse、生徒だったらTrue
    username = models.CharField(max_length=255)#氏名。特に説明なし
    password = models.CharField(max_length=100)#パスワード

#課題の基本情報テーブル    
class Kadai(models.Model) :
    kadai_id = models.CharField(primary_key=True, max_length=200)#この課題IDを入力することで課題の提出義務が生じる。どのユーザーに提出義務が生じているかは別テーブル[KadaiAdmin]で定義。アルファベットと数字ランダムで何桁かは検討中
    created_date = models.DateTimeField(default=timezone.now)#いつ作ったか。これは必要でしょう
    submission_deadline = models.DateTimeField()#提出期限
    kadai_desc = models.TextField() #課題についての説明。改行は/nで識別。
    question_cnt = models.IntegerField()#問題数

#誰がどの課題を提出しないといけないのかはこのテーブルでわかる
class KadaiAdmin(models.Model) :
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
    
#課題の問題の詳細
class KadaiQuestion(models.Model) :
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)#主キーではないことに注意！
    question_num = models.IntegerField()#問題の番号
    question_state = models.TextField()#問題文
    question_type = models.CharField(max_length=100)#問題の解答形式。(text, radio, checkbox, textarea, file...)
    is_multiple = models.BooleanField(blank=True)#選択形式の場合、複数選択が可能か否か
    
#選択問題だった際の項目
class QuestionItem(models.Model) :
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
    question_num = models.ForeignKey(KadaiQuestion, on_delete=models.CASCADE)
    question_item_index = models.CharField(max_length=20)#ア、イ、ウ・・・等といった選択肢の添字
    question_item_content = models.TextField()#選択肢のテキスト。入力する場所はテキストエリアで
    multiple_points = models.BooleanField(blank=True) #複数選択の場合、Trueだったらすべて選択した場合にしか点数を上げない。Falseだったら一つでも正解していたらその選択肢に用意されていた得点が入る。
    is_appropriate = models.IntegerField() #その項目が正解の場合はその項目(がある問題)につけている配点を、間違いの場合は0が入るようにする

#記述問題だった際の正解キーワード。    
class QuestionKeyword(models.Model) :
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
    question_num = models.ForeignKey(KadaiQuestion, on_delete=models.CASCADE)
    keyword = models.TextField(blank=True) #「どれか一つでも入力されていたら正解」という感じにしたい場合は、ひとつの単語を/で区切る。「問題の解答に何かが入力さえされていれば正解」という風にしたい場合は、NULLを入れる
    point = models.IntegerField() #配点
    
#生徒が回答した内容
class Answer(models.Model) :
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
    question_num = models.ForeignKey(KadaiQuestion, on_delete=models.CASCADE)
    question_answer = models.TextField(blank=True)
    question_answer_file = models.FileField(upload_to='uploaded_file/%Y/%m/%d', blank=True)