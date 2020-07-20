# estuary-cli
Stateless CLI over RestApi using estuary-testrunner. Smoothly control and configure your machines/devices.

## Code quality
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8db7b5e216984baebd9d158d3a707361)](https://www.codacy.com/manual/dinuta/estuary-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dinuta/estuary-cli&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/5ce99819df230698d95d/maintainability)](https://codeclimate.com/github/dinuta/estuary-cli/maintainability)

## Linux status
[![Build Status](https://travis-ci.org/dinuta/estuary-cli.svg?branch=master)](https://travis-ci.org/dinuta/estuary-cli)

## Win status
[![CircleCI](https://circleci.com/gh/dinuta/estuary-cli.svg?style=svg)](https://circleci.com/gh/dinuta/estuary-cli)

## Steps
-  deploy [estuary-testrunner](https://github.com/dinuta/estuary-testrunner)  on the target machine (metal/VM/Docker/IoT device)
-  connect to the target machine with this CLI

## CLI in action on Katacoda
https://katacoda.com/dinuta/scenarios/estuary-cli

## Interactive usage
```bash
python main.py 
python .\main.py --ip=192.168.0.10 --port=8080 --token=None
```

## Non-interactive usage
```bash
python .\main.py --ip=192.168.0.10 --port=8080 --token=None --cmds="dir;trump"
python .\main.py --ip=192.168.0.10 --port=8080 --token=None --cmds="dir;cat requirements.txt;trump"
```

## Params
```bash
PS > python main.py --help
Usage: main.py [OPTIONS]

Options:
  --ip TEXT     The IP/hostname of the target machine where estuary-testrunner
                is deployed

  --port TEXT   The port number of the target machine where estuary-testrunner
                is deployed

  --token TEXT  The authentication token that will be sent via 'Token' header.
                Use 'None' if estuary-testrunner is deployed unsecured

  --cmds TEXT   The commands to be sent separated by ";". Useful for non-
                interactive mode.

  --help        Show this message and exit.
```

## Stateless cli example  
![image](https://user-images.githubusercontent.com/43060213/79952987-e1142f00-8483-11ea-8fdc-8bef2b7f8d2a.png)  

## Use cases
-  Remote IoT device control
-  Remote machine control
-  Remote software settings
-  Remote debugging

## Exit cli
ctrl + c  
quit  
trump  
  
