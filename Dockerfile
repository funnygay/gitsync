FROM ubuntu:bionic

COPY . /gitSync
WORKDIR /gitSync

EXPOSE 3000

RUN apt-get update \
  && apt-get install -y python3 \
                        python3-pip \
                        python3-dev \
                        apt-transport-https \
                        wget \
                        git \
                        curl \
                        dpkg \
                        vim \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN echo "deb https://www.plasticscm.com/plasticrepo/stable/ubuntu/ ./" | tee /etc/apt/sources.list.d/plasticscm-stable.list
RUN wget https://www.plasticscm.com/plasticrepo/stable/ubuntu/Release.key -O - | apt-key add - 
RUN apt-get update \
&& apt-get install -y plasticscm-client-complete

RUN apt update
RUN apt install dirmngr gnupg apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" > /etc/apt/sources.list.d/mono-official-stable.list'
RUN apt update
RUN apt install -y -q mono-complete
RUN cp -f mono_setup /opt/plasticscm5/client/mono_setup \
  && cp -f /opt/plasticscm5/mono/lib/libgit2.so /usr/lib/libgit2.so \
  && mkdir ../root/.plastic4/ \
  && cp -f client.conf /root/.plastic4/client.conf 

CMD python gitsync.py -f /gitSync/data/repoList.json
