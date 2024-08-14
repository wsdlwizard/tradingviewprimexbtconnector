from flask import Flask, request, jsonify
import csv,os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    file_path1 = "c:\\data\\lorenze.csv"
    
    # Specify the path to the file in the shared folder
    #file_path = os.path.join(network_file, "lorenze.csv")
    if request.method == 'POST':
        data = request.json
        send_message(f"Received webhook data: {data}")
        # Add your custom processing logic here
        with open(file_path1,"a",newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[data['ticker'],data['price'],data['action'],data['interval'],datetime.utcnow()]])
       
            
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid method'}), 400

def send_message(data):
    print("This is a test")
    print(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

#this is the format of the message that will be sent to the webhook
'''{
  "ticker": "{{ticker}}",
  "price": "{{close}}",
  "time": "{{time}}",
  "alert_name": "{{alert_name}}",
  "condition": "Buy"  // or "Sell" based on the alert condition {{condition}}
}'''


#https://pypi.org/project/advanced-ta/
