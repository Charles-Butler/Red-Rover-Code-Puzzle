#!/bin/bash
# ------------------------------------------------------------------
# Charles Butler | Red Rover Submission
#          List Transformer mvp
# ------------------------------------------------------------------

VERSION=0.1.0
USAGE="Usage: command -ihv args"


# --- Body --------------------------------------------------------
#  SCRIPT LOGIC GOES HERE

STRING="id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
echo Given: $STRING 
# Transform into JSON like format:
# - id
# - name
# - email
# - type / contains 3 subfield
#   - id
#   - name
#   - customFields / contains 3 subfields
#     - c1
#     - c2
#     - c3
# - externalId

echo 'return formatted version like JSON'
printf "$STRING" | tr ',' '\n' | tr ')' ' ' | tr '(' '\n\t' | sed 's/^ *//' | sed 's/^/- /'
# -----------------------------------------------------------------
# Shell script Common template from https://stackoverflow.com/questions/14008125/shell-script-common-template