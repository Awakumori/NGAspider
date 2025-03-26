# NGAspider

艾泽拉斯国家地理爬虫 (NGA Spider)。用于爬取NGA论坛帖子标题和楼主成分。

## 项目介绍

新版本使用百度解语提取实体关键词，更换了NLP情感分析模型 (Natural Language Processing sentiment analysis model)，增加了分析项目。

> 新版本的分析报告尚未更新。
> 可以直接去nga的https://nga.178.com/read.php?tid=39620249 查看
> 新版本的源码尚未更新。

## 数据分析结果

### 分区发帖分布

#### 各个分区发帖数的比例饼状图
![image](https://user-images.githubusercontent.com/32727299/172158561-2e5cd962-681a-4785-a8d6-d7612b226706.png)

可以看出，水区占据了最大的份额，达到了55%。随后是大时代、晴风村。

#### 热度加权的分区比例饼状图
![image](https://user-images.githubusercontent.com/32727299/172158591-cc58626f-e644-4b29-82b6-3c4a705d8f79.png)

经过热度加权后，可以发现水区的份额进一步提高了。同时各分区的排名也有所变动。

#### 分区平均热度直方图
![image](https://user-images.githubusercontent.com/32727299/172158619-dfc51033-e186-495b-8fbc-d4dbf4056ea0.png)

可以看到平均热度最高的不出所料是晴风村。平均热度达到了惊人的52，远远超过排在最后的电子区和大时代。这说明大伙对于情感故事和舔狗故事还是最感兴趣的。

#### 各个分区发帖数的比例直方图
![image](https://user-images.githubusercontent.com/32727299/172158632-ea5c1b08-8291-45d4-984e-03f126c20821.png)

和上面的饼图是一个数据，但是换成直方图，更清晰地表明排名关系。

#### 热度加权的分区比例直方图
![image](https://user-images.githubusercontent.com/32727299/172158653-289dd1f5-4ca8-4196-a3bf-7e0c1b95111d.png)

同上。

### 热度分布分析

#### 总热度分布散点图
![image](https://user-images.githubusercontent.com/32727299/172158667-75e99998-3c9e-4314-bc4a-fa85c8e278d7.png)

横坐标是热度(控制在300以内)，纵坐标是符合该热度的主题帖数量。可以看出符合一个反比例的关系，这也符合我们的认知。存在大量无热度、低热度的帖子，同时有少量高热度帖子。可以看出回复过100的帖子就相对来说很少了。

#### 更小比例尺的总热度分布散点图
![image](https://user-images.githubusercontent.com/32727299/172158680-a3a7bcf4-b3dd-4430-87cc-c6c7cf5a537c.png)

在更小的比例尺(横坐标控制在50以内)下的总热度分布散点图。

#### 热度分布与分区
![image](https://user-images.githubusercontent.com/32727299/172158698-17eb6698-7c9a-4ff7-8329-8156e093df24.png)

#### 更小比例尺的热度分布与分区
![image](https://user-images.githubusercontent.com/32727299/172158702-4527593f-5cfb-4f17-b777-c540f7140973.png)

这两幅图没什么好说的。可以看出，水区的曲线下降的速率最大。换言之，水区的低热度帖子占比很高，是"最水的"，实至名归。

### 时间分布分析

#### 分时发帖数量(精确至分钟)
![image](https://user-images.githubusercontent.com/32727299/172158717-8b513581-2612-4c8e-a00c-20e5eaaa72e6.png)

横坐标是时间，24小时制，精确至分钟。可以看到还是很有规律的。我们看下面的小时图，更清楚一些。

#### 分时发帖数量(精确至小时)
![image](https://user-images.githubusercontent.com/32727299/172158730-e3323525-d98e-4277-b7b9-f052e305866e.png)

把横坐标缩放至小时单位。非常有规律的曲线，也符合我们的认知。
从零点到五点，发帖数快速下降。四点、五点钟的时候基本上熬夜的也都去睡了，发帖数达到低谷。随着六点钟开始陆续起床工作、上学，发帖数上升，一直到十点钟达到最高峰。
在十二点出现小下降，可能是在吃午饭。14点又回升，睡午觉的人都醒了。
随后从下午时段一路缓慢下降到晚上。

#### 分区分时发帖数量折线图(精确至小时)
![image](https://user-images.githubusercontent.com/32727299/172158742-d146e8b8-ba38-4fea-8f31-437a585e579a.png)

可以看出各分区的区别。还是比较符合规律的。大时代在十二点有一个极其明显的下降，这是不是说明大时代都是社畜，全去午休了呢。

#### 分区分时发帖数量气泡图(精确至小时)
![image](https://user-images.githubusercontent.com/32727299/172158749-ffe19874-6527-4e51-a590-1d25762e8571.png)

这个没啥好说的，主要是换种方式展示一下，可能更直观一些。

#### 分时发帖数量折线图(精确至曜日)
![image](https://user-images.githubusercontent.com/32727299/172158761-aa8c8305-5edc-44db-8079-bee040d491a2.png)

横坐标精确至曜日。通常我们认为周末论坛可能是最活跃的，但是数据却与常规的印象大相径庭。周四的发帖数最高，而周末的最低。

#### 分区分时发帖数量折线图(精确至曜日)
![image](https://user-images.githubusercontent.com/32727299/172158773-6767aa95-b624-4f82-a5df-93ffee53c0d2.png)

分区展示。没啥好说的。

#### 分时平均热度折线图(精确至小时)
![image](https://user-images.githubusercontent.com/32727299/172158788-27e118e4-b77d-4947-a082-391fefff42c2.png)

符合规律的一张图。可以看到，在论坛比较活跃的时间段(例如中午13-14时或晚上20时)，由于大量的主题帖，将平均热度稀释了。
而一个发表于早上8时的帖子，会经过一个上午的完整"曝光"，因此平均热度比较高。
因此想要建一个高楼，尽量选择早上8时发帖更好哦。

#### 分时平均热度折线图(精确至曜日)
![image](https://user-images.githubusercontent.com/32727299/172158799-cf25efe8-21de-4b07-ae01-59f6602bf48f.png)

周五平均热度最低而周一平均热度最高。

### 用户设备分析

#### 使用设备用户总分布饼状图
![image](https://user-images.githubusercontent.com/32727299/172158807-72da0262-6fbe-462e-8f2f-47a0397748b2.png)

安卓设备占压倒性的优势，达到了64%的占比。

#### 查询分区含果量(分区苹果用户占比)
![image](https://user-images.githubusercontent.com/32727299/172158818-40d3a866-8ea7-4a32-8991-53b485da0374.png)

可以发现，晴风村的苹果用户最多，达到了44%。
而令人惊讶的是，漩涡书院的苹果用户占比非常低，仅为20%，两者几乎差了一倍。
这个现象非常有趣。考虑到苹果用户占比最少的两个分区分别是小说和游戏相关，我们是否能够得到这样一个结论，即小说、游戏分区的年轻人比较多，而年轻人更喜欢用安卓。

### 用户发帖活跃度分析

#### 对称分区高发帖量用户排行榜(每分区前5名)
![image](https://user-images.githubusercontent.com/32727299/172158829-fcb25e3e-2485-42df-81a6-a19303d0ce32.png)

看一看各个分区谁最能水。

#### 水区高发帖量用户排行榜(前50名)
![image](https://user-images.githubusercontent.com/32727299/172158842-d3c91eb9-76c3-4e61-886e-beab94bc880c.png)

看一看水区谁最能水。

#### 历史发言数分区分布
![image](https://user-images.githubusercontent.com/32727299/172158848-7238b874-42e5-4333-9cc9-da247c0b16e8.png)

可以看到在0.2k-0.4k段有一个局部极值，随后符合一个反比例的曲线下降。

### 用户威望与组别分析

#### 总威望分布
![image](https://user-images.githubusercontent.com/32727299/172158859-c53c14f3-4f2c-4c80-9022-a527e37ce254.png)

把全部用户的威望染色。

#### 分区威望分布
![image](https://user-images.githubusercontent.com/32727299/172158870-2812d04a-7e44-49f6-acc6-9efb965843d8.png)

比较符合正态分布，0威望的最多。
值得一提的是，"稍微扣了一点"比"稍微加了一点"的要明显更多。
换言之，轻度论坛用户，比起略微做一些贡献，还是更喜欢略微违反一些论坛条例。

#### 总用户组分布
![image](https://user-images.githubusercontent.com/32727299/172158881-7383fb58-8d4b-4f9a-84b0-fe113d1736d5.png)

做一下用户组上的人口普查。老百姓还是占绝大多数的。
全部学徒与警告等级用户之和占比达到98.968%。

之后是同一张图，把占比最高的两个用户组(学徒39和警告等级1)去掉。
![image](https://user-images.githubusercontent.com/32727299/172158886-05834871-a23c-43db-99e6-31f15c303202.png)

接着将老百姓全部去掉，仅保留人上人。(去掉全部的学徒和警告等级)
![image](https://user-images.githubusercontent.com/32727299/172158893-587d86c8-c17c-4788-a170-95ef23016e74.png)

可以看到人上人阶级中，助手占一半。随后是工匠、专家、大师等等。

#### 总用户组分布(直方图)
![image](https://user-images.githubusercontent.com/32727299/172158905-82e8d147-1a98-4126-bbef-e3610e7d5140.png)

用户组人口普查的直方图形式。
注意纵坐标不是均匀缩放的。

### 用户注册时间分析

#### 注册时间分布条带图
![image](https://user-images.githubusercontent.com/32727299/172158911-98518eb3-a7ca-4e26-8730-7db493a5e075.png)

注册时间的染色图。粒度精确到月份。
注意到在2005-2010之间，准确的说是2007-2008的位置，出现了明显的空缺。那时候发生了什么笔者不得而知，或许论坛当时关闭了注册。

#### 注册时间分布折线图
![image](https://user-images.githubusercontent.com/32727299/172158921-0bb3ce7b-21c4-427c-8054-28e694bce39e.png)

用户注册时间的折线。
注意，由于粒度精确到年，因此这张图中看不到上一张图展示出的空缺。
可以发现，用户注册数量在2009年达到局部最高，然后出现了一个长达4年的下降。
接着从2013年开始攀升，到2015年开始以一个非常高的速率上升。
直至2019年，函数的导数突然变成零，并维持至今。

#### 注册时间分区分布折线图
![image](https://user-images.githubusercontent.com/32727299/172158930-5c91127d-123a-4ad2-906b-2835784fbcf8.png)

分区分时注册折线图，可以看到在2015年后的大扩张中，最多的用户涌入了水区。水区对应曲线(最上面的那一条)在2015-2018的上升幅度非常惊人

### 内容关键词分析

#### 关键词计数分布直方图
![image](https://user-images.githubusercontent.com/32727299/172158942-e6dff1bb-bf42-4c49-bae4-51ca20b38fc2.png)

对全区关键词进行直接计数。
排在前十位的是小说、美国、上海、疫情、游戏、手机、日本、视频、乌克兰、俄罗斯。

#### 非对称分区关键词计数分布
![image](https://user-images.githubusercontent.com/32727299/172158949-1155688a-142c-4bc2-8cc7-5e2def0df56e.png)

非对称分区计数。非对称意味着更火热的分区占有的关键词更多。

#### 对称分区关键词计数分布(每分区前5)
![image](https://user-images.githubusercontent.com/32727299/172158957-bceca8a4-84f7-4209-a46a-e07b47c65d38.png)

对称分区计数。对称意味着每个分区单独计算出现次数最多的关键词。
注意纵坐标非均匀缩放。

### 帖子内容分析

#### 标题长度分区分布
![image](https://user-images.githubusercontent.com/32727299/172158961-f585f208-18bb-4d87-8135-ba0a8455d0bd.png)

一张完美符合正态分布的图。
帖子的标题长度大多落在12-17个字之间。

#### 主楼长度分布
![image](https://user-images.githubusercontent.com/32727299/172158969-038ca01d-c253-4fa6-bd52-632e623da385.png)

能看出正文字符数为零的帖子居然是最多的。(一般是配了一张图)

### 情感分析

#### 情感倾向比例饼状图
![image](https://user-images.githubusercontent.com/32727299/172158977-0543911a-21b5-48a6-b52a-c644af368b15.png)

用深度学习 (deep learning) 对文本语义进行情感分析 (sentiment analysis)。
负面情感占比77.1%，正面感情占比22.9%。

#### 情感倾向分区分布
![image](https://user-images.githubusercontent.com/32727299/172158984-be0972f7-a560-4734-92f2-6af7186e6a9c.png)

注意纵坐标非均匀缩放。
所有的分区都是负面情感大于正面情感。

#### 情感倾向分区分布(负面感情倾向占比)
![image](https://user-images.githubusercontent.com/32727299/172158994-bd7e816b-1281-4132-ab9a-131e05cd2b31.png)

虽然所有的分区都是负面情感大于正面情感，但是它们的负面情感占比不同。
可以看出相对最快乐的分区和游戏、影音、小说有关，都是娱乐分区。
而最痛苦的分区是职场人生。其次是大时代。可以说是非常真实了。

#### 情感倾向和平均热度分区分布
![image](https://user-images.githubusercontent.com/32727299/172159005-192000ba-5a42-4ddd-b0aa-3ead3e8d1587.png)

来看一下情感倾向对于帖子平均热度的影响。
可以看到，大部分分区，负面情感的帖子更火热。
值得一提的是，网络游戏综合区一骑绝尘，正面情感的帖子比负面情感帖子热度更高。

#### 关键词负面情感倾向占比排行
![image](https://user-images.githubusercontent.com/32727299/172159013-621a7c44-088b-49e5-a318-8700e576ebd1.png)

可以看到，A股、利润、彩礼、利空、港股等关键词，负面情感率甚至达到了百分之百。
此外，蚊子、阳性、事故、裁员、散户、存款、资本家、贷款、团团、皮套等词语也是负面情感的重灾区。

#### 关键词正面情感倾向占比排行
![image](https://user-images.githubusercontent.com/32727299/172159034-06c70194-db92-4d52-9248-9b72a2faf537.png)

比较快乐的词。黑胶、网易、壁纸、音乐、礼物、四川、母亲节、东哥、奥特曼、周杰伦等等。

---
