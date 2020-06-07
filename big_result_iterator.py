"""
Query result consistency can be regulated by DB isolation level or by sorting.
If you need strong consistency, you can use "SERIALIZABLE" level (in case of postgres).
Otherwise you can just add sorting to your query or run query as-is.
"""
from typing import Iterable

import sqlalchemy
import sqlalchemy.orm


def iter_big_result(
        query: sqlalchemy.orm.Query,
        chunk_size: int,
        ) -> Iterable:
    if not isinstance(query, sqlalchemy.orm.Query):
        raise ValueError("iter_big_result expects only {} as query. Got - {}".format(
            sqlalchemy.orm.Query,
            type(query)
        ))
    offset = 0
    total = float('inf')
    if query._limit:
        total = query._limit
    while total > offset:
        chunk = (
            query
            .offset(offset)
            .limit(
                min(
                    chunk_size,
                    total - offset
                )
            )
            .all()
        )
        if not chunk:
            break
        offset += len(chunk)
        yield from chunk
