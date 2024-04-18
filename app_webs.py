from flask import Flask

app = Flask(__name__)

# Define base URL and port
BASE_URL = 'http://localhost'
PORT = 5000  # Change this to your desired port number

@app.route('/trigger-script', methods=['POST'])
def trigger_script():
    # Add code here to trigger your Python script
    # For example, you can execute a Python script using subprocess
    # Replace the following line with your actual code
    return 'Python script triggered successfully ashish '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
