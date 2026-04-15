# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D9uin7zWQna6KVNfgwo6aw/zh-cn_image_0000002540770988.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=578EA292970220F5FDA6780B8BC1C85BB99430AE8C54A8A59FF27E0784E3C7C2)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Djlebr-xSQGUtpr3douX6g/zh-cn_image_0000002571291285.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=ACEE7E8C86EDBFA09F7AA80C413DBC35A97FC7D9FADADEF7BF908ED6E8202B8D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Am6cQoZ5RcO4kBBQHjS_RQ/zh-cn_image_0000002540611338.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=121819F0BAF3A416724E67062DF32FAB4997E426F67CF5C5612F2A3CDE0B75CB)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/L8LYc6bcSsK5hRx-lzY9Lg/zh-cn_image_0000002571171333.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=839BA173D5F417A013684A900C28B91C4C8848993651E40F6231489F4F77964C)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/S73GzX1yQkWLxTJV1j0fGw/zh-cn_image_0000002540770990.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=72718E4B1F27C1470518A84891EE4CD1C5CD03ECF18690CE3E5BDA35F220B37A)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/PozmC_0sTca3qcvgCPajjA/zh-cn_image_0000002571291287.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=27150B8AACBF47EFDA57C05E4FBC4F8345EC51FA91F4540939BEDDF3F5D1A01C)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/X5hbVei-TsOkl7qQ_uy9aA/zh-cn_image_0000002540611340.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=3A2A46210F1DECF5A95F1DF3650C3B839CF6ECE1FDE49BEE3DFD8676CDAED2B8)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/uGGUZg79TTS4cpsxfthUgA/zh-cn_image_0000002571171335.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=F2507A81E38D7986071205D7BA9555BF2889296A291A691D12948AA8E4FE4B47)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Cn2VR9jcT_mfgcFz4EBuPw/zh-cn_image_0000002540770992.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=2B1E487BD3446C51797F57034B5500C9EB34F804A9484B079B86E689ED582302)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/xLxAePd6Thairt1qTqPXvw/zh-cn_image_0000002571291289.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=F4B661881DE9CDF65E620150AC557C2F11329028F38ED1B65117C3BEAEDE6706)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/BvZ3mhlFQNiaIsHmstlbYg/zh-cn_image_0000002540611342.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=1A6BFEF11D802D7D86D13A350A7AE1AC6A2C9D1A799580D665A09F0EEAAF1A99)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/v4Kn-5veQcWKZ1xg69v_EA/zh-cn_image_0000002571171337.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=FBD4783FB18A9BD36E8EF15D7E05253A1BC28BFD52EFCEB041F3742713FC5282)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/XOUqZYTmRDC63jXHid-H0w/zh-cn_image_0000002540770994.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=D1F0C219E267C7FA2346181383096A4124D1101F392459C1B7969743178F63D2)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/V75gLZj-S56I7xqg_om9Dg/zh-cn_image_0000002571291291.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=B94373753B87D1D8C2ECDB4D60656B6DAA413A1945AAA4A9AD6B4028F7C3B82E)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KA_GP2_oSyCCERg-a1wq7Q/zh-cn_image_0000002540611344.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=3CDCDE791C56CE2FB00B65DF0A13EDC686AD8F7036BDC7EC1C745D47EA6BE7FF)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dwOdk_OJTMqkmM-1zpYHWg/zh-cn_image_0000002571171339.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=AADEFBF335BD1D9655E5CB7C25F44ECB7D9FCAAF92331FA4A002161693ADBEB9)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/UwWBmWg2T7q0eA9d7_o4EA/zh-cn_image_0000002540770996.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=D6755E07585CA32DDF37AA41196E1F3C10F8C318C693648CE20864EE48E2086C)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/MRzccms_QX2me9yfMUuluA/zh-cn_image_0000002571291293.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=E4802140B61DED1D9D8CA70000AF4ED9DA81144B0FB6FD7790AFBBAF7BF57163)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8l21IKbRTmuFYP3q4tN94g/zh-cn_image_0000002540611346.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=EB6446C69815B41FAA89973DA6E2538F7D230FBA4B47A894E7C6A9923EB71974)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHFS0Ny6RMik9FekdTTQRA/zh-cn_image_0000002571171341.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=9679FF159AD5FBDE8A98D11D48A9D913680289A1D0BCAF1FA93DF15641AE4070)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/E8rCzPuNQBS6yaRzbbkAPQ/zh-cn_image_0000002540770998.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=4BE5F0D4C7394890666A75CD61D79AC1C9D76E1AFF442A0DE765FB1698CE5E79)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/EjDyHNnNQiK5YCz8ibMcFg/zh-cn_image_0000002571291295.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=3EDC61493BEA11203A37C6C9C76806733866B976C815DE8829BA12A95DD59A18)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/zRL2N4XzQcuYtomHBEknMw/zh-cn_image_0000002540611348.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=1C0EBC9CB211F6E32EFEBDF79C2FE63CE6334B30DA3A16E4B7D57B4F2DB50EC7)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FWZH9DdMRkuCzympVtI1Pg/zh-cn_image_0000002571171343.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=1E0E395A708D4A1FAC5563FFDF4EBAE2068122E769AC844E2FC413DD47D47D21)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/U7u2Vpp_SViRLVddsPqnAg/zh-cn_image_0000002540771000.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=9EBB8CF5217B40DA0D1BBB3E4EC6C87AEFBFC2A7B619D627381DBC7D1D5EA1AC)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/4hT5BW-RSwiKiGWy4DIqdw/zh-cn_image_0000002571291297.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=02070AD586C9B324D60450652BAF07A6D8C889148966F954B155051EB664E528)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/S3-2orqJQBqN5KoPTDbBPg/zh-cn_image_0000002540611350.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=F6F2446782A438CD29EB6B5A41BBA8A3FD84BEAEA164BA7F11B92CBF183FD84F)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/d_v13AIMTT6SLV5LoVEeCA/zh-cn_image_0000002571171345.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=99A0F3F1C3A25C1C81678E16F6C69B1513D48B38B4004CCAA316B755F63546B1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k_nEf1nNRiqLjNCPwnsxMw/zh-cn_image_0000002540771002.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=A1F6D5196DFF748F212E6DF8B9963F81BC53A902D5D34AE5304096FCC6B0183C)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ndx_xIKVQayZ2CrUURFM2w/zh-cn_image_0000002571291299.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=10917AA9ADA2F526F41A21F74C5BB6F39AB002D88112F99A5C90F14166514B67)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/CMKtEWizThi6Zb-Fl3yvHg/zh-cn_image_0000002540611352.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=88B264644CD5AF0B4846F6D4583BF83F5C10B070A87010E1B07300227FB6A458) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/480AwfIGSySYQ5Oe3k-jvw/zh-cn_image_0000002571171347.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=BC228382321D9428B09A3AC7F7DCB0B8F1B53EDDEB6774EA19273E466C9442F1)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cSfg-2rzScG6eL7Oo8o1TQ/zh-cn_image_0000002540771004.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=06906D4EED5CA8B21CA025B805C6E601750DD0A8C2744AA4EF37C7696750F3FD) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TsTkR1pGSwWCObQMteMtNg/zh-cn_image_0000002571291301.png?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=B2BD85D1C8C724FDCA49224E6AFD64E60B13160DBABF91580EAF6E88F3E3E766)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/IEKx6GPXSxW0enCRrn5Mnw/zh-cn_image_0000002540611354.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=47B6EB652D9DF04F5FD78F33F79993A422D6E8C8CBA3BBD92280FDFA02B03A9A) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/twZvgGyOTTi4sNAQEfF1xQ/zh-cn_image_0000002571171349.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024806Z&HW-CC-Expire=86400&HW-CC-Sign=23C00F95B824277871DC668186B75A445DEA5630A2C0620958A87246C9A72D69)
