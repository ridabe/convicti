from app import app
from app.Routes import routes

app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    app.run()
