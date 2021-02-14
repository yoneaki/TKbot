# TKbot
RTAラジオ略して、あるらじで使われるタイムキーパーbotです。
## コマンド一覧
- !isrunning
  - botが起動しているか確認するためのコマンドです。<br>コマンドを打つと"I'm ready!"と返してくれます。
- !settk base_interbal shorter_time dead_time
  - タイマーをセットするときに使用します。<br>使用する際はコマンド、数字それぞれにスペースを一つずつ設けてください。
    - "base_interval" "shorter_time"に達するまでのチャット送信のスパン
    - "shorter_time" 1分刻みになるタイミング
    - "dead_time" 終了予定時刻、強調表示
  - 使用例 !settk 2 5 10<br>動作 開始から2分おきに経過時間をチャットに送信し、5分経過後は1分おきに送信する。<br>10分に達したとき強調表示を用いてチャットが送信される。
- !starttk
  - "!settk"でセットした時間を元にタイマーをスタートする。
- !endtk
  - タイマーを停止させる
&copy; 2021 yoneaki
