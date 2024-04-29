import os
import json
from ast import literal_eval

def process_log_file(log_file):
    parsed_logs = []
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        parsed_logs.append(parse_log_line(line))
    
    return parsed_logs

def parse_log_line(line):
    print("parsing log line:",line)
    json_content = line.split('{', 1)[1].rsplit('}', 1)[0]
    print("json_content:",json_content)
    
    data_dict = literal_eval("{" + json_content + "}")
    # Parse the JSON content
    return {
        'log_data': data_dict
    }
def main(logs_folder, output_file):
    all_logs = []
    for filename in os.listdir(logs_folder):
        if filename.endswith('.log'):
            log_file = os.path.join(logs_folder, filename)
            all_logs.extend(process_log_file(log_file))
    
    json_logs = json.dumps(all_logs, indent=4)
    
    with open(output_file, 'w') as f:
        f.write(json_logs)
        
        
# PROJECTS\PROJ1\data_logs
if __name__ == "__main__":
    logs_folder = 'PROJECTS\PROJ1\data_logs'
    output_file = 'api_response_2.json'
    main(logs_folder, output_file)

    # Load the JSON data from the file
    filename = 'api_response_2.json'  # Replace 'your_json_file.json' with the path to your JSON file
    with open(filename, 'r') as f:
        data = json.load(f)
        
    for item in data[:5]:
        log_data = item['log_data']
        print("ID:", log_data['id'])
        print("Value:", log_data['value'])
        print("Categories:", log_data['categories'])
        print("Created At:", log_data['created_at'])
        print("Updated At:", log_data['updated_at'])
        print("Icon URL:", log_data['icon_url'])
        print("URL:", log_data['url'])
        print()