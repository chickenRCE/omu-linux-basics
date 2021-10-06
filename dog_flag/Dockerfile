FROM ubuntu:20.04

# Invariants
ARG PORT=10000
ARG USERNAME=user
ENV USERNAME ${USERNAME}
RUN useradd -m $USERNAME
RUN apt-get update && apt-get install -y \
    cowsay \
    xinetd \
    && rm -rf /var/lib/apt/lists/*

# Challenge files
RUN rm /usr/bin/cat
ADD chal /home/$USERNAME/
ADD xinetd.conf /etc/xinetd.d/chal
RUN chmod +x /home/$USERNAME/run /home/$USERNAME/init.sh
EXPOSE $PORT

CMD [ \
        "xinetd", \
        "-dontfork", \
        "-f", "/etc/xinetd.d/chal" \
    ]