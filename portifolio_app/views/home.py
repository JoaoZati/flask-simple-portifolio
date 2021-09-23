from portifolio_app import app


@app.route('/')
def home():
    return "<center><p>Home</p></center>"
