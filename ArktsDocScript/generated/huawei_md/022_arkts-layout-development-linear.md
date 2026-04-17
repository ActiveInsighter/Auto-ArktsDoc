# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D9uin7zWQna6KVNfgwo6aw/zh-cn_image_0000002540770988.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=3A9A2214EFC8B56B9C649BF27AA74552687F4285053915739C588903F3B1E079)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Djlebr-xSQGUtpr3douX6g/zh-cn_image_0000002571291285.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=F0C969DADE52C8969709E0399B5167E0DB1011486EE4E0BCA15A4D1627AEEE32)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Am6cQoZ5RcO4kBBQHjS_RQ/zh-cn_image_0000002540611338.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=A834DBCF733FA620F78435D6720D3D8C5D485D71177F6BCA361BB23B2663EA24)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/L8LYc6bcSsK5hRx-lzY9Lg/zh-cn_image_0000002571171333.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=8C26FA3348E04BA5F27C6F8B3393B87D41629DCF111F926ACA86E957A211F960)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/S73GzX1yQkWLxTJV1j0fGw/zh-cn_image_0000002540770990.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=E6FCF0B1AC9B1BF8928CA30C5CC9B8B52758720FD98E90932C2A66F0F2ABC966)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/PozmC_0sTca3qcvgCPajjA/zh-cn_image_0000002571291287.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=2F180142B071566BFCAB82DFC14EBDC792353CEE213B902D26BC6E45E7C5A724)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/X5hbVei-TsOkl7qQ_uy9aA/zh-cn_image_0000002540611340.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=52BDE878AE919BF941AE703FE5FF0452E50427A3E6D1F1D3CFD9C45136071C4A)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/uGGUZg79TTS4cpsxfthUgA/zh-cn_image_0000002571171335.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=38951F53CEB72522B9D3ECBBC1E57A77DCAE0B44E3FED5140565E4708A7D7063)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Cn2VR9jcT_mfgcFz4EBuPw/zh-cn_image_0000002540770992.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=D189B1E03E1B12CBDBC0B1CC78B854454009734D6644FFA726A0120BA07336FC)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/xLxAePd6Thairt1qTqPXvw/zh-cn_image_0000002571291289.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=018729431CA7AC44652BAD725CCBBE023E25B3C72C93A5642FB88A839E70C09A)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/BvZ3mhlFQNiaIsHmstlbYg/zh-cn_image_0000002540611342.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=1E77BEA836B363720435C2DAD43C1F328ACB241889BE7A9F3B1FD041ACEDD60E)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/v4Kn-5veQcWKZ1xg69v_EA/zh-cn_image_0000002571171337.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=3C19060123C168DC1191137D74ADFEA28CE5B52C0A2F4A7BB6865EAB1273EE1F)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/XOUqZYTmRDC63jXHid-H0w/zh-cn_image_0000002540770994.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=5ED86E154B5B08AF6EA4BF756D65D1D20A00636E67543F0585285874CB47780B)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/V75gLZj-S56I7xqg_om9Dg/zh-cn_image_0000002571291291.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=844C5D1690421B73B480B2EE626BD8F7F344C747D98A733C658C44FA4EB1E25F)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KA_GP2_oSyCCERg-a1wq7Q/zh-cn_image_0000002540611344.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=C9FED18A09CAAD3FDCE0B5FD069CF53C75B118E33B92FD8BEE8A27CBD55B648E)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dwOdk_OJTMqkmM-1zpYHWg/zh-cn_image_0000002571171339.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=A31DD3CE037B4AF4EDB5D90F6AE40D5CE01663E2CDF4619DA2F42BD6308BC561)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/UwWBmWg2T7q0eA9d7_o4EA/zh-cn_image_0000002540770996.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=B3FDF43CF3E2E92019040B18D77AAD6873C4D5E870DF288A5DB405D18E349660)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/MRzccms_QX2me9yfMUuluA/zh-cn_image_0000002571291293.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=EEC843C114EA5CCF622796B3222563F7B2CE196C3F9A5DC3FCEBB853BB344E39)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8l21IKbRTmuFYP3q4tN94g/zh-cn_image_0000002540611346.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=BC737AB4A77AE4A3432B03956D74240C918B00DE3E06C451C2B770AFDD832E60)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHFS0Ny6RMik9FekdTTQRA/zh-cn_image_0000002571171341.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=1C72CB2674A1A050D69C60693F509D4676AF44FCF1E9D13E36F24B2FF5F6C93A)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/E8rCzPuNQBS6yaRzbbkAPQ/zh-cn_image_0000002540770998.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=565D292C2AF8738D7FA47DF8D98F3AF4AC6CD0F862923291A17FD0A04FC509C6)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/EjDyHNnNQiK5YCz8ibMcFg/zh-cn_image_0000002571291295.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=5F2DFD604776972E052A7BFA7A6DDE7876DFE58D669681C39E137B72FC71C9E1)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/zRL2N4XzQcuYtomHBEknMw/zh-cn_image_0000002540611348.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=1765871D8A7F4FE214A019A72932EF7073C5DDE621D648D45C66763D13E3367F)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FWZH9DdMRkuCzympVtI1Pg/zh-cn_image_0000002571171343.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=8B54430483BB5C8CEC618382C0489F7643859B2120D4E0D975B65EB9834CB650)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/U7u2Vpp_SViRLVddsPqnAg/zh-cn_image_0000002540771000.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=53B18E20DE998753933C3498A91B37985BAB1179B0692FAF6B8CA34B0CB94842)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/4hT5BW-RSwiKiGWy4DIqdw/zh-cn_image_0000002571291297.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=D5FC7ED32783B46F374C52FC664D558208D3667DAD7F7C841BBEAED54719932C)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/S3-2orqJQBqN5KoPTDbBPg/zh-cn_image_0000002540611350.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=C75AA7824630FA1388723EE8FBCF43DE90B19D68FE551E903172750BAF45D056)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/d_v13AIMTT6SLV5LoVEeCA/zh-cn_image_0000002571171345.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=D0786C3F07F3251947EC195B423B7D0DFB5026BFFFA041B31A4B4C64EA09547D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k_nEf1nNRiqLjNCPwnsxMw/zh-cn_image_0000002540771002.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=EE3191904710EA0D813802A771CC0CD62EA34CE34ADA872113AAF93A8B456496)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ndx_xIKVQayZ2CrUURFM2w/zh-cn_image_0000002571291299.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=1AAF8CE5C26EAE029E623C5EED12C00AF415384DC4AD3A55912962A2354CDF72)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/CMKtEWizThi6Zb-Fl3yvHg/zh-cn_image_0000002540611352.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=E40079B49978BC0C95E886BE24CB23E58761457A1210D83368CFAC3EC84F2E4E) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/480AwfIGSySYQ5Oe3k-jvw/zh-cn_image_0000002571171347.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=8360792C6E2238E48F39AC36C2A3DA90BBF1B574C44DA7D426C5A4EA8AB5F836)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cSfg-2rzScG6eL7Oo8o1TQ/zh-cn_image_0000002540771004.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=B820582FD8A95E534ADEABC520F2E1E593AC8F4912747A90193F5C95C64DE385) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TsTkR1pGSwWCObQMteMtNg/zh-cn_image_0000002571291301.png?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=95C5EF7F7401094F025EE1E930046DECB11BD43BBBF049D9A6216386BDBA4E87)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/IEKx6GPXSxW0enCRrn5Mnw/zh-cn_image_0000002540611354.gif?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=5A3EBDF1DD082B7793050D0D857E5EC5249CEEDCA576B699A48B0D5EB3C68072) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/twZvgGyOTTi4sNAQEfF1xQ/zh-cn_image_0000002571171349.gif?HW-CC-KV=V1&HW-CC-Date=20260417T025050Z&HW-CC-Expire=86400&HW-CC-Sign=82D205FC785DD7AA0B98E498E1619EEC1247F97BFCC58CA4117FF8C1F4245380)
