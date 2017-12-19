# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
import datetime
from zheye import zheye
from urllib.parse import urljoin

from scrapy.loader import ItemLoader

from ZhiHu.items import ZhiHuQuestionItem
from ZhiHu.items import ZhiHuAnswerItem


class ZhihuSpider(scrapy.Spider):

    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    answer_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit={1}&offset={2}'

    accout = '18810266409'
    passwd = 'XXxx19911014'

    headers = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
    }

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        urls = [urljoin(response.url, url) for url in urls]
        urls = filter(lambda x: True if x.startswith("https") else False, urls)
        for url in urls:
            match_obj = re.match(r'(.*zhihu.com/question/(\d+))(/|$).*', url)
            if match_obj:
                request_url = match_obj.group(1)
                question_id = match_obj.group(2)
                yield scrapy.Request(request_url, headers=self.headers,
                                     meta={'question_id': question_id},
                                     callback=self.parse_question)
            else:
                pass

    def parse_question(self, response):
        item_loader = ItemLoader(item=ZhiHuQuestionItem(), response=response)

        item_loader.add_xpath('title',
                              '//h1[@class="QuestionHeader-title"]/text()')
        item_loader.add_xpath('content',
                              '//div[@class="QuestionHeader-detail"]')
        item_loader.add_value('url',
                              response.url)
        item_loader.add_value('zhihu_id',
                              int(response.meta['question_id']))
        item_loader.add_xpath('answer_num',
                              '//h4[@class="List-headerText"]/span/text()')
        item_loader.add_xpath('comments_num',
                              '//div[@class="QuestionHeader-Comment"]//button/text()')
        item_loader.add_xpath('watch_user_num',
                              '//div[@class="NumberBoard-value"]/text()')
        item_loader.add_xpath('click_num',
                              '//div[@class="NumberBoard-value"]/text()')
        item_loader.add_xpath('topics',
                              '//div[@class="QuestionHeader-topics"]//div[@class="Popover"]/div/text()')

        yield item_loader.load_item()

        yield scrapy.Request(self.answer_url.format(response.meta['question_id'], 20, 0),
                             headers=self.headers,
                             callback=self.parse_answer)

    def parse_answer(self, response):

        answers_json = json.loads(response.text)
        answer_item = ZhiHuAnswerItem()

        is_end = answers_json['paging']['is_end']
        next_url = answers_json['paging']['next']

        for ans_json in answers_json['data']:
            answer_item['zhihu_id'] = ans_json['id']
            answer_item['url'] = ans_json['url']
            answer_item['question_id'] = ans_json['question']['id']
            answer_item['author_id'] = ans_json['author']['id'] if 'id' in ans_json['author'] else None
            answer_item['content'] = ans_json['content'] if 'content' in ans_json else None
            answer_item['praise_num'] = ans_json['voteup_count']
            answer_item['comments_num'] = ans_json['comment_count']
            answer_item['create_time'] = ans_json['created_time']
            answer_item['update_time'] = ans_json['updated_time']
            answer_item['crawl_time'] = datetime.datetime.now()

            yield answer_item

        if is_end == 'false':
            yield scrapy.Request(next_url,
                                 headers=self.headers,
                                 callback=self.parse_answer)

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com',
                               headers=self.headers,
                               callback=self.login)]

    def login(self, response):
        xsrf = response.xpath('/html/body/input/@value').extract()[0]
        t = str(int(time.time() * 1000))
        url = 'https://www.zhihu.com/captcha.gif?r={}&type=login&lang=cn'.format(t)
        post_data = {
            '_xsrf': xsrf,
            'password': self.passwd,
            'captcha_type': 'cn',
            'phone_num': self.accout
        }

        yield scrapy.Request(url, headers=self.headers,
                             meta={'post_data': post_data},
                             callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        with open('pic_captcha.gif', "wb") as f:
            f.write(response.body)

        z = zheye()
        pos = z.Recognize('pic_captcha.gif')
        pos_arr = []
        if len(pos) == 2:
            if pos[0][1] > pos[1][1]:
                pos_arr.append([pos[1][1], pos[1][0]])
                pos_arr.append([pos[0][1], pos[0][0]])
            else:
                pos_arr.append([pos[0][1], pos[0][0]])
                pos_arr.append([pos[1][1], pos[1][0]])
        else:
            pos_arr.append([pos[0][1], pos[0][0]])

        post_data = response.meta.get('post_data', {})
        post_url = "https://www.zhihu.com/login/phone_num"

        if len(pos) == 2:
            post_data['captcha'] = '{"img_size": [200, 44], "input_points": [[%.2f, %f], [%.2f, %f]]}' % (
                pos_arr[0][0] / 2, pos_arr[0][1] / 2, pos_arr[1][0] / 2, pos_arr[1][1] / 2)
        else:
            post_data['captcha'] = '{"img_size": [200, 44], "input_points": [%.2f, %f]}' % (
                pos_arr[0][0] / 2, pos_arr[0][1] / 2)

        # print(post_data)
        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        text_json = json.loads(response.text)
        if 'msg' in text_json and text_json['msg'] == '登录成功':
            print('登录成功')

            for url in self.start_urls:

                yield scrapy.Request(url, headers=self.headers, dont_filter=True)
