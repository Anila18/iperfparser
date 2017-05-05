import argparse
import json
from pprint import pprint

def parseIPerf(file_name):
    data = ""

    with open (file_name) as iperf_data:
        data = iperf_data.read()

    data_points = data.split("\n\n")
    for point in data_points:
        for line in point.split('\n'):
            if (line[0] != '['):
                print(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pfile", help="the iperf data file")
    parser.add_argument("jfile", help="the json data file")
    parser.add_argument("floor", help="the floor the data was taken on")

    args = parser.parse_args()

    parseIPerf(args.pfile)

    with open(args.jfile) as json_file:
        data = json.load(json_file)

    pprint(data)

    for point in data['points']:
        pprint(point)


main()
