# pyuppaal
Python library for manipulating UPPAAL xml files. Can currently import, export and layout models.

This project was created from the existing launchpad site https://launchpad.net/pyuppaal.

## Original README

1) Installation Instructions 
pyuppaal depends on the following ubuntu packages:
python-pygraphviz, python-ply

On ubuntu run:
apt-get install python-pygraphviz, python-ply

2) Running pyuppal scripts

To autolayout a model run bin/layout_uppaal, use option --help for arguments.

3) Using pyuppal

To use pyuppal in your application or the python shell, use import pyuppaal. 
Remember to have pyuppaal in you PYTHONPATH.

4) Running tests
To run tests invoke the test script test/run_tests.sh:

sh test/run_tests.sh

Remember to have verifyta in you path else the test case for UPPAAL integration
will fail. 
