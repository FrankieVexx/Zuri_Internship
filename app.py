from flask import *
import json, time, datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def APIend():
    # Get slack name and track from the url
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    # Getting current date and time information
    current_day = datetime.datetime.now().strftime("%A")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Github information
    github_repo_url = "https://github.com/FrankieVexx/Zuri_Internship"
    github_file_url = f'{github_repo_url}/app.py'
    
    
    data = {"slack_name": "Frankie",
        "current_day": "Thursday",
        "utc_time": "2023-09-07T21:55:45Z",
        "track": "backend",
        "github_file_url": "https://github.com/FrankieVexx/Zuri_Internship/app.py",
        "github_repo_url": "https://github.com/FrankieVexx/Zuri_Internship",
         "status_code": "200"
    }
    
    data["current_day"] = current_day
    data["utc_time"] = current_time
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)