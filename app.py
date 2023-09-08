import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def APIend():
    # Get query parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    # Getting current date and time information
    current_day = datetime.datetime.now().strftime("%A")
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # GitHub information
    github_repo_url = "https://github.com/FrankieVexx/Zuri_Internship"
    github_file_url = f'{github_repo_url}/blob/main/app.py'
    
    #JSON response
    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)