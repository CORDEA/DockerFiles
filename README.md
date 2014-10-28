# DockerFiles

自分がdockerを扱う上で楽になるように作成したコマンドとDockerfile

## dockerun.py

```bash
docker run -it -u cordea -w /home/cordea --name hoge hoge/hoge
```
と打ち込むのが面倒になったため作成したコマンド

`python dockerun.py ...`でも勿論動きます。


#### 各オプションのデフォルト値

| Option         | Default       |
| -------------- | ------------- |
| user name      | huge          |
| working dir    | /home/huge    |
| container name | hoge          |


また、デフォルトで`-it`オプションが付くようになっています。
各オプションのデフォルト値を変更するために必要な箇所は`dockerun.py`の中にコメントで示してあります。

### コマンドとして利用する場合

#### Mac OS X

pathが通っている場所にdockerunの名前で保存して下さい。(私の場合は`/usr/local/bin/`に入れています)

```sh
mv dockerun.py /usr/local/bin/dockerun
chown root:wheel /usr/local/bin/dockerun
chmod 755 /usr/local/bin/dockerun

```

で、Terminalを立ち上げて

```sh
dockerun huge/hoge

```

のようにすればコマンドとして働きます


　
## Ubuntu/Dockerfile

ubuntuのDockerfileは私が使いやすいようにカスタムしたimageを作成します。

行っていることは以下の通りです。

1. apt-get update
* wget, zip, zsh, vim, python-pip のインストール
* percol のインストール
*  **huge** ユーザーの作成(`/home/huge`も同時に作成されます)
* sudo コマンドをパスワード無しで通せるように`sudoers`に上書き
* ユーザー変更, `/home/huge`に移る
* dotfiles.zipをダウンロード *1
* unzipで解凍, 展開
* dotfiles, dotfiles.zipを削除
* デフォルトのコマンドに`zsh`を指定して終了


*1:
dotfiles.zipは私が使用している`.vimrc`や`.percol.d`と言った設定ファイルを固めて自サーバーに置いているものです。
公開しておりませんので使用される場合、こちらは個々人で書き換えて下さい。