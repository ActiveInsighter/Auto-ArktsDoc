# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2kDCh7CRQd2c9RHiV4K33A/zh-cn_image_0000002533065768.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=4D9A891E77E9CC0FD43177ED1E593D7BAC9E0DDCBBFC7B956EBF4F007A421F95)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KVAii1ufSx-bTC91qvVSUA/zh-cn_image_0000002563865671.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=2552D4DAD901F17B8C8F8CE710B940C3595DD0346B22E7BB9BBCB686F01E95C6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/D21NY5gRTLuE4xGjp1FSxg/zh-cn_image_0000002563785717.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=31E10EE87B2795EDEB0BEDFE19FD0FE15D88A807DF75463C274AA0806DC604D3)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/QlKU6i6nQYC5g4VfHgpn1w/zh-cn_image_0000002532905822.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=B6CA274700597A96F3926CAC24EFBA6BD0BDCE282D5C3186D01539F63BB02AF9)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/K9h5auCTR56UKh8sq-tooQ/zh-cn_image_0000002533065770.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=EE4254B84379C6A0E43E5BFA07FE4A9FA66678D2DD333F196502B715A6172236)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Q1nG2SLYSpSKFkJBnlzF_g/zh-cn_image_0000002563865673.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=F8688797700A0609DE2B599D18F71A8B6CF61FEB8F2A41F9AD94B50BE975A4C5)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/NHSJpvh4SjSx6ojQ4O2mDA/zh-cn_image_0000002563785719.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=5567BF923C5183E735C26791A4C35300CB09ECDC38DE08F2958755C921B788FD)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/xrY7nOCYRh6hhkmvcpHBIA/zh-cn_image_0000002532905824.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=47C2A0BC5244B5C3DBA1761B06D37B8D0032CC0BE87D6614CDD989397206E109)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xGznUek8S5OrLCtfsHRpvA/zh-cn_image_0000002533065772.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=8B12770F8E5C297C49D88E89360FB23097D0ACC40B0422DD8FCFDAABEE6B02B8)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/0189OcYlQCyHHDQBLhqEmQ/zh-cn_image_0000002563865675.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=4B7967DC14851508596A3881E40238A4F03205277AA3EB75CEE8C9E1D0273DF4)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/uraiwTPoRPuyTjHw0k1rkw/zh-cn_image_0000002563785721.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=8CC8B95A459FB2391D3D053B07461EDD374385A866DA6BF2B56CBB58605D6CBD)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BwKA-RxeSLOhlzB48cw41w/zh-cn_image_0000002532905826.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=4B7AD133E4927129BDC3AA15160BF9F512D08DCC02BB801E6599B8A4F68B0DB1)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/1Y3RdVbHQ0S_pgMasvHQzg/zh-cn_image_0000002533065774.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=89C6781B0F0FAB3F5602A5AF1BDB5AADE3AE23606D21F1DBDEA2E7219427D591)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-NZO93ovSKWW_3b0b25KGQ/zh-cn_image_0000002563865677.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=11BA37D377473D6A9502273B941192C1051685A70C8E3B4135002422CEA47EB2)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/PXeZlwzAQ6yKKbyhUyB-7A/zh-cn_image_0000002563785723.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=E216E2006C0F1DF4677FCDECB4D07161EFF3B789E8AEEDD63DBB7F42908EF050)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Bre_MGGuRGGpps-pFtX3aw/zh-cn_image_0000002532905828.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=ACA93B9BC80CD50DEC6B26D8ED18D4777180F5985B7279E12D3FC940CCF47B19)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/aSFiu_mtRN-aTAgkz3B_KQ/zh-cn_image_0000002533065776.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=AD50E30923546C7574E936B3AC809DB07548D406E2EBBEF0986F949B200CD7D3)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/bznWYxisROKEzHOPpoG7MA/zh-cn_image_0000002563865679.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=A2D0759A53C3D0DDD973172125C353F381074BFBBAE81DAF94F9ECE5D14260A5)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/_3LP6XEfSriqUnHfAjCftA/zh-cn_image_0000002563785725.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=6DFFD84CA3E209FED08320A6F7A1D0306AD2FFE1984F7DDBE5BB1387520EBE9F)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/encSzqJJRiCYuPsnY_0rsw/zh-cn_image_0000002532905830.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=06DDAB307DD76CA664D43DEC487F9ACBD040BA6AD9F5FD43D3D3DAE2C8B5276D)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/vh8VwOU4TLSvkxMKUK_yuw/zh-cn_image_0000002533065778.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=0D16EF80E1D0D60C3A81B7EA4A200B15A509F95783A04999E8923AE5C27A6AB5)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/A8MA4xqVTbKvLd9FriHqEw/zh-cn_image_0000002563865681.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=6F51AECFC737EE86ECEAB1BCE1D5D3286DD2966DE68F8ABEA7FB70D9DCDAF47D)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/fC-g1K4OShOFjfG-zWQ2YA/zh-cn_image_0000002563785727.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=0C718BC8D9FDAF7DB7F61B0B3AD47FF2C05BD83947726059407446E357A8AEF6)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/3kbAzY7XTlCt3HGhxsTOHw/zh-cn_image_0000002532905832.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=EA0180B52766C980EAE291FB4C814241B6EB89AA6383B8BC2B9240691BA8005C)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/bddDaCClQjyfqVTFNnwlfg/zh-cn_image_0000002533065780.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=EF1B970602A398038CC9A1609A9762262C432E61A156E8E563CA537073B8D447)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/4bXtGpF9QYCPgoYtBZ275g/zh-cn_image_0000002563865683.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=1D3ADCA53F8218D58F80A8E560B75187933A003A2DFCB8E85FA7E3F29FB1ACF5)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NRYsAuiaQmikpzMiwriR4w/zh-cn_image_0000002563785729.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=C2BC5F679B388E94DB9FD8963A8911B386F5EFB9FC92B6890A01007E9D1F8FB0)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zJzaKxwzTXyCn_Z1QcSsJw/zh-cn_image_0000002532905834.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=A3FE4EC088ABEEFAEFDCAB8CF0AC41EF854BE02A3BB74F4EB08670ADB3DA10F6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/_UCCmaJqRxaBiErx49WHJA/zh-cn_image_0000002533065782.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=DA3FBD65A07A790D6DE69ADD6ADDDA77055702AEB5DF9003A31ADCD1B52FE497)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/DWsZS7sLT-OD-s4HPSJO9w/zh-cn_image_0000002563865685.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=E21971F080A9725485D851394649A597F96211CEAD6A168CC7C70080B095FA74)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Zbn96dLfTwKSxGLrIaeXFg/zh-cn_image_0000002563785731.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=C3B5BF74DA47045DD832106F145FD7A8D13B32A274CA7ECF60E1E50B419BEB92) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yU6tUNUjTO2svPXE1OlJQg/zh-cn_image_0000002532905836.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=C44D9310F397462B79EB1C31EA24569E8D887CB0D630DE9F157A1EFE8A437968)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-OZWkKiJR2mj9MnC2mwffg/zh-cn_image_0000002533065784.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=4FC3CB99E4503EF4FCCCA1F39948B5E9940496CF14746064C209B11B093D78CC) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/3AZzpvQ9SWeTxjmybjhX9w/zh-cn_image_0000002563865687.png?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=020D206BEC8E20AACF65D047137687763AB865559FCA98DDEDF814D57AC01166)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/v7BIM8M3QtG7dVVfzJin7g/zh-cn_image_0000002563785733.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=923924BA7A984FBC178C4499B276B02D9BA0F6DA2DA5C5118296B904A224C66A) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/IFmP0kw5TsibVgJ05Ia46w/zh-cn_image_0000002532905838.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094825Z&HW-CC-Expire=86400&HW-CC-Sign=6537F3E707548187D88F765A154D141F3DFFBCBB82C894E84857D8D2CB0B93E8)
