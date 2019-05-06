from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

app.run(debug=True)

#运行前先到python3.7里执行>>> from app import db
#>>> db.create_all()创建数据库