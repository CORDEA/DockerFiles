ROM ubuntu

MAINTAINER huge


RUN apt-get -y update

RUN apt-get install -y wget zip zsh vim python-pip
RUN pip install percol

RUN adduser --disabled-password --gecos '' huge
RUN adduser huge sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER huge
WORKDIR /home/huge
ENV HOME /home/huge

RUN wget ### dotfiles.zip URL ###
RUN unzip dotfiles.zip

RUN sudo cp -r dotfiles/.[a-zA-Z0-9]* ./
RUN sudo rm -rf dotfiles*

ENTRYPOINT ["/usr/bin/zsh"]
