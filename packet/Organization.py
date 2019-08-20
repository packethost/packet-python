# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Organization:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.website = data.get("website")
        self.twitter = data.get("twitter")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.tax_id = data.get("tax_id")
        self.main_phone = data.get("main_phone")
        self.billing_phone = data.get("billing_phone")
        self.credit_amount = data.get("credit_amount")
        self.personal = data.get("personal")
        self.customdata = data.get("customdata")
        self.attn = data.get("attn")
        self.purchase_order = data.get("purchase_order")
        self.billing_name = data.get("billing_name")
        self.enforce_2fa = data.get("enforce_2fa")
        self.enforce_2fa_at = data.get("enforce_2fa_at")
        self.short_id = data.get("short_id")
        self.account_id = data.get("account_id")
        self.enabled_features = data.get("enabled_features")
        self.maintenance_email = data.get("maintenance_email")
        self.abuse_email = data.get("abuse_email")
        self.address = data.get("address")
        self.billing_address = data.get("billing_address")
        self.account_manager = data.get("account_manager")
        self.logo = data.get("logo")
        self.logo_thumb = data.get("logo_thumb")
        self.projects = data.get("projects")
        self.plan = data.get("plan")
        self.monthly_spend = data.get("monthly_spend")
        self.current_user_abilities = data.get("current_user_abilities")
        self.href = data.get("href")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
