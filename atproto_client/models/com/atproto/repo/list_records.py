##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

import typing_extensions as te
from pydantic import Field

from atproto_client.models import string_formats

if t.TYPE_CHECKING:
    from atproto_client import models
    from atproto_client.models.unknown_type import UnknownType
from atproto_client.models import base


class Params(base.ParamsModelBase):
    """Parameters model for :obj:`com.atproto.repo.listRecords`."""

    collection: string_formats.Nsid  #: The NSID of the record type.
    repo: string_formats.Handle  #: The handle or DID of the repo.
    cursor: t.Optional[str] = None  #: Cursor.
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)  #: The number of records to return.
    reverse: t.Optional[bool] = None  #: Flag to reverse the order of the returned records.
    rkey_end: t.Optional[str] = None  #: DEPRECATED: The highest sort-ordered rkey to stop at (exclusive).
    rkey_start: t.Optional[str] = None  #: DEPRECATED: The lowest sort-ordered rkey to start from (exclusive).


class ParamsDict(t.TypedDict):
    collection: string_formats.Nsid  #: The NSID of the record type.
    repo: string_formats.Handle  #: The handle or DID of the repo.
    cursor: te.NotRequired[t.Optional[str]]  #: Cursor.
    limit: te.NotRequired[t.Optional[int]]  #: The number of records to return.
    reverse: te.NotRequired[t.Optional[bool]]  #: Flag to reverse the order of the returned records.
    rkey_end: te.NotRequired[t.Optional[str]]  #: DEPRECATED: The highest sort-ordered rkey to stop at (exclusive).
    rkey_start: te.NotRequired[t.Optional[str]]  #: DEPRECATED: The lowest sort-ordered rkey to start from (exclusive).


class Response(base.ResponseModelBase):
    """Output data model for :obj:`com.atproto.repo.listRecords`."""

    records: t.List['models.ComAtprotoRepoListRecords.Record']  #: Records.
    cursor: t.Optional[str] = None  #: Cursor.


class Record(base.ModelBase):
    """Definition model for :obj:`com.atproto.repo.listRecords`."""

    cid: string_formats.Cid  #: Cid.
    uri: string_formats.AtUri  #: Uri.
    value: 'UnknownType'  #: Value.

    py_type: t.Literal['com.atproto.repo.listRecords#record'] = Field(
        default='com.atproto.repo.listRecords#record', alias='$type', frozen=True
    )
