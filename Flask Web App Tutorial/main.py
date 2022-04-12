from website import create_app

app = create_app() 

# only runs when this is executed, not imported
if __name__ == '__main__':
    app.run(debug=True)


# command to run the app:    python "Flask Web App Tutorial\main.py"