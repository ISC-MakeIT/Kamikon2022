# Kamikon2022

## clone方法
以下urlを参考に仮想環境を作成してください。  
尚、既にこのチュートリアルを終えている人は、チュートリアル内で作成した仮想環境内でクローンをお願いします。

https://tutorial.djangogirls.org/ja/django_installation/

仮想環境内にて以下のコマンドを実行。

```
git clone git@github.com:ISC-MakeIT/Kamikon2022.git
```

しかしこれでは動かせないので、djangoその他諸々サービスをインストールすべく、  
Kamikon2022ディレクトリ内で以下のコマンドを実行。

```
pip install -r requirements.txt
```

## html, css, js, imgの扱い
### html
Kamikon2022/templates/pls下にて作成してください。
ページことにフォルダ分けしたほうがいいかもしれません。
divでのグループ分けを徹底してくださいますようお願いします。

### css
Kamikon2022/pls/static/css下にて、scssファイルで作成してください。

### js
Kamikon2022/static/js下にて作成してください。
scss記法はこちら↓
https://qiita.com/nchhujimiyama/items/8a6aad5abead39d1352a
自動でコンパイルするようなので、特にコマンドを打つ必要もないようです。

### img
kamikon2022/static/img下に置いてください。

## 基本設定
settings.pyではなく、local_settings.pyをsettings.pyと同じディレクトリ下に新規で作成してください。
何を書けばいいかをテキストデータとして別途神コンのHackMDにて添付します。そのテキストをコピペしてください。

manage.pyは今現在local_settings.pyで動くように設定されています。

## DB
models.pyに、どのように使うかなど詳細情報が記載してあります。
### ユーザー情報(Users)
```
{
    "userid": "qawsedrftgyhujikolp",
    "usertype": "true",
    "username": "朝比奈一麒",
    "password": "qawsedrftgyhujikolp"
}
```

### 課題の基本情報(Kadai)
```
{
    "kadai_id": "qawsedrftgyhujikolp",
    "created_date": "2022,10,1",
    "submission_deadline": "2022,10,1",
    "kadai_desc": "数学プリント何番を全問解いた後、全体が映るよう写真を撮影し、その画像データをこちらに送信してください。なるべくはっきり移るようにしてください。あまりにも不明瞭な場合、送りなおすよう指示をすることがあります。",
    "question_cnt": 1
}
```

### 課題の提出義務(KadaiAdmin)
```
{
    "userid": "qawsedrftgyhujikolp",
    "kadai_id": qawsedrftgyhujikolp"
}
```

### 課題の問題の詳細(KadaiQuestion)
```
{
    "kadai_id": "qawsedrftgyhujikolp",
    "question_num": "1",
    "question_state": "ななよさんは8:05AMに学校に着き、2:30PMに学校を出ました。しんたろう君が学校にいた時間はどのくらいですか？",
    "question_type": "textarea",
    "is_multiple": NULL
}
```

### 選択問題だった際の各項目(QuestionItem)
```
{
    "kadai_id": "qawsedrftgyhujikolp",
    "question_num": "1",
    "question_item_index": "ア",
    "question_item_content": "選択肢",
    "multiple_points", NULL,
    "is_appropriate", 3
}
```

### 記述問題だった際の正解キーワード(QuestionKeyword)
```
{
    "kadai_id": "qawsedrftgyhujikolp",
    "question_num": "1",
    "keyword": "推敲/非常に/santamonica",
    "point": 5
}
```

### 生徒の回答(Answer)
```
{
    "userid": "qawsedrftgyhujikolp",
    "kadai_id": "qawsedrftgyhujikolp",
    "question_num": "1",
    "question_answer": "ア"
    "question_answer_file": NULL
}
```

## タスク進め方
### issueの作成
- メニューから、「issues」を選択
- 「new issue」を押し、終わらせたい課題の目標と説明を記入し、submit

### ブランチの作成&切替
- ブランチ名は、「feature-{issue番号}」とする
- ```git switch -c feature-{issue番号}```のコマンドを実行してブランチを切り替える

後はいつもの通り

### WARNING!!
- ***ブランチの切替はコードの変更がない状態で行うこと***
- ***定期的にgit pull origin masterコマンドを実行する***
- ***変更をプッシュしていないけどどうしてもブランチ移行などしたいときは、変更を退避させておく(詳細の説明は省く)***