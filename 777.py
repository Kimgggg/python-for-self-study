# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7
from sys import argv
from os.path import exists
import json


script, fileName = argv
testList = []
#testList = [做座坐作左醉最组阻走总踪渍自子桌准撞状装桩妆转专抓著注住助主逐竹蛛朱周重众种终中置致治制志至指纸止直织知只之证正整睁争震真侦针着这者遮照找招掌长张湛站战占粘沾乍渣怎泽择责则造早糟暂在再仔运晕越月约院怨圆原员冤遇谕预育雨与渔鱼余于右又有友游油由幽用泳哟硬应影萤英印隐饮引音因意易亦议艺义以已疑咦依医衣伊一腋夜也耶要药邀样阳焰验厌演眼颜研言烟呀亚牙鸭询寻醺血学选续绪序许需虚须秀凶性幸兴醒型形星信新心谢写鞋些效笑校小消肖像项向想响详箱相陷宪线现显嫌贤闲鲜先下隙细系戏喜洗袭席息析吸西物舞午五吾无屋握我问吻纹文喂谓位未卫委尾唯围为望忘往枉网亡万碗玩完弯外挖脱托吞推团土涂突投头偷痛筒同通停听厅铁贴调条田添天替体题提藤特套讨逃躺汤探谈摊态太台她他索所缩孙碎岁随虽算蒜诉送松四死斯思私丝司说睡水谁双摔刷束术署殊叔售受寿首守手收嗜释室适是试饰事似市世示士始使蚀食实识时石十湿施师失尸剩绳声生慎什深身伸射设少烧上伤闪山傻沙杀色三赛塞萨软入儒如肉溶容日扔认忍人热让染然群确却券犬蜷全趣去取求请情清轻青琴亲窃怯且茄切巧枪前器汽起启奇其漆期戚瀑普浦蒲破迫婆屏凭评平品片皮批碰篷蓬朋砰喷配陪跑旁判盘派牌排拍怕帕爬偶哦女懦弩弄牛年逆你泥能内呢闹难南男奈乃那哪拿暮幕目木母某谋抹魔摩模摸命明名面眠米谜迷懵们妹美每梅枚没么帽冒毛忙慢满蛮卖买嘛吗码玛马麻略率旅落论伦乱露路禄录鲁喽漏流留令另领绫凌灵琳淋邻瞭料聊疗量谅亮两良脸莲连笠利丽立力理里礼璃离狸类了勒乐老浪狼郎烂蓝兰来辣啦扩况快块裤袴库苦口控空肯客刻克可科柯靠烤考看凯开卡咖俊君绝决卷据剧具句巨举局居就救酒久究镜竟净警精经京劲近进尽紧金今巾借界解姐结街接窖较觉叫脚角焦交酱奖讲将江箭鉴溅渐剑荐件见简检捡间嫁架假甲家加祭继既迹剂际技记计己几急即级吉及基鸡矶机击祸或伙火活混婚昏惠绘会回灰晃慌换环欢怀话画化华划花护户胡狐忽呼乎候后吼哄鸿红横哼恨很痕黑和何合喝呵号好毫行喊含害海孩还哈过果国鬼诡光灌馆官观关怪挂顾故固谷够购沟共功公工更耕艮跟根给各个隔格割哥告搞高刚干感敢赶概盖改该富咐附负父府福符服缝丰愤粉纷吩分啡非飞放房方饭犯返反烦翻番帆法发二尔而儿嗯恩恶躲多顿钝对队断段端杜赌独毒斗都胴动东定顶碟掉吊店电点典蒂第弟地底等灯的德得道盗到倒岛刀当蛋弹但胆单袋待带代大打答达搭错从聪刺次此磁疵蠢纯垂吹创船传穿川触处楚除初出抽充冲齿持迟池痴吃程乘呈成称趁沉车吵钞唱场常尝产缠差刹察查曾策测侧厕藏舱仓惨餐参菜踩彩财才猜擦部步布不博播玻波并冰别表标便变边避壁必币比绷本奔被背备狈北杯抱报保宝包绑帮扮伴半办板阪搬班拜败百白吧罢把巴八暗案安艾矮挨哀啊阿]
#testList2 = [做座坐作左醉最组阻走总踪渍自子桌准撞状装桩妆转专抓著注住助主逐竹蛛朱周重众种终中置致治制志至指纸止直织知只之证正整睁争震真侦针着这者遮照找招掌长张湛站战占粘沾乍渣怎泽择责则造早糟暂在再仔运晕越月约院怨圆原员冤遇谕预育雨与渔鱼余于右又有友游油由幽用泳哟硬应影萤英印隐饮引音因意易亦议艺义以已疑咦依医衣伊一腋夜也耶要药邀样阳焰验厌演眼颜研言烟呀亚牙鸭询寻醺血学选续绪序许需虚须秀凶性幸兴醒型形星信新心谢写鞋些效笑校小消肖像项向想响详箱相陷宪线现显嫌贤闲鲜先下隙细系戏喜洗袭席息析吸西物舞午五吾无屋握我问吻纹文喂谓位未卫委尾唯围为望忘往枉网亡万碗玩完弯外挖脱托吞推团土涂突投头偷痛筒同通停听厅铁贴调条田添天替体题提藤特套讨逃躺汤探谈摊态太台她他索所缩孙碎岁随虽算蒜诉送松四死斯思私丝司说睡水谁双摔刷束术署殊叔售受寿首守手收嗜释室适是试饰事似市世示士始使蚀食实识时石十湿施师失尸剩绳声生慎什深身伸射设少烧上伤闪山傻沙杀色三赛塞萨软入儒如肉溶容日扔认忍人热让染然群确却券犬蜷全趣去取求请情清轻青琴亲窃怯且茄切巧枪前器汽起启奇其漆期戚瀑普浦蒲破迫婆屏凭评平品片皮批碰篷蓬朋砰喷配陪跑旁判盘派牌排拍怕帕爬偶哦女懦弩弄牛年逆你泥能内呢闹难南男奈乃那哪拿暮幕目木母某谋抹魔摩模摸命明名面眠米谜迷懵们妹美每梅枚没么帽冒毛忙慢满蛮卖买嘛吗码玛马麻略率旅落论伦乱露路禄录鲁喽漏流留令另领绫凌灵琳淋邻瞭料聊疗量谅亮两良脸莲连笠利丽立力理里礼璃离狸类了勒乐老浪狼郎烂蓝兰来辣啦扩况快块裤袴库苦口控空肯客刻克可科柯靠烤考看凯开卡咖俊君绝决卷据剧具句巨举局居就救酒久究镜竟净警精经京劲近进尽紧金今巾借界解姐结街接窖较觉叫脚角焦交酱奖讲将江箭鉴溅渐剑荐件见简检捡间嫁架假甲家加祭继既迹剂际技记计己几急即级吉及基鸡矶机击祸或伙火活混婚昏惠绘会回灰晃慌换环欢怀话画化华划花护户胡狐忽呼乎候后吼哄鸿红横哼恨很痕黑和何合喝呵号好毫行喊含害海孩还哈过果国鬼诡光灌馆官观关怪挂顾故固谷够购沟共功公工更耕艮跟根给各个隔格割哥告搞高刚干感敢赶概盖改该富咐附负父府福符服缝丰愤粉纷吩分啡非飞放房方饭犯返反烦翻番帆法发二尔而儿嗯恩恶躲多顿钝对队断段端杜赌独毒斗都胴动东定顶碟掉吊店电点典蒂第弟地底等灯的德得道盗到倒岛刀当蛋弹但胆单袋待带代大打答达搭错从聪刺次此磁疵蠢纯垂吹创船传穿川触处楚除初出抽充冲齿持迟池痴吃程乘呈成称趁沉车吵钞唱场常尝产缠差刹察查曾策测侧厕藏舱仓惨餐参菜踩彩财才猜擦部步布不博播玻波并冰别表标便变边避壁必币比绷本奔被背备狈北杯抱报保宝包绑帮扮伴半办板阪搬班拜败百白吧罢把巴八暗案安艾矮挨哀啊阿]

testList2 = ["吴","z"]


f = open(fileName, 'r')
testList =  f.read()
f.close

#a = testList.index("\"")

#print a

#for x in testList:
    #print testList[x]
#    print x



x = set(testList)
y = set(testList2)

print x - y

'''
>>> a = open('/Users/playcrab/Desktop/test/data.txt')
>>> b = open('/Users/playcrab/Desktop/test/id.json')
>>> testList = a.read()
>>> a.close
<built-in method close of file object at 0x10920c810>
>>> b.write(testList)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for writing
>>> b = open('/Users/playcrab/Desktop/test/id.json', 'w')
>>> b.write(testList)
>>> b.close
<built-in method close of file object at 0x10920c930>
>>> 

'''