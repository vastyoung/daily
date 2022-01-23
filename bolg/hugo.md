# `Hugo笔记:`

`hugo new posts/my-first-post.md`: 新建

`git remote add origin git@github.com:vastyoung/vastyoung.github.io.git` 添加远程仓库

`hugo --baseUrl="https://vastyoung.github.io/" --buildDrafts`

`hugo --buildDrafts`

`hugo server --buildDrafts --bind=0.0.0.0 --baseURL="192.168.0.108"` 启动服务器

## 禁用LiveReload

```test
hugo server --watch=false

hugo server --disableLiveReload
```
