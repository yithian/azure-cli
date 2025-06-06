# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vnet-gateway list",
)
class List(AAZCommand):
    """List virtual network gateways.

    :example: List virtual network gateways in a resource group.
        az network vnet-gateway list -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2024-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways", "2024-07-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VirtualNetworkGatewaysList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _element.id = AAZStrType()
            _element.identity = AAZIdentityObjectType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.value.Element.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.active_active = AAZBoolType(
                serialized_name="activeActive",
            )
            properties.admin_state = AAZStrType(
                serialized_name="adminState",
            )
            properties.allow_remote_vnet_traffic = AAZBoolType(
                serialized_name="allowRemoteVnetTraffic",
            )
            properties.allow_virtual_wan_traffic = AAZBoolType(
                serialized_name="allowVirtualWanTraffic",
            )
            properties.auto_scale_configuration = AAZObjectType(
                serialized_name="autoScaleConfiguration",
            )
            properties.bgp_settings = AAZObjectType(
                serialized_name="bgpSettings",
            )
            properties.custom_routes = AAZObjectType(
                serialized_name="customRoutes",
            )
            _ListHelper._build_schema_address_space_read(properties.custom_routes)
            properties.disable_ip_sec_replay_protection = AAZBoolType(
                serialized_name="disableIPSecReplayProtection",
            )
            properties.enable_bgp = AAZBoolType(
                serialized_name="enableBgp",
            )
            properties.enable_bgp_route_translation_for_nat = AAZBoolType(
                serialized_name="enableBgpRouteTranslationForNat",
            )
            properties.enable_dns_forwarding = AAZBoolType(
                serialized_name="enableDnsForwarding",
            )
            properties.enable_high_bandwidth_vpn_gateway = AAZBoolType(
                serialized_name="enableHighBandwidthVpnGateway",
            )
            properties.enable_private_ip_address = AAZBoolType(
                serialized_name="enablePrivateIpAddress",
            )
            properties.gateway_default_site = AAZObjectType(
                serialized_name="gatewayDefaultSite",
            )
            _ListHelper._build_schema_sub_resource_read(properties.gateway_default_site)
            properties.gateway_type = AAZStrType(
                serialized_name="gatewayType",
            )
            properties.inbound_dns_forwarding_endpoint = AAZStrType(
                serialized_name="inboundDnsForwardingEndpoint",
                flags={"read_only": True},
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.nat_rules = AAZListType(
                serialized_name="natRules",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resiliency_model = AAZStrType(
                serialized_name="resiliencyModel",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.sku = AAZObjectType()
            properties.v_net_extended_location_resource_id = AAZStrType(
                serialized_name="vNetExtendedLocationResourceId",
            )
            properties.virtual_network_gateway_migration_status = AAZObjectType(
                serialized_name="virtualNetworkGatewayMigrationStatus",
            )
            properties.virtual_network_gateway_policy_groups = AAZListType(
                serialized_name="virtualNetworkGatewayPolicyGroups",
            )
            properties.vpn_client_configuration = AAZObjectType(
                serialized_name="vpnClientConfiguration",
            )
            properties.vpn_gateway_generation = AAZStrType(
                serialized_name="vpnGatewayGeneration",
            )
            properties.vpn_type = AAZStrType(
                serialized_name="vpnType",
            )

            auto_scale_configuration = cls._schema_on_200.value.Element.properties.auto_scale_configuration
            auto_scale_configuration.bounds = AAZObjectType()

            bounds = cls._schema_on_200.value.Element.properties.auto_scale_configuration.bounds
            bounds.max = AAZIntType()
            bounds.min = AAZIntType()

            bgp_settings = cls._schema_on_200.value.Element.properties.bgp_settings
            bgp_settings.asn = AAZIntType()
            bgp_settings.bgp_peering_address = AAZStrType(
                serialized_name="bgpPeeringAddress",
            )
            bgp_settings.bgp_peering_addresses = AAZListType(
                serialized_name="bgpPeeringAddresses",
            )
            bgp_settings.peer_weight = AAZIntType(
                serialized_name="peerWeight",
            )

            bgp_peering_addresses = cls._schema_on_200.value.Element.properties.bgp_settings.bgp_peering_addresses
            bgp_peering_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.bgp_settings.bgp_peering_addresses.Element
            _element.custom_bgp_ip_addresses = AAZListType(
                serialized_name="customBgpIpAddresses",
            )
            _element.default_bgp_ip_addresses = AAZListType(
                serialized_name="defaultBgpIpAddresses",
                flags={"read_only": True},
            )
            _element.ipconfiguration_id = AAZStrType(
                serialized_name="ipconfigurationId",
            )
            _element.tunnel_ip_addresses = AAZListType(
                serialized_name="tunnelIpAddresses",
                flags={"read_only": True},
            )

            custom_bgp_ip_addresses = cls._schema_on_200.value.Element.properties.bgp_settings.bgp_peering_addresses.Element.custom_bgp_ip_addresses
            custom_bgp_ip_addresses.Element = AAZStrType()

            default_bgp_ip_addresses = cls._schema_on_200.value.Element.properties.bgp_settings.bgp_peering_addresses.Element.default_bgp_ip_addresses
            default_bgp_ip_addresses.Element = AAZStrType()

            tunnel_ip_addresses = cls._schema_on_200.value.Element.properties.bgp_settings.bgp_peering_addresses.Element.tunnel_ip_addresses
            tunnel_ip_addresses.Element = AAZStrType()

            ip_configurations = cls._schema_on_200.value.Element.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ip_configurations.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.ip_configurations.Element.properties
            properties.private_ip_address = AAZStrType(
                serialized_name="privateIPAddress",
                flags={"read_only": True},
            )
            properties.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address = AAZObjectType(
                serialized_name="publicIPAddress",
            )
            _ListHelper._build_schema_sub_resource_read(properties.public_ip_address)
            properties.subnet = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(properties.subnet)

            nat_rules = cls._schema_on_200.value.Element.properties.nat_rules
            nat_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.nat_rules.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties.nat_rules.Element.properties
            properties.external_mappings = AAZListType(
                serialized_name="externalMappings",
            )
            properties.internal_mappings = AAZListType(
                serialized_name="internalMappings",
            )
            properties.ip_configuration_id = AAZStrType(
                serialized_name="ipConfigurationId",
            )
            properties.mode = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.type = AAZStrType()

            external_mappings = cls._schema_on_200.value.Element.properties.nat_rules.Element.properties.external_mappings
            external_mappings.Element = AAZObjectType()
            _ListHelper._build_schema_vpn_nat_rule_mapping_read(external_mappings.Element)

            internal_mappings = cls._schema_on_200.value.Element.properties.nat_rules.Element.properties.internal_mappings
            internal_mappings.Element = AAZObjectType()
            _ListHelper._build_schema_vpn_nat_rule_mapping_read(internal_mappings.Element)

            sku = cls._schema_on_200.value.Element.properties.sku
            sku.capacity = AAZIntType(
                flags={"read_only": True},
            )
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            virtual_network_gateway_migration_status = cls._schema_on_200.value.Element.properties.virtual_network_gateway_migration_status
            virtual_network_gateway_migration_status.error_message = AAZStrType(
                serialized_name="errorMessage",
            )
            virtual_network_gateway_migration_status.phase = AAZStrType()
            virtual_network_gateway_migration_status.state = AAZStrType()

            virtual_network_gateway_policy_groups = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups
            virtual_network_gateway_policy_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups.Element.properties
            properties.is_default = AAZBoolType(
                serialized_name="isDefault",
                flags={"required": True},
            )
            properties.policy_members = AAZListType(
                serialized_name="policyMembers",
                flags={"required": True},
            )
            properties.priority = AAZIntType(
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vng_client_connection_configurations = AAZListType(
                serialized_name="vngClientConnectionConfigurations",
                flags={"read_only": True},
            )

            policy_members = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups.Element.properties.policy_members
            policy_members.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups.Element.properties.policy_members.Element
            _element.attribute_type = AAZStrType(
                serialized_name="attributeType",
            )
            _element.attribute_value = AAZStrType(
                serialized_name="attributeValue",
            )
            _element.name = AAZStrType()

            vng_client_connection_configurations = cls._schema_on_200.value.Element.properties.virtual_network_gateway_policy_groups.Element.properties.vng_client_connection_configurations
            vng_client_connection_configurations.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(vng_client_connection_configurations.Element)

            vpn_client_configuration = cls._schema_on_200.value.Element.properties.vpn_client_configuration
            vpn_client_configuration.aad_audience = AAZStrType(
                serialized_name="aadAudience",
            )
            vpn_client_configuration.aad_issuer = AAZStrType(
                serialized_name="aadIssuer",
            )
            vpn_client_configuration.aad_tenant = AAZStrType(
                serialized_name="aadTenant",
            )
            vpn_client_configuration.radius_server_address = AAZStrType(
                serialized_name="radiusServerAddress",
            )
            vpn_client_configuration.radius_server_secret = AAZStrType(
                serialized_name="radiusServerSecret",
            )
            vpn_client_configuration.radius_servers = AAZListType(
                serialized_name="radiusServers",
            )
            vpn_client_configuration.vng_client_connection_configurations = AAZListType(
                serialized_name="vngClientConnectionConfigurations",
            )
            vpn_client_configuration.vpn_authentication_types = AAZListType(
                serialized_name="vpnAuthenticationTypes",
            )
            vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
                serialized_name="vpnClientAddressPool",
            )
            _ListHelper._build_schema_address_space_read(vpn_client_configuration.vpn_client_address_pool)
            vpn_client_configuration.vpn_client_ipsec_policies = AAZListType(
                serialized_name="vpnClientIpsecPolicies",
            )
            vpn_client_configuration.vpn_client_protocols = AAZListType(
                serialized_name="vpnClientProtocols",
            )
            vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
                serialized_name="vpnClientRevokedCertificates",
            )
            vpn_client_configuration.vpn_client_root_certificates = AAZListType(
                serialized_name="vpnClientRootCertificates",
            )

            radius_servers = cls._schema_on_200.value.Element.properties.vpn_client_configuration.radius_servers
            radius_servers.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.radius_servers.Element
            _element.radius_server_address = AAZStrType(
                serialized_name="radiusServerAddress",
                flags={"required": True},
            )
            _element.radius_server_score = AAZIntType(
                serialized_name="radiusServerScore",
            )
            _element.radius_server_secret = AAZStrType(
                serialized_name="radiusServerSecret",
            )

            vng_client_connection_configurations = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vng_client_connection_configurations
            vng_client_connection_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vng_client_connection_configurations.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vng_client_connection_configurations.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.virtual_network_gateway_policy_groups = AAZListType(
                serialized_name="virtualNetworkGatewayPolicyGroups",
                flags={"required": True},
            )
            properties.vpn_client_address_pool = AAZObjectType(
                serialized_name="vpnClientAddressPool",
                flags={"required": True},
            )
            _ListHelper._build_schema_address_space_read(properties.vpn_client_address_pool)

            virtual_network_gateway_policy_groups = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vng_client_connection_configurations.Element.properties.virtual_network_gateway_policy_groups
            virtual_network_gateway_policy_groups.Element = AAZObjectType()
            _ListHelper._build_schema_sub_resource_read(virtual_network_gateway_policy_groups.Element)

            vpn_authentication_types = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_authentication_types
            vpn_authentication_types.Element = AAZStrType()

            vpn_client_ipsec_policies = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_ipsec_policies
            vpn_client_ipsec_policies.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_ipsec_policies.Element
            _element.dh_group = AAZStrType(
                serialized_name="dhGroup",
                flags={"required": True},
            )
            _element.ike_encryption = AAZStrType(
                serialized_name="ikeEncryption",
                flags={"required": True},
            )
            _element.ike_integrity = AAZStrType(
                serialized_name="ikeIntegrity",
                flags={"required": True},
            )
            _element.ipsec_encryption = AAZStrType(
                serialized_name="ipsecEncryption",
                flags={"required": True},
            )
            _element.ipsec_integrity = AAZStrType(
                serialized_name="ipsecIntegrity",
                flags={"required": True},
            )
            _element.pfs_group = AAZStrType(
                serialized_name="pfsGroup",
                flags={"required": True},
            )
            _element.sa_data_size_kilobytes = AAZIntType(
                serialized_name="saDataSizeKilobytes",
                flags={"required": True},
            )
            _element.sa_life_time_seconds = AAZIntType(
                serialized_name="saLifeTimeSeconds",
                flags={"required": True},
            )

            vpn_client_protocols = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_protocols
            vpn_client_protocols.Element = AAZStrType()

            vpn_client_revoked_certificates = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates
            vpn_client_revoked_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.thumbprint = AAZStrType()

            vpn_client_root_certificates = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates
            vpn_client_root_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_cert_data = AAZStrType(
                serialized_name="publicCertData",
                flags={"required": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_address_space_read = None

    @classmethod
    def _build_schema_address_space_read(cls, _schema):
        if cls._schema_address_space_read is not None:
            _schema.address_prefixes = cls._schema_address_space_read.address_prefixes
            return

        cls._schema_address_space_read = _schema_address_space_read = AAZObjectType()

        address_space_read = _schema_address_space_read
        address_space_read.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )

        address_prefixes = _schema_address_space_read.address_prefixes
        address_prefixes.Element = AAZStrType()

        _schema.address_prefixes = cls._schema_address_space_read.address_prefixes

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_vpn_nat_rule_mapping_read = None

    @classmethod
    def _build_schema_vpn_nat_rule_mapping_read(cls, _schema):
        if cls._schema_vpn_nat_rule_mapping_read is not None:
            _schema.address_space = cls._schema_vpn_nat_rule_mapping_read.address_space
            _schema.port_range = cls._schema_vpn_nat_rule_mapping_read.port_range
            return

        cls._schema_vpn_nat_rule_mapping_read = _schema_vpn_nat_rule_mapping_read = AAZObjectType()

        vpn_nat_rule_mapping_read = _schema_vpn_nat_rule_mapping_read
        vpn_nat_rule_mapping_read.address_space = AAZStrType(
            serialized_name="addressSpace",
        )
        vpn_nat_rule_mapping_read.port_range = AAZStrType(
            serialized_name="portRange",
        )

        _schema.address_space = cls._schema_vpn_nat_rule_mapping_read.address_space
        _schema.port_range = cls._schema_vpn_nat_rule_mapping_read.port_range


__all__ = ["List"]
