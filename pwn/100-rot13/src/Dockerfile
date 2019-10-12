# Use Ubuntu LTS 18.04
FROM ubuntu:18.04

# Add required files to /app and set working directory
WORKDIR /app
ADD . /app

# Install dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends xinetd libc6-i386

# Setup file permissions
RUN adduser --disabled-password --gecos '' rot13
RUN chown root:rot13 /app/rot13
RUN chown root:rot13 /app/flag.txt
RUN chown root:rot13 /app/rot13.c
RUN chown root:rot13 /app/Dockerfile

RUN chmod 750 /app/rot13
RUN chmod 440 /app/flag.txt
RUN chmod 440 /app/rot13.c
RUN chmod 440 /app/Dockerfile

# Deploy the service file
COPY rot13.service /etc/xinetd.d/nodes

# Expose port 1337 and run xinetd
RUN echo "rot13 1337/tcp" >> /etc/services
EXPOSE 1337
CMD ["xinetd", "-dontfork"]
