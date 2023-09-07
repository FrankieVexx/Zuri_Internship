from flask import *
import json, time, datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def APIend():
    # Get slack name and track from the url
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    # Getting current date and time information
    current_day = datetime.datetime.now().strftime("%A")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Github information
    github_repo_url = "https://github.com/FrankieVexx/Zuri_Internship"
    github_file_url = f'{github_repo_url}/apiend.py'
    
    
    data = {"slack_name": "FrankieVexx",
        "current_day": "Thursday",
        "utc_time": "2023-09-07T09:33:05Z",
        "track": "backend",
        "github_file_url": "https://github.com/FrankieVexx/Zuri_Internship/apiend.py",
        "github_repo_url": "https://github.com/FrankieVexx/Zuri_Internship",
         "status_code": "200"
    }
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)