#!/bin/bash
set -e

if [ "$#" -ne 2 ]; then
    echo "Usage: planner <domain.pddl> <problem.pddl>"
    exit 1
fi

DOMAIN_PDDL=$1
PROBLEM_PDDL=$2

WORKDIR=/planner/work/$(uuidgen)
mkdir -p "$WORKDIR"

cp "$DOMAIN_PDDL" "$WORKDIR/domain.pddl"
cp "$PROBLEM_PDDL" "$WORKDIR/problem.pddl"

cd "$WORKDIR"

echo "[1/3] Converting PDDL to domain.m"
/planner/upmurphi/bin/pddl2upm domain.pddl problem.pddl > domain.m

echo "[2/3] Compiling the planner"
/planner/upmurphi/bin/upmc domain.m || {
    echo "upmc failed"
    exit 1
}

echo "Generated files:"
ls -lh

if [ ! -f domain_planner ]; then
    echo "Compilation failed: domain_planner executable not found."
    exit 1
fi

echo "[3/3] Running the planner"
./domain_planner > plan.txt

cat plan.txt