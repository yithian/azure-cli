ARG image=mcr.microsoft.com/azurelinux/base/core:3.0

FROM ${image} AS build-env
ARG cli_version=dev

RUN tdnf update -y

# kernel-headers, glibc-devel, binutils are needed to install psutil python package on ARM64
# ca-certificates: Azure Linux by default only adds a very minimal set of root certs to trust certain Microsoft
# resources (primarily packages.microsoft.com). ca-certificates contains the official Microsoft curated set of
# trusted root certificates. It has replaced the set of Mozilla Trusted Root Certificates.
RUN tdnf install -y binutils file rpm-build gcc libffi-devel python3-devel openssl-devel make diffutils patch \
    dos2unix perl sed kernel-headers glibc-devel binutils ca-certificates

WORKDIR /azure-cli

COPY . .

# Azure Linux 3's python3 is 3.12, the rpm paths are
#   /usr/src/azl/RPMS/x86_64/azure-cli-2.63.0-1.azl3.x86_64.rpm
#   /usr/src/azl/RPMS/aarch64/azure-cli-2.63.0-1.azl3.aarch64.rpm
RUN --mount=type=secret,id=PIP_INDEX_URL export PIP_INDEX_URL=$(cat /run/secrets/PIP_INDEX_URL) && \
    dos2unix ./scripts/release/rpm/azure-cli.spec && \
    REPO_PATH=$(pwd) CLI_VERSION=$cli_version PYTHON_PACKAGE=python3 PYTHON_CMD=python3 \
    rpmbuild -v -bb --clean scripts/release/rpm/azure-cli.spec && \
    cp /usr/src/*/RPMS/*/azure-cli-${cli_version}-1.*.rpm /azure-cli-dev.rpm && \
    mkdir /out && cp /usr/src/*/RPMS/*/azure-cli-${cli_version}-1.*.rpm /out/

FROM ${image} AS execution-env

RUN tdnf update -y

COPY --from=build-env /azure-cli-dev.rpm ./
RUN tdnf install -y ./azure-cli-dev.rpm && \
    az --version
