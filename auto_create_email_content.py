# Created by mqgao at 2019/2/18

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from parse_excel import get_records
from email_content import get_content, get_phone_message
from get_zip_file import zip_files
import os
import time


SEND_LIST = 'send-list.txt'
have_sent = open(SEND_LIST, 'r', encoding='utf-8').read().split('\n')

pdfmetrics.registerFont(TTFont('Chinese', 'MS-Yahei.ttf'))


def write_to_pdf(name, phone, email, pdf_file, destination):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Chinese", 14)
    can.drawString(150, 635, name.encode('utf-8'))
    can.drawString(150, 615, phone)
    can.drawString(150, 595, email)
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    # new_pdf = PdfFileReader(packet)
    # read your existing PDF
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open(pdf_file, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    for i in range(10):
        try:
            output.addPage(existing_pdf.getPage(i+1))
        except IndexError as e:
            break

    # finally, write "output" to a real file
    output_stream = open(destination, "wb")
    output.write(output_stream)
    output_stream.close()
    print('write to {} okay'.format(destination))


CV, NLP = 'CV', 'NLP'
BG, TG = 'BG', 'TG'
FULL, HALF = 'FULL', 'HALF'
NL_BASE = '附件4 -- 人工智能与自然语言处理课程协议{}-{}'
CV_BASE = '附件4 -- 深度学习与计算机视觉课程协议{}-{}'

type_mapper = {
    CV: CV_BASE,
    NLP: NL_BASE,
}


def write_contract_by_category(name, phone, email, course, category, money):
    if money == HALF: comment = '(含50%奖学金)'
    else: comment = ''

    file_postfix = type_mapper[course].format(comment, name)

    desination = 'pdf-outputs/{}.pdf'.format(file_postfix)

    write_to_pdf(name, phone, email,
                 'pdf-files/{}-{}-{}.pdf'.format(course, category, money),
                 desination)

    return desination


def create_zip_file(name, contract_path, category):
    root = 'need-send-to-email'
    files = [os.path.join(root, s) for s in os.listdir(root)] + [contract_path]
    zip_files(files, 'zipfiles/{}-{}-课程协议-编程测试'.format(name, category))


def parse_records(filename, scholarships=None):
    "input a record, get the category"

    email_content = open('email-content.txt', 'w', encoding='utf-8')

    records = get_records(filename)

    k_name, k_phone, k_email = '姓名', '手机号码', '邮箱'
    k_wechat, k_scholarship = '微信号', '奖学金'
    k_major, k_type = '报名主修方向', '报名课程类型'
    k_degree = '最高学历'

    k_school = '目前就读或毕业学校(必填)'
    k_study = '就读专业'

    students_number = len(records[k_name])

    new_student_num = 0

    phone_numbers = []

    for i in range(students_number):
        name, phone, email = records[k_name][i], records[k_phone][i], records[k_email][i]
        _type, major = records[k_type][i], records[k_major][i]
        wechat = records[k_wechat][i]

        try:
            phone = str(int(phone))
        except:
            phone = ''

        school, study = records[k_school][i], records[k_study][i]

        degree = records[k_degree][i]

        try:
            reduce_money = records[k_scholarship][i]
        except KeyError:
            reduce_money = ""

        if reduce_money: give_scholarship = True
        else:
            give_scholarship = False

        if '保过' in _type: _type = BG
        else:
            _type = TG

        # print(major)
        if '自然语言' in major: major = NLP
        else:
            major = CV

        if email.endswith('con'): email = email[:-len('con')]+'com'

        user_id = '{}-{}-{}-{}-{}'.format(name, phone, email, major, _type)
        if user_id in have_sent: continue

        print(_type)

        # if not give_scholarship and degree == '硕士' or degree == '博士':
        #     s = input('if has scholarship for {} {} {}? 0 for Not 1 for Yes(default 0)'.format(school, study, degree))
        #     if s == '1': give_scholarship = True

        contract_path = write_contract_by_category(name, str(phone), str(email), major, _type, HALF if give_scholarship else FULL)

        CV_title = '深度学习与计算机视觉'
        NLP_title = '人工智能与自然语言处理'

        course_title = CV_title if major == CV else NLP_title

        title = "【{}-{}】培训课程编程能力测试及课程协议".format(name, course_title)

        split = """
{} ##########################
{}
{}
        \n""".format(i, email, title)

        print(split)

        email_content.write(split)
        email_content.write(get_content(name, give_scholarship))

        create_zip_file(name, contract_path, course_title)

        have_sent.append(user_id)
        new_student_num += 1
        phone_numbers.append((name, phone, email))

    email_content.close()

    with open(SEND_LIST, 'w', encoding='utf-8') as f:
        f.write('\n'.join(have_sent))

    print('Need Send {} emails'.format(new_student_num))

    print('Need send message: ')
    for i, (n, p, e) in enumerate(phone_numbers):
        print('*'*18)
        print((i+1, n, p))
        print(get_phone_message(n, e))


if __name__ == '__main__':
    # for a, b, c in product([CV, NLP], [BG, TG], [FULL, HALF]):
    #     write_contract_by_category('高民权', '18910321429', 'mqgao@qq.com', a, b, c)
    # write_contract_by_category('曾冯庆阳', '13163023060', '649977910@qq.com', CV, TG, HALF)
    excle_path = '/Users/mqgao/Library/Mobile Documents/com~apple~CloudDocs/2019春天-人工智能与自然语言:计算机视觉/【拿不到 offer全额退款】人工智能与 NLP _ 第一批.xls'
    # excle_path = '/Users/mqgao/Downloads/【拿不到 offer全额退款】海外线下报名表 (1).xls'
    parse_records(excle_path, [])
    # create_zip_file(1, 2)
