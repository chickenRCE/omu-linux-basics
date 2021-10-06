# Peekaboo: nth column

## Description

Flag is `omu{<flag you got from challenge>}`

Type the following command to connect to the challenge:
`nc <remote ip> <port>`

## Solution

```
cut -b 22 lots_of_text.txt | tr -d '\n'
```

## Learning Outcome

Teach some extra commands like `cut` and `tr`

## Flag

`omu{h0w_do_you_k33p_finding_me_:O}`