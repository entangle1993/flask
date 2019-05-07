# flask 
 
## 数据库  
注册，编辑等需要创建数据库  

\>> from app import db  
\>> db.create_all()

如果有两个要添加到数据库的新字段，因此第一步是生成迁移脚本：
(对应文件夹或者添加环境变量)  

$ flask db migrate -m "new fields in user model"

$ flask db upgrade


I hope you realize how useful it is to work with a migration framework. Any users that were in the database are still there, the migration framework surgically applies the changes in the migration script without destroying any data.

learned from:
> https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
