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
    "identity federated-credential update",
)
class Update(AAZCommand):
    """Update a federated identity credential under an existing user assigned identity.

    :example: Update a federated identity credential under a specific user assigned identity using subject.
        az identity federated-credential update --identity-name myIdentityName --name myFicName --resource-group myResourceGroup --issuer myIssuer --subject mySubject --audiences myAudiences

    :example: Update a federated identity credential under a specific user assigned identity using claimsMatchingExpression.
        az identity federated-credential update --identity-name myIdentityName --name myFicName --resource-group myResourceGroup --issuer myIssuer --claims-matching-expression-version 1 --claims-matching-expression-value "claims['sub'] eq 'foo'" --audiences myAudiences
    """

    _aaz_info = {
        "version": "2025-01-31-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managedidentity/userassignedidentities/{}/federatedidentitycredentials/{}", "2025-01-31-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the federated identity credential resource.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]{1}[a-zA-Z0-9-_]{2,119}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.",
            required=True,
        )
        _args_schema.identity_name = AAZStrArg(
            options=["--identity-name"],
            help="The name of the identity resource.",
            required=True,
        )

        # define Arg Group "ClaimsMatchingExpression"

        _args_schema = cls._args_schema
        _args_schema.claims_matching_expression_version = AAZIntArg(
            options=["--cme-version", "--claims-matching-expression-version"],
            arg_group="ClaimsMatchingExpression",
            help="Specifies the version of the claims matching expression used in the expression.",
            is_preview=True,
        )
        _args_schema.claims_matching_expression_value = AAZStrArg(
            options=["--cme-value", "--claims-matching-expression-value"],
            arg_group="ClaimsMatchingExpression",
            help="The wildcard-based expression for matching incoming claims. Cannot be used with --subject.",
            is_preview=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.audiences = AAZListArg(
            options=["--audiences"],
            arg_group="Properties",
            help="The aud value in the token sent to Azure for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure to issue the access token.",
        )
        _args_schema.issuer = AAZStrArg(
            options=["--issuer"],
            arg_group="Properties",
            help="The openId connect metadata URL of the issuer of the identity provider that Azure AD would use in the token exchange protocol for validating tokens before issuing a token as the user-assigned managed identity.",
        )
        _args_schema.subject = AAZStrArg(
            options=["--subject"],
            arg_group="Properties",
            help="The sub value in the token sent to Azure AD for getting the user-assigned managed identity token. The value configured in the federated credential and the one in the incoming token must exactly match for Azure AD to issue the access token. Either 'subject' or 'claimsMatchingExpression' must be defined, but not both.",
            nullable=True,
        )

        audiences = cls._args_schema.audiences
        audiences.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FederatedIdentityCredentialsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.FederatedIdentityCredentialsCreateOrUpdate(ctx=self.ctx)()
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

    class FederatedIdentityCredentialsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}/federatedIdentityCredentials/{federatedIdentityCredentialResourceName}",
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
                    "federatedIdentityCredentialResourceName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.identity_name,
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
                    "api-version", "2025-01-31-preview",
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
            _UpdateHelper._build_schema_federated_identity_credential_read(cls._schema_on_200)

            return cls._schema_on_200

    class FederatedIdentityCredentialsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName}/federatedIdentityCredentials/{federatedIdentityCredentialResourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "federatedIdentityCredentialResourceName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.identity_name,
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
                    "api-version", "2025-01-31-preview",
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
            _UpdateHelper._build_schema_federated_identity_credential_read(cls._schema_on_200_201)

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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("audiences", AAZListType, ".audiences", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("claimsMatchingExpression", AAZObjectType)
                properties.set_prop("issuer", AAZStrType, ".issuer", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("subject", AAZStrType, ".subject")

            audiences = _builder.get(".properties.audiences")
            if audiences is not None:
                audiences.set_elements(AAZStrType, ".")

            claims_matching_expression = _builder.get(".properties.claimsMatchingExpression")
            if claims_matching_expression is not None:
                claims_matching_expression.set_prop("languageVersion", AAZIntType, ".claims_matching_expression_version", typ_kwargs={"flags": {"required": True}})
                claims_matching_expression.set_prop("value", AAZStrType, ".claims_matching_expression_value", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_federated_identity_credential_read = None

    @classmethod
    def _build_schema_federated_identity_credential_read(cls, _schema):
        if cls._schema_federated_identity_credential_read is not None:
            _schema.id = cls._schema_federated_identity_credential_read.id
            _schema.name = cls._schema_federated_identity_credential_read.name
            _schema.properties = cls._schema_federated_identity_credential_read.properties
            _schema.system_data = cls._schema_federated_identity_credential_read.system_data
            _schema.type = cls._schema_federated_identity_credential_read.type
            return

        cls._schema_federated_identity_credential_read = _schema_federated_identity_credential_read = AAZObjectType()

        federated_identity_credential_read = _schema_federated_identity_credential_read
        federated_identity_credential_read.id = AAZStrType(
            flags={"read_only": True},
        )
        federated_identity_credential_read.name = AAZStrType(
            flags={"read_only": True},
        )
        federated_identity_credential_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        federated_identity_credential_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        federated_identity_credential_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_federated_identity_credential_read.properties
        properties.audiences = AAZListType(
            flags={"required": True},
        )
        properties.claims_matching_expression = AAZObjectType(
            serialized_name="claimsMatchingExpression",
        )
        properties.issuer = AAZStrType(
            flags={"required": True},
        )
        properties.subject = AAZStrType()

        audiences = _schema_federated_identity_credential_read.properties.audiences
        audiences.Element = AAZStrType()

        claims_matching_expression = _schema_federated_identity_credential_read.properties.claims_matching_expression
        claims_matching_expression.language_version = AAZIntType(
            serialized_name="languageVersion",
            flags={"required": True},
        )
        claims_matching_expression.value = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_federated_identity_credential_read.system_data
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

        _schema.id = cls._schema_federated_identity_credential_read.id
        _schema.name = cls._schema_federated_identity_credential_read.name
        _schema.properties = cls._schema_federated_identity_credential_read.properties
        _schema.system_data = cls._schema_federated_identity_credential_read.system_data
        _schema.type = cls._schema_federated_identity_credential_read.type


__all__ = ["Update"]
