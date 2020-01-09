# from flaskblog import create_app, prr

# app = create_app()
# g=prr()
# print(g)

# if __name__ == '__main__':
#     app.run(debug=True)


from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
