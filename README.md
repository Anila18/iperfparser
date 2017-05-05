# iPerfParser
Parsing iPerf into Json

## Run It

```
$ python parseperf.py [iperf client output].txt [json distance input].json [output json].json
```

## Other Thoughts

- Expects certain spacing in the iperf client output... can change to regex later
- Adds transfer amount in MBytes, bandwidth in Mbps, and package percentage in % to the json file
- Will fill in points in order
- No error checking... besides argparse 
