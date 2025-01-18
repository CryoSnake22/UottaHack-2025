import mysql.connector


def insert_data_in_batches(data, db_config, table_name, batch_size=10000):
    """
    Insert lines from a large file into a MySQL table in batches.

    :param file_path: Path to the input file.
    :param db_config: MySQL connection configuration as a dictionary.
    :param table_name: Target MySQL table name.
    :param batch_size: Number of rows to insert per batch.
    """
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    batch = []
    for item in data:
        if item.get("href") is not None:
            batch.append(
                (
                    item.get("href"),
                    item.get("username"),
                    item.get("password"),
                    item.get("protocol"),
                    item.get("host"),
                    item.get("port"),
                    item.get("hostname"),
                    item.get("pathname"),
                    item.get("search"),
                    item.get("hash"),
                    item.get("application"),
                )
            )

            # INSERT INTO {table_name}
            # (href, username, password, protocol, host, port, hostname, pathname, search, hash, application)
            # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
        if len(batch) >= batch_size:
            cursor.executemany(
                f"""

                INSERT INTO {table_name} 
                (href, username, password, protocol, host, port, hostname, pathname, search, hash, application) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                username = VALUES(username),
                password = VALUES(password),
                protocol = VALUES(protocol),
                host = VALUES(host),
                port = VALUES(port),
                hostname = VALUES(hostname),
                pathname = VALUES(pathname),
                search = VALUES(search),
                hash = VALUES(hash),
                application = VALUES(application);
                """,
                batch,
            )
            conn.commit()
            batch = []  # Reset batch after inserting

            # INSERT INTO {table_name}
            # (href, username, password, protocol, host, port, hostname, pathname, search, hash, application)
            # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    if batch:
        cursor.executemany(
            f"""


            INSERT INTO {table_name} 
            (href, username, password, protocol, host, port, hostname, pathname, search, hash, application) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            username = VALUES(username),
            password = VALUES(password),
            protocol = VALUES(protocol),
            host = VALUES(host),
            port = VALUES(port),
            hostname = VALUES(hostname),
            pathname = VALUES(pathname),
            search = VALUES(search),
            hash = VALUES(hash),
            application = VALUES(application);
            """,
            batch,
        )
        conn.commit()
    cursor.close()
    conn.close()
    print("Data import complete!")
