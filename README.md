### Big Result Set Iterator

`iter_big_result(query, chunk_size: int)`
Takes sqlalchemy.orm.Query object and chunk size.
Returns query result iterator, asking no more than chunk_size lines as necessary.


Query result consistency can be regulated by DB isolation level or by sorting.
If you need strong consistency, you can use "SERIALIZABLE" level (in case of postgres).
Otherwise you can just add sorting to your query or run query as-is.


Tested on Python 3.5.2.
