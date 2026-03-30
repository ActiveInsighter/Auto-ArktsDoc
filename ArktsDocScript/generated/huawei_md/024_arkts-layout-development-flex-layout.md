# 弹性布局 (Flex)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout

## 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yVz3KobcQ8yBs1B8uvP35A/zh-cn_image_0000002563785737.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=51B23595014A7E3FDAFFA7268B0F271742C8232BA5252084BD35C2F55C953D38)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yaGb7_BUT2m3IU8Kj7qaVw/zh-cn_image_0000002532905842.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=4DF1220B45F8CDCCCF409DA9A4DBC3DEDE9FF936AF21B02032C8DF9D5FA6C0C3)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/M64C6Bu5R1GXwiUo8NXEBw/zh-cn_image_0000002533065790.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=FF2418A42EF85E67A6F12FCF5DB835B451C933E2AE6778787C10F60FB62E9BDB)
- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.RowReverse }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/0uBy3G_AQWSd7DW8A-MCRQ/zh-cn_image_0000002563865693.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=5DF2A56476277D26B77EDC24CBDB713516F9101F8B964ABFB71B729D614827AE)
- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。 ```typescript Flex({ direction: FlexDirection.Column }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/jPUIudTdS1-nM4inm5t4lw/zh-cn_image_0000002563785739.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=E64CDCC42C3E3CEB3D32AF247F7EE4AE07068D08E1110DF35473DBCE91D4C1E0)
- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.ColumnReverse }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/thCaeS79Rsy7D3QjQViRtg/zh-cn_image_0000002532905844.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=5E981770F351363FF187EC421EFAC3060892D6CF428E319ED187DBB6614E86BF)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

- FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。 ```typescript Flex({ wrap: FlexWrap.NoWrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/eOoxKeyMT3GsNAJaVVzP_Q/zh-cn_image_0000002533065792.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=B7DCD47BB168A9793054EC0073F0990FF18715A96368C96462B73BBBE24BED0B)
- FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。 ```typescript Flex({ wrap: FlexWrap.Wrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#D2B48C') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/KSw1FrfTRgCLBzPl8T3FPA/zh-cn_image_0000002563865695.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=D2D5A950626B122CCBE57BBDDF27FF99999915C4E87ADC1E373CDA515963AB29)
- FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。 ```typescript Flex({ wrap: FlexWrap.WrapReverse}) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/sxk1ZK5BQ62rcKUxyEQFww/zh-cn_image_0000002563785741.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=10888C33B124E42734D2B248258DFC21A345698A091B1B503FB61012415601E2)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/P6aWaOFvT_eCvevC6AKEIg/zh-cn_image_0000002532905846.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=0BEC1352822707385723C13F98A3E01117104FD8A4A0C185F6984D40943E0431)

- FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.Start }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/XTvflTR9QHqkL4eoPBQl8g/zh-cn_image_0000002533065794.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=8BDCBD6C3C00D44CAA09B77493472829B6209D4053933815C30F0A738CD315B7)
- FlexAlign.Center：子元素在主轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.Center }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/uZKxRiFRT1Kw-EHtwleYyQ/zh-cn_image_0000002563865697.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=580A875BA9A0C906E7E534DEE9B8FB1EFDD1817BE43287DF803BD4459F590284)
- FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.End }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/_nuh-m_8QCC2tqGoClRisA/zh-cn_image_0000002563785743.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=5D0CC56659F32DCC6B6CF75C5D2514E894D7BB2925C214116086C9BE44F96727)
- FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/xdgk0zgKTvyMNW8mUilWPQ/zh-cn_image_0000002532905848.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=B4A30950ED7E5A236A22AA2321C272848BB1F329B156A7AAC1330A54A19A5106)
- FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。 ```typescript Flex({ justifyContent: FlexAlign.SpaceAround }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/z4ZXak5eS5ecnuZCUyhvjA/zh-cn_image_0000002533065796.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=03B80C104155035433BF8F66FB999F5A1953BCF15A7371A9AD48541B1FA25A0F)
- FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/TV7-xqDFSV-IUy64DFQF4A/zh-cn_image_0000002563865699.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=86353557607F4A040E75702F068E4D1285CB1561BF1E439F678FD9F3F86927FF)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

- ItemAlign.Auto：使用Flex容器中默认配置。 ```typescript Flex({ alignItems: ItemAlign.Auto }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/K-MS6_UpQm6Pth1graUPWw/zh-cn_image_0000002563785745.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=F0D5DC2084FA6C99DD2F58E39DD33652A53937ECF411DB1FB03359C2B924631D)
- ItemAlign.Start：交叉轴方向首部对齐。 ```typescript Flex({ alignItems: ItemAlign.Start }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/4p4kUNZ4Tja_A9g8OrvnVQ/zh-cn_image_0000002532905850.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=67F13B19E594A78EB036DDC44C7AB048C273820B73C327EA8F36111402E9A2B9)
- ItemAlign.Center：交叉轴方向居中对齐。 ```typescript Flex({ alignItems: ItemAlign.Center }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/iWfwds_KQXGZ_TI7QVszRw/zh-cn_image_0000002533065798.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=D88B640E7D26070004A8B180B74C7C7B53764E78F324DCB732C8932C16ECAC3E)
- ItemAlign.End：交叉轴方向底部对齐。 ```typescript Flex({ alignItems: ItemAlign.End }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/1-jAwVSyRGS79Xt80yZaog/zh-cn_image_0000002563865701.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=3EF2720E134F3FB8BF1F41D8DDD93C9A0DE2DEE81BE45ED01D1185BBA8A96A98)
- ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。 ```typescript Flex({ alignItems: ItemAlign.Stretch }) {  Text('1').width('33%').backgroundColor('#F5DEB3')  Text('2').width('33%').backgroundColor('#D2B48C')  Text('3').width('33%').backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EQbFO6eHTaGsYx8VTkPdtg/zh-cn_image_0000002563785747.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=BF4FA7E809A8B23CE7CB393C0DC1129F2843AA565952CE3DDB278838CCF01419)
- ItemAlign.Baseline：交叉轴方向文本基线对齐。 ```typescript Flex({ alignItems: ItemAlign.Baseline }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/GkzNlRUPSB2Fcw7lLMydPQ/zh-cn_image_0000002532905852.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=3F9E1EE033A36163E666C73BA44FA64291604D2AD896D2A4570905E7F5BA7904)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/L68mmhgxQgGK9khBPMrN_g/zh-cn_image_0000002533065800.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=0EC01149D5A297FA92798AD7A820DCC61464D6D5417B9DA067DBC9ADDD2B5346)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

- FlexAlign.Start：子元素各行与交叉轴起点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Nv3Mmn7yRdWKsDAeOLY91A/zh-cn_image_0000002563865703.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=3BB5DB7D76E97FDC149A01CB03D13A1136A832CA58FCB9418B0D8B69E799ED20)
- FlexAlign.Center：子元素各行在交叉轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wVMoCOwaTbSaFXszl2Jibw/zh-cn_image_0000002563785749.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=F5E6032BD50F4DAE2FA33F3D1ECAAC8BDA4072BB378BCCC2321E3E15747AC094)
- FlexAlign.End：子元素各行与交叉轴终点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/srC_06YFRz6qO5O3KTDaEQ/zh-cn_image_0000002532905854.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=40F562ED6E6E4B7CE308EFA329750E205E0F3E529B7AED2F63AE568D87706C2E)
- FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/5SGK2jcgR4OULMk_Tfs4eg/zh-cn_image_0000002533065802.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=7F2C7355BFC40B4855C0F54FF3DF3DBB5AD5959DDAF6422FEF9174A4A8928401)
- FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/cXr8a3jcRMaztIY-rhdkzg/zh-cn_image_0000002563865705.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=1EABA485E86934B4B47952026AD6E0494D827AFCE055E52EE05264BA87331C67)
- FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/L2KUn7_BTU-eBKvglGXduw/zh-cn_image_0000002563785751.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=1D4877B61B52ECC8DF281734DFBD0E874BC3AC61D2E24F957DB2055E4EA20FAB)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

- [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。 ```typescript Flex() {  Text('flexBasis("auto")')  .flexBasis('auto')  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis("auto")'+' width("40%")')  .width('40%')  .flexBasis('auto')  .height(100)  .backgroundColor('#D2B48C')  Text('flexBasis(100)')  .flexBasis(100)  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis(100)')  .flexBasis(100)  .width(200)  .height(100)  .backgroundColor('#D2B48C') }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/AcMXL7uDSnOk9GFMAuChAA/zh-cn_image_0000002532905856.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=8FF382301AFE09A0C24A399E4EC435FD8ED6E782B4AA0F2F7E97DA58375D2D89)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/gCptMCPFTJyvQ1SKKRoH8A/zh-cn_image_0000002533065804.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=B53B2420A5A351CED973FCB98EB6EABD4569D0BAAD30E3F42E1E7E5F39020B9D)

父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp * 1/5=108vp，第二个元素为100vp+40vp * 4/5=132vp。

- [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('flexShrink(3)')  .flexShrink(3)  .width(200)  .height(100)  .backgroundColor('#F5DEB3')  Text('no flexShrink')  .width(200)  .height(100)  .backgroundColor('#D2B48C')  Text('flexShrink(2)')  .flexShrink(2)  .width(200)  .height(100)  .backgroundColor('#F5DEB3') }.width(400).height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/GQfJlufXTB2AcC-7HB9wcw/zh-cn_image_0000002563865707.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=79F2069E60F8E4C9342DCD67EE50308A8990992E6FBBC9C6D1856837F4537781) 父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。 将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) * 3=68vp，第三个元素为200vp - (220vp / 5) * 2=112vp。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/IS4NVFqhQTWvO-Y5MDf4uA/zh-cn_image_0000002563785753.png?HW-CC-KV=V1&HW-CC-Date=20260330T024725Z&HW-CC-Expire=86400&HW-CC-Sign=5CEC770F743A4977B2D20825B9F8FBE5A233BFC16FA8C9476DA79286B7BE4AAA)
