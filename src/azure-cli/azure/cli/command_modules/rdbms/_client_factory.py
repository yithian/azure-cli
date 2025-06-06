# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.cli.core.profiles import ResourceType
from azure.cli.core.auth.identity import get_environment_credential, AZURE_CLIENT_ID

# pylint: disable=import-outside-toplevel

RM_URI_OVERRIDE = 'AZURE_CLI_RDBMS_RM_URI'
SUB_ID_OVERRIDE = 'AZURE_CLI_RDBMS_SUB_ID'


def get_mariadb_management_client(cli_ctx, **_):
    from os import getenv
    from azure.mgmt.rdbms.mariadb import MariaDBManagementClient

    # Allow overriding resource manager URI using environment variable
    # for testing purposes. Subscription id is also determined by environment
    # variable.
    rm_uri_override = getenv(RM_URI_OVERRIDE)
    if rm_uri_override:
        client_id = getenv(AZURE_CLIENT_ID)
        if client_id:
            credentials = get_environment_credential()
        else:
            from msrest.authentication import Authentication  # pylint: disable=import-error
            credentials = Authentication()

        return MariaDBManagementClient(
            subscription_id=getenv(SUB_ID_OVERRIDE),
            base_url=rm_uri_override,
            credential=credentials)
    # Normal production scenario.
    return get_mgmt_service_client(cli_ctx, MariaDBManagementClient)


def get_mysql_management_client(cli_ctx, **_):
    from os import getenv
    from azure.mgmt.rdbms.mysql import MySQLManagementClient

    # Allow overriding resource manager URI using environment variable
    # for testing purposes. Subscription id is also determined by environment
    # variable.
    rm_uri_override = getenv(RM_URI_OVERRIDE)
    if rm_uri_override:
        client_id = getenv(AZURE_CLIENT_ID)
        if client_id:
            credentials = get_environment_credential()
        else:
            from msrest.authentication import Authentication  # pylint: disable=import-error
            credentials = Authentication()

        return MySQLManagementClient(
            subscription_id=getenv(SUB_ID_OVERRIDE),
            base_url=rm_uri_override,
            credential=credentials)
    # Normal production scenario.
    return get_mgmt_service_client(cli_ctx, MySQLManagementClient)


def get_mysql_flexible_management_client(cli_ctx, **_):
    from os import getenv
    from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient

    # Allow overriding resource manager URI using environment variable
    # for testing purposes. Subscription id is also determined by environment
    # variable.
    rm_uri_override = getenv(RM_URI_OVERRIDE)
    if rm_uri_override:
        client_id = getenv(AZURE_CLIENT_ID)
        if client_id:
            credentials = get_environment_credential()
        else:
            from msrest.authentication import Authentication  # pylint: disable=import-error
            credentials = Authentication()

        return MySQLManagementClient(
            subscription_id=getenv(SUB_ID_OVERRIDE),
            base_url=rm_uri_override,
            credential=credentials)
    # Normal production scenario.
    return get_mgmt_service_client(cli_ctx, MySQLManagementClient)


def get_postgresql_management_client(cli_ctx, **_):
    from os import getenv
    from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient

    # Allow overriding resource manager URI using environment variable
    # for testing purposes. Subscription id is also determined by environment
    # variable.
    rm_uri_override = getenv(RM_URI_OVERRIDE)
    if rm_uri_override:
        client_id = getenv(AZURE_CLIENT_ID)
        if client_id:
            credentials = get_environment_credential()
        else:
            from msrest.authentication import Authentication  # pylint: disable=import-error
            credentials = Authentication()

        return PostgreSQLManagementClient(
            subscription_id=getenv(SUB_ID_OVERRIDE),
            base_url=rm_uri_override,
            credential=credentials)
    # Normal production scenario.
    return get_mgmt_service_client(cli_ctx, PostgreSQLManagementClient)


def get_postgresql_flexible_management_client(cli_ctx, subscription_id=None, **_):
    from os import getenv
    from azure.mgmt.postgresqlflexibleservers import PostgreSQLManagementClient
    # Allow overriding resource manager URI using environment variable
    # for testing purposes. Subscription id is also determined by environment
    # variable.
    rm_uri_override = getenv(RM_URI_OVERRIDE)
    subscription = subscription_id if subscription_id is not None else getenv(SUB_ID_OVERRIDE)
    if rm_uri_override:
        client_id = getenv(AZURE_CLIENT_ID)
        if client_id:
            credentials = get_environment_credential()
        else:
            from msrest.authentication import Authentication  # pylint: disable=import-error
            credentials = Authentication()

        return PostgreSQLManagementClient(
            subscription_id=subscription,
            base_url=rm_uri_override,
            credential=credentials)
    # Normal production scenario.
    return get_mgmt_service_client(cli_ctx, PostgreSQLManagementClient, subscription_id=subscription)


def cf_mariadb_servers(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).servers


def cf_mysql_servers(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).servers


def cf_postgres_servers(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).servers


def cf_mariadb_firewall_rules(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).firewall_rules


def cf_mysql_firewall_rules(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).firewall_rules


def cf_postgres_firewall_rules(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).firewall_rules


def cf_mariadb_config(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).configurations


def cf_mysql_config(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).configurations


def cf_postgres_config(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).configurations


def cf_mariadb_log(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).log_files


def cf_mysql_log(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).log_files


def cf_postgres_log(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).log_files


def cf_mariadb_db(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).databases


def cf_mysql_db(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).databases


def cf_postgres_db(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).databases


def cf_mariadb_virtual_network_rules_operations(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).virtual_network_rules


def cf_mysql_virtual_network_rules_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).virtual_network_rules


def cf_postgres_virtual_network_rules_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).virtual_network_rules


def cf_mariadb_replica(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).replicas


def cf_mysql_replica(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).replicas


def cf_postgres_replica(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).replicas


def cf_mariadb_private_endpoint_connections_operations(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).private_endpoint_connections


def cf_mariadb_private_link_resources_operations(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).private_link_resources


def cf_mysql_private_endpoint_connections_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).private_endpoint_connections


def cf_mysql_private_link_resources_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).private_link_resources


def cf_postgres_private_endpoint_connections_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).private_endpoint_connections


def cf_postgres_private_link_resources_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).private_link_resources


def cf_mysql_server_keys_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).server_keys


def cf_postgres_server_keys_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).server_keys


def cf_mysql_server_ad_administrators_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).server_administrators


def cf_postgres_server_ad_administrators_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).server_administrators


def cf_mariadb_check_resource_availability_sterling(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).check_name_availability


def cf_mysql_check_resource_availability_sterling(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).check_name_availability


def cf_postgres_check_resource_availability_sterling(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).check_name_availability


def cf_mysql_location_based_performance_tier_operations(cli_ctx, _):
    return get_mysql_management_client(cli_ctx).location_based_performance_tier


def cf_postgres_location_based_performance_tier_operations(cli_ctx, _):
    return get_postgresql_management_client(cli_ctx).location_based_performance_tier


def cf_mariadb_location_based_performance_tier_operations(cli_ctx, _):
    return get_mariadb_management_client(cli_ctx).location_based_performance_tier


# Meru operations for flexible servers
def cf_mysql_flexible_servers(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).servers


def cf_mysql_flexible_firewall_rules(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).firewall_rules


def cf_mysql_flexible_config(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).configurations


def cf_mysql_flexible_db(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).databases


def cf_mysql_flexible_replica(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).replicas


def cf_mysql_flexible_location_capabilities(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).location_based_capabilities


def cf_mysql_flexible_log(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).log_files


def cf_mysql_flexible_backups(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).backups


def cf_mysql_flexible_adadmin(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).azure_ad_administrators


def cf_mysql_check_resource_availability(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).check_name_availability


def cf_mysql_check_resource_availability_without_location(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).check_name_availability_without_location


def cf_mysql_flexible_private_dns_zone_suffix_operations(cli_ctx, _):
    return get_mysql_flexible_management_client(cli_ctx).get_private_dns_zone_suffix


def cf_postgres_flexible_servers(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).servers


def cf_postgres_flexible_firewall_rules(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).firewall_rules


def cf_postgres_flexible_virtual_endpoints(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).virtual_endpoints


def cf_postgres_flexible_config(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).configurations


def cf_postgres_flexible_replica(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).replicas


def cf_postgres_flexible_location_capabilities(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).location_based_capabilities


def cf_postgres_flexible_server_capabilities(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).server_capabilities


def cf_postgres_flexible_backups(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).backups


def cf_postgres_flexible_ltr_backups(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).ltr_backup_operations


def cf_postgres_flexible_operations(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).flexible_server


def cf_postgres_flexible_admin(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).administrators


def cf_postgres_flexible_migrations(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).migrations


def cf_postgres_flexible_server_threat_protection_settings(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).server_threat_protection_settings


def cf_postgres_flexible_server_log_files(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).log_files


def cf_postgres_check_resource_availability(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).check_name_availability


def cf_postgres_flexible_db(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).databases


def cf_postgres_check_resource_availability_with_location(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).check_name_availability_with_location


def cf_postgres_flexible_private_dns_zone_suffix_operations(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).get_private_dns_zone_suffix


def cf_postgres_flexible_private_endpoint_connections(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).private_endpoint_connections


def cf_postgres_flexible_private_endpoint_connection(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).private_endpoint_connection


def cf_postgres_flexible_private_link_resources(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).private_link_resources


def cf_postgres_flexible_tuning_options(cli_ctx, _):
    return get_postgresql_flexible_management_client(cli_ctx).tuning_options


def resource_client_factory(cli_ctx, subscription_id=None):
    return get_mgmt_service_client(cli_ctx, ResourceType.MGMT_RESOURCE_RESOURCES, subscription_id=subscription_id)


def private_dns_client_factory(cli_ctx, subscription_id=None):
    from azure.mgmt.privatedns import PrivateDnsManagementClient
    return get_mgmt_service_client(cli_ctx, PrivateDnsManagementClient, subscription_id=subscription_id).private_zones


def private_dns_link_client_factory(cli_ctx, subscription_id=None):
    from azure.mgmt.privatedns import PrivateDnsManagementClient
    return get_mgmt_service_client(cli_ctx, PrivateDnsManagementClient,
                                   subscription_id=subscription_id).virtual_network_links
