#!/bin/bash

# Create a directory to output files
mkdir -p /output

# Run the planner
popf3-clp "$@" > /output/plan.txt 2> /output/error.log

# Capture the exit code of the planner
EXIT_CODE=$?

# Check if file is empty
if [ ! -s /output/plan.txt ]; then
    rm /output/error.log
fi

# See plan in terminal
if [ -f /output/plan.txt ]; then
    cat /output/plan.txt
fi

exit $EXIT_CODE