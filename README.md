# estuary-cli
Stateless CLI over RestApi using estuary-testrunner

## Steps
- deploy [estuary-testrunner](https://github.com/dinuta/estuary-testrunner)  on the target machine (metal/VM/Docker)
- connect to the target machine with this cli

## Usage
```bash
python main.py 

PS C:\Users\cdinuta\IdeaProjects\estuary-cli> python .\main.py --help                                                                                                                                                     Usage: main.py [OPTIONS]

Options:
  --ip TEXT     The IP/hostname of the target machine where estuary-
                testrunner is running
  --port TEXT   The port number of the target machine where estuary-
                testrunner is running
  --token TEXT  The authentication token that will be sent via 'Token' header
  --help        Show this message and exit.
```


