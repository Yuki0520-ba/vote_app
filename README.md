# vote_app

## このwebアプリケーションについて
所属する軽音サークルで使用する投票機能を持つwebアプリケーション。


## 機能
- 出演バンドの登録
- 出演バンド情報の編集
- 出演バンドの削除
- 投票
- 投票結果確認
- 全出演バンド情報の削除



## 技術について
- python 
- django(webフレームワーク)
- PostgresSQL(データベース)
- Heroku(デプロイ先)

## 課題
現在のままでは1人で何回も投票ができてしまうという問題点がある。  
今後はこの問題を回避するためにオリジナルのユーザーモデルを作成し、それを用いてログインさせることで回避していきたい。

