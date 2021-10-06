#include <stdio.h>
#include <stdlib.h>

int main(){
    system("if [ \"$(id -u)\" != \"0\" ]; then     echo \"Only the root user can get the flag!\" 1>&2; else     echo \"omu{Th3_PATH_to_hacking_stardom!}\"; fi");
    return 0;
}
