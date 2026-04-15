# 弹性布局 (Flex)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout

## 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/VDvLb4-1QDOHdSiBN6lObw/zh-cn_image_0000002540611358.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=0C1DAD944EE5692B9C9AE3E418A431B8E7254558BF5302F372C436CF9A9ECE59)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/AUCjM6i9TEOS521hpkYI8g/zh-cn_image_0000002571171353.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=F8D335EB24AB32638AE0A74D1262BF001E2A54C36142141909BE7E69969AF6EF)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/E34jIvXMQ6akH6Qhq2FJaQ/zh-cn_image_0000002540771010.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=EC61411F9811F390DC4FB96EC83BB64F8DD6CCD59627DD50F7D0BCD55B3A8B17)
- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.RowReverse }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/a6hkNAKOQOO2AQpDpZcTmA/zh-cn_image_0000002571291307.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=ECA4896D87427F640B0915E21460F0B4789488A9A2F919522E54D8489E311060)
- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。 ```typescript Flex({ direction: FlexDirection.Column }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ncMxTHY4Tt63SSgE8-UY-g/zh-cn_image_0000002540611360.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=2EBB93C5273B4D91A61EACFF742752C1D0EA4ACC6C1E71EA386E7CD360B3AD16)
- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.ColumnReverse }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/MsiPXF0jQ8a8k_-4dd6g0g/zh-cn_image_0000002571171355.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=D8C9D9750F4BD5F4BA873026492B2F13DCE881477A2CCDF975DA8C96B43E3F02)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

- FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。 ```typescript Flex({ wrap: FlexWrap.NoWrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/KTmSiCCySF2ri3ojxin98g/zh-cn_image_0000002540771012.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=10E1F371AF09C2102D712C50D53151E4675A1A16001C3A267A737D5E1EBC9D81)
- FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。 ```typescript Flex({ wrap: FlexWrap.Wrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#D2B48C') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/xbIRwG9nRiC6O19LTY7ryw/zh-cn_image_0000002571291309.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=AB4F47A0F34DD994771E47BCDDB991E4DE611E91BF3CFBDC294E714231AC597A)
- FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。 ```typescript Flex({ wrap: FlexWrap.WrapReverse}) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/DHGCosJiQbmoJiYsJVVQ6A/zh-cn_image_0000002540611362.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=E34DC34859CD8FDC8F9438F982FF6AC204CA656D7156EB5CBD194D614FE189BA)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ODQUUULeQbOFfR0oT9wwuw/zh-cn_image_0000002571171357.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=C1341C22C1AAEF09F538CF300EE9B0A11A582F1E337CE2DACE788ACE2FFB6ACD)

- FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.Start }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/yPJgpU9BTem3SdYFiftHpA/zh-cn_image_0000002540771014.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=7BD629B7F2CC97EE0B7E4653C68AA33EE51A203D2541F9EA7A76CED4500F2172)
- FlexAlign.Center：子元素在主轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.Center }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/jU2Q_0XcQvO_gFfHdFB8Nw/zh-cn_image_0000002571291311.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=6378CB484DEBBB6556D6BA2C3DC647B76DF94A500A92845291F4F51DEEF20892)
- FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.End }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/5PqOBOpeRYWrUkQpjcPFcA/zh-cn_image_0000002540611364.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=6A23AB7ED9D3CA1651B1B4E97F8DB4BC94E1622ADD7F42B63F948FB536085E55)
- FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xtqx6cHwRpeNGqlqRg0Dyg/zh-cn_image_0000002571171359.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=6761C40BE50A837F256470DEE44ED05550BDCEDAA725AA77B6D6574737FF9479)
- FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。 ```typescript Flex({ justifyContent: FlexAlign.SpaceAround }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/clei4MXCSXaoAu0S2tjUjQ/zh-cn_image_0000002540771016.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=D24075F1B4E5DC7F18A3D59A5F960AC7CCFD58261D95E34C4A157D190C1CD325)
- FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Ec39TgPpRw2AmYOMOHi2IA/zh-cn_image_0000002571291313.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=60B9C8D67816CFA4C1F3A0BCF5DEE7479037FCF4A0B4B4E7B73930D9973386A4)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

- ItemAlign.Auto：使用Flex容器中默认配置。 ```typescript Flex({ alignItems: ItemAlign.Auto }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ZdR0MlWnT3mbpJxoZDXBmQ/zh-cn_image_0000002540611366.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=876085A312DBE2AE044D0F8C7BA085F95A63279AB9F1B9E7732FFEF66397EDF6)
- ItemAlign.Start：交叉轴方向首部对齐。 ```typescript Flex({ alignItems: ItemAlign.Start }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/oIvCgqC_SwKT38_XfD2urg/zh-cn_image_0000002571171361.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=5B18AF610E72375D85FCD943F4E1E437AFEF2561594BD203E79936BC24819AFD)
- ItemAlign.Center：交叉轴方向居中对齐。 ```typescript Flex({ alignItems: ItemAlign.Center }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/QlN0XA2IQrirY_z6DZ_GjA/zh-cn_image_0000002540771018.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=D5D46A7EA40C2C3EC306102ECA629F586B50D87AA1DCCBFCFC6588290FC01FD2)
- ItemAlign.End：交叉轴方向底部对齐。 ```typescript Flex({ alignItems: ItemAlign.End }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/UF1f6ohBQK2_s_0kZgMSug/zh-cn_image_0000002571291315.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=1496C812179DCFE280A742A42E4C88223B10DDBBF143C3F01F0A7E69FA4D8538)
- ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。 ```typescript Flex({ alignItems: ItemAlign.Stretch }) {  Text('1').width('33%').backgroundColor('#F5DEB3')  Text('2').width('33%').backgroundColor('#D2B48C')  Text('3').width('33%').backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/EQJP0HKrSkqnnc_893zXnQ/zh-cn_image_0000002540611368.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=5FDD206A35B75119814FC4F3850C022F825732E73A54F12CD58FC5BF9D890CEE)
- ItemAlign.Baseline：交叉轴方向文本基线对齐。 ```typescript Flex({ alignItems: ItemAlign.Baseline }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/slyquiN1RV2PXXEWz9pEJA/zh-cn_image_0000002571171363.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=D019FD156650EA1988D8BE9A56AB0CB7236E2A562FC95FD881BA1B4E123D8F2E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ryukoXBiQf2L9WQoevdjLw/zh-cn_image_0000002540771020.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=AC2335F6F4B730521FFE2B5A8454F9F98D0804EC25DBB0352C4A784339D531C4)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

- FlexAlign.Start：子元素各行与交叉轴起点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3aaqNw81QuqRGwI2zncIkg/zh-cn_image_0000002571291317.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=0E586BEB56E9DA02A1449A3DBE5D905EC33AD92C2448FCC7E36228739626178C)
- FlexAlign.Center：子元素各行在交叉轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/wqx-SqjJRuqGjZ-TCSz6lA/zh-cn_image_0000002540611370.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=54500FF2C9B5F8AC6AF58E20EFA525AB76773C969FC68542D5F430A51E1EC526)
- FlexAlign.End：子元素各行与交叉轴终点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/PkESLzgLQmygsioqdRzcFA/zh-cn_image_0000002571171365.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=71AB25493545604C1AD8C367324DD3C7723B62A1BB421D1408BA38789361DCFC)
- FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Qnqg9xoDS7WaP4ZQj4Nz6A/zh-cn_image_0000002540771022.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=99960B3E5DF51A71DAC328BDE69E8218EBD8A863A47B2676E6D3BA62FB37C46D)
- FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/oiVfGQdISJWzepLrslDrvg/zh-cn_image_0000002571291319.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=BC9EF34F000727512199916B33F82D47CC5522C31F4513CB5A92411F32F8D4A0)
- FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/j__-DkTjT1OsxxgbqdzXPw/zh-cn_image_0000002540611372.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=06617F25A7252EF03FB812B07DD00CA70EF1950A8D34EA318F9A304FAC5A79AA)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

- [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。 ```typescript Flex() {  Text('flexBasis("auto")')  .flexBasis('auto')  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis("auto")'+' width("40%")')  .width('40%')  .flexBasis('auto')  .height(100)  .backgroundColor('#D2B48C')  Text('flexBasis(100)')  .flexBasis(100)  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis(100)')  .flexBasis(100)  .width(200)  .height(100)  .backgroundColor('#D2B48C') }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/kvDo1IjPTrC1VeOwKtVs4g/zh-cn_image_0000002571171367.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=91CA823CB671FCDCF0462EB436B7D64275A53671CA5099D704291F76345CBDEB)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/KTNdbLyrR428QlZoZKi5Ww/zh-cn_image_0000002540771024.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=249E8A63C14978A40595FEF4437A28B125244344BCAC87ACF5FF7B926F524D58)

父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp * 1/5=108vp，第二个元素为100vp+40vp * 4/5=132vp。

- [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('flexShrink(3)')  .flexShrink(3)  .width(200)  .height(100)  .backgroundColor('#F5DEB3')  Text('no flexShrink')  .width(200)  .height(100)  .backgroundColor('#D2B48C')  Text('flexShrink(2)')  .flexShrink(2)  .width(200)  .height(100)  .backgroundColor('#F5DEB3') }.width(400).height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/-lVi_YcGTz2dupCJd1pD_Q/zh-cn_image_0000002571291321.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=ACA4A902853C01C60CE5D68C5824E07D9E7390B083374ADB4213E9DC20DDE12B) 父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。 将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) * 3=68vp，第三个元素为200vp - (220vp / 5) * 2=112vp。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/003UsEuORouhZ_Y6ijQifw/zh-cn_image_0000002540611374.png?HW-CC-KV=V1&HW-CC-Date=20260415T024807Z&HW-CC-Expire=86400&HW-CC-Sign=19F5C10A81B90D50535F3EE2D1A7F13DD3F9A6E9483F67DFEB47367EBB4253DE)
