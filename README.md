=======================================

# Charles Submission @Charles-Butler

=======================================

## Instructions for running submission:

1. Open New terminal
2. Navigate (cd) to `/Red-Rover-Code-Puzzle`
3. run with `python rrStringTransformer.py` (for A-Z ordered sort)
4. For reverse order run with `python rrStringTransformer.py -d` or `--desc` (for Z-A order)

### Exact command may vary based on python installed eg. `python` could instead be `pip` `python3` `py`

Expected Output:

```
Given '(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)'
Sorting order = Ascending (A-Z)

Transformed String:
- id
- name
- email
- type
  - id
  - name
  - customFields
    - c1
    - c2
    - c3
- externalId

Sorted Output (A-Z):
- email
- externalId
- id
- name
- type
  - customFields
    - c1
    - c2
    - c3
  - id
  - name
```

==============================================================================

# Red Rover Code Puzzle

Thank you for your interest in joining our team. The following coding exercise helps us get a sense for your approach to turning a requirement into code. If you have any questions please reach out.

## Please do not use AI for this exercise!

We tried to keep this simple enough that it doesn't take a lot of your time, but this is exactly the type of problem that AI can solve in an instant. Please do not consult AI for any part of this exercise. Thank you for your integrity.

## Instructions

Using the technology of your choice, convert the following string:

`"(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)"`

To this output:

```
- id
- name
- email
- type
  - id
  - name
  - customFields
    - c1
    - c2
    - c3
- externalId
```

And also to this output:

```
- email
- externalId
- id
- name
- type
  - customFields
    - c1
    - c2
    - c3
  - id
  - name
```

~~Please send access to the source and a runnable copy of your app. ~~
