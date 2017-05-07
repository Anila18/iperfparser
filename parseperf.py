import argparse
import json

from pprint import pprint

def convertToM(number, btype):
    if (btype == 'KBytes' or btype == 'Kbits/sec'):
        return number/1000
    elif (btype == 'Bytes' or btype == 'Bits/sec'):
        return number/1000000
    else:
        return number

def parseIPerf(file_name, json_data):
    data = ""

    with open (file_name) as iperf_data:
        data = iperf_data.read()

    index = 0
    data_points = data.split("\n\n")

    for point in data_points:

        t = 0.0
        b = 0.0
        p = 0.0

        if (len(point.split('\n')) >= 12):
            sdata = point.split('\n')[11].split('  ')
            if (len(sdata) > 5):
                tdata = sdata[3].lstrip().split(' ')
                bdata = sdata[4].lstrip().split(' ')
                t = convertToM(float(tdata[0]), tdata[1])
                b = convertToM(float(bdata[0]), bdata[1])
                p = float(sdata[-1].split(' ')[-1].strip('(').strip(')').strip('%'))

        json_data['points'][index]['transferred_mbytes'] = t
        json_data['points'][index]['bandwidth_mbps'] = b
        json_data['points'][index]['packet_perc'] = p
        index += 1

    while index < len(json_data['points']):
        json_data['points'][index]['transferred_mbytes'] = 0.0
        json_data['points'][index]['bandwidth_mbps'] = 0.0
        json_data['points'][index]['packet_perc'] = 0.0
        index += 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pfile", help="the iperf data file")
    parser.add_argument("jfile", help="the json data file")
    parser.add_argument("ofile", help="the json output file")

    args = parser.parse_args()

    with open(args.jfile) as json_file:
        data = json.load(json_file)

    parseIPerf(args.pfile, data)

    with open(args.ofile, 'w+') as output_file:
        json.dump(data, output_file, indent=4)

main()
