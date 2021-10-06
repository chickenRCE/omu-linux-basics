FROM ubuntu:20.04

# Invariants
ARG USERNAME=play
ENV USERNAME ${USERNAME}
RUN useradd -m $USERNAME
RUN passwd --delete $USERNAME
RUN apt-get update && apt-get install -y \
    python3 \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Challenge files
ADD chal /home/$USERNAME/
ADD sshd_config /etc/ssh/sshd_config
RUN chmod +x /home/$USERNAME/run /home/$USERNAME/game.py
RUN mkdir /run/sshd

CMD ["/usr/sbin/sshd", "-D"]