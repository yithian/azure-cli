# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, record_only


class AzureBillingServiceScenarioTest(ScenarioTest):
    def _validate_invoice(self, invoice, include_url=False):
        self.assertIsNotNone(invoice)
        self.assertEqual(invoice['type'], 'Microsoft.Billing/invoices')
        self.assertTrue(invoice['id'] and invoice['name'])
        self.assertTrue(invoice['invoicePeriodStartDate'] and invoice['invoicePeriodEndDate'])
        self.assertTrue(invoice['invoicePeriodStartDate'] <= invoice['invoicePeriodEndDate'])
        self.assertIsNotNone(invoice['billingPeriodIds'])
        if include_url:
            self.assertIsNotNone(invoice['downloadUrl'])
        else:
            self.assertIsNone(invoice['downloadUrl'])

    def test_list_billing_periods(self):
        # list
        periods_list = self.cmd('billing period list').get_output_in_json()
        self.assertTrue(periods_list)
        # get
        period_name = periods_list[0]['name']
        self.kwargs.update({
            'period_name': period_name
        })
        self.cmd('billing period show -n {period_name}', checks=self.check('name', period_name))
        self.cmd('billing period list --top 3', checks=[
            self.check('length(@)', 3)
        ])

    @record_only()
    def test_list_enrollment_accounts(self):
        # list
        enrollment_accounts_list = self.cmd('billing enrollment-account list').get_output_in_json()
        self.assertTrue(enrollment_accounts_list)
        # get
        enrollment_account_name = enrollment_accounts_list[0]['name']
        self.kwargs.update({
            'enrollment_account_name': enrollment_account_name
        })
        self.cmd('billing enrollment-account show -n {enrollment_account_name}', checks=self.check('name', enrollment_account_name))

    def test_invoice_list(self):
        # please apply swagger changes: https://github.com/Azure/azure-rest-api-specs/pull/32870
        self.cmd(
            "billing invoice list --period-end-date '2025-06-30' --period-start-date '2000-01-01' "
            "--account-name 9a157b81-1503-516b-4fe8-7849e97ca70e:e6bd1c01-9e9b-4fa7-a9f1-6fe6cbad31fa_2019-05-31"
        )
