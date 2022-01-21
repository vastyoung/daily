# 配置ssh key

## 生成新的 SSH 密钥

1. 打开我们的终端

2. 创建新的 SSH 密钥:
    `ssh-keygen -t ed25519 -C "your_email@example.com"` #最后替换成我们的GitHub 电子邮件地址

3. 创建完成会提示我们以下内容(按回车键, 这将接受默认文件位置):

    ```test
    Enter a file in which to save the key (/c/Users/you/.ssh/id_algorithm):[Press enter]
    ```

4. 会提示我们输入安全密码(我们回车即可):

    ```test
    Enter passphrase (empty for no passphrase): [Type a   passphrase]
    Enter same passphrase again: [Type passphrase again]
    ```

5. 我们会生成两个文件一个公钥一个私钥(他们在 .ssh 目录里面)；

6. 查看我们的公钥:
    `cat ~/.ssh/id_ed25519.pub`

7. 把我们的公钥添加到 github 上面；

8. 进入我们的 github 点击设置,然后点击 SSH 和 GPG 密钥,点击新建 SSH 密钥，会弹出两个输入框，第一个输入框中我们想要的标题，第二个输入框中填写我们复制过来的公钥即可。

## 哪一个文件是不能泄露给外界的?

不能泄露给外界的是没有带.pub的那个文件。(公钥和私钥文件名是差不多的，公钥比私钥多了个.pub结尾)

## 能够泄露给外界的是哪个文件?

能够泄露给外界的是文件以.pub结尾的文件。

## 上传到 github 的是哪个文件?

上传到 github 的是以.pub结尾的文件。

## github 是只能上传一个 key 还是可以上传多个key?

github 是可以上传多个key的。

公钥和私钥的作用：对我们的信息进行加密，把我们想要公开的信息公开，不想要公开的信息隐藏起来。
