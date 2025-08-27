import sqlite3
import sys
import re
import datetime

CREATE_TABLE="""
CREATE TABLE web_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT,
    client_identity TEXT,
    user_id TEXT,
    timestamp INTEGER,
    request_line TEXT,
    status_code INTEGER,
    size INTEGER
);
"""

INSERT="""
INSERT INTO web_logs (ip_address,client_identity,timestamp,request_line,status_code,size) VALUES (?,?,?,?,?,?)
"""

LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - (\S+) \[(.*?)\] "(.*?)" (\d+) (\d+)'

def to_unixtime(date):
    parsed = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S %z")
    return datetime.datetime.timestamp(parsed)

def parse_log(line):
    match = re.match(LOG_PATTERN, line)
    if match:
        timestamp = to_unixtime(match.group(3))
        return {
            "ip_address": match.group(1),
            "client_identity": match.group(2),
            "timestamp": timestamp,
            "request": match.group(4),
            "status_code": int(match.group(5)),
            "size": int(match.group(6))
        }
    else:
        return None

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit(1)

filename = sys.argv[1]

con = sqlite3.connect("logs.db")
cur = con.cursor()
cur.execute(CREATE_TABLE)

try:
    with open(filename, 'r') as file:
        for line in file:
            log = parse_log(line)
            cur.execute(INSERT, list(log.values()))
        con.commit()
except FileNotFoundError:
    print(f"File not found: {filename}")
except Exception as e:
    print(f"An error occurred: {e}")

con.close()
# Below code converts data into output.csv

import sqlite3
import math

QUERY="""
SELECT COUNT(*),
   DATE(TIMESTAMP, 'unixepoch')
FROM   web_logs
GROUP  BY strftime('%d', TIMESTAMP, 'unixepoch'); 
"""

con = sqlite3.connect("logs.db")
cur = con.cursor()
res = cur.execute(QUERY)
results = res.fetchall()

output = ""
for result in results:
    number_of_instances = math.ceil(result[0] / 100)
    output += f"m5.large,{result[1]},{number_of_instances}\n"

with open("output.csv", "w") as file:
    file.write(output)

