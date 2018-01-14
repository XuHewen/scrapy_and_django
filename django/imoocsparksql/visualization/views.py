from django.shortcuts import render
from django.http import JsonResponse
from utils import MysqlUtils


# Create your views here.
def index(request):
    if request.method.lower() == 'get':
        return render(request, 'index.html')


def ajax_data(request, day):
    conn = MysqlUtils.get_connection()
    cur = conn.cursor()

    sql = 'select cms_id, times from day_video_topn where day=day order by times desc limit 5'
    cur.execute(sql)

    id2course = {
        "1459": 'Spark',
        '3520': 'Django',
        '2923': 'Scrapy',
        '1412': 'Mysql',
        '2513': 'DeepLearning'
    }

    data = cur.fetchall()
    for i, value in enumerate(data):
        data[i]['cms_id'] = id2course[str(value['cms_id'])]

    MysqlUtils.release_connection(conn, cur)

    return JsonResponse(data, safe=False)

