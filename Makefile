SHELL=/bin/sh

PYTHON		?= python3
SOURCE		 = src
MODEL		 = model
SAMPLE		 = test_sample
ADDRESS		 = 192.168.0.101
FILE		?= output

all:

run run_test run.test test:
	${PYTHON} ${SOURCE}/test.py --model=${MODEL}.pth\
		--sample=${SAMPLE}.pcap\
		--address=${ADDRESS}\
		--filename=${FILE}.pcap

clean clear:
	rm -rf ${SOURCE}/__pycache__
