# 弹性布局 (Flex)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout

## 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/NNKVn_-PRSe58zClKDDB7w/zh-cn_image_0000002541959810.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=D348EBEF87BE5B996FE8D603C545F8A0920A348D063230F736957BA2A805BCE1)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VMldtHsrQjaxvUmCLMqBZw/zh-cn_image_0000002572639755.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=75C66F87D767B5CD61757CAE38F1F007E616C8D6F3E8D575F11B3111E61B9772)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Hh5OnemJSKios5KxZuy7dQ/zh-cn_image_0000002542119448.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=E88510CC76398ECA090E8B995FD9F58B0CE9E4925187A5A4BBA78C9088D9800D)
- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.RowReverse }) {  Text('1').width('33%').height(50).backgroundColor('#F5DEB3')  Text('2').width('33%').height(50).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/R21jaIzMR3GqbsLOA1UeAw/zh-cn_image_0000002572679719.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=AE34D0DB0910D5D108728111539A3410A5F3259A084F7A242A82A5F6351BBC38)
- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。 ```typescript Flex({ direction: FlexDirection.Column }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/myCWqJC9SUCmYRB9ZU2ulw/zh-cn_image_0000002541959812.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=52FDF62196932F527B9354A0BF67B6F70D68338C190CAA5A32AB1FB86F91AED4)
- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。 ```typescript Flex({ direction: FlexDirection.ColumnReverse }) {  Text('1').width('100%').height(50).backgroundColor('#F5DEB3')  Text('2').width('100%').height(50).backgroundColor('#D2B48C')  Text('3').width('100%').height(50).backgroundColor('#F5DEB3') } .height(70) .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/SWKQBzCnReuJvP_ECjSqGA/zh-cn_image_0000002572639757.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=554306D41A00A018FE01CFD658785466A21CA5F07CFD3A1B1036B37963713E55)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

- FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。 ```typescript Flex({ wrap: FlexWrap.NoWrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/9L27CsweSBuATrO-jbzFxQ/zh-cn_image_0000002542119450.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=349F5627952B2CBA1E67D9601E563D0BB6837007A82E26ACC949DD1EAD69C826)
- FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。 ```typescript Flex({ wrap: FlexWrap.Wrap }) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#D2B48C') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/TeOc4D-ESrKiFqgKJofnhw/zh-cn_image_0000002572679721.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=DD4CF54B799F3BFB3FD4D62E820958896BEAD0179E95BFD7EF850D98AB42F9C1)
- FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。 ```typescript Flex({ wrap: FlexWrap.WrapReverse}) {  Text('1').width('50%').height(50).backgroundColor('#F5DEB3')  Text('2').width('50%').height(50).backgroundColor('#D2B48C')  Text('3').width('50%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/rcYPeQsoRrSc6qIvnfDb3Q/zh-cn_image_0000002541959814.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=237B91819D16F69E9E31F7D8588F0671AF6F5592302AAA968B1E9832C5C2417D)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/2iHAXJ0TRf66Pem9AflOYg/zh-cn_image_0000002572639759.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=AE431C4EA0CA9C44BAC76E67E888B290D88545B236A748C7B450B24E13F587E0)

- FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.Start }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Rpw7ApclQNaWycsArWYC1A/zh-cn_image_0000002542119452.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=6646495649199969E77D41457E951D48AE930D2B3EF88986472EBA310BB35984)
- FlexAlign.Center：子元素在主轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.Center }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/H7goChHDSze9BJKV4won3g/zh-cn_image_0000002572679723.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=7E0231E4462E6C0F1BA3BDBE599A6AB15DAA6DC6CF293F71C176D8AB88EF81CB)
- FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。 ```typescript Flex({ justifyContent: FlexAlign.End }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/gce00f-nRdyDbwy3a34eKg/zh-cn_image_0000002541959816.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=D644C65BE90BDDB7B35E5980D909F5A2B61FD302B4019E6D649F8244140B4A83)
- FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/W3gWl6ZRQMi_YEgjXPhHuQ/zh-cn_image_0000002572639761.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=1ADAA9C1419A076857CFA73F169BB33980DC056E11027963E67FFE450C7D5AC0)
- FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。 ```typescript Flex({ justifyContent: FlexAlign.SpaceAround }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/XehsoO9ERyGNoN5o-_fpVA/zh-cn_image_0000002542119454.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=DB5A658FAC8EAF3E660ABD3E8AB351E7B6F4962E55AA9D507241F08F6F185E57)
- FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  Text('1').width('20%').height(50).backgroundColor('#F5DEB3')  Text('2').width('20%').height(50).backgroundColor('#D2B48C')  Text('3').width('20%').height(50).backgroundColor('#F5DEB3') } .width('90%') .padding({ top: 10, bottom: 10 }) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/v5w2WntDSmCJd5oVg3BzNg/zh-cn_image_0000002572679725.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=48AD98C8DD5D861DBEB2026B1D64B5CF8CB8E3D866470714B472B6FC398B7BAD)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

- ItemAlign.Auto：使用Flex容器中默认配置。 ```typescript Flex({ alignItems: ItemAlign.Auto }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IIDmDnizQAOMcAkvMl-FAg/zh-cn_image_0000002541959818.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=1F21DA0F1E172EC6E2DF124081CF4FF8C6EB7FB9B7EF397C3E2598BEE02FFE80)
- ItemAlign.Start：交叉轴方向首部对齐。 ```typescript Flex({ alignItems: ItemAlign.Start }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/FAvjmVf3Q7iRyoPp9jjsLw/zh-cn_image_0000002572639763.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=857A829D516D18D8D4884045579083BE916565D74F1BF6C6B4CA288750C7BB40)
- ItemAlign.Center：交叉轴方向居中对齐。 ```typescript Flex({ alignItems: ItemAlign.Center }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/L_G3oTmoRhmLZrgAGxQOVw/zh-cn_image_0000002542119456.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=AF1B6B38017B4EE0B1AFE8C57E99703F0C0C00E9BC98095FEB2BED39642B28EF)
- ItemAlign.End：交叉轴方向底部对齐。 ```typescript Flex({ alignItems: ItemAlign.End }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/2YsdPOA4SWey-5pkdgAqfw/zh-cn_image_0000002572679727.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=77912C85FA2E0B5255391542D9C6C80CA54D68AC12C29E4B9108BD9777B8306C)
- ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。 ```typescript Flex({ alignItems: ItemAlign.Stretch }) {  Text('1').width('33%').backgroundColor('#F5DEB3')  Text('2').width('33%').backgroundColor('#D2B48C')  Text('3').width('33%').backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/ZUAcQ-f6RPuyQ5yEfGqY5w/zh-cn_image_0000002541959820.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=8180D63E86FFA712BE3E6BAF38EB54D3EAE6EE8684CC343812B46C35D44A9E84)
- ItemAlign.Baseline：交叉轴方向文本基线对齐。 ```typescript Flex({ alignItems: ItemAlign.Baseline }) {  Text('1').width('33%').height(30).backgroundColor('#F5DEB3')  Text('2').width('33%').height(40).backgroundColor('#D2B48C')  Text('3').width('33%').height(50).backgroundColor('#F5DEB3') } .size({ width: '90%', height: 80 }) .padding(10) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qSyRSzhbS3ilmtVW0MjeoA/zh-cn_image_0000002572639765.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=FD7EE58374C9C54CACA8368B2DB457531A079ABEF0A1A9DFF12A05466114744A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/d4W0HgHvTS-LNxvkZxtXyQ/zh-cn_image_0000002542119458.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=A45336A15FE21A503B557858A08893080723749135F63E4651F1F4FFE033C45C)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

- FlexAlign.Start：子元素各行与交叉轴起点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/8FDCo03nQoahNQvUctGeTw/zh-cn_image_0000002572679729.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=CA80B0702CBD114E7E5055CD06C283962A0031055340B3F1216846792E6F4AEC)
- FlexAlign.Center：子元素各行在交叉轴方向居中对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/xno7jNK0StqL3co5WSKq1g/zh-cn_image_0000002541959822.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=610BE4C93BCB3D24D5C80ED4178A64E9AB6258C482E1A38AA0FFB4BF8B3071E9)
- FlexAlign.End：子元素各行与交叉轴终点对齐。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/4_BmfNyzQLiZeRYJchoS9Q/zh-cn_image_0000002572639767.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=6514319E874795840A26902B01C3AFBA4B3E0F1F1A239CCA36D81EADB03CD797)
- FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/DPeyM03QQIaeIHIzZ1kDWw/zh-cn_image_0000002542119460.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=D35764B767A9B481303638560FCE4E732BBE407ACBC245F61B794E5317A6C8D6)
- FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5kYsbGeQSjKziGYGH3ghig/zh-cn_image_0000002572679731.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=7E8552CA38312B7A6901BEBDDAF8035672D35CD1982A98C89BA25F1A2DF7412F)
- FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。 ```typescript Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {  Text('1').width('30%').height(20).backgroundColor('#F5DEB3')  Text('2').width('60%').height(20).backgroundColor('#D2B48C')  Text('3').width('40%').height(20).backgroundColor('#D2B48C')  Text('4').width('30%').height(20).backgroundColor('#F5DEB3')  Text('5').width('20%').height(20).backgroundColor('#D2B48C') } .width('90%') .height(100) .backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/sga26L10TaKrlKHc6xv8zQ/zh-cn_image_0000002541959824.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=E16B66120B52FB4A1DC60CD47A2BC3DA288972A15F0E1B3D4B7299448DB4E82F)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

- [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。 ```typescript Flex() {  Text('flexBasis("auto")')  .flexBasis('auto')  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis("auto")'+' width("40%")')  .width('40%')  .flexBasis('auto')  .height(100)  .backgroundColor('#D2B48C')  Text('flexBasis(100)')  .flexBasis(100)  .height(100)  .backgroundColor('#F5DEB3')  Text('flexBasis(100)')  .flexBasis(100)  .width(200)  .height(100)  .backgroundColor('#D2B48C') }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/oo3dETeTQg-xjpVHhVlCHg/zh-cn_image_0000002572639769.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=9200522CE6ADC73E4967B6A641B504A7254AC66DA4FC48D2832DB242079C1A83)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/b9rbzAwPRSCxQL19MlM0mw/zh-cn_image_0000002542119462.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=7D94D2362E0B0097C72FA143D77FA96E9D25F4F002EB7AD549D14791C95E87CB)

父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp * 1/5=108vp，第二个元素为100vp+40vp * 4/5=132vp。

- [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。 ```typescript Flex({ direction: FlexDirection.Row }) {  Text('flexShrink(3)')  .flexShrink(3)  .width(200)  .height(100)  .backgroundColor('#F5DEB3')  Text('no flexShrink')  .width(200)  .height(100)  .backgroundColor('#D2B48C')  Text('flexShrink(2)')  .flexShrink(2)  .width(200)  .height(100)  .backgroundColor('#F5DEB3') }.width(400).height(120).padding(10).backgroundColor('#AFEEEE') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Wkkir7W0R2qdzzQlsk9yIw/zh-cn_image_0000002572679733.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=1823F161A5BB742424EA2DE871719F67924D40F8650B51CDE24A1ECF7E1B9421) 父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。 将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) * 3=68vp，第三个元素为200vp - (220vp / 5) * 2=112vp。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/zlQ79reaR1KEpF83wv2Qzw/zh-cn_image_0000002541959826.png?HW-CC-KV=V1&HW-CC-Date=20260419T025726Z&HW-CC-Expire=86400&HW-CC-Sign=9405C6AFA0EB868E7CE0513F9E1A08A409C0205F9ED5947332DB753A6D953D0C)
