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
    "monitor log-analytics workspace update",
)
class Update(AAZCommand):
    """Update a workspace instance.

    :example: Update a workspace instance.
        az monitor log-analytics workspace update --resource-group myresourcegroup --retention-time 30 --workspace-name myworkspace

    :example: Update the defaultDataCollectionRuleResourceId of the workspace
        az monitor log-analytics workspace update --resource-group myresourcegroup --workspace-name myworkspace --data-collection-rule "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dcrName}".
    """

    _aaz_info = {
        "version": "2025-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}", "2025-02-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
        _args_schema.workspace_name = AAZStrArg(
            options=["-n", "--name", "--workspace-name"],
            help="Name of the Log Analytics Workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
                max_length=63,
                min_length=4,
            ),
        )

        # define Arg Group "Identity"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--type", "--identity-type"],
            arg_group="Identity",
            help="Type of managed service identity.",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned = AAZDictArg(
            options=["--user-assigned"],
            arg_group="Identity",
            help="The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.",
            nullable=True,
        )

        user_assigned = cls._args_schema.user_assigned
        user_assigned.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.data_collection_rule = AAZStrArg(
            options=["--data-collection-rule"],
            arg_group="Properties",
            help="The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dcrName}.",
            nullable=True,
        )
        _args_schema.ingestion_access = AAZStrArg(
            options=["--ingestion-access"],
            arg_group="Properties",
            help="The public network access type to access workspace ingestion.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.query_access = AAZStrArg(
            options=["--query-access"],
            arg_group="Properties",
            help="The public network access type to access workspace query.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.retention_time = AAZIntArg(
            options=["--retention-time"],
            arg_group="Properties",
            help="The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.",
            nullable=True,
        )
        _args_schema.quota = AAZFloatArg(
            options=["--quota"],
            arg_group="Properties",
            help="The workspace daily quota for ingestion in gigabytes. The minimum value is 0.023 and default is -1 which means unlimited.",
            nullable=True,
        )

        # define Arg Group "Replication"

        _args_schema = cls._args_schema
        _args_schema.replication_enabled = AAZBoolArg(
            options=["--replication-enabled"],
            arg_group="Replication",
            help="Specifies whether the replication is enabled or not. When true, workspace configuration and data is replicated to the specified location. If replication is been enabled, location must be provided.",
            nullable=True,
        )

        # define Arg Group "Sku"

        _args_schema = cls._args_schema
        _args_schema.capacity_reservation_level = AAZIntArg(
            options=["--level", "--capacity-reservation-level"],
            arg_group="Sku",
            help="The capacity reservation level for this workspace, when CapacityReservation sku is selected. The maximum value is 1000 and must be in multiples of 100. If you want to increase the limit, please contact LAIngestionRate@microsoft.com.",
            nullable=True,
            enum={"100": 100, "1000": 1000, "10000": 10000, "200": 200, "2000": 2000, "25000": 25000, "300": 300, "400": 400, "500": 500, "5000": 5000, "50000": 50000},
        )
        _args_schema.sku_name = AAZStrArg(
            options=["--sku", "--sku-name"],
            arg_group="Sku",
            help="The name of the SKU.",
            enum={"CapacityReservation": "CapacityReservation", "Free": "Free", "LACluster": "LACluster", "PerGB2018": "PerGB2018", "PerNode": "PerNode", "Premium": "Premium", "Standalone": "Standalone", "Standard": "Standard"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WorkspacesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.WorkspacesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkspacesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

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
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2025-02-01",
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
            _UpdateHelper._build_schema_workspace_read(cls._schema_on_200)

            return cls._schema_on_200

    class WorkspacesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

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
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2025-02-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_workspace_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZIdentityObjectType)
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("defaultDataCollectionRuleResourceId", AAZStrType, ".data_collection_rule")
                properties.set_prop("publicNetworkAccessForIngestion", AAZStrType, ".ingestion_access")
                properties.set_prop("publicNetworkAccessForQuery", AAZStrType, ".query_access")
                properties.set_prop("replication", AAZObjectType)
                properties.set_prop("retentionInDays", AAZIntType, ".retention_time", typ_kwargs={"nullable": True})
                properties.set_prop("sku", AAZObjectType)
                properties.set_prop("workspaceCapping", AAZObjectType)

            replication = _builder.get(".properties.replication")
            if replication is not None:
                replication.set_prop("enabled", AAZBoolType, ".replication_enabled")

            sku = _builder.get(".properties.sku")
            if sku is not None:
                sku.set_prop("capacityReservationLevel", AAZIntType, ".capacity_reservation_level")
                sku.set_prop("name", AAZStrType, ".sku_name", typ_kwargs={"flags": {"required": True}})

            workspace_capping = _builder.get(".properties.workspaceCapping")
            if workspace_capping is not None:
                workspace_capping.set_prop("dailyQuotaGb", AAZFloatType, ".quota")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_workspace_read = None

    @classmethod
    def _build_schema_workspace_read(cls, _schema):
        if cls._schema_workspace_read is not None:
            _schema.etag = cls._schema_workspace_read.etag
            _schema.id = cls._schema_workspace_read.id
            _schema.identity = cls._schema_workspace_read.identity
            _schema.location = cls._schema_workspace_read.location
            _schema.name = cls._schema_workspace_read.name
            _schema.properties = cls._schema_workspace_read.properties
            _schema.system_data = cls._schema_workspace_read.system_data
            _schema.tags = cls._schema_workspace_read.tags
            _schema.type = cls._schema_workspace_read.type
            return

        cls._schema_workspace_read = _schema_workspace_read = AAZObjectType()

        workspace_read = _schema_workspace_read
        workspace_read.etag = AAZStrType()
        workspace_read.id = AAZStrType(
            flags={"read_only": True},
        )
        workspace_read.identity = AAZIdentityObjectType()
        workspace_read.location = AAZStrType(
            flags={"required": True},
        )
        workspace_read.name = AAZStrType(
            flags={"read_only": True},
        )
        workspace_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        workspace_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        workspace_read.tags = AAZDictType()
        workspace_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_workspace_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_workspace_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_workspace_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_workspace_read.properties
        properties.created_date = AAZStrType(
            serialized_name="createdDate",
            flags={"read_only": True},
        )
        properties.customer_id = AAZStrType(
            serialized_name="customerId",
            flags={"read_only": True},
        )
        properties.default_data_collection_rule_resource_id = AAZStrType(
            serialized_name="defaultDataCollectionRuleResourceId",
        )
        properties.failover = AAZObjectType()
        properties.features = AAZFreeFormDictType()
        properties.force_cmk_for_query = AAZBoolType(
            serialized_name="forceCmkForQuery",
        )
        properties.modified_date = AAZStrType(
            serialized_name="modifiedDate",
            flags={"read_only": True},
        )
        properties.private_link_scoped_resources = AAZListType(
            serialized_name="privateLinkScopedResources",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_network_access_for_ingestion = AAZStrType(
            serialized_name="publicNetworkAccessForIngestion",
        )
        properties.public_network_access_for_query = AAZStrType(
            serialized_name="publicNetworkAccessForQuery",
        )
        properties.replication = AAZObjectType()
        properties.retention_in_days = AAZIntType(
            serialized_name="retentionInDays",
            nullable=True,
        )
        properties.sku = AAZObjectType()
        properties.workspace_capping = AAZObjectType(
            serialized_name="workspaceCapping",
        )

        failover = _schema_workspace_read.properties.failover
        failover.last_modified_date = AAZStrType(
            serialized_name="lastModifiedDate",
            flags={"read_only": True},
        )
        failover.state = AAZStrType(
            flags={"read_only": True},
        )

        private_link_scoped_resources = _schema_workspace_read.properties.private_link_scoped_resources
        private_link_scoped_resources.Element = AAZObjectType()

        _element = _schema_workspace_read.properties.private_link_scoped_resources.Element
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
        )
        _element.scope_id = AAZStrType(
            serialized_name="scopeId",
        )

        replication = _schema_workspace_read.properties.replication
        replication.created_date = AAZStrType(
            serialized_name="createdDate",
            flags={"read_only": True},
        )
        replication.enabled = AAZBoolType()
        replication.last_modified_date = AAZStrType(
            serialized_name="lastModifiedDate",
            flags={"read_only": True},
        )
        replication.location = AAZStrType()
        replication.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        sku = _schema_workspace_read.properties.sku
        sku.capacity_reservation_level = AAZIntType(
            serialized_name="capacityReservationLevel",
        )
        sku.last_sku_update = AAZStrType(
            serialized_name="lastSkuUpdate",
            flags={"read_only": True},
        )
        sku.name = AAZStrType(
            flags={"required": True},
        )

        workspace_capping = _schema_workspace_read.properties.workspace_capping
        workspace_capping.daily_quota_gb = AAZFloatType(
            serialized_name="dailyQuotaGb",
        )
        workspace_capping.data_ingestion_status = AAZStrType(
            serialized_name="dataIngestionStatus",
            flags={"read_only": True},
        )
        workspace_capping.quota_next_reset_time = AAZStrType(
            serialized_name="quotaNextResetTime",
            flags={"read_only": True},
        )

        system_data = _schema_workspace_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_workspace_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_workspace_read.etag
        _schema.id = cls._schema_workspace_read.id
        _schema.identity = cls._schema_workspace_read.identity
        _schema.location = cls._schema_workspace_read.location
        _schema.name = cls._schema_workspace_read.name
        _schema.properties = cls._schema_workspace_read.properties
        _schema.system_data = cls._schema_workspace_read.system_data
        _schema.tags = cls._schema_workspace_read.tags
        _schema.type = cls._schema_workspace_read.type


__all__ = ["Update"]
