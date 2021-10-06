# Peekaboo: nth line

## Description

Flag is `omu{<flag you got from challenge>}`

Type the following command to connect to the challenge:
`nc <remote ip> <port>`

## Solution

```
head -n52 lots_of_text.txt | tail -n1
```

## Learning Outcome

Testing some concepts taught about chaining operations and alternatives to cat (head / tail)

## Flag

`omu{peekaboo_you_found_m3!}`
