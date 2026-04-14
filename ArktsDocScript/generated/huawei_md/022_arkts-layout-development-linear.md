# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D9uin7zWQna6KVNfgwo6aw/zh-cn_image_0000002540770988.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=0E7B363121FA3FFEFF1BAAC046B2849D1D4800EFB4FB9DDA084D0588B2D6C1FD)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Djlebr-xSQGUtpr3douX6g/zh-cn_image_0000002571291285.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=3BBC6BAAF68E8CB8D983606B40E8F88E48A9BE8D490DBBBD1B2636C0872CABF4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Am6cQoZ5RcO4kBBQHjS_RQ/zh-cn_image_0000002540611338.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=7515F4764BFD57FC5336C1A18FFA7B1056B06152D8555183049264BFCA570FDB)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/L8LYc6bcSsK5hRx-lzY9Lg/zh-cn_image_0000002571171333.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=C671C93E57E1665A4D0430FFFE90DC8F4E0A75E4262F039C5CF7F363E484FA74)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/S73GzX1yQkWLxTJV1j0fGw/zh-cn_image_0000002540770990.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=90977981281D8FC40443535F3825E406B862671ACF864FB2CDAA09295FFD18E2)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/PozmC_0sTca3qcvgCPajjA/zh-cn_image_0000002571291287.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=B8C64270A600DD714B479B12E7898FA644FCEE2C10F2DFFB20E9917DCA639448)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/X5hbVei-TsOkl7qQ_uy9aA/zh-cn_image_0000002540611340.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=FAC2A36F64D671B087302C9C7EF53EA18F5952304B32FBD2FC2877717E4B9152)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/uGGUZg79TTS4cpsxfthUgA/zh-cn_image_0000002571171335.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=534ACDCC7A65298E43F83C19DCB5A7942CECFA416086266F449E312205899FE7)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Cn2VR9jcT_mfgcFz4EBuPw/zh-cn_image_0000002540770992.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=F193870A111F207775A67EE83067B1CDBC33E5028D7BCE8E46AF5DC2E894618A)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/xLxAePd6Thairt1qTqPXvw/zh-cn_image_0000002571291289.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=5D0A4EEB507513A5AE708DA97CA35AA86D74F352F30E94165C46AB3791CDC579)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/BvZ3mhlFQNiaIsHmstlbYg/zh-cn_image_0000002540611342.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=B5F065B35531EACFA54BCB4261F3808B6EE8D1034A55DC6FD5688514B08D71BE)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/v4Kn-5veQcWKZ1xg69v_EA/zh-cn_image_0000002571171337.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=49D2AA40D378A04FF5A443A1C4FE9CE27C000F4F551D2719ECD3F83DE2AFD3D9)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/XOUqZYTmRDC63jXHid-H0w/zh-cn_image_0000002540770994.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=1AE6CE9CC66817E252FD827A78106EC8ED28A168159A3E6DF75C930216E1273C)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/V75gLZj-S56I7xqg_om9Dg/zh-cn_image_0000002571291291.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=2AFBBCFA33602F458786BEB987821962CF6C81298C06C956653D8F322021B6E6)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KA_GP2_oSyCCERg-a1wq7Q/zh-cn_image_0000002540611344.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=73E54317AE3638A5C9F7B1DF05F4C90FB8D86AD1509B862AA535528EBB307E6C)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dwOdk_OJTMqkmM-1zpYHWg/zh-cn_image_0000002571171339.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=D148C62CDF25CBB230C41E09A352CC129196CBFD8891510D54812C5941929C68)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/UwWBmWg2T7q0eA9d7_o4EA/zh-cn_image_0000002540770996.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=683457B1D1115A68C4FC4BACE3C6DFF210376811E0534DC0FA4742849F5961D3)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/MRzccms_QX2me9yfMUuluA/zh-cn_image_0000002571291293.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=5DC19F6729ACDE6A8FA4B7BCC66A8C319425C2E32CFA267E58A1574C76B5F016)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8l21IKbRTmuFYP3q4tN94g/zh-cn_image_0000002540611346.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=9E0875D8D18987AE6471282CD1F3E501840ADDE6F807A1AF2734624D9D6B16EE)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHFS0Ny6RMik9FekdTTQRA/zh-cn_image_0000002571171341.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=5CCC1451D70228276B4846A4BF3EF2EE22EE65543224E844E64542CFCFE02D30)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/E8rCzPuNQBS6yaRzbbkAPQ/zh-cn_image_0000002540770998.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=F7CEDF31221D796459AEB2A19C81BE7B9EF654B6265C4F5592E9ECB5A3F08DE2)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/EjDyHNnNQiK5YCz8ibMcFg/zh-cn_image_0000002571291295.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=821C91C6EF41CC03E4AFD28730772F59F16E12A261A0A6A2BAC1EE62E98E6EF8)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/zRL2N4XzQcuYtomHBEknMw/zh-cn_image_0000002540611348.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=868CA0D02EEBB694CE5B55CBC300DF354F62BF9FDBD7696B793356E338EF6645)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FWZH9DdMRkuCzympVtI1Pg/zh-cn_image_0000002571171343.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=C3F6E73BB042AF8DC0E678E79F9F6F25B60E65E474FD30DD075102153EDA0847)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/U7u2Vpp_SViRLVddsPqnAg/zh-cn_image_0000002540771000.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=938D5545C2B12ACDC07EE62A5358E51263B6F8D2AE310739743E144D6411ADB5)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/4hT5BW-RSwiKiGWy4DIqdw/zh-cn_image_0000002571291297.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=E80C6F666B714FDDDE7BF737F70C1FF7F668158D1F58684329463891FAC330BF)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/S3-2orqJQBqN5KoPTDbBPg/zh-cn_image_0000002540611350.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=203497BEE8B6764F85D73ED16D797D3CE5F8A79A78A0CF2D3027233E869E3006)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/d_v13AIMTT6SLV5LoVEeCA/zh-cn_image_0000002571171345.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=288532CFCE560F8BA80D2A3C77B5D815A4490CAFEE0698AC27C15165806D15E6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/k_nEf1nNRiqLjNCPwnsxMw/zh-cn_image_0000002540771002.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=54509477AC1B8408AC3CB847D092A3686F166C519E7DAAA98E86197D0B96243D)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ndx_xIKVQayZ2CrUURFM2w/zh-cn_image_0000002571291299.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=B4C070EB1217FAB136DD28E4FAAFAEEF4638EE67C5780833DBA9751EC1B4695B)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/CMKtEWizThi6Zb-Fl3yvHg/zh-cn_image_0000002540611352.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=3A0556506D69D765D2CD5CEF47AB2EA4EFB92585B00F15036F2B1AC882D1347F) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/480AwfIGSySYQ5Oe3k-jvw/zh-cn_image_0000002571171347.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=BDE5B2AFA49C3A2117F576FE6F10D93C13CBEFD5FC9E5831F17F69DA93632431)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cSfg-2rzScG6eL7Oo8o1TQ/zh-cn_image_0000002540771004.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=99E36D7C9D152441166D831EF2B091169DE3FCE108E45A6E3B006BBD3D7C390F) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TsTkR1pGSwWCObQMteMtNg/zh-cn_image_0000002571291301.png?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=3139BE3F5950EEB47ACD530A6D33C65D0EE7C1F3C9349694A6E7E026468566DA)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/IEKx6GPXSxW0enCRrn5Mnw/zh-cn_image_0000002540611354.gif?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=DA0DCF40F5F2060EC6199CBDE26CA35274FF34E7B5A1855D5F802BBCFB317A99) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/twZvgGyOTTi4sNAQEfF1xQ/zh-cn_image_0000002571171349.gif?HW-CC-KV=V1&HW-CC-Date=20260414T025027Z&HW-CC-Expire=86400&HW-CC-Sign=E4F80D8276DD9DB12C7EDFFBB260A3F997CBFC857C13DFF969C2A42132FF3558)
