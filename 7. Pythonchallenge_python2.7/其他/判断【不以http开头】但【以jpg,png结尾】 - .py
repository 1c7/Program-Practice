﻿# python2.7
# 2012/11/9


import re


# 列表下标是从0开始的
list = ['ho.jpg', 'http://jdstatic.tankr.net/appicon.png', 'http://jdstatic.tankr.net/favicon.ico', 'http://feeds.feedburner.com/jandan', 'http://jandan.net/archives/Jandan.xml', '/', '/', '/tag/\xe8\xb5\xb0\xe8\xbf\x9b\xe7\xa7\x91\xe5\xad\xa6', '/new', '/home', '/comments', '/?random', '/category/playbus', '/v', '/m', '/fml', '/ooxx', '/pic', 'http://talk.jandan.net/', 'http://jandan.xd.com/', 'http://jandan.net/2012/11/09', 'http://jandan.net/2012/11/09/transparent-back-seat.html', 'http://jandan.net/2012/11/09/transparent-back-seat.html#comments', 'http://jandan.net/2012/11/09/transparent-back-seat.html', 'http://jandan.net/author/ws', 'http://jandan.net/2012/11/09/boy-steals-4000-for-candy.html', 'http://jandan.net/2012/11/09/boy-steals-4000-for-candy.html#comments', 'http://jandan.net/2012/11/09/boy-steals-4000-for-candy.html', 'http://jandan.net/tag/%e6%82%b2%e5%89%a7%e5%95%8a', 'http://jandan.net/author/lxsed', 'http://jandan.net/2012/11/09/impossibly-thin-hybrid-drive.html', 'http://jandan.net/2012/11/09/impossibly-thin-hybrid-drive.html#comments', 'http://jandan.net/2012/11/09/impossibly-thin-hybrid-drive.html', 'http://jandan.net/author/pwwp', 'http://jandan.net/2012/11/09/slice-tongue-win-back-wife.html', 'http://jandan.net/2012/11/09/slice-tongue-win-back-wife.html#comments', 'http://jandan.net/2012/11/09/slice-tongue-win-back-wife.html', 'http://jandan.net/tag/%e9%87%8d%e5%8f%a3%e5%91%b3', 'http://jandan.net/author/lxsed', 'http://jandan.net/2012/11/09/methamphetamine-vaccine.html', 'http://jandan.net/2012/11/09/methamphetamine-vaccine.html#comments', 'http://jandan.net/2012/11/09/methamphetamine-vaccine.html', 'http://jandan.net/tag/%e8%b5%b0%e8%bf%9b%e7%a7%91%e5%ad%a6', 'http://jandan.net/author/ws', 'http://jandan.net/2012/11/09/real-gold-card.html', 'http://jandan.net/2012/11/09/real-gold-card.html#comments', 'http://jandan.net/2012/11/09/real-gold-card.html', 'http://jandan.net/tag/%e7%88%b7%e6%9c%89%e9%92%b1', 'http://jandan.net/author/hugh', 'http://jandan.net/2012/11/09/ragecomic-saved-life.html', 'http://jandan.net/2012/11/09/ragecomic-saved-life.html#comments', 'http://jandan.net/2012/11/09/ragecomic-saved-life.html', 'http://jandan.net/tag/geek', 'http://jandan.net/author/hugh', 'http://jandan.net/2012/11/09/fml-604.html', 'http://jandan.net/2012/11/09/fml-604.html#comments', 'http://jandan.net/2012/11/09/fml-604.html', 'http://jandan.net/tag/%e5%8f%91%e9%9c%89%e5%95%a6', 'http://jandan.net/author/eirene', 'http://jandan.net/2012/11/09/live-in-cemetery.html', 'http://jandan.net/2012/11/09/live-in-cemetery.html#comments', 'http://jandan.net/2012/11/09/live-in-cemetery.html', 'http://jandan.net/tag/%e7%9c%9f%e7%9a%84%e7%8c%9b%e5%a3%ab', 'http://jandan.net/author/eirene', 'http://jandan.net/2012/11/08/incurable-cancer.html', 'http://jandan.net/2012/11/08/incurable-cancer.html#comments', 'http://jandan.net/2012/11/08/incurable-cancer.html', 'http://jandan.net/tag/%e6%82%b2%e5%89%a7%e5%95%8a', 'http://jandan.net/author/shixinxin', 'http://jandan.net/2012/11/08/obama-romney.html', 'http://jandan.net/2012/11/08/obama-romney.html#comments', 'http://jandan.net/2012/11/08/obama-romney.html', 'http://jandan.net/tag/wtf', 'http://jandan.net/author/admin', 'http://jandan.net/2012/11/08/hurricane-sandy-before-and-after-shots.html', 'http://jandan.net/2012/11/08/hurricane-sandy-before-and-after-shots.html#comments', 'http://jandan.net/2012/11/08/hurricane-sandy-before-and-after-shots.html', 'http://jandan.net/tag/%e6%82%b2%e5%89%a7%e5%95%8a', 'http://jandan.net/author/pwwp', 'http://jandan.net/2012/11/08/gmail-is-most-used-email.html', 'http://jandan.net/2012/11/08/gmail-is-most-used-email.html#comments', 'http://jandan.net/2012/11/08/gmail-is-most-used-email.html', 'http://jandan.net/tag/geek', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/street-lights-controled-by-ipad.html', 'http://jandan.net/2012/11/08/street-lights-controled-by-ipad.html#comments', 'http://jandan.net/2012/11/08/street-lights-controled-by-ipad.html', 'http://jandan.net/tag/geek', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/chinese-makes-ark.html', 'http://jandan.net/2012/11/08/chinese-makes-ark.html#comments', 'http://jandan.net/2012/11/08/chinese-makes-ark.html', 'http://jandan.net/tag/%e5%9b%bd%e5%86%85%e8%a7%82%e5%85%89', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/my-mom-is-fit.html', 'http://jandan.net/2012/11/08/my-mom-is-fit.html#comments', 'http://jandan.net/2012/11/08/my-mom-is-fit.html', 'http://jandan.net/tag/%e7%be%8e%e5%a5%b3', 'http://jandan.net/author/mailer', 'http://jandan.net/2012/11/08/british-mad-mullah.html', 'http://jandan.net/2012/11/08/british-mad-mullah.html#comments', 'http://jandan.net/2012/11/08/british-mad-mullah.html', 'http://jandan.net/tag/%e7%9c%9f%e7%9a%84%e7%8c%9b%e5%a3%ab', 'http://jandan.net/author/lxsed', 'http://jandan.net/2012/11/08/gummy-python-candy.html', 'http://jandan.net/2012/11/08/gummy-python-candy.html#comments', 'http://jandan.net/2012/11/08/gummy-python-candy.html', 'http://jandan.net/tag/%e9%85%b7', 'http://jandan.net/author/hugh', 'http://jandan.net/2012/11/08/grand-hotel-opening.html', 'http://jandan.net/2012/11/08/grand-hotel-opening.html#comments', 'http://jandan.net/2012/11/08/grand-hotel-opening.html', 'http://jandan.net/tag/%e5%86%b7%e6%96%b0%e9%97%bb', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/obama-win-on-facebook.html', 'http://jandan.net/2012/11/08/obama-win-on-facebook.html#comments', 'http://jandan.net/2012/11/08/obama-win-on-facebook.html', 'http://jandan.net/tag/%e5%86%b7%e6%96%b0%e9%97%bb', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/thai-tattoo-violence.html', 'http://jandan.net/2012/11/08/thai-tattoo-violence.html#comments', 'http://jandan.net/2012/11/08/thai-tattoo-violence.html', 'http://jandan.net/tag/%e5%86%b7%e6%96%b0%e9%97%bb', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/smell-the-armpit.html', 'http://jandan.net/2012/11/08/smell-the-armpit.html#comments', 'http://jandan.net/2012/11/08/smell-the-armpit.html', 'http://jandan.net/tag/%e9%87%8d%e5%8f%a3%e5%91%b3', 'http://jandan.net/author/lucius', 'http://jandan.net/2012/11/08/bamboo-billboard.html', 'http://jandan.net/2012/11/08/bamboo-billboard.html#comments', 'http://jandan.net/2012/11/08/bamboo-billboard.html', 'http://jandan.net/tag/%e8%ae%be%e8%ae%a1', 'http://jandan.net/author/pwwp', 'http://jandan.net/2012/11/07/personal-stars.html', 'http://jandan.net/2012/11/07/personal-stars.html#comments', 'http://jandan.net/2012/11/07/personal-stars.html', 'http://jandan.net/tag/geek', 'http://jandan.net/author/lucius', 'http://jandan.net/page/2', 'http://jandan.net/page/3', 'http://jandan.net/page/4', 'http://jandan.net/page/5', 'http://jandan.net/page/6', 'http://jandan.net/page/2', 'http://jandan.net/page/1251', 'http://jandan.net/page/2', 'http://jandan.net/more', 'http://feed.feedsky.com/diggdigest', 'http://www.jue.so/', 'http://www.nuandao.com/?utm_campaign=campaign1&utm_medium=banner&utm_source=jiandan&utm_content=260x85', 'http://www.wowsai.com/index.php?app=shopping&act=topics&view=single&utm_source=jandan&utm_medium=banner&utm_content=danshenjiebugudan&utm_campaign=huodong12', 'http://jandan.net/tag/geek', 'http://jandan.net/tag/\xe6\xbc\xab\xe7\x94\xbb', 'http://jandan.net/tag/\xe4\xb9\x90\xe9\xab\x98', 'http://jandan.net/tag/\xe5\xb0\x8f\xe8\xb4\xb4\xe5\xa3\xab', 'http://jandan.net/tag/meme', 'http://jandan.net/tag/diy', 'http://jandan.net/tag/\xe8\xb5\xb0\xe8\xbf\x9b\xe7\xa7\x91\xe5\xad\xa6', 'http://jandan.net/tag/\xe6\x97\xa0\xe5\x8e\x98\xe5\xa4\xb4\xe7\xa0\x94\xe7\xa9\xb6', 'http://jandan.net/tag/\xe5\xa4\x96\xe6\x98\x9f\xe4\xba\xba', 'http://jandan.net/tag/\xe5\xa4\xa9\xe6\x96\x87', 'http://jandan.net/tag/nasa', 'http://jandan.net/tag/\xe5\x86\xb7\xe6\x96\xb0\xe9\x97\xbb', 'http://jandan.net/tag/\xe7\x9c\x9f\xe7\x9a\x84\xe7\x8c\x9b\xe5\xa3\xab', 'http://jandan.net/tag/\xe5\xa4\xa7\xe4\xb8\x88\xe5\xa4\xab', 'http://jandan.net/tag/\xe7\x88\xb7\xe6\x9c\x89\xe9\x92\xb1', 'http://jandan.net/tag/\xe8\x87\xb4\xe5\xaf\x8c\xe4\xbf\xa1\xe6\x81\xaf ', 'http://jandan.net/tag/\xe9\x87\x8d\xe5\x8f\xa3\xe5\x91\xb3', 'http://jandan.net/tag/\xe4\xbd\x95\xe5\x85\xb6\xe4\xbd\x8e\xe4\xbf\x97\xe7\x84\x89', 'http://jandan.net/tag/SEX', 'http://jandan.net/tag/\xe6\x82\xb2\xe5\x89\xa7\xe5\x95\x8a', 'http://jandan.net/tag/\xe5\x9b\xbd\xe5\x86\x85\xe8\xa7\x82\xe5\x85\x89', 'http://jandan.net/tag/\xe6\x97\xa0\xe8\x81\x8a\xe5\x9b\xbe\xe9\x9b\x86', 'http://jandan.net/tag/\xe5\xa4\xa7\xe5\x90\x90\xe6\xa7\xbd', 'http://jandan.net/tag/\xe7\xbe\x8e\xe5\xa5\xb3', 'http://jandan.net/tag/\xe4\xb8\x80\xe6\x97\xa5\xe4\xb8\x80\xe7\x8c\xab', 'http://jandan.net/tag/\xe7\x8b\x97', 'http://jandan.net/tag/\xe7\xac\xa8\xe8\xb4\xbc', 'http://jandan.net/tag/\xe9\x85\xb7', 'http://jandan.net/tag/\xe8\x90\x8c', 'http://jandan.net/tag/\xe7\x8e\xaf\xe4\xbf\x9d', 'http://jandan.net/tag/\xe7\x96\xaf\xe7\x8b\x82\xe5\x90\x89\xe5\xb0\xbc\xe6\x96\xaf', 'http://jandan.net/tag/\xe6\x9d\xaf\xe5\x85\xb7\xe5\x82\xbb\xe7\xbc\xba', 'http://jandan.net/tag/\xe9\xab\x98\xe7\xa7\x91\xe6\x8a\x80', 'http://jandan.net/tag/\xe6\x95\xb0\xe7\xa0\x81\xe4\xba\xa7\xe5\x93\x81', 'http://jandan.net/tag/app', 'http://jandan.net/tag/\xe6\x9c\xba\xe5\x99\xa8\xe4\xba\xba', 'http://jandan.net/tag/android', 'http://jandan.net/tag/\xe8\x8b\xb9\xe6\x9e\x9c', 'http://jandan.net/tag/\xe8\xae\xbe\xe8\xae\xa1', 'http://jandan.net/tag/\xe5\xbb\xba\xe7\xad\x91', 'http://jandan.net/tag/\xe8\xae\xbe\xe8\xae\xa1\xe5\xbf\xab\xe8\xaf\xbb', 'http://jandan.net/tag/\xe8\x89\xba\xe6\x9c\xaf', 'http://jandan.net/tag/\xe5\xb9\xbf\xe5\x91\x8a', 'http://jandan.net/tag/\xe6\xb8\xb8\xe6\x88\x8f', 'http://jandan.net/tag/\xe5\x8f\x91\xe9\x9c\x89\xe5\x95\xa6', 'http://jandan.net/tag/\xe8\xb6\x85\xe8\xbd\xbd\xe9\xb8\xa1', 'http://jandan.net/tag/\xe5\x91\xa8\xe6\x9c\xab\xe5\x95\xa6', 'http://jandan.net/tag/\xe9\x80\x8f\xe9\x9c\xb2\xe7\xa4\xbe', 'http://jandan.net/tag/\xe6\xb2\xa1\xe5\x93\x81\xe7\xac\x91\xe8\xaf\x9d\xe9\x9b\x86', 'http://jandan.net/2012/11/08/my-mom-is-fit.html', 'http://jandan.net/2012/11/08/chinese-makes-ark.html', 'http://jandan.net/2012/11/08/hurricane-sandy-before-and-after-shots.html', 'http://jandan.net/2012/11/08/obama-romney.html', 'http://jandan.net/2012/11/08/incurable-cancer.html', 'http://jandan.net/2012/11/09/ragecomic-saved-life.html', 'http://jandan.net/2012/11/09/real-gold-card.html', 'http://jandan.net/2012/11/09/fml-604.html', 'http://jandan.net/2012/11/03/12-accidental-death.html', 'http://jandan.net/2012/11/06/wuhao-curated-shop.html', 'http://jandan.net/2012/11/08/chinese-makes-ark.html', 'http://jandan.net/2012/11/03/hondajet-production.html', 'http://jandan.net/2012/11/08/my-mom-is-fit.html', 'http://jandan.net/2012/11/05/small-world-2012.html', 'http://jandan.net/2012/11/06/ghibli-characters.html', 'http://jandan.net/2012/11/05/beauty-and-coffin.html', 'http://jandan.net/pic#comment-1608141', 'javascript:acv_vote(1608141,1,2);', 'javascript:acv_vote(1608141,0,2);', 'http://jandan.net/pic#comment-1607905', 'javascript:acv_vote(1607905,1,2);', 'javascript:acv_vote(1607905,0,2);', 'http://jandan.net/pic#comment-1607623', 'javascript:acv_vote(1607623,1,2);', 'javascript:acv_vote(1607623,0,2);', 'http://jandan.net/pic#comment-1608185', 'javascript:acv_vote(1608185,1,2);', 'javascript:acv_vote(1608185,0,2);', 'http://jandan.net/pic#comment-1608345', 'javascript:acv_vote(1608345,1,2);', 'javascript:acv_vote(1608345,0,2);', 'http://jandan.net/pic#comment-1608527', 'javascript:acv_vote(1608527,1,2);', 'javascript:acv_vote(1608527,0,2);', 'http://jandan.net/pic#comment-1607907', 'javascript:acv_vote(1607907,1,2);', 'javascript:acv_vote(1607907,0,2);', 'http://jandan.net/pic#comment-1607343', 'javascript:acv_vote(1607343,1,2);', 'javascript:acv_vote(1607343,0,2);', 'https://www.upyun.com/?utm_source=jandan1&utm_medium=ad&utm_campaign=upyun&md=jandan1', 'http://www.aliyun.com/', 'http://wordpress.org/', 'http://jandan.net/ad', 'http://my1510.cn/', 'http://www.appinn.com/', 'http://playbus.net/', 'http://www.williamlong.info/', 'http://gezhi.org/', 'http://apple4.us/', 'http://www.u148.net/', 'http://www.waakee.com/', 'http://solidot.org/', 'http://www.guao.hk/', 'http://www.leica.org.cn', 'http://www.bilibili.tv/', 'http://fun4hi.com/', 'http://www.jifenzhong.com/', 'http://www.acfun.tv/', 'http://talk.jandan.net/', 'http://jandan.net/link', 'http://jandan.net/xmlrpc.php?rsd', 'http://jandan.net/wp-includes/wlwmanifest.xml', 'http://tankr.net/s/small/7KJY.jpg', 'http://tankr.net/s/small/7EAQ.jpg', 'http://tankr.net/s/small/ITJG.jpg', 'http://tankr.net/s/small/0I99.jpg', 'http://tankr.net/s/small/L3WQ.jpg', 'http://pagead2.googlesyndication.com/pagead/show_ads.js', 'http://tankr.net/s/custom/W2KA.jpg', 'http://tankr.net/s/custom/4JA2.png', 'http://tankr.net/s/custom/TZCL.jpg', 'http://tankr.net/s/custom/E9XG.jpg', 'http://tankr.net/s/custom/9G2P.jpg', 'http://tankr.net/s/custom/S8DT.jpg', 'http://ww2.sinaimg.cn/mw600/79ffea53jw1dynuysov9ij.jpg', 'http://tankr.net/s/custom/QUAB.jpg', 'http://tankr.net/s/custom/WL2D.jpg', 'http://tankr.net/s/custom/4OZG.jpg', 'http://tankr.net/s/custom/7403.jpg', 'http://tankr.net/s/custom/HCHC.jpg', 'http://tankr.net/s/custom/XKT9.jpg', 'http://tankr.net/s/custom/RN6O.jpg', 'http://tankr.net/s/custom/OBDW.png', 'http://tankr.net/s/custom/88Q7.jpg', 'http://tankr.net/s/custom/81MF.jpg', 'http://tankr.net/s/custom/Z79H.png', 'http://tankr.net/s/custom/JM9J.jpg', 'http://widget.weibo.com/relationship/followbutton.php?btn=red&amp;style=1&amp;uid=1723063831&amp;width=62&amp;height=22&amp;language=zh_cn', 'http://jdstatic.tankr.net/ajax/125.js?v=20121105', 'http://a.alimama.cn/inf.js', 'http://jdstatic.tankr.net/s/jueso.jpg', 'http://jdstatic.tankr.net/s/nuandao.jpg', 'http://jdstatic.tankr.net/s/wowsai3.jpg', 'http://ww3.sinaimg.cn/bmiddle/6af0aea2jw1dyliwp7wkjj.jpg', 'http://s1.dwstatic.com/group1/M00/AA/B3/2ce3a4be76e4325c399ad1de83ee66c1.jpg', 'http://ww4.sinaimg.cn/mw600/7241dcedjw1dynmodtdnxj.jpg', 'http://fmn.rrimg.com/fmn057/xiaozhan/20121108/1355/original_dKFx_3dad00002461118c.jpg', 'http://ww1.sinaimg.cn/mw600/b05bd106jw1dynqnmylpvj.jpg', 'http://ww2.sinaimg.cn/bmiddle/64181e08jw1dynwsffneij.jpg', 'http://ww3.sinaimg.cn/mw600/80ef084agw1dynoat6w3mj.jpg', 'http://ww2.sinaimg.cn/bmiddle/6628711bjw1dynk7sud7sj.jpg', 'http://pagead2.googlesyndication.com/pagead/show_ads.js', 'http://jdstatic.tankr.net/logos.gif', 'http://jdstatic.tankr.net/ajax/jquery.min.js', 'http://jdstatic.tankr.net/ajax/banner.js?v=20121105', ' + _bdhmProtocol + ']

index = 0
result = []
for one in list:
    pattern = re.compile(r'^[^http]',re.I)
    match = pattern.search(one)
    
    if match:
        #print list[index]
        result.append(list[index])
    index = index + 1

#print index+1  #这是每次循环都会自动增加的下标,循环完成后里面就是列表元素的个数，因为下标是从0开始的，所以要+1
#print result



last = []
lastIndex = 0 #又是存下标用的
for o in result:
    linshi = o  #把每一个元素保存到linshi中，
    houzhui = linshi.split('.')[-1]    #拆分，拿到后缀(如果无法拆分会原样返回,比如拆分123123，会返回123123)
    if linshi == houzhui:
        lastIndex = lastIndex+1
        continue    # 去下一次循环
    
    pattern = re.compile(r'jpg$|png$|bmp$|gif$|jpeg$|ico$',re.I)
    match = pattern.search(houzhui)
    
    if match:
        last.append(result[lastIndex])
    lastIndex = lastIndex+1


print last   
    
#[jpg$|png$|bmp$|gif$|jpeg$|ico$]
#

#del list[0]  # del可以删除数组中指定下表的元素
#print list[0]


#.*































