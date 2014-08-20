#!/usr/bin/env python
#
# Purpose: convert file from picoquant format to global curve format.
#
# Author: John Robinson
# 
# Date: 8-13-2014
#
# Usage: convert file_name
#
# Result: converts file_name.xxx to file_name.prn
#
# cd '/Users/jmrobinson/Cubbies/GiHo-JMR_Cubby/8_11_2014/analysis/no_drug/Mg'
#
import os, sys, json

def get_params(param_file_name):
	try:
		params_file=open(param_file_name,'r')
		params = json.load(params_file)
		params_file.close()
	except:
		params = {u'tcal': 0.016, u'start': 55, u'stop': 1100, u'chi_sqr': 115}
		print "Params not specified. Creating from default."
		params_file=open(param_file_name,'w')
		json.dump(params, params_file, sort_keys=False, indent=4, separators=(',', ': '))
		params_file.close()
		#json.dumps(params, sort_keys=True, indent=4, separators=(',', ': '))
	return params # params is a dictionary

def convert_one(filename_in):
	param_file_name = 'fitting_params.json'
	p = get_params(param_file_name)
	print p
	last_line = p['stop'] + 50
	# filename_in = root + '.dat'
	root = filename_in.split('.')[0]
	filename_out = root + '.prn'
	print "Converting: ", filename_in, "--> ", filename_out
	f_in = open(filename_in, 'r')
	# print 'opened: ', filename_in
	f_out = open(filename_out, 'w')
	# print 'writing to: ', filename_out
	str = '{:>12}  {:>12} {:>12}  {:>12}\r\n'.format(p['tcal'], p['start'], p['stop'], p['chi_sqr'])
	f_out.write(str)

	lines = f_in.readlines()
	body = False
	for line in lines[0:last_line]:
		#print line
		words = line.split()
		if body == True:
			time = words[0]
			IR = words[1]
			sample = words[2]
			str = '{:>12}  {:>12} \r\n'.format(IR, sample)
			f_out.write(str)
		for word in words:
			if word == 'Time[ns]':
				# print 'found end of header'
				body = True
	f_in.close()
	f_out.close()

def convert_all():
	#path = "/Users/jmrobinson/Cubbies/Maria_Cubby/research/TCSPC/196/analysis/35/Mg"
	path = "."
	dirs = os.listdir( path )
	for file in dirs:
		words = file.split('.')
		if (len(words) > 1):
			if (words[1] == 'dat'):				
				convert_one(file)

def main():
	num_args = len(sys.argv) - 1
	if (num_args == 0):
		# print 'Call convert with one argument, the filename to be converted'
		# sys.exit(0)
		convert_all()
	elif (num_args == 1):
		f_name = sys.argv[1]
		convert_one(f_name)

if __name__ == "__main__":
	main()