from ext import app

if __name__ == '__main__':
    from routes import home, about, services,news, contact, profile
    app.run(debug=True)


