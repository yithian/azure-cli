# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['acr'] = """
type: group
short-summary: Manage private registries with Azure Container Registries.
"""

helps['acr build'] = """
type: command
short-summary: Queues a quick build, providing streaming logs for an Azure Container Registry.
examples:
  - name: Queue a local context as a Linux build, tag it, and push it to the registry.
    text: >
        az acr build -t sample/hello-world:{{.Run.ID}} -r myregistry .
  - name: Queue a local context as a Linux build, tag it, and push it to the registry without streaming logs.
    text: >
        az acr build -t sample/hello-world:{{.Run.ID}} -r myregistry --no-logs .
  - name: Queue a local context as a Linux build without pushing it to the registry.
    text: >
        az acr build -t sample/hello-world:{{.Run.ID}} -r myregistry --no-push .
  - name: Queue a local context as a Linux build without pushing it to the registry.
    text: >
        az acr build -r myregistry .
  - name: Queue a remote GitHub context as a Windows build, tag it, and push it to the registry.
    text: >
        az acr build -r myregistry https://github.com/Azure/acr-builder.git -f Windows.Dockerfile --platform windows
  - name: Queue a remote OCI Artifact context build.
    text: >
        az acr build -r myregistry oci://myregistry.azurecr.io/myartifact:mytag
  - name: Queue a local context as a Linux build on arm/v7 architecture, tag it, and push it to the registry.
    text: >
        az acr build -t sample/hello-world:{{.Run.ID}} -r myregistry . --platform linux/arm/v7
  - name: Queue a local context as a Linux build, tag it, and push it to the ABAC-based Repository Permission enabled registry and use the caller's Entra identity to authenticate with the source registry.
    text: >
        az acr build -t sample/hello-world:{{.Run.ID}} -r myregistry . --source-acr-auth-id [caller]
"""

helps['acr check-health'] = """
type: command
short-summary: Gets health information on the environment and optionally a target registry.
examples:
  - name: Gets health state with target registry 'myregistry', skipping confirmation for pulling image.
    text: >
        az acr check-health -n myregistry -y
  - name: Gets health state of the environment, without stopping on first error.
    text: >
        az acr check-health --ignore-errors
  - name: Gets health state with target registry 'myregistry', and checks allowed permissions to the specific repository 'myrepo'.
    text: >
        az acr check-health -n myregistry --repository myrepo
"""

helps['acr check-name'] = """
type: command
short-summary: Checks if an Azure Container Registry name is valid and available for use.
examples:
  - name: Check if a registry name already exists.
    text: >
        az acr check-name -n doesthisnameexist
"""

helps['acr config'] = """
type: group
short-summary: Configure policies for Azure Container Registries.
"""

helps['acr config content-trust'] = """
type: group
short-summary: Manage content-trust policy for Azure Container Registries.
"""

helps['acr config authentication-as-arm'] = """
type: group
short-summary: Manage 'Azure AD authenticate as ARM' policy for Azure Container Registries.
"""

helps['acr config authentication-as-arm show'] = """
type: command
short-summary: Show the configured 'Azure AD authenticate as ARM' policy for an Azure Container Registry.
examples:
  - name: Show the configured 'Azure AD authenticate as ARM' policy for an Azure Container Registry
    text: >
        az acr config authentication-as-arm show -r myregistry
"""

helps['acr config authentication-as-arm update'] = """
type: command
short-summary: Update 'Azure AD authenticate as ARM' policy for an Azure Container Registry.
examples:
  - name: Disable 'Azure AD authenticate as ARM' policy for an Azure Container Registry, so only ACR audienced tokens can be used for authentication
    text: >
        az acr config authentication-as-arm update -r myregistry --status Disabled
  - name: Enable 'Azure AD authenticate as ARM' policy for an Azure Container Registry, it will allow both ACR and ARM audienced tokens to be used for authentication
    text: >
        az acr config authentication-as-arm update -r myregistry --status Enabled
"""

helps['acr config content-trust show'] = """
type: command
short-summary: Show the configured content-trust policy for an Azure Container Registry.
examples:
  - name: Show the configured content-trust policy for an Azure Container Registry
    text: >
        az acr config content-trust show -r myregistry
"""

helps['acr config content-trust update'] = """
type: command
short-summary: Update content-trust policy for an Azure Container Registry.
examples:
  - name: Update content-trust policy for an Azure Container Registry
    text: >
        az acr config content-trust update -r myregistry --status Enabled
"""

helps['acr config retention'] = """
type: group
short-summary: Manage retention policy for Azure Container Registries.
"""

helps['acr config retention show'] = """
type: command
short-summary: Show the configured retention policy for an Azure Container Registry.
examples:
  - name: Show the configured retention policy for an Azure Container Registry
    text: >
        az acr config retention show -r myregistry
"""

helps['acr config retention update'] = """
type: command
short-summary: Update retention policy for an Azure Container Registry.
examples:
  - name: Enable retention policy for an Azure Container Registry to delete an untagged manifest after 30 days.
    text: >
        az acr config retention update -r myregistry --status Enabled --days 30 --type UntaggedManifests
  - name: Enable retention policy for an Azure Container Registry to delete a manifest as soon as it gets untagged.
    text: >
        az acr config retention update -r myregistry --status Enabled --days 0 --type UntaggedManifests
"""

helps['acr config soft-delete'] = """
type: group
short-summary: Manage soft-delete policy for Azure Container Registries.
"""

helps['acr config soft-delete show'] = """
type: command
short-summary: Show the configured soft-delete policy for an Azure Container Registry.
examples:
  - name: Show the configured soft-delete policy for an Azure Container Registry
    text: >
        az acr config soft-delete show -r myregistry
"""

helps['acr config soft-delete update'] = """
type: command
short-summary: Update soft-delete policy for an Azure Container Registry.
examples:
  - name: Enable soft-delete policy for an Azure Container Registry to purge a soft-deleted manifest after 30 days.
    text: >
        az acr config soft-delete update -r myregistry --status Enabled --days 30
"""

helps['acr create'] = """
type: command
short-summary: Create an Azure Container Registry.
examples:
  - name: Create a managed container registry with the Standard SKU.
    text: >
        az acr create -n myregistry -g MyResourceGroup --sku Standard
  - name: Create a registry with ABAC-based Repository Permission enabled.
    text: >
        az acr create -n myregistry -g MyResourceGroup --sku Standard --role-assignment-mode rbac-abac
"""

helps['acr credential'] = """
type: group
short-summary: Manage login credentials for Azure Container Registries.
"""

helps['acr credential renew'] = """
type: command
short-summary: Regenerate login credentials for an Azure Container Registry.
examples:
  - name: Renew the second password for an Azure Container Registry.
    text: >
        az acr credential renew -n myregistry --password-name password2
  - name: Regenerate login credentials for an Azure Container Registry. (autogenerated)
    text: az acr credential renew --name myregistry --password-name password --resource-group MyResourceGroup
    crafted: true
"""

helps['acr credential show'] = """
type: command
short-summary: Get the login credentials for an Azure Container Registry.
examples:
  - name: Get the login credentials for an Azure Container Registry.
    text: >
        az acr credential show -n myregistry
  - name: Get the username used to log in to an Azure Container Registry.
    text: >
        az acr credential show -n myregistry --query username
  - name: Get a password used to log in to an Azure Container Registry.
    text: >
        az acr credential show -n myregistry --query 'passwords[0].value'
"""

helps['acr delete'] = """
type: command
short-summary: Deletes an Azure Container Registry.
examples:
  - name: Delete an Azure Container Registry.
    text: >
        az acr delete -n myregistry
"""

helps['acr helm'] = """
type: group
short-summary: Manage helm charts for Azure Container Registries.
"""

helps['acr helm delete'] = """
type: command
short-summary: Delete a helm chart version in an Azure Container Registry.
examples:
  - name: Delete all versions of a helm chart in an Azure Container Registry
    text: >
        az acr helm delete -n myregistry mychart
  - name: Delete a helm chart version in an Azure Container Registry
    text: >
        az acr helm delete -n myregistry mychart --version 0.3.2
"""

helps['acr helm list'] = """
type: command
short-summary: List all helm charts in an Azure Container Registry.
examples:
  - name: List all helm charts in an Azure Container Registry
    text: >
        az acr helm list -n myregistry
"""

helps['acr helm push'] = """
type: command
short-summary: Push a helm chart package to an Azure Container Registry.
examples:
  - name: Push a chart package to an Azure Container Registry
    text: >
        az acr helm push -n myregistry mychart-0.3.2.tgz
  - name: Push a chart package to an Azure Container Registry, overwriting the existing one.
    text: >
        az acr helm push -n myregistry mychart-0.3.2.tgz --force
"""

helps['acr helm repo'] = """
type: group
short-summary: Manage helm chart repositories for Azure Container Registries.
"""

helps['acr helm repo add'] = """
type: command
short-summary: Add a helm chart repository from an Azure Container Registry through the Helm CLI.
long-summary: Helm must be installed on your machine.
examples:
  - name: Add a helm chart repository from an Azure Container Registry to manage helm charts.
    text: >
        az acr helm repo add -n myregistry
"""

helps['acr helm show'] = """
type: command
short-summary: Describe a helm chart in an Azure Container Registry.
examples:
  - name: Show all versions of a helm chart in an Azure Container Registry
    text: >
        az acr helm show -n myregistry mychart
  - name: Show a helm chart version in an Azure Container Registry
    text: >
        az acr helm show -n myregistry mychart --version 0.3.2
"""

helps['acr helm install-cli'] = """
type: command
short-summary: Download and install Helm command-line tool.
examples:
  - name: Install the default version of Helm CLI to the default location
    text: >
        az acr helm install-cli
  - name: Install a specified version of Helm CLI to the default location
    text: >
        az acr helm install-cli --client-version x.x.x
  - name: Install the default version of Helm CLI to a specified location
    text: >
        az acr helm install-cli --install-location /folder/filename
  - name: Install a specified version of Helm CLI to a specified location
    text: >
        az acr helm install-cli --client-version x.x.x --install-location /folder/filename
"""

helps['acr import'] = """
type: command
short-summary: Imports an image to an Azure Container Registry from another Container Registry. Import removes the need to docker pull, docker tag, docker push. For larger images consider using `--no-wait`.
examples:
  - name: Import an image from 'sourceregistry' to 'myregistry'. The image inherits its source repository and tag names.
    text: >
        az acr import -n myregistry --source sourceregistry.azurecr.io/sourcerepository:sourcetag
  - name: Import an image from a public repository on Docker Hub. The image uses the specified repository and tag names.
    text: >
        az acr import -n myregistry --source docker.io/library/hello-world:latest -t targetrepository:targettag
  - name: Import an image from a private repository using its username and password. This also applies to registries outside Azure.
    text: >
        az acr import -n myregistry --source myprivateregistry.azurecr.io/hello-world:latest -u username -p password
  - name: Import an image from an Azure container registry in a different subscription.
    text: |
        az acr import -n myregistry --source sourcerepository:sourcetag -t targetrepository:targettag \\
            -r /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/sourceResourceGroup/providers/Microsoft.ContainerRegistry/registries/sourceRegistry
  - name: Import an image without waiting for successful completion. Failures during import will not be reflected. Run `az acr repository show-tags` to confirm that import succeeded.
    text: >
        az acr import -n myregistry --source sourceregistry.azurecr.io/sourcerepository:sourcetag --no-wait
"""

helps['acr list'] = """
type: command
short-summary: Lists all the container registries under the current subscription.
examples:
  - name: List container registries and show the results in a table, across multiple resource groups.
    text: >
        az acr list -o table
  - name: List container registries in a resource group and show the results in a table.
    text: >
        az acr list -g MyResourceGroup -o table
"""

helps['acr login'] = """
type: command
short-summary: Log in to an Azure Container Registry through the Docker CLI.
long-summary: Docker must be installed on your machine. Once done, use `docker logout <registry url>` to log out. (If you only need a refresh token and do not want to install Docker, specify '--expose-token')
examples:
  - name: Log in to an Azure Container Registry
    text: >
        az acr login -n myregistry
  - name: Get an Azure Container Registry access token
    text: >
        az acr login -n myregistry --expose-token
"""

helps['acr network-rule'] = """
type: group
short-summary: Manage network rules for Azure Container Registries.
"""

helps['acr network-rule add'] = """
type: command
short-summary: Add a network rule.
examples:
  - name: Add a rule to allow access for a specific IP address-range.
    text: >
        az acr network-rule add -n myregistry --ip-address 23.45.1.0/24
"""

helps['acr network-rule list'] = """
type: command
short-summary: List network rules.
examples:
  - name: List network rules for a registry.
    text: >
        az acr network-rule list -n myregistry
"""

helps['acr network-rule remove'] = """
type: command
short-summary: Remove a network rule.
examples:
  - name: Remove a rule that allows access for a specific IP address-range.
    text: >
        az acr network-rule remove -n myregistry --ip-address 23.45.1.0/24
"""

helps['acr pack'] = """
type: group
short-summary: Manage Azure Container Registry Tasks that use Cloud Native Buildpacks.
"""

helps['acr pack build'] = """
type: command
short-summary: Queues a quick build task that builds an app and pushes it into an Azure Container Registry.
examples:
  - name: Queue a build for the current directory with the CloudFoundry builder.
    text: az acr pack build -r myregistry -t {{.Run.Registry}}/node-app:{{.Run.ID}} --builder cloudfoundry/cnb:bionic .
  - name: Queue a build for the given GitHub repository with the Heroku builder.
    text: az acr pack build -r myregistry -t {{.Run.Registry}}/node-app:{{.Run.ID}} --pull --builder heroku/buildpacks:18 https://github.com/Azure-Samples/nodejs-docs-hello-world.git
"""

helps['acr replication'] = """
type: group
short-summary: Manage geo-replicated regions of Azure Container Registries.
"""

helps['acr replication create'] = """
type: command
short-summary: Create a replicated region for an Azure Container Registry.
examples:
  - name: Create a replicated region for an Azure Container Registry.
    text: >
        az acr replication create -r myregistry -l westus
  - name: Create a replicated region for an Azure Container Registry. (autogenerated)
    text: az acr replication create --location westus --registry myregistry --resource-group MyResourceGroup
    crafted: true
"""

helps['acr replication delete'] = """
type: command
short-summary: Delete a replicated region from an Azure Container Registry.
examples:
  - name: Delete a replicated region from an Azure Container Registry.
    text: >
        az acr replication delete -n MyReplication -r myregistry
"""

helps['acr replication list'] = """
type: command
short-summary: List all of the regions for a geo-replicated Azure Container Registry.
examples:
  - name: List replications and show the results in a table.
    text: >
        az acr replication list -r myregistry -o table
"""

helps['acr replication show'] = """
type: command
short-summary: Get the details of a replicated region.
examples:
  - name: Get the details of a replicated region
    text: >
        az acr replication show -n MyReplication -r myregistry
"""

helps['acr replication update'] = """
type: command
short-summary: Updates a replication.
examples:
  - name: Update tags for a replication
    text: >
        az acr replication update -n MyReplication -r myregistry --tags key1=value1 key2=value2
  - name: Updates a replication. (autogenerated)
    text: az acr replication update --name MyReplication --registry myregistry --resource-group MyResourceGroup --tags key1=value1 key2=value2
    crafted: true
"""

helps['acr repository'] = """
type: group
short-summary: Manage repositories (image names) for Azure Container Registries.
"""

helps['acr repository delete'] = """
type: command
short-summary: Delete a repository or image in an Azure Container Registry.
long-summary: This command deletes all associated layer data that are not referenced by any other manifest in the container registry.
examples:
  - name: Delete an image manifest by tag. This deletes the manifest referenced by 'hello-world:latest' and all other tags referencing the same manifest.
    text: az acr repository delete -n myregistry --image hello-world:latest
  - name: Delete an image manifest by sha256-based manifest digest. This deletes the manifest identified by 'hello-world@sha256:abc123' and all tags referencing the manifest.
    text: az acr repository delete -n myregistry --image hello-world@sha256:abc123
  - name: Delete a repository from an Azure Container Registry. This deletes all manifests and tags under 'hello-world'.
    text: az acr repository delete -n myregistry --repository hello-world
"""

helps['acr repository list'] = """
type: command
short-summary: List repositories in an Azure Container Registry.
examples:
  - name: List repositories in a given Azure Container Registry.
    text: az acr repository list -n myregistry
"""

helps['acr repository list-deleted'] = """
type: command
short-summary: List soft-deleted repositories in an Azure Container Registry.
examples:
  - name: List soft-deleted repositories in a given Azure Container Registry.
    text: az acr repository list-deleted -n myregistry
"""

helps['acr repository show'] = """
type: command
short-summary: Get the attributes of a repository or image in an Azure Container Registry.
examples:
  - name: Get the attributes of the repository 'hello-world'.
    text: az acr repository show -n myregistry --repository hello-world
  - name: Get the attributes of the image referenced by tag 'hello-world:latest'.
    text: az acr repository show -n myregistry --image hello-world:latest
  - name: Get the attributes of the image referenced by digest 'hello-world@sha256:abc123'.
    text: az acr repository show -n myregistry --image hello-world@sha256:abc123
"""

helps['acr repository show-manifests'] = """
type: command
short-summary: Show manifests of a repository in an Azure Container Registry.
examples:
  - name: Show manifests of a repository in an Azure Container Registry.
    text: az acr repository show-manifests -n myregistry --repository MyRepository
  - name: Show the latest 10 manifests ordered by timestamp of a repository in an Azure Container Registry.
    text: az acr repository show-manifests -n myregistry --repository MyRepository --top 10 --orderby time_desc
  - name: Show the detailed information of the latest 10 manifests ordered by timestamp of a repository in an Azure Container Registry.
    text: az acr repository show-manifests -n myregistry --repository MyRepository --top 10 --orderby time_desc --detail
"""

helps['acr repository show-tags'] = """
type: command
short-summary: Show tags for a repository in an Azure Container Registry.
examples:
  - name: Show tags of a repository in an Azure Container Registry.
    text: az acr repository show-tags -n myregistry --repository MyRepository
  - name: Show the detailed information of tags of a repository in an Azure Container Registry.
    text: az acr repository show-tags -n myregistry --repository MyRepository --detail
  - name: Show the detailed information of the latest 10 tags ordered by timestamp of a repository in an Azure Container Registry.
    text: az acr repository show-tags -n myregistry --repository MyRepository --top 10 --orderby time_desc --detail
"""

helps['acr repository untag'] = """
type: command
short-summary: Untag an image in an Azure Container Registry.
long-summary: This command does not delete the manifest referenced by the tag or any associated layer data.
examples:
  - name: Untag an image from a repository.
    text: az acr repository untag -n myregistry --image hello-world:latest
"""

helps['acr repository update'] = """
type: command
short-summary: Update the attributes of a repository or image in an Azure Container Registry.
examples:
  - name: Update the attributes of the repository 'hello-world' to disable write operation.
    text: az acr repository update -n myregistry --repository hello-world --write-enabled false
  - name: Update the attributes of the image referenced by tag 'hello-world:latest' to disable write operation.
    text: az acr repository update -n myregistry --image hello-world:latest --write-enabled false
  - name: Update the attributes of the image referenced by digest 'hello-world@sha256:abc123' to disable write operation.
    text: az acr repository update -n myregistry --image hello-world@sha256:abc123 --write-enabled false
"""

helps['acr cache'] = """
type: group
short-summary: Manage cache rules in Azure Container Registries.
"""

helps['acr cache show'] = """
type: command
short-summary: Show a cache rule.
examples:
  - name: Show a cache rule.
    text: az acr cache show -r myregistry -n MyRule
"""

helps['acr cache list'] = """
type: command
short-summary: List the cache rules in an Azure Container Registry.
examples:
  - name: List the cache rules in an Azure Container Registry.
    text: az acr cache list -r myregistry
"""

helps['acr cache create'] = """
type: command
short-summary: Create a cache rule.
examples:
  - name: Create a cache rule without a credential set.
    text: az acr cache create -r myregistry -n MyRule -s docker.io/library/ubuntu -t ubuntu
  - name: Create a cache rule with a credential set.
    text: az acr cache create -r myregistry -n MyRule -s docker.io/library/ubuntu -t ubuntu -c MyCredSet
"""

helps['acr cache update'] = """
type: command
short-summary: Update the credential set on a cache rule.
examples:
  - name: Change or add a credential set to an existing cache rule.
    text: az acr cache update -r myregistry -n MyRule -c NewCredSet
  - name: Remove a credential set from an existing cache rule.
    text: az acr cache update -r myregistry -n MyRule --remove-cred-set
"""

helps['acr cache delete'] = """
type: command
short-summary: Delete a cache rule.
examples:
  - name: Delete a cache rule.
    text: az acr cache delete -r myregistry -n MyRule
"""

helps['acr credential-set'] = """
type: group
short-summary: Manage credential sets in Azure Container Registries.
"""

helps['acr credential-set show'] = """
type: command
short-summary: Show a credential set.
examples:
  - name: Show a credential set rule.
    text: az acr credential-set show -r myregistry -n MyCredSet
"""

helps['acr credential-set list'] = """
type: command
short-summary: List the credential sets in an Azure Container Registry.
examples:
  - name: List the credential sets in an Azure Container Registry.
    text: az acr credential-set list -r myregistry
"""

helps['acr credential-set create'] = """
type: command
short-summary: Create a credential set.
examples:
  - name: Create a credential set.
    text: az acr credential-set create -r myregistry -n MyDockerHubCredSet -l docker.io -u https://MyKeyvault.vault.azure.net/secrets/usernamesecret -p https://MyKeyvault.vault.azure.net/secrets/passwordsecret
"""

helps['acr credential-set update'] = """
type: command
short-summary: Update the username or password Azure Key Vault secret ID on a credential set.
examples:
  - name: Update the password Azure Key Vault secret ID.
    text: az acr credential-set update -r myregistry -n MyDockerHubCredSet -p https://MyKeyvault.vault.azure.net/secrets/newsecretname
"""

helps['acr credential-set delete'] = """
type: command
short-summary: Delete a credential set.
examples:
  - name: Delete a credential set.
    text: az acr credential-set delete -r myregistry -n MyCredSet
"""

helps['acr manifest'] = """
type: group
short-summary: Manage artifact manifests in Azure Container Registries.
"""

helps['acr manifest show'] = """
type: command
short-summary: Get a manifest in an Azure Container Registry.
examples:
  - name: Get the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest show -r myregistry -n hello-world:latest
  - name: Get the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest show myregistry.azurecr.io/hello-world:latest
  - name: Get the manifest of the artifact referenced by digest 'hello-world@sha256:abc123'.
    text: az acr manifest show -r myregistry -n hello-world@sha256:abc123
  - name: Get the raw, unformatted manifest of the artifact 'hello-world:latest'.
    text: az acr manifest show -r myregistry -n hello-world:latest --raw
"""

helps['acr manifest list'] = """
type: command
short-summary: List the manifests in a repository in an Azure Container Registry.
examples:
  - name: List the manifests of the repository 'hello-world'.
    text: az acr manifest list -r myregistry -n hello-world
  - name: List the manifests of the repository 'hello-world'.
    text: az acr manifest list myregistry.azurecr.io/hello-world
"""

helps['acr manifest delete'] = """
type: command
short-summary: Delete a manifest in an Azure Container Registry.
examples:
  - name: Delete the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest delete -r myregistry -n hello-world:latest
  - name: Delete the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest delete myregistry.azurecr.io/hello-world:latest
  - name: Delete the manifest of the artifact referenced by digest 'hello-world@sha256:abc123'.
    text: az acr manifest delete -r myregistry -n hello-world@sha256:abc123
"""

helps['acr manifest list-referrers'] = """
type: command
short-summary: List the referrers to a manifest in an Azure Container Registry.
examples:
  - name: List the referrers to the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest list-referrers -r myregistry -n hello-world:latest
  - name: List the referrers to the manifest of the artifact 'hello-world:latest'.
    text: az acr manifest list-referrers myregistry.azurecr.io/hello-world:latest
  - name: List the referrers to the manifest of the artifact referenced by digest 'hello-world@sha256:abc123'.
    text: az acr manifest list-referrers -r myregistry -n hello-world@sha256:abc123
"""

helps['acr manifest show-metadata'] = """
type: command
short-summary: Get the metadata of an artifact in an Azure Container Registry.
examples:
  - name: Get the metadata of the tag 'hello-world:latest'.
    text: az acr manifest show-metadata -r myregistry -n hello-world:latest
  - name: Get the metadata of the tag 'hello-world:latest'.
    text: az acr manifest show-metadata myregistry.azurecr.io/hello-world:latest
  - name: Get the metadata of the manifest referenced by digest 'hello-world@sha256:abc123'.
    text: az acr manifest show-metadata -r myregistry -n hello-world@sha256:abc123
"""

helps['acr manifest list-metadata'] = """
type: command
short-summary: List the metadata of the manifests in a repository in an Azure Container Registry.
examples:
  - name: List the metadata of the manifests in the repository 'hello-world'.
    text: az acr manifest list-metadata -r myregistry -n hello-world
  - name: List the metadata of the manifests in the repository 'hello-world'.
    text: az acr manifest list-metadata myregistry.azurecr.io/hello-world
  - name: List the metadata of all manifests (tagged/untagged) in the repository 'hello-world'.
    text: az acr manifest list-metadata -r myregistry -n hello-world --query "[]"
  - name: List the metadata of untagged manifests in the repository 'hello-world'.
    text: az acr manifest list-metadata -r myregistry -n hello-world --query "[?tags==null]"
"""

helps['acr manifest update-metadata'] = """
type: command
short-summary: Update the manifest metadata of an artifact in an Azure Container Registry.
examples:
  - name: Update the metadata of the tag 'hello-world:latest'.
    text: az acr manifest update-metadata -r myregistry -n hello-world:latest --write-enabled false
  - name: Update the metadata of the tag 'hello-world:latest'.
    text: az acr manifest update-metadata myregistry.azurecr.io/hello-world:latest --write-enabled false
  - name: Update the metadata of the artifact referenced by digest 'hello-world@sha256:abc123'.
    text: az acr manifest update-metadata -r myregistry -n hello-world@sha256:abc123 --write-enabled false
"""

# Deprecated
helps['acr manifest metadata'] = """
type: group
short-summary: Manage artifact manifest metadata in Azure Container Registries.
"""

helps['acr manifest metadata show'] = """
type: command
short-summary: Get the metadata of an artifact in an Azure Container Registry.
"""

helps['acr manifest metadata list'] = """
type: command
short-summary: List the metadata of the manifests in a repository in an Azure Container Registry.
"""

helps['acr manifest metadata update'] = """
type: command
short-summary: Update the manifest metadata of an artifact in an Azure Container Registry.
"""

helps['acr manifest list-deleted'] = """
type: command
short-summary: List the soft-deleted manifests in a repository in an Azure Container Registry.
examples:
  - name: List the soft-deleted manifests in the repository 'hello-world'.
    text: az acr manifest list-deleted -r myregistry -n hello-world
  - name: List the soft-deleted manifests in the repository 'hello-world'.
    text: az acr manifest list-deleted myregistry.azurecr.io/hello-world
"""

helps['acr manifest list-deleted-tags'] = """
type: command
short-summary: List the soft-deleted tags in a repository in an Azure Container Registry.
examples:
  - name: List the soft-deleted tags in the repository 'hello-world'.
    text: az acr manifest list-deleted-tags -r myregistry -n hello-world
  - name: List the soft-deleted tags in the repository 'hello-world'.
    text: az acr manifest list-deleted-tags myregistry.azurecr.io/hello-world
  - name: List the soft-deleted tags that match tag 'latest' in the repository 'hello-world'.
    text: az acr manifest list-deleted-tags -r myregistry -n hello-world:latest
  - name: List the soft-deleted tags that match tag 'latest' in the repository 'hello-world'.
    text: az acr manifest list-deleted-tags myregistry.azurecr.io/hello-world:latest
"""

helps['acr manifest restore'] = """
type: command
short-summary: Restore a soft-deleted artifact and tag in an Azure Container Registry.
examples:
  - name: Restore the manifest matching digest 'sha256:abc123' with tag 'latest' in the repository 'hello-world'.
    text: az acr manifest restore -r myregistry -n hello-world:latest -d sha256:abc123
  - name: Restore the manifest matching digest 'sha256:abc123' with tag 'latest' in the repository 'hello-world'.
    text: az acr manifest restore myregistry.azurecr.io/hello-world:latest -d sha256:abc123
  - name: Restore the most recently deleted manifest associated with the tag 'latest' in the repository 'hello-world'.
    text: az acr manifest restore -r myregistry -n hello-world:latest
  - name: Restore the most recently deleted manifest associated with the tag 'latest' in the repository 'hello-world'.
    text: az acr manifest restore myregistry.azurecr.io/hello-world:latest
"""

helps['acr run'] = """
type: command
short-summary: Queues a quick run providing streamed logs for an Azure Container Registry.
examples:
  - name: Queue a run to execute a container command.
    text: >
        az acr run -r myregistry --cmd '$Registry/myimage' /dev/null
  - name: Queue a run with the task definition from the standard input. Either 'Ctrl + Z'(Windows) or 'Ctrl + D'(Linux) terminates the input stream.
    text: >
        az acr run -r myregistry -f - /dev/null
  - name: Queue a run to execute the tasks passed through the pipe.
    text: >
        cat task.yaml | az acr run -r myregistry -f - /dev/null
  - name: Queue a local context, pushed to ACR with streaming logs.
    text: >
        az acr run -r myregistry -f bash-echo.yaml ./workspace
  - name: Queue a remote git context with streaming logs.
    text: >
        az acr run -r myregistry https://github.com/Azure-Samples/acr-tasks.git -f hello-world.yaml
  - name: Queue a remote git context with streaming logs and runs the task on Linux platform.
    text: >
        az acr run -r myregistry https://github.com/Azure-Samples/acr-tasks.git -f build-hello-world.yaml --platform linux
  - name: Queue a remote OCI Artifact context and runs the task.
    text: >
        az acr run -r myregistry oci://myregistry.azurecr.io/myartifact:mytag -f hello-world.yaml
  - name: Queue a run to execute a container command in an ABAC-based Repository Permission enabled registry and use the caller's Entra identity to authenticate with the source registry.
    text: >
        az acr run -r myregistry --cmd '$Registry/myimage' /dev/null --source-acr-auth-id [caller]
"""

helps['acr scope-map'] = """
type: group
short-summary: Manage scope access maps for Azure Container Registries.
"""

helps['acr scope-map create'] = """
type: command
short-summary: Create a scope map for an Azure Container Registry.
examples:
  - name: Create a scope map that allows content/write and metadata/read actions for `hello-world` repository, and content/read action for `hello-world-again`.
    text: >
        az acr scope-map create -n MyScopeMap -r myregistry --repository hello-world content/write metadata/read --repository hello-world-again content/read --description "Sample scope map."
  - name: Create a scope map that allows all repository actions for `test`, and all gateway actions for `connectedRegistry`.
    text: >
        az acr scope-map create -n MyScopeMap -r myregistry --description "Sample scope map."
          --repository test content/delete content/read content/write metadata/read metadata/write
          --gateway connectedRegistry config/read config/write message/read message/write

"""

helps['acr scope-map delete'] = """
type: command
short-summary: Delete a scope map for an Azure Container Registry.
examples:
  - name: Delete the scope map 'MyScopeMap'.
    text: >
        az acr scope-map delete -n MyScopeMap -r myregistry
"""

helps['acr scope-map list'] = """
type: command
short-summary: List all scope maps for an Azure Container Registry.
examples:
  - name: List scope maps under the registry 'myregistry'.
    text: >
        az acr scope-map list -r myregistry
"""

helps['acr scope-map show'] = """
type: command
short-summary: Show details and attributes of a scope map for an Azure Container Registry.
examples:
  - name: Get information for the scope map 'MyScopeMap'.
    text: >
        az acr scope-map show -n MyScopeMap -r myregistry
"""

helps['acr scope-map update'] = """
type: command
short-summary: Update a scope map for an Azure Container Registry.
examples:
  - name: Update the scope map 'MyScopeMap' removing metadata/read and content/read actions for `hello-world` repository, and message/write action for `connectedRegistry`.
    text: >
        az acr scope-map update -n MyScopeMap -r myregistry --remove-repo hello-world metadata/read content/read --remove-gateway connectedRegistry message/write
"""

helps['acr show'] = """
type: command
short-summary: Get the details of an Azure Container Registry.
examples:
  - name: Get the login server for an Azure Container Registry.
    text: >
        az acr show -n myregistry --query loginServer
  - name: Get the details of an Azure Container Registry
    text: az acr show --name myregistry --resource-group MyResourceGroup
    crafted: true
  - name: Check status of ABAC-based Repository Permission on a registry.
    text: >
        az acr show --name myregistry --resource-group MyResourceGroup --query roleAssignmentMode
"""

helps['acr show-usage'] = """
type: command
short-summary: Get the storage usage for an Azure Container Registry.
examples:
  - name: Get the storage usage for an Azure Container Registry.
    text: >
        az acr show-usage -n myregistry
"""

helps['acr task'] = """
type: group
short-summary: Manage a collection of steps for building, testing and OS & Framework patching container images using Azure Container Registries.
"""

helps['acr task cancel-run'] = """
type: command
short-summary: Cancel a specified run of an Azure Container Registry.
examples:
  - name: Cancel a run
    text: >
        az acr task cancel-run -r myregistry --run-id runId
"""

helps['acr task create'] = """
type: command
short-summary: Create a series of steps for building, testing and OS & Framework patching containers. Tasks support triggers from git commits and base image updates.
examples:
  - name: Create a task without the source location.
    text: >
        az acr task create -n hello-world -r myregistry --cmd '$Registry/myimage' -c /dev/null
  - name: Create a task with the definition from the standard input and with a timer trigger that runs the task at the top of every hour using the default trigger name. Either 'Ctrl + Z'(Windows) or 'Ctrl + D'(Linux) terminates the input stream.
    text: |
        cat task.yaml | az acr task create -n hello-world -r myregistry -f - -c /dev/null \\
            --schedule "0 */1 * * *"
        az acr task create -n hello-world -r myregistry -f - -c /dev/null --schedule "0 */1 * * *"
  - name: Create a Linux task from a public GitHub repository which builds the hello-world image without triggers and uses a build argument.
    text: |
        az acr task create -t hello-world:{{.Run.ID}} -n hello-world -r myregistry \\
            -c https://github.com/Azure/acr-builder.git -f Dockerfile \\
            --commit-trigger-enabled false --base-image-trigger-enabled false \\
            --arg DOCKER_CLI_BASE_IMAGE=docker:18.03.0-ce-git
  - name: Create a Linux task using a specific branch of a private Azure DevOps repository which builds the hello-world image on Arm architecture (V7 variant) and has triggers enabled.
    text: |
        az acr task create -t hello-world:{{.Run.ID}} -n hello-world -r myregistry \\
            -c https://msazure.visualstudio.com/DefaultCollection/Project/_git/Repo#Branch:Folder \\
            -f Dockerfile --git-access-token <Personal Access Token> --platform linux/arm/v7
  - name: Create a Linux task from a public GitHub repository which builds the hello-world image with both a git commit and pull request trigger enabled. Note that this task does not use Source Registry (myregistry), so we can explicitly set Auth mode as None for it.
    text: |
        az acr task create -t hello-world:{{.Run.ID}} -n hello-world -r myregistry  -f Dockerfile \\
            --no-push true --auth-mode None -c https://github.com/Azure-Samples/acr-build-helloworld-node.git \\
            --pull-request-trigger-enabled true --git-access-token 000000000000000000000000000000000
  - name: Create a Windows task from a public GitHub repository which builds the Azure Container Builder image on Amd64 architecture with only base image trigger enabled.
    text: |
        az acr task create -t acb:{{.Run.ID}} -n acb-win -r myregistry \\
            -c https://github.com/Azure/acr-builder.git -f Windows.Dockerfile \\
            --commit-trigger-enabled false --platform Windows/amd64
  - name: Create a Linux multi-step task from a public GitHub repository with both system-assigned and user-assigned managed identities and base image, git commit, pull request, and timer triggers that run the task at noon on Mondays through Fridays with the timer trigger name provided.
    text: |
        az acr task create -t hello-world:{{.Run.ID}} -n hello-world -r myregistry \\
            --pull-request-trigger-enabled true --schedule "dailyTimer:0 12 * * Mon-Fri" \\
            -c https://github.com/Azure-Samples/acr-tasks.git#:multipleRegistries -f testtask.yaml \\
            --assign-identity [system] "/subscriptions/<subscriptionId>/resourcegroups/<myResourceGroup>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<myUserAssignedIdentitiy>"
  - name: Create a task without the source location in an ABAC-based Repository Permission registry and specify a system-assigned managed identity used for auth with the source registry.
    text: >
        az acr task create -n hello-world -r myregistry --cmd '$Registry/myimage' -c /dev/null --source-acr-auth-id [system]
  - name: Create a task without the source location in an ABAC-based Repository Permission registry and specify a user-assigned managed identity used for auth with the source registry.
    text: >
        az acr task create -n hello-world -r myregistry --cmd '$Registry/myimage' -c /dev/null --source-acr-auth-id "/subscriptions/<subscriptionId>/resourcegroups/<myResourceGroup>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<myUserAssignedIdentitiy>"
  - name: Create a task without the source location in an ABAC-based Repository Permission registry with both system-assigned and user-assigned managed identities, and specify the system-assigned managed identity used for auth with the source registry.
    text: |
        az acr task create -n hello-world -r myregistry --cmd '$Registry/myimage' -c /dev/null --source-acr-auth-id [system]
            --assign-identity [system] "/subscriptions/<subscriptionId>/resourcegroups/<myResourceGroup>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<myUserAssignedIdentitiy>"
"""

helps['acr task credential'] = """
type: group
short-summary: Manage credentials for a task. Please see https://aka.ms/acr/tasks/cross-registry-authentication for more information.
"""

helps['acr task credential add'] = """
type: command
short-summary: Add a custom registry login credential to the task
examples:
  - name: Add a registry login credential to a task using a plain text username and password.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            -u myusername -p mysecret
  - name: Add a registry login credential to a task using key vault secret URIs for the username and password and the task system-assigned identity.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            -u https://mykeyvault.vault.azure.net/secrets/secretusername -p https://mykeyvault.vault.azure.net/secrets/secretpassword \\
            --use-identity [system]
  - name: Add a registry login credential to a task using key vault secret URIs for the username and password and a task user-assigned identity given by its client id.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            -u https://mykeyvault.vault.azure.net/secrets/secretusername -p https://mykeyvault.vault.azure.net/secrets/secretpassword \\
            --use-identity 00000000-0000-0000-0000-000000000000
  - name: Add a registry login credential to a task using a plain text username and key vault secret URI for the password and the task user-assigned identity given by its client id.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            -u myusername -p https://mykeyvault.vault.azure.net/secrets/secretpassword \\
            --use-identity 00000000-0000-0000-0000-000000000000
  - name: Add a registry login credential to a task using a plain text username and key vault secret URI for the password and the default managed identity for the task if one exists.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            -u myusername -p https://mykeyvault.vault.azure.net/secrets/secretpassword
  - name: Add a registry login credential to a task that uses only the task system-assigned identity to authenticate to the registry.
    text: |
        az acr task credential add -n taskname -r registryname --login-server myregistry.docker.io \\
            --use-identity [system]
"""

helps['acr task credential list'] = """
type: command
short-summary: List all the custom registry credentials for task.
examples:
  - name: List the Credentials for a task.
    text: >
        az acr task credential list -n taskname -r registryname
"""

helps['acr task credential remove'] = """
type: command
short-summary: Remove credential for a task.
examples:
  - name: Remove a registry login credential from a task.
    text: >
        az acr task credential remove -n taskname -r registryname --login-server myregistry.docker.io
"""

helps['acr task credential update'] = """
type: command
short-summary: Update the registry login credential for a task.
examples:
  - name: Update the credential for a task
    text: |
        az acr task credential update -n taskname -r registryname --login-server myregistry.docker.io \\
            -u myusername2 -p mysecret
"""

helps['acr task delete'] = """
type: command
short-summary: Delete a task from an Azure Container Registry.
examples:
  - name: Delete a task from an Azure Container Registry.
    text: >
        az acr task delete -n MyTask -r myregistry
"""

helps['acr task identity'] = """
type: group
short-summary: Managed Identities for Task. Please see https://aka.ms/acr/tasks/task-create-managed-identity for more information.
"""

helps['acr task identity assign'] = """
type: command
short-summary: Update the managed identity for a task.
examples:
  - name: Enable the system-assigned identity on an existing task. This will replace all existing user-assigned identities for that task.
    text: >
        az acr task identity assign -n MyTask -r myregistry
  - name: Assign user-assigned managed identities to an existing task. This will remove the existing system-assigned identity.
    text: |
        az acr task identity assign -n MyTask -r myregistry \\
            --identities "/subscriptions/<SUBSCRIPTON ID>/resourcegroups/<RESOURCE GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myUserAssignedIdentitiy"
  - name: Assign both system-assigned and user-assigned managed identities to an existing task.
    text: |
        az acr task identity assign -n MyTask -r myregistry \\
            --identities [system] "/subscriptions/<SUBSCRIPTON ID>/resourcegroups/<RESOURCE GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myUserAssignedIdentitiy"
"""

helps['acr task identity remove'] = """
type: command
short-summary: Remove managed identities for a task.
examples:
  - name: Remove the system-assigned identity from a task.
    text: >
        az acr task identity remove -n MyTask -r myregistry
  - name: Remove a user-assigned identity from a task.
    text: |
        az acr task identity remove -n MyTask -r myregistry \\
            --identities "/subscriptions/<SUBSCRIPTON ID>/resourcegroups/<RESOURCE GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myUserAssignedIdentitiy"
  - name: Remove all managed identities from a task.
    text: >
        az acr task identity remove -n MyTask -r myregistry --identities [all]
"""

helps['acr task identity show'] = """
type: command
short-summary: Display the managed identities for task.
examples:
  - name: Display the managed identities for a task.
    text: >
        az acr task identity show -n MyTask -r myregistry
"""

helps['acr task list'] = """
type: command
short-summary: List the tasks for an Azure Container Registry.
examples:
  - name: List tasks and show the results in a table.
    text: >
        az acr task list -r myregistry -o table
"""

helps['acr task list-runs'] = """
type: command
short-summary: List all of the executed runs for an Azure Container Registry, with the ability to filter by a specific Task.
examples:
  - name: List all of the runs for a registry and show the results in a table.
    text: >
        az acr task list-runs -r myregistry -o table
  - name: List runs for a task and show the results in a table.
    text: >
        az acr task list-runs -r myregistry -n MyTask -o table
  - name: List the last 10 successful runs for a registry and show the results in a table.
    text: >
        az acr task list-runs -r myregistry --run-status Succeeded --top 10 -o table
  - name: List all of the runs that built the image 'hello-world' for a registry and show the results in a table.
    text: >
        az acr task list-runs -r myregistry --image hello-world -o table
"""

helps['acr task logs'] = """
type: command
short-summary: Show logs for a particular run. If no run-id is supplied, show logs for the last created run.
examples:
  - name: Show logs for the last created run in the registry.
    text: >
        az acr task logs -r myregistry
  - name: Show logs for the last created run in the registry, filtered by task.
    text: >
        az acr task logs -r myregistry -n MyTask
  - name: Show logs for a particular run.
    text: >
        az acr task logs -r myregistry --run-id runId
  - name: Show logs for the last created run in the registry that built the image 'hello-world'.
    text: >
        az acr task logs -r myregistry --image hello-world
"""

helps['acr task run'] = """
type: command
short-summary: Manually trigger a task that might otherwise be waiting for git commits or base image update triggers.
examples:
  - name: Trigger a task run.
    text: >
        az acr task run -n MyTask -r myregistry
  - name: Trigger a task run by overriding the context and file passed during Task create with a remote repository.
    text: >
        az acr task run -n MyTask -r myregistry -c https://github.com/Azure-Samples/acr-build-helloworld-node.git -f Dockerfile
  - name: Trigger a task run by overriding the context and file passed during Task create with a local context.
    text: >
        az acr task run -n MyTask -r myregistry -c . -f Dockerfile
  - name: Trigger a task run by adding or overriding build arguments set during Task create.
    text: |
        az acr task run -n MyTask -r myregistry --arg DOCKER_CLI_BASE_IMAGE=docker:18.03.0-ce-git
"""

helps['acr task show'] = """
type: command
short-summary: Get the properties of a named task for an Azure Container Registry.
examples:
  - name: Get the properties of a task, displaying the results in a table.
    text: >
        az acr task show -n MyTask -r myregistry -o table

  - name: Get the properties of a task, including secure properties.
    text: >
        az acr task show -n MyTask -r myregistry --with-secure-properties
"""

helps['acr task show-run'] = """
type: command
short-summary: Get the properties of a specified run of an Azure Container Registry Task.
examples:
  - name: Get the details of a run, displaying the results in a table.
    text: >
        az acr task show-run -r myregistry --run-id runId -o table
"""

helps['acr task timer'] = """
type: group
short-summary: Manage timer triggers for a task
"""

helps['acr task timer add'] = """
type: command
short-summary: Add a timer trigger to a task.
examples:
  - name: Add a timer trigger which schedules the task at 09:30 (UTC) every day of the week from Monday through Friday.
    text: >
        az acr task timer add -n taskname -r registryname --timer-name t2 --schedule "30 9 * * 1-5"
"""

helps['acr task timer list'] = """
type: command
short-summary: List all timer triggers for a task.
examples:
  - name: List all timer triggers for a task.
    text: >
        az acr task timer list -n taskname -r registryname
"""

helps['acr task timer remove'] = """
type: command
short-summary: Remove a timer trigger from a task.
examples:
  - name: Remove a timer trigger from a task.
    text: >
        az acr task timer remove -n taskname -r registryname --timer-name t2
"""

helps['acr task timer update'] = """
type: command
short-summary: Update the timer trigger for a task.
examples:
  - name: Update the schedule of a timer trigger for a task.
    text: >
        az acr task timer update -n taskname -r registryname --timer-name t2 --schedule "0 12 * * *"
  - name: Update the status of a timer trigger for a task.
    text: >
        az acr task timer update -n taskname -r registryname --timer-name t2 --enabled False
"""

helps['acr task update'] = """
type: command
short-summary: Update a task for an Azure Container Registry.
examples:
  - name: Update base image updates to trigger on all dependent images of a multi-stage dockerfile, and status of a task in an Azure Container Registry.
    text: >
        az acr task update -n MyTask -r myregistry --base-image-trigger-type All --status Disabled
  - name: Update platform for the Build step of your Task to Windows (prev Linux).
    text: >
        az acr task update -n MyTask -r myregistry --platform Windows
  - name: Update task's triggers and context for an Azure Container Registry.
    text: |
        az acr task update -n hello-world -r myregistry -f Dockerfile \\
            --commit-trigger-enabled false --pull-request-trigger-enabled true \\
            -c https://msazure.visualstudio.com/DefaultCollection/Project/_git/Repo#Branch:Folder
  - name: Update a task for an Azure Container Registry. (autogenerated)
    text: |
        az acr task update --image MyImage --name MyTask --registry myregistry \\
            --context https://github.com/Azure-Samples/acr-build-helloworld-node.git
    crafted: true
  - name: Update the task using the system-assigned managed identity for authentication with the source registry in Azure Container Registry.
    text: >
        az acr task update -n MyTask -r myregistry --source-acr-auth-id [system]
  - name: Update the task using the user-assigned managed identity for authentication with the source registry in Azure Container Registry.
    text: >
        az acr task update -n MyTask -r myregistry --source-acr-auth-id "/subscriptions/<subscriptionId>/resourcegroups/<myResourceGroup>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<myUserAssignedIdentitiy>"
"""

helps['acr task update-run'] = """
type: command
short-summary: Patch the run properties of an Azure Container Registry Task.
examples:
  - name: Update an existing run to be archived.
    text: >
        az acr task update-run -r myregistry --run-id runId --no-archive false
"""

helps['acr taskrun'] = """
type: group
short-summary: Manage taskruns using Azure Container Registries.
"""


helps['acr taskrun delete'] = """
type: command
short-summary: Delete a taskrun from an Azure Container Registry.
examples:
  - name: Delete a taskrun from an Azure Container Registry.
    text: >
        az acr taskrun delete -r myregistry -n MyTaskRun -g MyResourceGroup
"""

helps['acr taskrun list'] = """
type: command
short-summary: List the taskruns for an Azure Container Registry.
examples:
  - name: List taskruns and show the results in a table.
    text: >
        az acr taskrun list -r myregistry -g MyResourceGroup -o table
"""

helps['acr taskrun show'] = """
type: command
short-summary: Get the properties of a named taskrun for an Azure Container Registry.
examples:
  - name: Get the properties of a taskrun, displaying the results in a table.
    text: >
        az acr taskrun show -r myregistry -n MyTaskRun -o table
"""

helps['acr taskrun logs'] = """
type: command
short-summary: Show run logs for a particular taskrun.
examples:
  - name: Show run logs for a particular taskrun.
    text: >
        az acr taskrun logs -r myregistry -n MyTaskRun
"""

helps['acr token'] = """
type: group
short-summary: Manage tokens for an Azure Container Registry.
"""

helps['acr token create'] = """
type: command
short-summary: Create a token associated with a scope map for an Azure Container Registry.
examples:
  - name: Create a token with repository permissions defined in the scope map 'MyScopeMap'.
    text: >
        az acr token create -n MyToken -r myregistry --scope-map MyScopeMap
  - name: Create a token which has read permissions on hello-world repository.
    text: >
        az acr token create -n myToken -r myregistry --repository hello-world content/read metadata/read
  - name: Create a token without credentials and with all gateway permissions.
    text: |
        az acr token create -n myToken -r myregistry --repository hello-world content/read
          --gateway registry config/read config/write message/read message/write --no-passwords
  - name: Create a token in disabled status.
    text: >
        az acr token create -n MyToken -r myregistry --scope-map MyScopeMap --status disabled
"""

helps['acr token credential'] = """
type: group
short-summary: Manage credentials of a token for an Azure Container Registry.
"""

helps['acr token credential delete'] = """
type: command
short-summary: Delete a token credential.
examples:
  - name: Delete both passwords for the token 'MyToken'.
    text: az acr token credential delete -n MyToken -r myregistry --password1 --password2
"""

helps['acr token credential generate'] = """
type: command
short-summary: Generate or replace one or both passwords of a token for an Azure Container Registry. For using token and password to access a container registry, see https://aka.ms/acr/repo-permissions.
examples:
  - name: Generate password1 for the token 'MyToken', with an expiration of 30 days.
    text: az acr token credential generate -n MyToken -r myregistry --password1 --days 30
"""

helps['acr token delete'] = """
type: command
short-summary: Delete a token for an Azure Container Registry.
examples:
  - name: Delete the token 'MyToken'.
    text: >
        az acr token delete -n MyToken -r myregistry
"""

helps['acr token list'] = """
type: command
short-summary: List all tokens for an Azure Container Registry.
examples:
  - name: List tokens under the registry 'myregistry'.
    text: >
        az acr token list -r myregistry
"""

helps['acr token show'] = """
type: command
short-summary: Show details and attributes of a token for an Azure Container Registry.
examples:
  - name: Get information for the token 'MyToken'.
    text: >
        az acr token show -n MyToken -r myregistry
"""

helps['acr token update'] = """
type: command
short-summary: Update a token (replace associated scope map) for an Azure Container Registry.
examples:
  - name: Update the token 'MyToken', making it associated with the scope map 'MyNewScopeMap'.
    text: >
        az acr token update -n MyToken -r myregistry --scope-map MyNewScopeMap
"""

helps['acr artifact-streaming'] = """
type: group
short-summary: Manage artifact streaming for any repositories or supported images in an ACR.
"""

helps['acr artifact-streaming operation'] = """
type: group
short-summary: Manage the streaming artifact creation operations for ACR.
"""

helps['acr artifact-streaming operation cancel'] = """
type: command
short-summary: Cancel the given streaming artifact operation for ACR.
examples:
  - name: Cancel the streaming artifact creation associated with the id 'OperationId' under repository 'MyRepo' in ACR 'myregistry'.
    text: >
        az acr artifact-streaming operation cancel -n myregistry --repository MyRepo --id OperationId
"""

helps['acr artifact-streaming operation show'] = """
type: command
short-summary: Check the operation status for artifact streaming in an ACR.
examples:
  - name: Get the streaming artifact creation status for id 'OperationId' under repository 'MyRepo' in ACR 'myregistry'.
    text: >
        az acr artifact-streaming operation show -n myregistry --repository MyRepo --id OperationId
"""

helps['acr artifact-streaming create'] = """
type: command
short-summary: Create a referrers streaming artifact for a specific image in an ACR.
examples:
  - name: Create the streaming artifact of 'MyImage' in the registry 'myregistry'.
    text: >
        az acr artifact-streaming create -n myregistry -t MyImage
"""

helps['acr artifact-streaming update'] = """
type: command
short-summary: Enable or disable auto-creation of streaming artifacts for newly pushed images under a given registry.
long-summary: Enable or disable auto-creation of streaming artifacts for newly pushed images under a given registry. Note that whenever the flag is enabled, new images pushed into the selected registry will have auto-creation enabled and will be associated with the original image as a referrers artifact.
examples:
  - name: Enable artifact streaming for 'MyRepository' associated with the registry 'myregistry'.
    text: >
        az acr artifact-streaming update -n myregistry --repository MyRepository --enable-streaming True
  - name: Disable artifact streaming for 'MyRepository' associated with the registry 'myregistry'.
    text: >
        az acr artifact-streaming update -n myregistry --repository MyRepository --enable-streaming False
"""

helps['acr artifact-streaming show'] = """
type: command
short-summary: Show if artifact streaming is enabled in a repository for an Azure Container Registry.
examples:
  - name: Get the repository 'MyRepo' streaming status.
    text: >
        az acr artifact-streaming show -n myregistry --repository MyRepo
"""

helps['acr agentpool'] = """
type: group
short-summary: Manage private Tasks agent pools with Azure Container Registries.
"""

helps['acr agentpool create'] = """
type: command
short-summary: Create an agent pool for an Azure Container Registry.
examples:
  - name: Create the agent pool 'MyAgentName' associated with the registry 'myregistry'.
    text: >
        az acr agentpool create -n MyAgentName -r myregistry
  - name: Create the agent pool 'MyAgentName' with 2 agent count.
    text: >
        az acr agentpool create -n MyAgentName -r myregistry --count 2
  - name: Create the agent pool 'MyAgentName' associated with the registry 'myregistry' in VNET subnet.
    text: >
        az acr agentpool create -n MyAgentName -r myregistry --subnet-id /subscriptions/<SubscriptionId>/resourceGroups/<ResourceGroupName>/providers/Microsoft.ClassicNetwork/virtualNetworks/<myNetwork>/subnets/<subNet>
"""

helps['acr agentpool update'] = """
type: command
short-summary: Update an agent pool for an Azure Container Registry.
examples:
  - name: Update the agent pool 'MyAgentName' count to 5
    text: >
        az acr agentpool update -n MyAgentName -r myregistry --count 5
"""

helps['acr agentpool delete'] = """
type: command
short-summary: Delete an agent pool.
examples:
  - name: Delete the agent pool 'MyAgentName'.
    text: >
        az acr agentpool delete -n MyAgentName -r myregistry
"""

helps['acr agentpool list'] = """
type: command
short-summary: List the agent pools for an Azure Container Registry.
examples:
  - name: List agent pools and show the result in a table.
    text: >
        az acr agentpool list -r myregistry -o table
"""

helps['acr agentpool show'] = """
type: command
short-summary: Get the properties of a specified agent pool for an Azure Container Registry.
examples:
  - name: Get the properties of an agent pool, displaying the results in a table.
    text: >
        az acr agentpool show -n MyAgentName -r myregistry -o table
"""


helps['acr update'] = """
type: command
short-summary: Update an Azure Container Registry.
examples:
  - name: Update tags for an Azure Container Registry.
    text: >
        az acr update -n myregistry --tags key1=value1 key2=value2
  - name: Enable the administrator user account for an Azure Container Registry.
    text: >
        az acr update -n myregistry --admin-enabled true
  - name: Turn on ABAC-based Repository Permission on an existing registry.
    text: >
        az acr update -n myregistry --role-assignment-mode rbac-abac
"""

helps['acr webhook'] = """
type: group
short-summary: Manage webhooks for Azure Container Registries.
"""

helps['acr webhook create'] = """
type: command
short-summary: Create a webhook for an Azure Container Registry.
examples:
  - name: Create a webhook for an Azure Container Registry that will deliver docker push and delete events to a service URI.
    text: >
        az acr webhook create -n mywebhook -r myregistry --uri http://myservice.com --actions push delete
  - name: Create a webhook for an Azure Container Registry that will deliver docker push events to a service URI with a basic authentication header.
    text: >
        az acr webhook create -n mywebhook -r myregistry --uri http://myservice.com --actions push --headers "Authorization=Basic 000000"
  - name: Create a webhook for an Azure Container Registry that will deliver helm chart push and delete events to a service URI.
    text: >
        az acr webhook create -n mywebhook -r myregistry --uri http://myservice.com --actions chart_push chart_delete
"""

helps['acr webhook delete'] = """
type: command
short-summary: Delete a webhook from an Azure Container Registry.
examples:
  - name: Delete a webhook from an Azure Container Registry.
    text: >
        az acr webhook delete -n mywebhook -r myregistry
"""

helps['acr webhook get-config'] = """
type: command
short-summary: Get the service URI and custom headers for the webhook.
examples:
  - name: Get the configuration information for a webhook.
    text: >
        az acr webhook get-config -n mywebhook -r myregistry
"""

helps['acr webhook list'] = """
type: command
short-summary: List all of the webhooks for an Azure Container Registry.
examples:
  - name: List webhooks and show the results in a table.
    text: >
        az acr webhook list -r myregistry -o table
"""

helps['acr webhook list-events'] = """
type: command
short-summary: List recent events for a webhook.
examples:
  - name: List recent events for a webhook.
    text: >
        az acr webhook list-events -n mywebhook -r myregistry
"""

helps['acr webhook ping'] = """
type: command
short-summary: Trigger a ping event for a webhook.
examples:
  - name: Trigger a ping event for a webhook.
    text: >
        az acr webhook ping -n mywebhook -r myregistry
"""

helps['acr webhook show'] = """
type: command
short-summary: Get the details of a webhook.
examples:
  - name: Get the details of a webhook.
    text: >
        az acr webhook show -n mywebhook -r myregistry
"""

helps['acr webhook update'] = """
type: command
short-summary: Update a webhook.
examples:
  - name: Update headers for a webhook.
    text: >
        az acr webhook update -n mywebhook -r myregistry --headers "Authorization=Basic 000000"
  - name: Update the service URI and actions for a webhook.
    text: >
        az acr webhook update -n mywebhook -r myregistry --uri http://myservice.com --actions push delete
  - name: Disable a webhook.
    text: >
        az acr webhook update -n mywebhook -r myregistry --status disabled
"""

# region connected-registry
helps['acr connected-registry'] = """
type: group
short-summary: Manage connected registry resources with Azure Container Registries.
"""

helps['acr connected-registry create'] = """
type: command
short-summary: Create a connected registry for an Azure Container Registry.
examples:
  - name: Create a connected registry in registry mode with access to repos app/hello-world and service/mycomponent. It'll create a sync token and scope-map with the right repo permissions.
    text: |
        az acr connected-registry create --registry mycloudregistry --name myconnectedregistry \\
            --repository "app/hello-world" "service/mycomponent"
  - name: Create a read only connected registry with only read permissions and pass the sync token
    text: |
        az acr connected-registry create --registry mycloudregistry  --name myreadonlyacr \\
            --mode readonly --parent myconnectedregistry --sync-token mySyncTokenName
  - name: Create a read only connected registry with client tokens, that syncs every day at midninght and sync window of 4 hours.
    text: |
        az acr connected-registry create -r mycloudregistry -n myreadonlyacr -p myconnectedregistry \\
            --repository "app/mycomponent" -m ReadOnly -s "0 12 * * *" -w PT4H \\
            --client-tokens myTokenName1 myTokenName2
"""

helps['acr connected-registry delete'] = """
type: command
short-summary: Delete a connected registry from Azure Container Registry.
examples:
  - name: Delete a read only connected registry 'myconnectedregistry' from parent registry 'mycloudregistry'.
    text: >
        az acr connected-registry delete --registry mycloudregistry --name myconnectedregistry
  - name: Delete a read only connected registry 'myconnectedregistry' and it's sync token and scope-map from parent registry 'mycloudregistry'.
    text: >
        az acr connected-registry delete -r mycloudregistry -n myconnectedregistry --cleanup
"""

helps['acr connected-registry deactivate'] = """
type: command
short-summary: Deactivate a connected registry from Azure Container Registry.
examples:
  - name: Deactivate a connected registry 'myconnectedregistry'.
    text: >
        az acr connected-registry deactivate -r mycloudregistry -n myconnectedregistry
"""

helps['acr connected-registry list'] = """
type: command
short-summary: List all the connected registries under the current parent registry.
examples:
  - name: List all the connected registries of 'mycloudregistry' in table format.
    text: >
        az acr connected-registry list --registry mycloudregistry --output table
  - name: List only the inmediate children of 'mycloudregistry' in expanded form in a table.
    text: >
        az acr connected-registry list --registry mycloudregistry --no-children --output table
  - name: List all the offspring of 'myconnectedregistry' in expanded form inside a table.
    text: >
        az acr connected-registry list -r mycloudregistry -p myconnectedregistry --output table
"""

helps['acr connected-registry list-client-tokens'] = """
type: command
short-summary: List all the client tokens associated to a specific connected registries.
examples:
  - name: List all client tokens of 'myreadonlyacr'.
    text: >
        az acr connected-registry list-client-tokens -r mycloudregistry -n myreadonlyacr -o table
"""

helps['acr connected-registry show'] = """
type: command
short-summary: Show connected registry details.
examples:
  - name: Show all the details of the 'myreadonlyacr' registry in table form.
    text: >
        az acr connected-registry show --registry mycloudregistry --name myreadonlyacr --output table
"""

helps['acr connected-registry update'] = """
type: command
short-summary: Update a connected registry for an Azure Container Registry.
examples:
  - name: Update the connected registry client Tokens.
    text: |
        az acr connected-registry update --registry mycloudregistry --name myconnectedregistry \\
            --remove-client-tokens myTokenName1 --add-client-tokens myTokenName2 myTokenName3

  - name: Update the sync and window time of a connected registry.
    text: |
        az acr connected-registry update --registry mycloudregistry --name myreadonlyacr \\
            --sync-schedule "0 12 * * *" --sync-window PT4H
"""

helps['acr connected-registry get-settings'] = """
type: command
short-summary: Retrieve information required to activate a connected registry, and creates or rotates the sync token credentials.
examples:
  - name: Get the settings information required to install a connected registry without the password.
    text: >
        az acr connected-registry get-settings -r mycloudregistry -n myconnectedregistry --parent-protocol http
  - name: Generate a new sync token password 1 or rotates the password if it already exists, and gets the settings information required to install a connected registry.
    text: >
        az acr connected-registry get-settings -r mycloudregistry -n myconnectedregistry --generate-password 1 --parent-protocol https
"""

helps['acr connected-registry permissions'] = """
type: group
short-summary: Manage the repository permissions accross multiple connected registries. Please see https://aka.ms/acr/connected-registry for more information.
"""

helps['acr connected-registry permissions update'] = """
type: command
short-summary: Add and remove repository permissions accross all the necessary connected registry sync scope maps.
examples:
  - name: Add permissions to synchronize images from 'repo1' and 'repo2' to the connected registry 'myconnectedregistry' and its ancestors.
    text: >
        az acr connected-registry permissions update -r mycloudregistry -n myconnectedregistry --add repo1 repo2
  - name: Remove permissions to synchronize images from 'repo1' and 'repo2' to the connected registry 'myconnectedregistry' and its descendants.
    text: >
        az acr connected-registry permissions update -r mycloudregistry -n myconnectedregistry --remove repo1 repo2
  - name: Remove permissions to synchronize 'repo1' images and adds permissions for 'repo2' images.
    text: >
        az acr connected-registry permissions update -r mycloudregistry -n myconnectedregistry --remove repo1 --add repo2
"""

helps['acr connected-registry permissions show'] = """
type: command
short-summary: Show the connected registry sync scope map information.
examples:
  - name: Show details and attributes of a sync scope map for a connected registry.
    text: >
        az acr connected-registry permissions show -r mycloudregistry -n myconnectedregistry
"""

# To be deprecated
helps['acr connected-registry install'] = """
type: group
short-summary: Help to access the necessary information for installing a connected registry. Please see https://aka.ms/acr/connected-registry for more information.
"""

helps['acr connected-registry install info'] = """
type: command
short-summary: Retrieve information required to activate a connected registry.
examples:
  - name: Set http as the parent protocol, and prints the values required to activate a connected registry in json format
    text: >
        az acr connected-registry install info --registry mycloudregistry --name myconnectedregistry --parent-protocol http
"""

helps['acr connected-registry install renew-credentials'] = """
type: command
short-summary: Retrieve information required to activate a connected registry, and renews the sync token credentials.
examples:
  - name: Set http as the parent protocol, and prints the values in json format required to activate a connected registry and the newly generated sync token credentials.
    text: >
        az acr connected-registry install renew-credentials -r mycloudregistry -n myconnectedregistry --parent-protocol http
"""

helps['acr connected-registry repo'] = """
type: command
short-summary: Update all the necessary connected registry sync scope maps repository permissions.
examples:
  - name: Add permissions to synchronize images from 'repo1' and 'repo2' to the connected registry 'myconnectedregistry' and its ancestors.
    text: >
        az acr connected-registry repo -r mycloudregistry -n myconnectedregistry --add repo1 repo2
  - name: Remove permissions to synchronize images from 'repo1' and 'repo2' to the connected registry 'myconnectedregistry' and its descendants.
    text: >
        az acr connected-registry repo -r mycloudregistry -n myconnectedregistry --remove repo1 repo2
  - name: Remove permissions to synchronize 'repo1' images and adds permissions for 'repo2' images.
    text: >
        az acr connected-registry repo -r mycloudregistry -n myconnectedregistry --remove repo1 --add repo2
"""
# endregion

# region private-endpoint-connection
# be careful to keep long-summary consistent in this region
helps['acr private-endpoint-connection'] = """
type: group
short-summary: Manage container registry private endpoint connections
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-endpoint-connection approve'] = """
type: command
short-summary: Approve a private endpoint connection request for a container registry
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-endpoint-connection reject'] = """
type: command
short-summary: Reject a private endpoint connection request for a container registry
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-endpoint-connection list'] = """
type: command
short-summary: List all private endpoint connections to a container registry
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-endpoint-connection show'] = """
type: command
short-summary:  Show details of a container registry's private endpoint connection
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-endpoint-connection delete'] = """
type: command
short-summary:  Delete a private endpoint connection request for a container registry
long-summary: To create a private endpoint connection use "az network private-endpoint create". For more information see https://aka.ms/acr/private-link
"""

helps['acr private-link-resource'] = """
type: group
short-summary: Manage registry private link resources.
"""

helps['acr private-link-resource list'] = """
type: command
short-summary: list the private link resources supported for a registry
"""
# endregion

# region encryption
helps['acr encryption'] = """
type: group
short-summary: Manage container registry encryption
long-summary: For more information, see http://aka.ms/acr/cmk
"""

helps['acr encryption rotate-key'] = """
type: command
short-summary: Rotate (update) the container registry's encryption key
long-summary: For more information, see http://aka.ms/acr/cmk
"""

helps['acr encryption show'] = """
type: command
short-summary: Show the container registry's encryption details
long-summary: For more information, see http://aka.ms/acr/cmk
"""
# endregion

# region identity
helps['acr identity'] = """
type: group
short-summary: Manage service (managed) identities for a container registry
"""

helps['acr identity assign'] = """
type: command
short-summary: Assign a managed identity to a container registry
long-summary: Managed identities can be user-assigned or system-assigned
"""

helps['acr identity remove'] = """
type: command
short-summary: Remove a managed identity from a container registry
"""

helps['acr identity show'] = """
type: command
short-summary: Show the container registry's identity details
"""

helps['acr show-endpoints'] = """
type: command
short-summary: Display registry endpoints
"""
# endregion
