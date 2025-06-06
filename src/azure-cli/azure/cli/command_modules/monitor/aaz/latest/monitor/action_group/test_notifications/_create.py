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
    "monitor action-group test-notifications create",
)
class Create(AAZCommand):
    """Create an action group test-notifications.

    :example: Create an action group test-notifications with action group
        az monitor action-group test-notifications create --action-group MyActionGroup --resource-group MyResourceGroup -a email alice alice@example.com usecommonalertsChema --alert-type budget
    """

    _aaz_info = {
        "version": "2024-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/actiongroups/{}/createnotifications", "2024-10-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.action_group_name = AAZStrArg(
            options=["--action-group", "--action-group-name"],
            help="The name of the action group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.alert_type = AAZStrArg(
            options=["--alert-type"],
            help="The value of the supported alert type. Supported alert type values are: servicehealth, metricstaticthreshold, metricsdynamicthreshold, logalertv2, smartalert, webtestalert, logalertv1numresult, logalertv1metricmeasurement, resourcehealth, activitylog, budget",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=30,
            ),
        )

        # define Arg Group "NotificationRequest"

        _args_schema = cls._args_schema
        _args_schema.arm_role_receivers = AAZListArg(
            options=["--arm-role-receivers"],
            arg_group="NotificationRequest",
            help="The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported.",
        )
        _args_schema.automation_runbook_receivers = AAZListArg(
            options=["--automation-runbook-receivers"],
            arg_group="NotificationRequest",
            help="The list of AutomationRunbook receivers that are part of this action group.",
        )
        _args_schema.azure_app_push_receivers = AAZListArg(
            options=["--azure-app-push-receivers"],
            arg_group="NotificationRequest",
            help="The list of AzureAppPush receivers that are part of this action group.",
        )
        _args_schema.azure_function_receivers = AAZListArg(
            options=["--azure-function-receivers"],
            arg_group="NotificationRequest",
            help="The list of azure function receivers that are part of this action group.",
        )
        _args_schema.email_receivers = AAZListArg(
            options=["--email-receivers"],
            arg_group="NotificationRequest",
            help="The list of email receivers that are part of this action group.",
        )
        _args_schema.event_hub_receivers = AAZListArg(
            options=["--event-hub-receivers"],
            arg_group="NotificationRequest",
            help="The list of event hub receivers that are part of this action group.",
        )
        _args_schema.incident_receivers = AAZListArg(
            options=["--incident-receivers"],
            arg_group="NotificationRequest",
            help="The list of incident receivers that are part of this action group.",
        )
        _args_schema.itsm_receivers = AAZListArg(
            options=["--itsm-receivers"],
            arg_group="NotificationRequest",
            help="The list of ITSM receivers that are part of this action group.",
        )
        _args_schema.logic_app_receivers = AAZListArg(
            options=["--logic-app-receivers"],
            arg_group="NotificationRequest",
            help="The list of logic app receivers that are part of this action group.",
        )
        _args_schema.sms_receivers = AAZListArg(
            options=["--sms-receivers"],
            arg_group="NotificationRequest",
            help="The list of SMS receivers that are part of this action group.",
        )
        _args_schema.voice_receivers = AAZListArg(
            options=["--voice-receivers"],
            arg_group="NotificationRequest",
            help="The list of voice receivers that are part of this action group.",
        )
        _args_schema.webhook_receivers = AAZListArg(
            options=["--webhook-receivers"],
            arg_group="NotificationRequest",
            help="The list of webhook receivers that are part of this action group.",
        )

        arm_role_receivers = cls._args_schema.arm_role_receivers
        arm_role_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.arm_role_receivers.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the arm role receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.role_id = AAZStrArg(
            options=["role-id"],
            help="The arm role id.",
            required=True,
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )

        automation_runbook_receivers = cls._args_schema.automation_runbook_receivers
        automation_runbook_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.automation_runbook_receivers.Element
        _element.automation_account_id = AAZStrArg(
            options=["automation-account-id"],
            help="The Azure automation account Id which holds this runbook and authenticate to Azure resource.",
            required=True,
        )
        _element.is_global_runbook = AAZBoolArg(
            options=["is-global-runbook"],
            help="Indicates whether this instance is global runbook.",
            required=True,
        )
        _element.managed_identity = AAZStrArg(
            options=["managed-identity"],
            help="The principal id of the managed identity. The value can be \"None\", \"SystemAssigned\" ",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Indicates name of the webhook.",
        )
        _element.runbook_name = AAZStrArg(
            options=["runbook-name"],
            help="The name for this runbook.",
            required=True,
        )
        _element.service_uri = AAZStrArg(
            options=["service-uri"],
            help="The URI where webhooks should be sent.",
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )
        _element.webhook_resource_id = AAZStrArg(
            options=["webhook-resource-id"],
            help="The resource id for webhook linked to this runbook.",
            required=True,
        )

        azure_app_push_receivers = cls._args_schema.azure_app_push_receivers
        azure_app_push_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.azure_app_push_receivers.Element
        _element.email_address = AAZStrArg(
            options=["email-address"],
            help="The email address registered for the Azure mobile app.",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the Azure mobile app push receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )

        azure_function_receivers = cls._args_schema.azure_function_receivers
        azure_function_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.azure_function_receivers.Element
        _element.function_app_resource_id = AAZStrArg(
            options=["function-app-resource-id"],
            help="The azure resource id of the function app.",
            required=True,
        )
        _element.function_name = AAZStrArg(
            options=["function-name"],
            help="The function name in the function app.",
            required=True,
        )
        _element.http_trigger_url = AAZStrArg(
            options=["http-trigger-url"],
            help="The http trigger url where http request sent to.",
            required=True,
        )
        _element.managed_identity = AAZStrArg(
            options=["managed-identity"],
            help="The principal id of the managed identity. The value can be \"None\", \"SystemAssigned\" ",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the azure function receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )

        email_receivers = cls._args_schema.email_receivers
        email_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.email_receivers.Element
        _element.email_address = AAZStrArg(
            options=["email-address"],
            help="The email address of this receiver.",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the email receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )

        event_hub_receivers = cls._args_schema.event_hub_receivers
        event_hub_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.event_hub_receivers.Element
        _element.event_hub_name = AAZStrArg(
            options=["event-hub-name"],
            help="The name of the specific Event Hub queue",
            required=True,
        )
        _element.event_hub_name_space = AAZStrArg(
            options=["event-hub-name-space"],
            help="The Event Hub namespace",
            required=True,
        )
        _element.managed_identity = AAZStrArg(
            options=["managed-identity"],
            help="The principal id of the managed identity. The value can be \"None\", \"SystemAssigned\" ",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the Event hub receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="The Id for the subscription containing this event hub",
            required=True,
        )
        _element.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The tenant Id for the subscription containing this event hub",
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )

        incident_receivers = cls._args_schema.incident_receivers
        incident_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.incident_receivers.Element
        _element.connection = AAZObjectArg(
            options=["connection"],
            help="The incident service connection",
            required=True,
        )
        _element.incident_management_service = AAZStrArg(
            options=["incident-management-service"],
            help="The incident management service type",
            required=True,
            enum={"Icm": "Icm"},
        )
        _element.mappings = AAZDictArg(
            options=["mappings"],
            help="Field mappings for the incident service",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the Incident receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )

        connection = cls._args_schema.incident_receivers.Element.connection
        connection.id = AAZStrArg(
            options=["id"],
            help="GUID value representing the connection ID for the incident management service.",
            required=True,
        )
        connection.name = AAZStrArg(
            options=["name"],
            help="The name of the connection.",
            required=True,
        )

        mappings = cls._args_schema.incident_receivers.Element.mappings
        mappings.Element = AAZStrArg()

        itsm_receivers = cls._args_schema.itsm_receivers
        itsm_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.itsm_receivers.Element
        _element.connection_id = AAZStrArg(
            options=["connection-id"],
            help="Unique identification of ITSM connection among multiple defined in above workspace.",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the Itsm receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.region = AAZStrArg(
            options=["region"],
            help="Region in which workspace resides. Supported values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'",
            required=True,
        )
        _element.ticket_configuration = AAZStrArg(
            options=["ticket-configuration"],
            help="JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.",
            required=True,
        )
        _element.workspace_id = AAZStrArg(
            options=["workspace-id"],
            help="OMS LA instance identifier.",
            required=True,
        )

        logic_app_receivers = cls._args_schema.logic_app_receivers
        logic_app_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.logic_app_receivers.Element
        _element.callback_url = AAZStrArg(
            options=["callback-url"],
            help="The callback url where http request sent to.",
            required=True,
        )
        _element.managed_identity = AAZStrArg(
            options=["managed-identity"],
            help="The principal id of the managed identity. The value can be \"None\", \"SystemAssigned\" ",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the logic app receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.resource_id = AAZStrArg(
            options=["resource-id"],
            help="The azure resource id of the logic app receiver.",
            required=True,
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )

        sms_receivers = cls._args_schema.sms_receivers
        sms_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.sms_receivers.Element
        _element.country_code = AAZStrArg(
            options=["country-code"],
            help="The country code of the SMS receiver.",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the SMS receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.phone_number = AAZStrArg(
            options=["phone-number"],
            help="The phone number of the SMS receiver.",
            required=True,
        )

        voice_receivers = cls._args_schema.voice_receivers
        voice_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.voice_receivers.Element
        _element.country_code = AAZStrArg(
            options=["country-code"],
            help="The country code of the voice receiver.",
            required=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the voice receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.phone_number = AAZStrArg(
            options=["phone-number"],
            help="The phone number of the voice receiver.",
            required=True,
        )

        webhook_receivers = cls._args_schema.webhook_receivers
        webhook_receivers.Element = AAZObjectArg()

        _element = cls._args_schema.webhook_receivers.Element
        _element.identifier_uri = AAZStrArg(
            options=["identifier-uri"],
            help="Indicates the identifier uri for aad auth.",
        )
        _element.managed_identity = AAZStrArg(
            options=["managed-identity"],
            help="The principal id of the managed identity. The value can be \"None\", \"SystemAssigned\" ",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the webhook receiver. Names must be unique across all receivers within an action group.",
            required=True,
        )
        _element.object_id = AAZStrArg(
            options=["object-id"],
            help="Indicates the webhook app object Id for aad auth.",
        )
        _element.service_uri = AAZStrArg(
            options=["service-uri"],
            help="The URI where webhooks should be sent.",
            required=True,
        )
        _element.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="Indicates the tenant id for aad auth.",
        )
        _element.use_aad_auth = AAZBoolArg(
            options=["use-aad-auth"],
            help="Indicates whether or not use AAD authentication.",
            default=False,
        )
        _element.use_common_alert_schema = AAZBoolArg(
            options=["use-common-alert-schema"],
            help="Indicates whether to use common alert schema.",
            default=False,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ActionGroupsCreateNotificationsAtActionGroupResourceLevel(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ActionGroupsCreateNotificationsAtActionGroupResourceLevel(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/actionGroups/{actionGroupName}/createNotifications",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "actionGroupName", self.ctx.args.action_group_name,
                    required=True,
                ),
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
                    "api-version", "2024-10-01-preview",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("alertType", AAZStrType, ".alert_type", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("armRoleReceivers", AAZListType, ".arm_role_receivers")
            _builder.set_prop("automationRunbookReceivers", AAZListType, ".automation_runbook_receivers")
            _builder.set_prop("azureAppPushReceivers", AAZListType, ".azure_app_push_receivers")
            _builder.set_prop("azureFunctionReceivers", AAZListType, ".azure_function_receivers")
            _builder.set_prop("emailReceivers", AAZListType, ".email_receivers")
            _builder.set_prop("eventHubReceivers", AAZListType, ".event_hub_receivers")
            _builder.set_prop("incidentReceivers", AAZListType, ".incident_receivers")
            _builder.set_prop("itsmReceivers", AAZListType, ".itsm_receivers")
            _builder.set_prop("logicAppReceivers", AAZListType, ".logic_app_receivers")
            _builder.set_prop("smsReceivers", AAZListType, ".sms_receivers")
            _builder.set_prop("voiceReceivers", AAZListType, ".voice_receivers")
            _builder.set_prop("webhookReceivers", AAZListType, ".webhook_receivers")

            arm_role_receivers = _builder.get(".armRoleReceivers")
            if arm_role_receivers is not None:
                arm_role_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".armRoleReceivers[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("roleId", AAZStrType, ".role_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            automation_runbook_receivers = _builder.get(".automationRunbookReceivers")
            if automation_runbook_receivers is not None:
                automation_runbook_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".automationRunbookReceivers[]")
            if _elements is not None:
                _elements.set_prop("automationAccountId", AAZStrType, ".automation_account_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("isGlobalRunbook", AAZBoolType, ".is_global_runbook", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("managedIdentity", AAZStrType, ".managed_identity")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("runbookName", AAZStrType, ".runbook_name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("serviceUri", AAZStrType, ".service_uri")
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")
                _elements.set_prop("webhookResourceId", AAZStrType, ".webhook_resource_id", typ_kwargs={"flags": {"required": True}})

            azure_app_push_receivers = _builder.get(".azureAppPushReceivers")
            if azure_app_push_receivers is not None:
                azure_app_push_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".azureAppPushReceivers[]")
            if _elements is not None:
                _elements.set_prop("emailAddress", AAZStrType, ".email_address", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            azure_function_receivers = _builder.get(".azureFunctionReceivers")
            if azure_function_receivers is not None:
                azure_function_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".azureFunctionReceivers[]")
            if _elements is not None:
                _elements.set_prop("functionAppResourceId", AAZStrType, ".function_app_resource_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("functionName", AAZStrType, ".function_name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("httpTriggerUrl", AAZStrType, ".http_trigger_url", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("managedIdentity", AAZStrType, ".managed_identity")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            email_receivers = _builder.get(".emailReceivers")
            if email_receivers is not None:
                email_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".emailReceivers[]")
            if _elements is not None:
                _elements.set_prop("emailAddress", AAZStrType, ".email_address", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            event_hub_receivers = _builder.get(".eventHubReceivers")
            if event_hub_receivers is not None:
                event_hub_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".eventHubReceivers[]")
            if _elements is not None:
                _elements.set_prop("eventHubName", AAZStrType, ".event_hub_name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("eventHubNameSpace", AAZStrType, ".event_hub_name_space", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("managedIdentity", AAZStrType, ".managed_identity")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("subscriptionId", AAZStrType, ".subscription_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("tenantId", AAZStrType, ".tenant_id")
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            incident_receivers = _builder.get(".incidentReceivers")
            if incident_receivers is not None:
                incident_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".incidentReceivers[]")
            if _elements is not None:
                _elements.set_prop("connection", AAZObjectType, ".connection", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("incidentManagementService", AAZStrType, ".incident_management_service", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("mappings", AAZDictType, ".mappings", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            connection = _builder.get(".incidentReceivers[].connection")
            if connection is not None:
                connection.set_prop("id", AAZStrType, ".id", typ_kwargs={"flags": {"required": True}})
                connection.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            mappings = _builder.get(".incidentReceivers[].mappings")
            if mappings is not None:
                mappings.set_elements(AAZStrType, ".")

            itsm_receivers = _builder.get(".itsmReceivers")
            if itsm_receivers is not None:
                itsm_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".itsmReceivers[]")
            if _elements is not None:
                _elements.set_prop("connectionId", AAZStrType, ".connection_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("region", AAZStrType, ".region", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("ticketConfiguration", AAZStrType, ".ticket_configuration", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("workspaceId", AAZStrType, ".workspace_id", typ_kwargs={"flags": {"required": True}})

            logic_app_receivers = _builder.get(".logicAppReceivers")
            if logic_app_receivers is not None:
                logic_app_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".logicAppReceivers[]")
            if _elements is not None:
                _elements.set_prop("callbackUrl", AAZStrType, ".callback_url", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("managedIdentity", AAZStrType, ".managed_identity")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("resourceId", AAZStrType, ".resource_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            sms_receivers = _builder.get(".smsReceivers")
            if sms_receivers is not None:
                sms_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".smsReceivers[]")
            if _elements is not None:
                _elements.set_prop("countryCode", AAZStrType, ".country_code", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("phoneNumber", AAZStrType, ".phone_number", typ_kwargs={"flags": {"required": True}})

            voice_receivers = _builder.get(".voiceReceivers")
            if voice_receivers is not None:
                voice_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".voiceReceivers[]")
            if _elements is not None:
                _elements.set_prop("countryCode", AAZStrType, ".country_code", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("phoneNumber", AAZStrType, ".phone_number", typ_kwargs={"flags": {"required": True}})

            webhook_receivers = _builder.get(".webhookReceivers")
            if webhook_receivers is not None:
                webhook_receivers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".webhookReceivers[]")
            if _elements is not None:
                _elements.set_prop("identifierUri", AAZStrType, ".identifier_uri")
                _elements.set_prop("managedIdentity", AAZStrType, ".managed_identity")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("objectId", AAZStrType, ".object_id")
                _elements.set_prop("serviceUri", AAZStrType, ".service_uri", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("tenantId", AAZStrType, ".tenant_id")
                _elements.set_prop("useAadAuth", AAZBoolType, ".use_aad_auth")
                _elements.set_prop("useCommonAlertSchema", AAZBoolType, ".use_common_alert_schema")

            return self.serialize_content(_content_value)

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
            _schema_on_200.action_details = AAZListType(
                serialized_name="actionDetails",
            )
            _schema_on_200.completed_time = AAZStrType(
                serialized_name="completedTime",
            )
            _schema_on_200.context = AAZObjectType()
            _schema_on_200.created_time = AAZStrType(
                serialized_name="createdTime",
            )
            _schema_on_200.state = AAZStrType(
                flags={"required": True},
            )

            action_details = cls._schema_on_200.action_details
            action_details.Element = AAZObjectType()

            _element = cls._schema_on_200.action_details.Element
            _element.detail = AAZStrType(
                serialized_name="Detail",
            )
            _element.mechanism_type = AAZStrType(
                serialized_name="MechanismType",
            )
            _element.name = AAZStrType(
                serialized_name="Name",
            )
            _element.send_time = AAZStrType(
                serialized_name="SendTime",
            )
            _element.status = AAZStrType(
                serialized_name="Status",
            )
            _element.sub_state = AAZStrType(
                serialized_name="SubState",
            )

            context = cls._schema_on_200.context
            context.context_type = AAZStrType(
                serialized_name="contextType",
            )
            context.notification_source = AAZStrType(
                serialized_name="notificationSource",
            )

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
