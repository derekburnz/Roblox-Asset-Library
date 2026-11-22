#!/bin/bash
# all.sh NAME... : one process per model, 8 at a time
printf "%s\n" "$@" | xargs -P 8 -I{} sh -c 'QA_OUT=${QD:-o}/{}.json /home/user/.venv-bpy/bin/python run.py {} >/dev/null 2>${QD:-o}/{}.err || echo FAIL {}'
