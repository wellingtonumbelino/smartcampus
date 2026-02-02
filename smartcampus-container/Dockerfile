# STAGE 1 - Build UPMurphi
FROM ubuntu:22.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Dependencies for building UPMurphi
RUN apt-get update && apt-get install -y \
    build-essential \
    flex \
    bison \
    libc6-dev-i386 \
    gcc-multilib \
    g++-multilib \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Copy UPMurphi source code
COPY upmurphi ./upmurphi

# Compile UPMurphi
WORKDIR /build/upmurphi/src
RUN make

# STAGE 2 - Runtime
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Dependencies for running UPMurphi
RUN apt-get update && apt-get install -y \
    g++ \
    make \
    libc6-dev \
    uuid-runtime \
    dos2unix \
    gcc-multilib \
    g++-multilib \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /planner

# Copy UPMurphi binary from the builder stage
COPY --from=builder /build/upmurphi /planner/upmurphi

# Executable entrypoint
COPY entrypoint.sh /planner/entrypoint.sh
RUN dos2unix /planner/entrypoint.sh && chmod +x /planner/entrypoint.sh

ENTRYPOINT ["/planner/entrypoint.sh"]