## main.py
from app import app

def main():
    app.run(debug=1, host="::", port="5005")

if __name__ == "__main__":
    main()
