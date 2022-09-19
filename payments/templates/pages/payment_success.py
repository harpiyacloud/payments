# Copyright (c) 2022, Harpiya Software Technologies

import harpiya

no_cache = True


def get_context(context):
	token = harpiya.local.form_dict.token
	doc = harpiya.get_doc(harpiya.local.form_dict.doctype, harpiya.local.form_dict.docname)

	context.payment_message = ""
	if hasattr(doc, "get_payment_success_message"):
		context.payment_message = doc.get_payment_success_message()
