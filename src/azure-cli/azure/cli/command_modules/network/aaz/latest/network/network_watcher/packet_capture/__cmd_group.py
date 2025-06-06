# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network network-watcher packet-capture",
)
class __CMDGroup(AAZCommandGroup):
    """These commands require that both Azure Network Watcher is enabled for the VMs region and that AzureNetworkWatcherExtension is enabled on the VM.
    """
    pass


__all__ = ["__CMDGroup"]
