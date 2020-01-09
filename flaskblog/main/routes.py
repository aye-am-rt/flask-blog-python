from flask import render_template, request, Blueprint
from flaskblog.models import Post

main= Blueprint('main', __name__)



# to create database go to directory where you want to create database by defalult current directory, and 
# >>>python >>> from app import db >>> db.create_all() 
# >>> from app import User, Post
# >>> user_1=User(username='corey', email='c@test.com', password='password')
# >>> db.session.add(user_1)
# >>> db.session.commit()
# >>> User.query.all()
# [User('corey', 'c@test.com', 'default.png')]
# >>> User.query.first()
# User('corey', 'c@test.com', 'default.png')
# >>>User.query.filter_by(username='Corey').all()
# >>> db.drop_all()


# posts = [{'author':'ritesh tiwari','title':'blog post 1','content':'first post content','date_posted':'08 december 2019'},
# {'author':'jane doe','title':'blog post 2','content':'second post content','date_posted':'09 december 2019'}]


@main.route('/')
@main.route('/home')
def index():
    ##posts=Post.query.all()
    # print(len(posts))
    # posts.extend(dummyList)
    # print("after adding dummy list",len(posts))
    page=request.args.get('page', 1, type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('index.html', posts=posts)


# >>> from flaskblog.models import Post 
# >>> posts=Post.query.all()
# >>> for post in posts:
# ...     print(post)

# >>> posts=Post.query.paginate()
# >>> posts
# <flask_sqlalchemy.Pagination object at 0x000001EB50501E80>
# >>> dir(posts)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'has_next', 'has_prev', 'items', 'iter_pages', 'next', 'next_num', 'page', 'pages', 'per_page', 'prev', 'prev_num', 'query', 'total']
# >>> posts.per_page
# 20
# >>> posts.page
# 1
# >>> posts.per_page=10
# >>> posts.per_page
# 10



@main.route('/about')
def about():
    return render_template('about.html',title='About')
