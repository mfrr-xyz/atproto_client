##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

from atproto_client.models import base


class Response(base.ResponseModelBase):
    """Output data model for :obj:`app.bsky.unspecced.getConfig`."""

    check_email_confirmed: t.Optional[bool] = None  #: Check email confirmed.
