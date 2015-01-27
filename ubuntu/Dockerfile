ROM ubuntu

MAINTAINER Yoshihiro Tanaka <feria.primavera@gmail.com>


RUN apt-get -y update && \
    apt-get install -y wget zip zsh vim python-pip && \
    pip install percol

RUN adduser --disabled-password --gecos '' huge && \
    adduser huge sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER huge
ENV HOME /home/huge
WORKDIR $HOME

RUN wget ### dotfiles.zip URL ### && \
    unzip dotfiles.zip

RUN sudo cp -r dotfiles/.[a-zA-Z0-9]* ./
RUN sudo rm -rf dotfiles*

ENTRYPOINT ["/usr/bin/zsh"]
