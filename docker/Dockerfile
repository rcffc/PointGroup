FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends git wget unzip bzip2
RUN apt-get update && apt-get install -y feh sudo
#python3.7 python3-pip

# Change default shell
SHELL [ "/bin/bash", "--login", "-c" ]

# Create a non-root user
ARG username=taro
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER

USER $USER

# install miniconda
ENV MINICONDA_VERSION latest
ENV CONDA_DIR $HOME/miniconda3
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-$MINICONDA_VERSION-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
    
# make non-activate conda commands available
ENV PATH=$CONDA_DIR/bin:$PATH 

# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile

# make conda activate command available from /bin/bash --interative shells
RUN conda init bash

# Potential TODO: Install extra packages for GUI stuff?

# create a project directory inside user home
COPY . /app
WORKDIR /app
ENV PROJECT_DIR /app

# Install PointGroup
RUN conda create -n pointgroup python=3.7
RUN echo "source activate pointgroup" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# Install Pytorch
RUN conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch


RUN pip install -r requirements.txt
RUN conda install -c bioconda google-sparsehash 

RUN conda install libboost && \
conda install -c daleydeng gcc-5 # need gcc-5.4 for sparseconv

USER root
RUN apt-get update && apt-get install -y libboost-dev libsparsehash-dev python2.7 nano

RUN cd lib/spconv && \
python setup.py bdist_wheel && \
cd dist && \
pip install *.whl

RUN cd lib/pointgroup_ops && \
python setup.py develop

RUN pip install gdown
RUN gdown https://drive.google.com/uc?id=1wGolvj73i-vNtvsHhg_KXonNH2eB_6-w

#RUN nano /etc/ssh/sshd_config