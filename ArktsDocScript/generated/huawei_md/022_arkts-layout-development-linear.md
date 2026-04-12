# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/XDACe416Q36Gcr3_ncpY5Q/zh-cn_image_0000002538288552.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=74AB4D8BE5154E4DCA6509B162301758CF1D44A8EB422071B2F9CCD0084F9D13)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/UqNlIQk2Rduc6OqIcaHMLg/zh-cn_image_0000002569168315.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=934C6A0D5D4A8E40BEF139D9EF1CAA2268FFDB6B7E1F490A08A0ECAB635D924E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/wgqBxzsRS3CajQ5Xjbu_tA/zh-cn_image_0000002569128341.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=EBB5673D54330090295B6D550EC42425BB9CB423015E4467ADF824A2AADDF403)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/gTiplfjHQ9ejfBz1UlMiqA/zh-cn_image_0000002538128620.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=BFDC8774372ABADB19A27E26277399F1E204CDE4CC3D862BEED602C359A73E50)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/oORhqgxURVSdlorCkYBKeg/zh-cn_image_0000002538288554.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=F7B9480D2D9BC419295B3ED969E98EE37631CC56106486EC3608EE7C6EE9DAB4)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/fDaNBV1HTIS3j32gPDRFiA/zh-cn_image_0000002569168317.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=6F1CE6C364DE3D0A6DC5402B250D213DDF1E6385228E1067D96C38037201F98B)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/y8U_fManQKuv0y8WxzQ-2Q/zh-cn_image_0000002569128343.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=067B65CC32A35CF76849D2B0B4F92CA6B6DCF478BFA37FBCDA9CD5B957D9E56F)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/-ILok6pzTvq6TQ85GQUgag/zh-cn_image_0000002538128622.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=CFB65D2726E862AE2DFA35F8EACB6BE5B9BD6DDBD868424600DF88BF31F487B2)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/JZR_UZvWTXiJgPaxWCaEqA/zh-cn_image_0000002538288556.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=CC39F2F19055A1D890D73D3E996F0B52A1959DD83E31EB6CF7CDF00953E60B8E)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ETgBS35vTdCFLOodprrwdw/zh-cn_image_0000002569168319.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=8BE646F1184806FF0AD0202581D76C72BEA1354E547B96F25D09913AD3E3955A)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/aK_85xHTQ6Wrk6YEIwRoPA/zh-cn_image_0000002569128345.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=835814E99D16C497626C5532DA6BAA31A86B81B5EAE6FE6002415A1F5A98D11F)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/ATJdCMw5RU23vQyFm4qVkg/zh-cn_image_0000002538128624.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=11808CA222D5482D35AE577F9F974BFA290254DD7A111E67D49D8DC045965630)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/yJaAtyn-TvCTsCB912UNNA/zh-cn_image_0000002538288558.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=390E73A81915072D022E58EB5CAB3CF27511A5AD674231C980D32FD8DD07BEE8)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tB3BOMszQX-rDZH_hmpydg/zh-cn_image_0000002569168321.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=132F316ABA6F6A7035E22D14B9DF4CC82CA2860C836FE3B3A38B223326F42AC8)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sHy4Md5YRKaeMJfs4rPuLw/zh-cn_image_0000002569128347.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=91236D150503F08A37045F976260D675D3C062F45AAC4534C315655AA5097047)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/57hq5rTJTpedrQ1sXIF5gg/zh-cn_image_0000002538128626.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=7BC3284326AB3C49CBC20F8C79F29C36A3EB571212719D092681B2DC4A678A7E)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/P0Q_TUAbRVu7fKimTUvoAA/zh-cn_image_0000002538288560.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=E419AB3D6CA3ED414EA730411D394C65CD72CD94782720C14D288A4BEBD77F65)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/bJxikodYRvG1sHa_qFwkQQ/zh-cn_image_0000002569168323.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=67B0EA3FB68D337B6092972FD5F6DA35DEAF1E6C5BB706374778469808B49569)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/cTeAiFURTCSZ0v1nzun9jw/zh-cn_image_0000002569128349.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=C5CD0CB3A5E43D48DA5B9CD3C8C95E6E9AAAC53318C837AFCE92B023074573AF)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/GHZ4DaLSTNuEQO5074TQ_g/zh-cn_image_0000002538128628.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=32AE2168DC959DAAFFB59163E0FEA4B8CB9A046840899E5721CDC64C5D365AC4)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/KcyAsyYHToCcsmhn_CCZ2w/zh-cn_image_0000002538288562.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=0F783B5BCF85AC04CEDF9349CD44ECF835F847C56C397A19409B1A9E35D01A79)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/NWDiHpxMQu6nq67hS73bfA/zh-cn_image_0000002569168325.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=C444D4F0DFC15191A54BA8652AD31F2B14DD8F10B42EF3661A2F1787EDCAC5CF)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/rG8uXBgsSeGFAqWd1d15Hw/zh-cn_image_0000002569128351.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=A78780838BF2C2A6C48D6622103D1823A5B526853B82F7A5D2A3460E2E85EB25)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/r1qrMmyHTbyqZfBXdsBJbQ/zh-cn_image_0000002538128630.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=1468622B6D196C3D9CD02CE7308B76427852557AC43E3095C7C77E09CB331C27)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/wSzX-ij7SyWChgtFaiegqA/zh-cn_image_0000002538288564.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=ECEC72501F99FCAB502A98A7D6B60A0EC3B63443F030B3C882D48C4158A8AC36)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/sKrv1f9aT_Sj0u8Se0yWoA/zh-cn_image_0000002569168327.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=49834A9C1BC6523A8165F86CC2B7617CA2D0AF53ED199CA515AA04896FB30A67)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Nongj-JvS1-xvxGG02IsYw/zh-cn_image_0000002569128353.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=B32C56E4B3BEA1AF88341FA2B7E67EF3CD64A56EE74AC64723024DA776724B62)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/TGr6_w8FQWG2y7Dax1ByGA/zh-cn_image_0000002538128632.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=FAA47166200193BFF28F9BDF5AD045479B81EE655EF61556BBFDE63909875FB4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/pkpyaWdORVGD_sSkYhO6jw/zh-cn_image_0000002538288566.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=1C369EB1E0A4523E011992906473F3351E6DD951693560F9670EDEFF72F5B9D7)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qQFqwn0WQe6QnrgqFxZ-pw/zh-cn_image_0000002569168329.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=C24908F163F7613E436480FB1F1F0C303F20F9081887B0D3EF724D6807451D4B)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/uNstFSdBSle000yNIDT0JA/zh-cn_image_0000002569128355.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=275E61CE4E7A66796CAD64273AEAF119597CDD72D966B4E65959F0732D3738AC) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/fcFtGk_-RyqFG2nBZnZDjA/zh-cn_image_0000002538128634.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=521F5CF0AC7A37EE3AF2BB86BCE0ABF83BF52E5754B4102134BD9B53D4B5C427)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/D3ESBcpvSG6Is9VlFBRTrw/zh-cn_image_0000002538288568.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=AD44D7917E2BB8FE967B7D0E0FABF9A4878536B97DC9905AED9CDC7B2C80B6EA) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/7IGEDM-XQ46zivwtmD8SGA/zh-cn_image_0000002569168331.png?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=21D24BCCB9E8B3EB7B64B6385AB8C65209CD3C47938AD2CABD6DEEEBF093EFCF)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向  .scrollBar(BarState.On) // 滚动条常驻显示  .scrollBarColor(Color.Gray) // 滚动条颜色  .scrollBarWidth(10) // 滚动条宽度  .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ClLUzZmLQ7ePoaTIG_Dpzw/zh-cn_image_0000002569128357.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=1ABAB72DFCCE93213B0E970E636A2862F2738282482A4E0383FCC7EA076040A8) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向  .scrollBar(BarState.On) // 滚动条常驻显示  .scrollBarColor(Color.Gray) // 滚动条颜色  .scrollBarWidth(10) // 滚动条宽度  .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/iMD-V6oVTp-MhdLZYnrUdw/zh-cn_image_0000002538128636.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025248Z&HW-CC-Expire=86400&HW-CC-Sign=6D7FC405C8AA00D0619AC933749B52BDF903BD4B679A02FC7E8FDE4D1151B4B8)
