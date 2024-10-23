from flask import Flask, Response
import os

app = Flask(__name__)

# Function to load cheat sheet from a text file
def load_cheat_sheet(command):
    file_path = f"{command}.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return None

@app.route('/<command>', methods=['GET'])
def get_cheat_sheet(command):
    command = command.lower()  # Normalize the command to lowercase
    cheat_sheet = load_cheat_sheet(command)

    if cheat_sheet:
        return Response(cheat_sheet, mimetype='text/plain')
    else:
        return Response("Cheat sheet not found for the specified command.", status=404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
