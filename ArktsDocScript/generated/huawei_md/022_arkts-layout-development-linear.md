# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/wd1y7APuQF6AttmtO680DA/zh-cn_image_0000002542119426.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=A0810E58173BF2442A3B73BBC880C5C933245EFDC0B8A4B70CE91E10434D8477)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/q9Nu1yQCQWSow0PHkTkY6A/zh-cn_image_0000002572679697.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=707D180D9F7939E46DA1638C901B0BE9D78626E2A26958BC2018C3F88794A1BD)

## 基本概念

- 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
- 布局子元素：布局容器内部的元素。
- 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的主轴）。
- 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的交叉轴）。
- 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ZwSE2d4_T5yf6rxhsEZVYA/zh-cn_image_0000002541959790.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=7A3D1F00A65C24588BCC3903B1DFEEFC0401D3146D21BECD6D7BD0BF05154B50)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/D6ptUQzfR0iCT4mZHiT2LA/zh-cn_image_0000002572639735.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=8C069A4724952CFD075AC186EF285D0715AD95FB612ED009B759474A9B656E82)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/c9OKRdA1ROaJunaLAZ_CCQ/zh-cn_image_0000002542119428.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=A25AA69AD0AEF101C59C986286322B4C11DCB7DEDD9A524DF33A547AEA0363B9)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/KKlI0uvvRxO6bfiLlFsg_Q/zh-cn_image_0000002572679699.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=72FACE6F74E915DC4A9B9A669B118978BC3C7B686950595B3068E3B30EC4F111)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/f9E6YFh3STmG19D37EthWQ/zh-cn_image_0000002541959792.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=7D2DD6B4EFB13FD0F0AD6192DE2090275584C1799A6C597109703189EDFA2E2F)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/v508vox9Td6T4hS8awxSrw/zh-cn_image_0000002572639737.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=0E1690886DB7A189867C4A1FA8DF6CD4D983C4E40DCECD9179C7932CA9A89D1D)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/VtFtkpKbQY-byvuOrR7NEw/zh-cn_image_0000002542119430.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=3D476531B579B06C92BAB1EF98C00820A1C58634DC9AC514700C5671FC75E914)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ppQSJk-rTFm4SM5SYwOeBA/zh-cn_image_0000002572679701.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=14062E772315673AA3D85660287E5406CCEDD62FB255B53993965D186D5A82B1)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Ie0-D1aZSzuOTgPqQ8LlGQ/zh-cn_image_0000002541959794.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=F3472A977ACDA63ECC3BBA4F163B0B62E1A41273497B347E18D7863846C05399)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jnfHA_ZBTru6ePc2G64pYw/zh-cn_image_0000002572639739.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=202573C05B9A232986B69BE2F7A28B5679903E3060B7AC1A6E292BDEF496CA21)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/IAfh1MUpRSi0FNCCtpkq8w/zh-cn_image_0000002542119432.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=6375EEA7930D1F1F5DE48F7620309DBEADB90118B3DA307E44464B0AA06E020C)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/n52hAE93SZ6CpS4zBp3UjQ/zh-cn_image_0000002572679703.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=208F7517F7B8258C093A3F60E620E191423248685E291A5CB71D43B5780F92DC)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Pc0yK1uqQUeiKC87mQnaiQ/zh-cn_image_0000002541959796.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=632DCC8AEE6728535E0354A5F200CD2ED1B237EDDAC484D6C435A3F6BF8F811E)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/RolLWhxrSQizLn2JhkuKLg/zh-cn_image_0000002572639741.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=DD60764B48E45D04F9CCBD88E171DBF27A1B5261B73F3D43E7A020BF52FC7F9A)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/p9cWMJJoR5uuMIfZqo7BgQ/zh-cn_image_0000002542119434.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=A0CB6EBD0D6681C6CDC9ED52115345C7ADD42BE768EBBED8430D6D659AC91ABF)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/V4nbMqMzRtKLZIhg2X-NFQ/zh-cn_image_0000002572679705.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=EB6BA6A29EF8F08FFC3D9DFB3CC399DCBC23E3D7C5C87A5E94BA158949077211)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vPX6JvJCRMu3kqKV4Lksow/zh-cn_image_0000002541959798.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=FBEC13801A1363B4CD12D086097DBF7FFF6AAB068A9178E649884823A1E1B813)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/V4gwr3LDTyOGWpn3HWaaeA/zh-cn_image_0000002572639743.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=8783FDAAC80BF4AA6C3022A37C0082E295EFEC4E16651173375030E8895561E8)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/u0jC2r8dRM64Dnz1VrwemQ/zh-cn_image_0000002542119436.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=6FA159AB9A22E8C3A4862D0434317A34DE3F8FB6C24E7E6609B637B6CBC9E9F3)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Hkc2QLipT2ax05Y_mNIrsA/zh-cn_image_0000002572679707.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=F370B21111A387370193E24F8BA7DB7EC5EFEDEA259F767BB5C667A7074CE20C)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/8HS7ofZbT_CLJrjF6MRQWg/zh-cn_image_0000002541959800.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=12774BCF2CEFF8FEC2796CF3E497C533906FF207F1511AE8CEBCBD9880B03C6C)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/07FURV1FSumD_2gU7W29xQ/zh-cn_image_0000002572639745.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=C4213DF4A2F3DC25FBDE4B2BA432A367F4FCA228EBE621780DA0795DEB7C2903)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/FclKUNCOSy6dSOBc6PIVpw/zh-cn_image_0000002542119438.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=E600C0CCE38FFE853BA21F32F2C58DFCDFCB7F2F1BC88FCB3B33400E86702B79)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/nPVcd1R0Qz6P-QH7vKHypQ/zh-cn_image_0000002572679709.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=99C7A1C40CE937BD407105A0AAFCFFCE3F37862CF60398A696A0227906984214)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/GnmT6m2HR3OsrB2UxTNT3Q/zh-cn_image_0000002541959802.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=8597FDAC259DBA56580A004131912336B6BB1AF0A064BC273E6A5A087B65FBF6)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/GwaVFQsIQX66nthMUMMsEw/zh-cn_image_0000002572639747.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=CF040F597C2A2431D36E41C4AA3532375C9A6325ECB38ECFC39E2C5907BCEE52)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```typescript
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

**图9** 竖屏（自适应屏幕窄边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/QA984cu3R6ObNMh1YuWM4w/zh-cn_image_0000002542119440.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=36E8FBCE0E2542EEF870BF1EBF64F18F9A19B9DE71AC06069B848ECC991C80F1)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/qFN6z2pnTuu2ZRysq-VBpw/zh-cn_image_0000002572679711.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=5B5017BAA7AD12BB23DE6D9F4BE94238426CBC2B85163046A90ACBBA1B1992FA)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/jAHyNhtzSoeuDoZFIwGi0w/zh-cn_image_0000002541959804.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=9131C18B9F7333A6B94794F592C5ABCCCB997852D09895F74A5A94881AEFC52B) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/pr5G1ZlsTOa5koGvJOoQpA/zh-cn_image_0000002572639749.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=440EC817004EF69D4FAEBE0CB761D5D777B48B1633F7DA73FAF3B04798AC908F)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/5pd9OC89Q4mJwm31HoHNRQ/zh-cn_image_0000002542119442.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=C802CE1E765179D1D3FC4E4FD6564C83165CDBDEE70C0B7F7E17B46DFF1944EE) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/A6s-06F7SIai8Gov0FgHeQ/zh-cn_image_0000002572679713.png?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=2997D3C3555C10908C12FB41932256F5D8D3EFFE26F0A35B148CC0D6BF18BA29)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/5pwP4pFITESFzbZE7yYJ4g/zh-cn_image_0000002541959806.gif?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=2622F7C21C7AEC5713B2471401032B85C8CB9EA9F92B99B65EF0AF47CDCD28F4) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/k01nyotNS_Kvhj31mfdUeQ/zh-cn_image_0000002572639751.gif?HW-CC-KV=V1&HW-CC-Date=20260420T025806Z&HW-CC-Expire=86400&HW-CC-Sign=60D0E1B36BE903AF1D7425C52D36F9AF7B4B192D252249C3FE0AB487A9E6CB0A)
