# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Organization:
    def __init__(self, data):
        if "id" in data:
            self.id = data["id"]
        if "name" in data:
            self.name = data["name"]
        if "description" in data:
            self.description = data["description"]
        if "website" in data:
            self.website = data["website"]
        if "twitter" in data:
            self.twitter = data["twitter"]
        if "created_at" in data:
            self.created_at = data["created_at"]
        if "updated_at" in data:
            self.updated_at = data["updated_at"]
        if "tax_id" in data:
            self.tax_id = data["tax_id"]
        if "main_phone" in data:
            self.main_phone = data["main_phone"]
        if "billing_phone" in data:
            self.billing_phone = data["billing_phone"]
        if "credit_amount" in data:
            self.credit_amount = data["credit_amount"]
        if "personal" in data:
            self.personal = data["personal"]
        if "customdata" in data:
            self.customdata = data["customdata"]
        if "attn" in data:
            self.attn = data["attn"]
        if "purchase_order" in data:
            self.purchase_order = data["purchase_order"]
        if "billing_name" in data:
            self.billing_name = data["billing_name"]
        if "enforce_2fa" in data:
            self.enforce_2fa = data["enforce_2fa"]
        if "enforce_2fa_at" in data:
            self.enforce_2fa_at = data["enforce_2fa_at"]
        if "short_id" in data:
            self.short_id = data["short_id"]
        if "account_id" in data:
            self.account_id = data["account_id"]
        if "enabled_features" in data:
            self.enabled_features = data["enabled_features"]
        if "maintenance_email"in data:
            self.maintenance_email = data["maintenance_email"]
        if "abuse_email" in data:
            self.abuse_email = data["abuse_email"]
        if "address" in data:
            self.address = data["address"]
        if "billing_address" in data:
            self.billing_address = data["billing_address"]
        if "account_manager" in data:
            self.account_manager = data["account_manager"]
        if "logo" in data:
            self.logo = data["logo"]
        if "logo_thumb" in data:
            self.logo_thumb = data["logo_thumb"]
        if "projects" in data:
            self.projects = data["projects"]
        if "plan" in data:
            self.plan = data["plan"]
        if "monthly_spend" in data:
            self.monthly_spend = data["monthly_spend"]
        if "current_user_abilities" in data:
            self.current_user_abilities = data["current_user_abilities"]
        if "href" in data:
            self.href = data["href"]

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
