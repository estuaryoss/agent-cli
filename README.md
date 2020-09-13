<h1 align="center"><img src="./docs/images/banner_cli.png" alt="Testing as a service"></h1>  

Support project: <a href="https://paypal.me/catalindinuta?locale.x=en_US"><img src="https://lh3.googleusercontent.com/Y2_nyEd0zJftXnlhQrWoweEvAy4RzbpDah_65JGQDKo9zCcBxHVpajYgXWFZcXdKS_o=s180-rw" height="40" width="40" align="center"></a>    

# estuary-cli
Stateless CLI over REST API using estuary-agent. Smoothly control and configure your machine / CLI application.

## Code quality
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/086f5a66ac0841c4800dcddfdc9fb3c2)](https://www.codacy.com/gh/estuaryoss/estuary-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=estuaryoss/estuary-cli&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/8fffe56fb66038d7fa2d/maintainability)](https://codeclimate.com/github/estuaryoss/estuary-cli/maintainability)

## Linux status
[![Build Status](https://travis-ci.org/estuaryoss/estuary-cli.svg?branch=master)](https://travis-ci.org/estuaryoss/estuary-cli)

## Win status
[![CircleCI](https://circleci.com/gh/estuaryoss/estuary-cli.svg?style=svg)](https://circleci.com/gh/estuaryoss/estuary-cli)

## Steps
-  deploy [estuary-agent](https://github.com/dinuta/estuary-agent) or [estuary-agent-java](https://github.com/dinuta/estuary-agent-java)  on the target machine (metal/VM/Docker/IoT device)
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

The default endpoint is */command*. The endpoint can be overridden (E.g. Estuary deployer):
```bash
python .\main.py --ip=192.168.0.10 --port=8080 --token=None --endpoint=/docker/command --cmds="dir;cat requirements.txt;trump"
python .\main.py --ip=192.168.0.10 --port=8080 --token=None --endpoint=/kubectl/command --cmds="dir;cat requirements.txt;trump"
```

## Params
```bash
PS > python main.py --help
Usage: main.py [OPTIONS]

Options:
  --ip TEXT     The IP/hostname of the target machine where estuary-agent
                is deployed

  --port TEXT   The port number of the target machine where estuary-agent
                is deployed

  --token TEXT  The authentication token that will be sent via 'Token' header.
                Use 'None' if estuary-agent is deployed unsecured

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
  
