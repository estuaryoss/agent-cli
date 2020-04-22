# estuary-cli
Stateless CLI over RestApi using estuary-testrunner

## Coverage and code quality
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8db7b5e216984baebd9d158d3a707361)](https://www.codacy.com/manual/dinuta/estuary-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dinuta/estuary-cli&amp;utm_campaign=Badge_Grade)

## Linux status
[![Build Status](https://travis-ci.org/dinuta/estuary-cli.svg?branch=master)](https://travis-ci.org/dinuta/estuary-cli)

## Steps
-  deploy [estuary-testrunner](https://github.com/dinuta/estuary-testrunner)  on the target machine (metal/VM/Docker)
-  connect to the target machine with this CLI

## Usage
```bash
python main.py 
python .\main.py --ip=192.168.0.10 --port=8080 --token=None
```

## Params
```bash
PS > python .\main.py --help  
Usage: main.py [OPTIONS]

Options:
  --ip TEXT     The IP/hostname of the target machine where estuary-cli
                is running
  --port TEXT   The port number of the target machine where estuary-cli
                is running
  --token TEXT  The authentication token that will be sent via 'Token' header
  --help        Show this message and exit.
```

## Stateless cli example  
![image](https://user-images.githubusercontent.com/43060213/79952987-e1142f00-8483-11ea-8fdc-8bef2b7f8d2a.png)  

## Exit cli
ctrl + c  
quit  
trump  
  
