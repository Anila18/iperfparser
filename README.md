# iPerfParser
Parsing iPerf into Json

## Run It

```
$ python parseperf.py data.txt data.json out.json
```
Where:
- __data.txt__ is the iperf client example output
- __data.json__ is the distance json parser example output
- __out.json__ is the outfile 

## Other Thoughts

- Expects certain spacing in the iperf client output... can change to regex later
- Adds transfer amount in MBytes, bandwidth in Mbps, and package percentage in % to the json file
- Will fill in points in order
- No error checking... besides argparse
