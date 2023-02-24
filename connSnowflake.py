from __future__ import annotations

from glue.snowflake import Snowflake


def sf():
    sf = Snowflake(
            role='role_name',
            warehouse='wh_name',
            database='a_db',
            user='user_name',
            password='pwd_name')
    return sf