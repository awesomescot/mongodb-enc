#!/usr/bin/python
from pymongo import *
import yaml
import sys
from ConfigParser import SafeConfigParser
import argparse
import glob


parser = SafeConfigParser()
config = ['../conf/conf.ini']
found = parser.read(config)
database = parser.get('mongodb_info', 'mongodb_db_name')
collection = parser.get('mongodb_info', 'mongodb_collection_name')
host = parser.get('mongodb_info', 'mongodb_servers')

def connect_mongodb():
	con = Connection(host)
	col = con[database][collection]
	return col

def main():

	cmd_parser = argparse.ArgumentParser(description='Remove Nodes To Mongodb ENC')
	cmd_parser.add_argument('-n', '--node', dest='puppet_node', help='Puppet Node Hostname', required=True)
	args = cmd_parser.parse_args()

	col = connect_mongodb()
	col.remove({ 'node' : args.puppet_node})

if __name__ == "__main__":
	main()