from data_access.query import get_connection

print("test db connection:",end="")
with get_connection() as conn:
    print("ok")
