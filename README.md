# flask 

在当前文件夹输入 flask shell进入 python flask shell  
## 数据库  
注册，编辑等需要创建数据库  

\>> from app import db  
\>> db.create_all()

如果有两个要添加到数据库的新字段，因此第一步是生成迁移脚本：
(对应文件夹或者添加环境变量)  

$ flask db migrate -m "new fields in user model"

$ flask db upgrade


I hope you realize how useful it is to work with a migration framework. Any users that were in the database are still there, the migration framework surgically applies the changes in the migration script without destroying any data.

可以用navicat连接app.db，但是单独下载.db好像不行  
查询：
使用db.session.query()   

邮件的坑：
bash: syntax error near unexpected token `newline'

原因： 
符号「<」和「>」　是重定向字符，是特殊字符有特殊意义。

解决： 
去掉两个尖括号【<】和【>】。  
learned from:
> https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
