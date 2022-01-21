# flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) 是一个使用 Python 所编写的轻量级 Web应用框架。

## 安装 flask

### 创建一个虚拟环境

我们通过以下几条命令来创建虚拟环境:

```test
mkdir myproject
cd myproject
python3 -m venv venv
```

### 激活我们的虚拟环境

我们用一下命令激活我们的环境:

`. venv/bin/activate`

### 安装Flask

我们在虚拟环境中可以通过以下命令即可安装flask:
`pip install Flask`

## 快速入门(一个最小的应用程序)

```python

from flask import Flask #我们导入了Flask类

app = Flask(__name__)   #我们创建了这个类的一个实例

@app.route("/")         #我们使用route()装饰器告诉 Flask 哪个 URL 应该触发我们的函数
def hello_world():
    return "<p>Hello, World!</p>"

```

运行程序之前需要我们先配置flask的环境变量:

```bash
export FLASK_APP=hello  #配置环境变量
$ flask run             #启动flask
 * Running on http://127.0.0.1:5000/
```

我们现在运行的服务器现在只能自己能访问到，要想外部(其他人)也能访问我们的服务器只需要执行以下命令即可:

`flask run --host=0.0.0.0`
