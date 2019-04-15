# Created by mqgao at 2019/2/18

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter
"""

BASE_CONTENT = """


谢谢！

值得注意的是，我们的报名的流程为：

第一步：准到平台报名 
 -> 第二步：收到编程测试题、协议及课程详情
第三步：课程组打电话与保过班同学确认具体信息
第三步：参加编程预修课 (可选)
第四步：完成编程能力测试，协议确认无误，签订课程协议 
第五步：缴纳学费，按照邮件完成课程相关准备工作
第六步 3.29日：正式开课
      
最后，

祝您生活愉快学习进步，期待我们3月课程的相遇。 
"""

SCHOLAR_PART = """
鉴于您的优秀背景，我们给您50%课程费用的奖学金。

您收到的协议已经是减去了覆盖的费用，请核对。 
"""

NON_SCHOLAR_PART = ""

NEED_APPLY = '另外，因此次报名人数超过预期，奖学金申请者人数众多，奖学金名额已经发放完毕。'

FULL_CONTENT = """

尊敬的{}, 您好，感谢报名我们的课程。 
{}

一、 

为保证我们的课程质量与您的相关权益，我们将相关信息发送给您。 您收到的附件应该为一个 zip 压缩包，解压之后应该包括4个文件：

1. 致同学信： 介绍了我们课程的背景和宗旨；
2. 编程自测题:  为保障课程质量，我们需要首先进行编程能力测试。请在三道题中任选一道，使用 Python 程序完成编程任务，每道题我们给出了测试用例，您可以依据测试用例来进行自测。如果您的程序运行结果和我们给出的结果符合，那么就说明您的程序是通过的。 如果您对自己的结果不确信，请直接回复邮件进行咨询。 
3. 相关流程： 该文件描述了我们之后各种事务的整体流程，您可以参考里边的流程进行操作。有问题请及时联系我们。 
4. 课程协议：该协议里包含学费、付款方式、课程大纲、保密协议等相关事项，说明了课程与其他相关培训内容, 明确了双方的责任与义务。 
5. 正式课程之前的答疑群：我们为大家提供了编程能力讨论、课程信息讨论的微信群，大家可以扫描下方二维码加入群组，我们的老师会在其中解答大家的问题。 

{}

二、

如果您的程序已经通过自测，那么请检查我们的课程协议以及课程大纲，确认无误后，返回签名之后的协议， 课程协议在附件中，请您仔细阅读。 
您可以通过以下3种方式签署邮件：

+ 如果您习惯移动端，您可以下载“好签”APP打开此 pdf 进行电子签名，电子签名后通过此邮件进行回复；
+ 如果您在MAC或者 PC 端，您可以在 https://lightpdf.com/zh/sign-pdf 进行电子签名；
+ 如果您偏爱纸质版文件，也可以打印签字后寄送至“北京市朝阳区北四环中路27号盘古大观”。(推荐电子协议)

三、

我们的助教/老师会在近期通过您的预留电话联系您，如果有问题可以直接进行交流。

另外，对于编程有困难的同学，我们在测试里提供了一个计算机科学预修课程，大家可以上完之后再继续做题。


""" + BASE_CONTENT

RETURN_CONTRACT = "并已经确认协议"
NOT_RETURN_CONTRACT = "请您检查自己的协议内容，若确认无误，请签署之后返回协议。"
HAVE_PAID = "且已经完成付费"
NOT_PAID = '您的学费与付款方式在协议第6页，第11项中，请您参照内容进行后续步骤'

FINISH_RETURN = """

{}
{}-{}-课程协议确认

{}你好， 感谢您报名我们的课程， 您已经通过我们的资料审核、编程测试，{}，{}。 

为保证我们课程的正常进行，请同学们在付费完成后，完成以下准备事项： 
 
一、相关软件和环境：

[ ] 1. 添加老师微信: fortymiles， 请备注”第三期”+同学你自己的姓名+课程类别，例如“第三期+刘洋+CV”, “第三期+张帅+NLP”.  若已经添加老师，请给他发个信息，依照以上格式，老师可能现在还不知道你的名字。 
[ ] 2. 申请Trello 账号，并下载移动版，并且加入 Trello 项目  https://trello.com/invite/b/C7SloqR1/ccb9047babd4ae5aa9b5cf700fc7b1c9/ai-for-nlp-cv-course
--地址为为:  trello 为我们进行课程 Task管理 与消息通告的 billboard; 
[ ] 3. 申请GITHUB 账号 ，加入 GITHUB 地址
--我们课程的往期代码资料存放在 GITHUB： https://github.com/Artificial-Intelligence-for-NLP-and-CV, 你可以提前去了解我们课程的信息，当然，这一次的课程信息肯定会与上次不同，每次上完课后，该节课的信息(课件、代码)便会传至 GITHUB 中。 注册 GITHUB 账户是进行代码同步的唯一方式； 
[ ] 4. 加入 Slack 讨论组(可以在网页打开或者手机下载 slack 该 app)
https://join.slack.com/t/ai-for-nlp-and-cv-3th/shared_invite/enQtNTg3Njk4OTA2NDg3LTc0ZTJmNGFjNGFjOTVmNzVkZTAxNTE0ZTlmZjVmNTNkN2U2MTZhNWRkMDJjZWMwNGNiMmIzMWMxNGRkNzFhZWI
--Slack 为我们以后发布课程信息与讨论课程信息的主要地方，请各位同学手机 app 下载。 我们推荐大家使用Slack， 比起微信Slack可以让大家的学习和日常生活进行分离，比起钉钉，Slack 更加便捷、平等。 
[ ] 5. 下载 Zoom 软件，链接： http://www.zoomcloud.cn/download
--Zoom 是我们进行视频会议的软件，该软件的流程播放与高效的协作展示，为我们的课程提供了很大的方便。 
[ ] 6. 下载Anaconda
6.1 MacOS Version: https://repo.anaconda.com/archive/Anaconda3-2018.12-MacOSX-x86_64.pkg
6.2 Win32 Version: https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe
6.3 Linux Version: https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh
[ ] 7. 下载 Pycharm, Professional 版本和 Community 版本均可。 
[ ] 8. 安装 Anaconda, Pip 安装的代理环境:
8.1 Pip Source For MacOS and Linux: 
    $ mkdir ~/.pip
    $ touch ~/.pip/pip.conf
    $ vim ~/.pip/pip.conf  
    # 打开后按i进入插入模式， 将以下```和```中间的内容 copy 进pip.conf中，之后按<esc> -> : -> x(小写)进行退出
    ```
    [global]
    index-url = https://pypi.douban.com/simple
    [install]
    trusted-host=pypi.douban.com
    ```
8.2 Pip Source For Windows: https://blog.csdn.net/riverhope/article/details/78807203
        

二、建议的参考资料：

1. 黑客与画家 Hackers & Painters.pdf : https://github.com/Artificial-Intelligence-for-NLP-and-CV/References/blob/master/Hackers%20%26amp%3B%20Painters.pdf ， 这本书比较有趣，可以用来锻炼英文
2. DeepLearing的数学基础部分: https://github.com/Artificial-Intelligence-for-NLP-and-CV/References/blob/master/AI%20%26%20Machine%20Learning/DeepLearningBook.pdf 
3. 数学建模引论： https://github.com/Artificial-Intelligence-for-NLP-and-CV/References/blob/master/mathematicals/Frank%20R.%20Giordano%2C%20William%20P.%20Fox%2C%20Steven%20B.%20Horton-A%20First%20Course%20in%20Mathematical%20Modeling-Cengage%20Learning%20(2013).pdf
4. Hands on tensorflow: https://github.com/Artificial-Intelligence-for-NLP-and-CV/References/blob/master/AI%20%26%20Machine%20Learning/Hands.On.TensorFlow.pdf

以上代码存放在我们的课程组 GitHub的 公开参考文献中，请直接进行下载。

三、尽早开始在线课程：

依照 Trello 公告系统中的两门在线课程，希望大家按照上边的要求尽早开始。 
 
有问题请及时和我们老师联系， 期待3月29日我们正式课程上的相遇， 谢谢。 
 
祝您生活愉快， 学习进步！
"""


phone_message = """
{}，你好，感谢报名我们的课程，您的报名信息已经收到。 编程测试题目及课程协议、目录大纲已经发送至预留邮箱({})，请查收。如果您有问题需要联系我们，您与我们课程组的联系方式有三种： 
1. 通过发送邮件进行回复咨询；
2.邮件中会附带一个我们助教的微信二维码，可以添加助教二维码进行咨询；
3.如果问题紧急，可以拨打此电话。 
若有问题请及时联系，谢谢。 

【人工智能与自然语言/计算机视觉课程组】
"""

def get_phone_message(name, email):
    return phone_message.format(name, email)


def get_content(name, scholarship):
    return FULL_CONTENT.format(name, SCHOLAR_PART if scholarship else NON_SCHOLAR_PART,
                               NEED_APPLY if not scholarship else '')


def get_return_email(name, with_contract, finish_paid):
    info =[l.split('-') for l in open('send-list.txt').read().split('\n') if l]
    # print(info)
    info = {n:(p, m, c) for (n, p, m, c, t) in info}

    return FINISH_RETURN.format(info[name][1], name,
                                  '人工智能与自然语言处理' if info[name][-1] == 'NLP' else '深度学习与计算机视觉',
                                name,
                                RETURN_CONTRACT if with_contract else NOT_RETURN_CONTRACT,
                                HAVE_PAID if finish_paid else NOT_PAID
                                )

def get_batch_finish_email_content(users):
    for u in users:
        print('#'*18)
        print(get_return_email(*u))


if __name__ == '__main__':
    users = """
    张强 1 0
    """

    users = [line.replace(',', '').split() for line in users.split('\n') if line]
    users = [(line[0], int(line[1]), int(line[2])) for line in users if len(line) > 1]

    get_batch_finish_email_content(users)

    # print(get_content(name='高民权', scholarship=True))
    # useer_list =
    # print(get_return_email('倪天骄', 1))
    # print('#############')
    # print(get_return_email('倪天骄', 0))
