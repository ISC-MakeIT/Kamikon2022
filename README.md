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
