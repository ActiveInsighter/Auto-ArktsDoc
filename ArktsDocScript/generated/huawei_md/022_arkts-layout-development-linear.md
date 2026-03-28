# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2kDCh7CRQd2c9RHiV4K33A/zh-cn_image_0000002533065768.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=BD3DC93846AF21647D15721D4D1E9355C4DD3306272B9FC57B67E7C4F2CEFC7A)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KVAii1ufSx-bTC91qvVSUA/zh-cn_image_0000002563865671.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=4179922149B49631316F94915173DEDC3F6CE191741F8219BD418EE208BE25B5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/D21NY5gRTLuE4xGjp1FSxg/zh-cn_image_0000002563785717.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=9561C4C225365139E1B11144F0FB63F060F1F77EB4A7DF842DAE72ED22ACB972)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/QlKU6i6nQYC5g4VfHgpn1w/zh-cn_image_0000002532905822.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=8A3405D92FDCA2FF8ADF4FE88501A717B60868B85FAEAC0CC5E7C6D7B913688A)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/K9h5auCTR56UKh8sq-tooQ/zh-cn_image_0000002533065770.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=E4FFF9EB2C1E9A71E7943353087C308D51608DA70C97F2C3CB4A0816D7883A25)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Q1nG2SLYSpSKFkJBnlzF_g/zh-cn_image_0000002563865673.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=FDB898328A70D01BAA518F05764C97FDB085CD2C8D60C86D258C2DDD25739801)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/NHSJpvh4SjSx6ojQ4O2mDA/zh-cn_image_0000002563785719.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=26740A26CD4BACC6EF5B26488CB0BC84CF294C0783D10D6F0BA186596B18022E)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/xrY7nOCYRh6hhkmvcpHBIA/zh-cn_image_0000002532905824.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=B71DF570BD653E7E28862C1B7843A2CCB1CB11A9D62072AFC65D803895B71367)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xGznUek8S5OrLCtfsHRpvA/zh-cn_image_0000002533065772.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=DE72C9383E77D5495A9A21CE4CB89FD1B1236754EA30E8BD43682AD2E6F7D442)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/0189OcYlQCyHHDQBLhqEmQ/zh-cn_image_0000002563865675.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=89A2D59D87D4E6DD5AC7A4E6DC5A7D76F33DB0E0A93241B033FAA8268AA7A924)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/uraiwTPoRPuyTjHw0k1rkw/zh-cn_image_0000002563785721.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=775F1EFD7F27E1BBE3BE7AD88D060316D963D035CD2308473ECADC3D20A73F08)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BwKA-RxeSLOhlzB48cw41w/zh-cn_image_0000002532905826.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=248631FD94C026CF384E80F5B95616CD1ED9E3A24395E2A95B85EEE0496EF8F1)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/1Y3RdVbHQ0S_pgMasvHQzg/zh-cn_image_0000002533065774.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=F610E325607387AC05001DDBACF7E14283FE1F5E28E278DEA5B8E207967561EF)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-NZO93ovSKWW_3b0b25KGQ/zh-cn_image_0000002563865677.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=23B7B9CCE108AAC069FC4825C33626983096E89E250BC82F9335F5AA708864D6)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/PXeZlwzAQ6yKKbyhUyB-7A/zh-cn_image_0000002563785723.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=BAF3AB4A7BB072A9263235D07121F0D35C1BA908182552AC0531863CCFE26DD1)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Bre_MGGuRGGpps-pFtX3aw/zh-cn_image_0000002532905828.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=D323FFC549DA48DAB0D47B6AFDE22BF762A260A7D3AC45C68A60661963C9B5BC)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/aSFiu_mtRN-aTAgkz3B_KQ/zh-cn_image_0000002533065776.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=78CDF9735FE47AEB68D32669A3149E3C3AD3F52C152C4FF61A1CF3844B85547A)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/bznWYxisROKEzHOPpoG7MA/zh-cn_image_0000002563865679.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=9CF23459AE7097745481056666B29400811C7751DACDBABCB6E345401D117BB5)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/_3LP6XEfSriqUnHfAjCftA/zh-cn_image_0000002563785725.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=749369CE7B21D055B252DBDF79B7687AAA00C13F4C25F631529CD8C29C00B2BC)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/encSzqJJRiCYuPsnY_0rsw/zh-cn_image_0000002532905830.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=E03C0B93535EDFAA6B29CB4DA60324E2F893082428361B42876BB2537E0BEC7B)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/vh8VwOU4TLSvkxMKUK_yuw/zh-cn_image_0000002533065778.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=06288AA91910AC2ECDBDB04E30A2AC99CFF86617EE5ADC44927A77C66123B123)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/A8MA4xqVTbKvLd9FriHqEw/zh-cn_image_0000002563865681.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=70E697B52A50FAFC86EE21FDC339D3F01874FB4029CEE4054C04FB61E33796C9)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/fC-g1K4OShOFjfG-zWQ2YA/zh-cn_image_0000002563785727.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=43CD8267E5686FD1A60358914D77ED548F2085A520118D312A017BC21A541151)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/3kbAzY7XTlCt3HGhxsTOHw/zh-cn_image_0000002532905832.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=556C7D34307ACFC25F72FE6A80C83CD302593CFBD1860E4514C1D2D69391132A)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/bddDaCClQjyfqVTFNnwlfg/zh-cn_image_0000002533065780.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=743DA9653FDF51751CCF1387C302ED15EF937DB4011E391D633A8F258E9D095C)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/4bXtGpF9QYCPgoYtBZ275g/zh-cn_image_0000002563865683.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=5D7E075A35FA2D329C0A4C87B1F88293D88BD6D5C3945FB3E1099378D0FD28D9)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NRYsAuiaQmikpzMiwriR4w/zh-cn_image_0000002563785729.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=0320E0954A1089EAD607321AFDE907BB3403563115A6C50D6CBBFF9A5DF6787F)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zJzaKxwzTXyCn_Z1QcSsJw/zh-cn_image_0000002532905834.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=4F4BC78E72F5EEA4A44B9ADE1D83E099AFA1F2094322337DB6664BE99BF68A2A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/_UCCmaJqRxaBiErx49WHJA/zh-cn_image_0000002533065782.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=E66897CBA3EF9ED20530F666532BC55755C0032ECCEF4C8B5045CD4BD2CE094C)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/DWsZS7sLT-OD-s4HPSJO9w/zh-cn_image_0000002563865685.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=F97695EED57AFB606C085ABB294DB321FBCE6285A0CFA631614268C45F921D1A)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Zbn96dLfTwKSxGLrIaeXFg/zh-cn_image_0000002563785731.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=1DE5B5CD52585E235E62E6FEE84A925E236145679A2AD2923408D09B4EE6E3BA) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yU6tUNUjTO2svPXE1OlJQg/zh-cn_image_0000002532905836.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=9E728F17D24C7CAA5C18DB77CD48F9F8F18B4691E70885531E9274EF8983995F)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-OZWkKiJR2mj9MnC2mwffg/zh-cn_image_0000002533065784.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=66527ACD7D3FD8750114300F40578AEA36A942175823B60CB587E84BD11E807E) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/3AZzpvQ9SWeTxjmybjhX9w/zh-cn_image_0000002563865687.png?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=B16CE662CEADCFE15774B5D1D494699C775FC60E68F1D57B168238A53341CE14)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/v7BIM8M3QtG7dVVfzJin7g/zh-cn_image_0000002563785733.gif?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=BE9075BC219411C5881A4DCD353CB4139277EB02C28B8A55A1A3693382AFF4ED) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/IFmP0kw5TsibVgJ05Ia46w/zh-cn_image_0000002532905838.gif?HW-CC-KV=V1&HW-CC-Date=20260328T143308Z&HW-CC-Expire=86400&HW-CC-Sign=4DC7B07BBEFE32C4B87A10687ADD9B70B916381033D26AB7E4AEFC4A28E88A61)
