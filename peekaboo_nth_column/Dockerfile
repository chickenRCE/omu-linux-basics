FROM ubuntu:20.04

# Invariants
ARG PORT=10000
ARG USERNAME=user
ENV USERNAME ${USERNAME}
RUN useradd -m $USERNAME
RUN apt-get update && apt-get install -y \
    python \
    python3-pip \
    cowsay \
    xinetd \
    && rm -rf /var/lib/apt/lists/*

# Challenge files
ADD ptrlib.tar.gz /tmp
RUN pip install /tmp/ptrlib
ADD chal /home/$USERNAME/
ADD xinetd.conf /etc/xinetd.d/chal
RUN chmod +x /home/$USERNAME/run /home/$USERNAME/peekaboo
EXPOSE $PORT

CMD [ \
        "xinetd", \
        "-dontfork", \
        "-f", "/etc/xinetd.d/chal" \
    ]