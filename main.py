from app import create_app, db

app = create_app()

with app.app_context():
    from app.utils.init_load_db import init_load_db

    init_load_db(db)

if __name__ == "__main__":
    app.run(debug=True)
