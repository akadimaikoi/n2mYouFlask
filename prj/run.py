# prj/run.py

from app import create_app

projetct = create_app()

if __name__ == '__main__':
    app.env = "development"
    app.run(debug=True)
