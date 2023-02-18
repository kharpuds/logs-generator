import sys
import datetime
import time
import random

def main(args):
	if len(args) != 2:
		print("Incorrect args")
		exit(1)

	with open(args[1], 'w', encoding='utf-8') as my_file:
		my_list = ['Timestamp', 'IP', 'cpu_id', 'usage']
		my_file.write(' '.join(my_list) + '\n')

		for h in range(0,24):
			for m in range(0,60):
				date_time = datetime.datetime(2014, 10, 31, h, m)
				unix_time = time.mktime(date_time.timetuple())
				for sn3 in range(0,10):
					for sn4 in range (0,100):

						ip = '192.168.' + str(sn3) + '.' + str(sn4)

						my_list0 = [str(unix_time)[:-2], ip, '0', str(random.randint(0,100))]
						my_file.write(' '.join(my_list0) + '\n')

						my_list1 = [str(unix_time)[:-2], ip, '1', str(random.randint(0,100))]
						my_file.write(' '.join(my_list1) + '\n')
	    
	exit(0)

if __name__ == '__main__':
	main(sys.argv)
		    