#!/bin/bash
/usr/bin/python /opt/ibm-cloud-private-ce-2.1.0.2/cluster/hosts.py

cd /opt/ibm-cloud-private-ce-2.1.0.2/cluster

docker run -e LICENSE=accept --net=host \
-t -v "$(pwd)":/installer/cluster \
ibmcom/icp-inception:2.1.0.2 install