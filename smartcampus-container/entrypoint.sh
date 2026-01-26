#!/bin/bash
set -e

if [ "$#" -ne 2 ]; then
    echo "Usage: planner <domain.pddl> <problem.pddl>"
    exit 1
fi

DOMAIN_PDDL=$1
PROBLEM_PDDL=$2
WORKDIR=/planner/work/$(uuidgen)
OUTPUT_DIR=/planner/runtime/output

mkdir -p "$WORKDIR"
mkdir -p "$OUTPUT_DIR"

if [ ! -f "$DOMAIN_PDDL" ]: then
    echo "Error: Domain file not found: $DOMAIN_PDDL" | tee "$OUTPUT_DIR/error.log"
    exit 1
fi

if [ ! -f "$PROBLEM_PDDL" ]: then
    echo "Error: Problem file not found: $PROBLEM_PDDL" | tee "$OUTPUT_DIR"/error.log
    exit 1
fi

cd "$WORKDIR"
cp "$DOMAIN_PDDL" domain.pddl
cp "$PROBLEM_PDDL" problem.pddl


echo "[1/3] Converting PDDL to domain.m"
if ! /planner/upmurphi/bin/pddl2upm domain.pddl problem.pddl > domain.m 2> "$OUTPUT_DIR/error.log"; then
    echo "Error: pddl2upm failed" >> "$OUTPUT_DIR/error.log"
    exit 1
fi

echo "[2/3] Compiling the planner"
if ! /planner/upmurphi/bin/upmc domain.m >> "$OUTPUT_DIR/error.log" 2>&1; then
    echo "Error: upmc compilation failed" >> "$OUTPUT_DIR/error.log"
    exit 1
fi

echo "Generated files:"
ls -lh

if [ ! -f domain_planner ]; then
    echo "Error: Compilation failed - domain_planner executable not found." >> "$OUTPUT_DIR/error.log"
    exit 1
fi

echo "[3/3] Running the planner"
if ./domain_planner > "$OUTPUT_DIR/plan.txt" 2> >(tee -a "$OUTPUT_DIR/error.log"); then
    echo "Planner finished successfully"
    exit 0
else
    echo "Error: Planner execution failed" >> "$OUTPUT_DIR/error.log"
    exit 1
fi