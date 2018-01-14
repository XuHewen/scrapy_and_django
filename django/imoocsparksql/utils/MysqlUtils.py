import MySQLdb
import MySQLdb.cursors as cursors


def get_connection():
    user = 'root'
    password = '808258'
    host = '127.0.0.1'
    db_name = 'imooc_spark'
    port = 3306

    conn = MySQLdb.connect(user=user, password=password, host=host,
                           db=db_name, port=port, cursorclass=cursors.DictCursor)

    return conn


def release_connection(conn, cur):
    try:
        if cur is not None:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    conn = get_connection()
    cur = conn.cursor()
    sql = 'select cms_id, times from day_video_topn order by times desc limit 5'
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    release_connection(conn, cur)

