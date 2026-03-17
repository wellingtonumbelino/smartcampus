#!/bin/bash

# Create a directory to output files
OUTPUT_DIR="$(dirname "$1")/output"
mkdir -p "$OUTPUT_DIR"

# Run the planner
popf3-clp "$@" > "$OUTPUT_DIR/plan.txt" 2> "$OUTPUT_DIR/error.log"

# Capture the exit code of the planner
EXIT_CODE=$?

# Check if file is empty
if [ ! -s "$OUTPUT_DIR/plan.txt" ]; then
    rm "$OUTPUT_DIR/error.log"
fi

# See plan in terminal
if [ -f "$OUTPUT_DIR/plan.txt" ]; then
    cat "$OUTPUT_DIR/plan.txt"
fi

exit $EXIT_CODE