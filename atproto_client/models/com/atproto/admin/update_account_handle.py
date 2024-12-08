##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

from atproto_client.models import base, string_formats


class Data(base.DataModelBase):
    """Input data model for :obj:`com.atproto.admin.updateAccountHandle`."""

    did: string_formats.Did  #: Did.
    handle: string_formats.Handle  #: Handle.


class DataDict(t.TypedDict):
    did: string_formats.Did  #: Did.
    handle: string_formats.Handle  #: Handle.