# 弹性布局 (Flex)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout

## 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/WB0pWLeXTAGqi2GxxCMmrw/zh-cn_image_0000002569128361.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=97A95B79B29EC2DAAC49A811015FD7F488AEF15A161E5BAA6577326211BE5277)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/3cI-iSikRdylpvyW155PXQ/zh-cn_image_0000002538128640.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=A1B707EFA2EFA083335CE25486FBD2ED3FF150E4B384706A3A4B4A6107C20BD8)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/uSzwU_I9R1SsTpXpN1nQsQ/zh-cn_image_0000002538288574.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=E419DA0C534E1A77129E05CD60A957E077902747E5CF4219B4AFAF94E5504249)
- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.RowReverse }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/F74qWKM3SniMQBvBASVhfA/zh-cn_image_0000002569168337.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=81968D81E98B821E2083A6015F08A9B9DA896FC0F6FCC4C26DB5460C235A105D)
- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。 ```typescript Flex({ direction: FlexDirection.Column }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/w6Msz4WMQJWlPtjz9HrzhQ/zh-cn_image_0000002569128363.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=060345397CA7734BD3F3673679F8E50213FB7FDF8B447F0C1D40CD8D5744D8AE)
- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.ColumnReverse }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/coesRJyoTBiPt2lKqFFbWA/zh-cn_image_0000002538128642.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=475B49217A08A0D562B17DCC16144A6B3EE2DCA3CACE85A77E4856E7BCC72D72)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

- FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。 ```typescript Flex({ wrap: FlexWrap.NoWrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Hcz2BmEzS1Kp1jajXMxVzQ/zh-cn_image_0000002538288576.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=60003EAC87B34F554811D457DCC78BED0D1C9E82247AF17E57498502AF0B3B04)
- FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。 ```typescript Flex({ wrap: FlexWrap.Wrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#D2B48C') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/cOVDu9b5R1y7l61JQfH-Wg/zh-cn_image_0000002569168339.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=C7464C726211F9AA5BBF3AF23A4D93EAC352F2EF34955DE3456CA7015BD366D3)
- FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。 ```typescript Flex({ wrap: FlexWrap.WrapReverse}) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/iSSnAG1bRWOzeNjpCgiSpQ/zh-cn_image_0000002569128365.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=570842727356F19B80C8223DEE7CA320A580DA28D991A9A9A88D0EB62AA60256)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/fF9N0iRzQemUilQfAIyFaw/zh-cn_image_0000002538128644.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=14755470EA76DDE7B5293603CE1DC3E4A9A498BF1A349F2E27A060D4F76623D0)

- FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.Start }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Cp5sENT_SXeKAljGpbm-qA/zh-cn_image_0000002538288578.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=993C6BFA0EDCB28AC62E8473A13438235822886AFA016106BCBEEDA9A5A48DF3)
- FlexAlign.Center：子元素在主轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.Center }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/9xE_infuSN-bKcW4IXoirg/zh-cn_image_0000002569168341.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=FDF755A4CE20CD5E8E59713D67E62558C74CA7650F647C544C4686E63812CF6D)
- FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.End }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/yuwomQkhSoiojUjeFLDnow/zh-cn_image_0000002569128367.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=32F23805679C31C3656D25DC4F7B61D02EF427661EAC8DC0FCE5BE46EE835E2B)
- FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/g2yY1dKLQU-D7poATQiYgg/zh-cn_image_0000002538128646.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=6033F2838F6473941E1B6D48D0A5DB45CDB392CA04EB0B5C26F9252B763D241A)
- FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。 ```typescript Flex({ justifyContent: FlexAlign.SpaceAround }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/bUB7BEYHTSimJu4b257GrQ/zh-cn_image_0000002538288580.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=0E4CBA38F595C105F987847EF39667C98EB1D36F88302701AE7FC1ACF3DEE640)
- FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/upBHqzjRTY2alJPi1e3D5g/zh-cn_image_0000002569168343.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=4BC6BB23D1FF445881AD43ABAF1C6E0AB364F5A64750CBF4CC048068A4E33227)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

- ItemAlign.Auto：使用Flex容器中默认配置。 ```typescript Flex({ alignItems: ItemAlign.Auto }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/n6xmk0OIQUaiTzimhXaDww/zh-cn_image_0000002569128369.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=97C6152A7F07ED8F160E6BAA7119A9293ED91AB5C8AD907BDE9B4EB41BAE4F46)
- ItemAlign.Start：交叉轴方向首部对齐。 ```typescript Flex({ alignItems: ItemAlign.Start }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/jMoVBKoXSYS_l1Hz_9KDlw/zh-cn_image_0000002538128648.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=58A668341F52852D0F0F844173411941BE4B0EBD7C3F6104021411C1463DF730)
- ItemAlign.Center：交叉轴方向居中对齐。 ```typescript Flex({ alignItems: ItemAlign.Center }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/F5rzUSzhRiiwNL2MT4uVSg/zh-cn_image_0000002538288582.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=13FBADDF04EFD0D408D42090592081D96620861B2551ED20EB1CA18510C266F3)
- ItemAlign.End：交叉轴方向底部对齐。 ```typescript Flex({ alignItems: ItemAlign.End }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/4zlx6lkTSxuCJ8tyYgU0zg/zh-cn_image_0000002569168345.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=BC3EA738BEC17E0B9D4B170E58AC809B5A8C7678799ADEDBA7D508CF6EA5D54F)
- ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。 ```typescript Flex({ alignItems: ItemAlign.Stretch }) {  Text('1').width('33%').backgroundColor('#F5DEB3')  Text('2').width('33%').backgroundColor('#D2B48C')  Text('3').width('33%').backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/lG4vL8n3RSu65ndkVlKB4Q/zh-cn_image_0000002569128371.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=988E6E4B190303781A20108E9FB1B8467A31208BC1CDD808DBA3C51F1DDFA507)
- ItemAlign.Baseline：交叉轴方向文本基线对齐。 ```typescript Flex({ alignItems: ItemAlign.Baseline }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/CyoyDb2FSQKbFf2cCMzK9w/zh-cn_image_0000002538128650.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=CF68D558CEDBC4E68C334393E2E3CFED8F0C7CF97013DE914D80B6C98F53C6B1)

### 子元素设置交叉轴对齐

子元素的[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```typescript
Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
  Text('alignSelf Start').width('25%').height(80)
    .alignSelf(ItemAlign.Start)
    .backgroundColor('#F5DEB3')
  Text('alignSelf Baseline')
    .alignSelf(ItemAlign.Baseline)
    .width('25%')
    .height(80)
    .backgroundColor('#D2B48C')
  Text('alignSelf Baseline').width('25%').height(100)
    .backgroundColor('#F5DEB3')
    .alignSelf(ItemAlign.Baseline)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#D2B48C')
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#F5DEB3')

}.width('90%').height(220).backgroundColor('#AFEEEE')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/UD4IkOGBSwmBt1YJMhvICA/zh-cn_image_0000002538288584.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=3DFFD2830239D281E545A6277D8074DF10C43AFA246F667B57E00BD98C38794C)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

- FlexAlign.Start：子元素各行与交叉轴起点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/dVcVaoyPTZiJ_OTN3Kv1qQ/zh-cn_image_0000002569168347.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=8873673FCFD9CF073CFCE0A96BF53B1A93B6453F4B24B537EE77C9292197A5B8)
- FlexAlign.Center：子元素各行在交叉轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/kbjMrxcvRZ-wup5LWBfc1w/zh-cn_image_0000002569128373.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=510939DA82FC8453C1C548F6E8867EDE73E852116EFFAAF62D1BEF46953C3C5F)
- FlexAlign.End：子元素各行与交叉轴终点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sgebe7-2RaehSg1r5l1wOQ/zh-cn_image_0000002538128652.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=2EB6BC66055803D03E53C23658309B19CB2519753CC5FC91986AF7D813DEB9A0)
- FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/WK2VRuYkStSSmSL3wBUGZg/zh-cn_image_0000002538288586.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=7CB71ACD7488BF8C72BBDCEA65B007BC981BD1119103AF267398B67B30B7CB18)
- FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/yUR7uC-ySWOPocIG8eanbw/zh-cn_image_0000002569168349.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=187093E1BD17056C8E6D4FA23F97A84C5012878A00A1D1190DA3D1BBA167F927)
- FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/S3f3MNgGQnaQFHZ2qayTDg/zh-cn_image_0000002569128375.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=731CA51F7DA13F8251A5CBDBA685642F5A0AFE169DFBB63BBB218912203711A8)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

- [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。 ```typescript Flex() {  Text('flexBasis("auto")')  .flexBasis('auto')  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis("auto")'+' width("40%")')  .width('40%')  .flexBasis('auto')  .height(100)  .backgroundColor('#D2B48C')  Text('flexBasis(100)')  .flexBasis(100)  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis(100)')  .flexBasis(100)  .width(200)  .height(100)  .backgroundColor('#D2B48C') }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/WYp_BFegS2KHiGhVOdk9og/zh-cn_image_0000002538128654.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=DEBE00035D31749FC6B945F3C8687D94AF56B712D71FD53A807BBE607E0D21AF)
- [flexGrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。下述示例运行需要保证设备为横屏状态，否则运行效果可能存在差异。

```typescript
  Flex() {
    Text('flexGrow(1)')
      .flexGrow(1)
      .width(100)
      .height(100)
      .backgroundColor('#F5DEB3')
    Text('flexGrow(4)')
      .flexGrow(4)
      .width(100)
      .height(100)
      .backgroundColor('#D2B48C')

    Text('no flexGrow')
      .width(100)
      .height(100)
      .backgroundColor('#F5DEB3')
  }.width(360).height(120).padding(10).backgroundColor('#AFEEEE')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/yOQyBZfAT_-i1IZLwA9MaA/zh-cn_image_0000002538288588.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=8BAC91664747406AF36FCC3AABB40A0E3D9C31DA5075E1F0F694A906586F52E4)

父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp * 1/5=108vp，第二个元素为100vp+40vp * 4/5=132vp。

- [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('flexShrink(3)')  .flexShrink(3)  .width(200)  .height(100)  .backgroundColor('#F5DEB3')  Text('no flexShrink')  .width(200)  .height(100)  .backgroundColor('#D2B48C')  Text('flexShrink(2)')  .flexShrink(2)  .width(200)  .height(100)  .backgroundColor('#F5DEB3') }.width(400).height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/kPRDD3ZXRBK81oUx36pbuA/zh-cn_image_0000002569168351.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=931E3252DC9778A4C151A312AF0A6B63237027F76D94A72F16A5DC90334B69D4) 父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。 将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) * 3=68vp，第三个元素为200vp - (220vp / 5) * 2=112vp。

## 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

```typescript
@Entry
@Component
struct FlexExample {
  build() {
    Column() {
      Column({ space: 5 }) {
        Flex({
          direction: FlexDirection.Row,
          wrap: FlexWrap.NoWrap,
          justifyContent: FlexAlign.SpaceBetween,
          alignItems: ItemAlign.Center
        }) {
          Text('1').width('30%').height(50).backgroundColor('#F5DEB3')
          Text('2').width('30%').height(50).backgroundColor('#D2B48C')
          Text('3').width('30%').height(50).backgroundColor('#F5DEB3')
        }
        .height(70)
        .width('90%')
        .backgroundColor('#AFEEEE')
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/pxx-m2AJSca0VwrJcCKQ7w/zh-cn_image_0000002569128377.png?HW-CC-KV=V1&HW-CC-Date=20260411T023335Z&HW-CC-Expire=86400&HW-CC-Sign=CC1E98DBAFDF2CF5A5D8EDB092325D82569F26437B62627746D6011055385C69)
