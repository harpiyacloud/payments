# Copyright (c) 2022, Harpiya Software Technologies

import harpiya


def get_context(context):
	token = harpiya.local.form_dict.token

	if token:
		harpiya.db.set_value("Integration Request", token, "status", "Cancelled")
		harpiya.db.commit()
