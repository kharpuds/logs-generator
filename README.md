# logs-generator

### Problem Statement
Consider a monitoring system, which monitors 1000 servers. Each server has 2 CPUs. Each server generates a log for CPU usage every minute.

The format is like this:

Timestamp      IP                     cpu_id usage

1414689783    192.168.1.10   0          87

1414689783    192.168.1.10   1          90

1414689783    192.168.1.11   1          93


(1) Write a simulator to generate the logs for one day, say 2014-10-31, just use random numbers between 0% to 100% as CPU usage. The generator should write data to files in a directory. The timestamp is Unix time.


(2) Create a command line tool which takes a directory of data files as a parameter and lets you query CPU usage for a specific CPU in a given time period. It is an interactive command line tool which read a user’s commands from stdin.

The tool should support two commands. One command will print results to stdout. Its syntax is QUERY IP cpu_id time_start time_end. Time_start and time_end should be specified in the format YYYY-MM-DD HH:MM where YYYY is a four digit year, MM is a two digit month (i.e., 01 to 12), DD is the day of the month (i.e., 01 to 31), HH is the hour of the day, and MM is the minute of an hour. The second command to support is EXIT. It will exit the tool.

The tool may take several minutes to initialize, but the query result should be returned within 1 second.

### How to run:
1. generate.py
	Run this command in the command line interface: python generate.py <data_path>
	Eg: python generate.py temp.txt

2. query.py
	Run this command in the command line interface: python query.py <data_path>
	Eg: python query.py tmp.txt
	Then enter the query for eg: QUERY 192.168.1.10 1 2014-10-31 00:00 2014-10-31 00:05
	You will see the output like this, for eg: [('2014-10-31 00:00', '12%'), ('2014-10-31 00:01', '95%'), ('2014-10-31 00:02', '41%'), ('2014-10-31 00:03', '60%'), ('2014-10-31 00:04', '24%')]
	
### Implementation:
1. generate.py
The code takes in the datapath of the file from the input entered by the user in the CLI and creates a file in that path. It then appends these headers to the file: ['Timestamp', 'IP', 'cpu_id', 'usage'].
Considering 24 hours and 60 minutes, timestamp is generated for the date 2014-10-31. For each timestamp, I consider a combination of network IDs that go from 192.168.0.0 to 192.168.9.99. This generates 1000 server IPs. For each server, I set CPU ids to be 0 and 1. 
All these columns get written in the file mentioned in the datapath

2. query.py
I have used a nested dictionary. The outer dictionary stores a combination of IP address and CPU ID as the key. This key maps to an inner dict. 
The inner dictionary has timestamp as the key which maps to a tuple of date-time and corresponding CPU usage value. This is makes it easier to print the values in the required format when fetching query results. 
When a query is run, the code checks for out of bound date, out of bound IP address, whether end date is greater than start date or not and invalid number of query parameters. 
If these checks pass, the code does a lookup in the dictionary for the requested IP address and CPU ID. The code also converts the date time into timestamp for both the start and end times and finds the time difference. The code then iterates through values from start date till end date and returns tuples of corresponding date time and CPU usage pairs. These tuples are stored in the dictionary.

