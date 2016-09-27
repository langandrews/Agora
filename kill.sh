#!/bin/bash
#
#
# Should we do this in python instead??
#################

# Kill the process specified by command line arg
pid=$1
kill ${pid}
echo "kill.sh: Killing process ${pid}"

# Should also edit noauth-config to get rid of the corresponding entry
