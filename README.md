# Behave Web Selenium demo

Travis CI status on Master:
![CI](https://travis-ci.org/timbortnik/behave_web.svg?branch=master)

CircleCI status on Master:
![CI](https://circleci.com/gh/:owner/:repo/tree/:branch.png?circle-token=:circle-token)

Python Behave/Selenium test examples
![Output example](https://github.com/timbortnik/behave_web/blob/master/doc/behave_web.png)

Pycharm Community Run configuration example
![Output example](https://github.com/timbortnik/behave_web/blob/master/doc/pycharm_community_example.png)

BDD Feature: https://github.com/timbortnik/behave_web/blob/master/features/hipchat_login.feature

Step Definitions: https://github.com/timbortnik/behave_web/tree/master/features/steps

Page objects: https://github.com/timbortnik/behave_web/tree/master/pages

## Prerequisites
* Python 3.5, pip

## Installation
The project provides test examples.
To prepare local installation, use the following command

    pip install -r requirements.txt

## Usage
To run behave features, use command

    behave

to see console output, use

    behave --no-capture
