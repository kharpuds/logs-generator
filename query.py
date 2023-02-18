import sys
from datetime import datetime
import time

def main(args):
	# check for number of args
	if len(args) != 2:
		print("Incorrect args")
		exit(1)

	# Read logs and store the data in nested map. Each element has a key of server and cpu and its value is has key as timestamp and
	# value as a tuple of datetime and cpu usage (to be printed). This will take time but will help us to fetch data quickly.
	try:
		print('Reading Logs')
		dict_server_cpu = {}
		file = open(args[1], 'r')
		next(file)
		for log in file:
			data = log.strip().split(' ')
			k = data[1] + data[2]
			ts = data[0]
			cpu_usage = data[3]
			if k not in dict_server_cpu.keys():
				dict_server_cpu[k] = {}
			dict_server_cpu[k][ts] = tuple([datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M') , cpu_usage+'%'])
		print("Finished reading logs")
		print("Enter your query:")
	except:
		print("Incorrect file or error in reading logs")
		exit(2)

	# Code for Quering the logs. Handles different conditions
	try:			
		for line in sys.stdin:
			start_time = time.time()
			line_args = line.strip().split(' ')

			# Exit query
			if line_args[0] == "EXIT":
				print('Exiting...')
				return 0

			# Main query
			elif line_args[0] == "QUERY":
				k = line_args[1] + line_args[2]
				if k not in dict_server_cpu.keys():
					print("Invalid server IP, please enter server IP with the format 192.168.x.x")
					continue

				if(line_args[3] != '2014-10-31' or line_args[5] != '2014-10-31'):
					print("Date not present in logs. Please enter timestamp for 2014-10-31")
					continue

				datetime_start = datetime.strptime(line_args[3]+' '+line_args[4], '%Y-%m-%d %H:%M')
				unix_time_start = time.mktime(datetime_start.timetuple())
				datetime_end = datetime.strptime(line_args[5]+' '+line_args[6], '%Y-%m-%d %H:%M')
				unix_time_end = time.mktime(datetime_end.timetuple())
				total_timestamps_diff = int((unix_time_end - unix_time_start) / 60.0)
				if total_timestamps_diff < 0:
					print("End time should be greater than start time")
					continue

				ts_start = str(unix_time_start)[:-2]

				start_index = list(dict_server_cpu[k].keys()).index(ts_start)
				
				values = list(dict_server_cpu[k].values())[start_index:start_index+total_timestamps_diff]

				print("CPU" + line_args[2] + " usage on " + line_args[1]+":")
				print(*values, sep=',')

			# Incorrect query
			else:
				print("Incorrect QUERY")

			print("Time taken: ", time.time()-start_time , "s")
	except:
		print("Error in processing Query")
		exit(3)

if __name__ == '__main__':
	main(sys.argv)

