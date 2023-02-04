# Local_Chatbot_Messanger
## Python3によるchatbotの開発
### シーケンス図
![image](https://user-images.githubusercontent.com/101037787/216758174-1465bb09-307e-482d-a9fe-58549a08b0fa.png)

### server側の処理
<ol>
<li>socketシステムコールを用いてUDP用のソケットを作成</li>
<li>bindシステムコールを用いて使用するIPアドレスとポート番号を指定する</li>
（ここまででOS内部でパケットを受信する準備が完了）
<li>recvfromシステムコールを用いてclientからのmessageを待ち</li>
（サーバープログラムはreacvfromの引数から、受信したmessageの送り主（client）のIPアドレスとport番号を把握）
<li>sendtoシステムコールでclientへmessageを送信</li>
</ol>

### client側の処理
<ol>
<li>socketシステムコールを用いてUDP用のソケットを作成</li>
<li>sendtoシステムコールを用いてServerへmessageを送信</li>
<li>recvfromシステムコールでserverからmessageを受信</li>

### 主なソケットシステムコール一覧
|  システムコール  |  説明  |
| ---- | ---- |
|  socket()  |  ソケットの作成  |
|  close()  |  ソケットのクローズ  |
|  bind()  |  ソケットに自ホストのIPアドレスとポート番号を紐づける  |
|  recvfrom()  |  messageの受信を受け付ける（送信元のアドレスを返り値にする）  |
|  sendto()  |  送信先のアドレスを指定してmessageを送信  |

※messageの送受員はコネクションレス型
### 開発環境
python 3.10.9
