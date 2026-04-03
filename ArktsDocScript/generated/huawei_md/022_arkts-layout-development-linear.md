# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/6NaZwmA4QZ-RGWfLBnNznA/zh-cn_image_0000002566019097.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=8AFC7A6A48A69450EC2FA820083C8A718E32940DFF78EBE17CF8372586805573)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/P4gU1FqvTa-LnBi8X-oNJw/zh-cn_image_0000002566099109.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=8B06A75575E6207890C97F6891C444B0D4046220910E1C4A009A1D5F2979FD37)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/EbI7upElSCariKxd592W2Q/zh-cn_image_0000002535139298.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=CFCB184B1604B5BF7C3693AF453EE1DFE23E5CEDEACAF2DA5B1CC0B614C95779)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Ymj6Dq7US46tvCPnOStOvA/zh-cn_image_0000002535299236.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=A5C9F6EC641F5A5847BA9C78ECE2A5359B1C1F26E268195697B1F2D59F11E9EC)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ryNyIFvnSVaV9GpM28BXWg/zh-cn_image_0000002566019099.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=617054FE72AFDDC72EC18BDC7ADE25AE8984EAA96C4FFA4811AC0E6AC9D5040D)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/rkVziIJ6QLWloEZUXb9GPQ/zh-cn_image_0000002566099111.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=5A7D786D44D24A3EF6693035A81FFCD6508B392A5E147873F130F0961EE2FDC9)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/MZy2Uqs7QUG2LRtoE9R15g/zh-cn_image_0000002535139300.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=F0F53A77E8598A5BC28BA42A7580266B3705C94B161074D295D2C14E83ED16DE)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/rkbAI0PZQdeLoKNoZvoYDg/zh-cn_image_0000002535299238.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=5EA9A77909C736B3CF668EF6319D5EB2ABC594D0D824F8FC9538E2C4053B1D66)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/j6JR9_f4Rh6q2A152ElLqw/zh-cn_image_0000002566019101.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=1AAAF4F6E29EA45B29BC6824676F4F62C2522EFF89B6C7335157375DF3C0E0BF)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/GnE8L1i7QwOzYVQWuaKcfQ/zh-cn_image_0000002566099113.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=B119BB4EDA02BB4E1759866B657DD7609B9EE94783CBAFA50E7069CF2B774849)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/v0iuZGLcRs6EQ1Al980naw/zh-cn_image_0000002535139302.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=B2347428AE98E122731542FC13F8B97ADDEFE9EE9090E8529DA9B84EBEAF5D8D)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/NGbv51I-SUaAtON-IxRi6g/zh-cn_image_0000002535299240.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=00089DE2DA43D5D6154C396BC6B043AF0626A5D0B090F72D97CD70CB48B99070)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ySbVdrONSXy2uAL7aoVoJw/zh-cn_image_0000002566019103.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=1C600B5A459809D387D4BCE835C5875252DE9ABB7EB49301D55E1E76376BE5EB)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/XggoKEjoS4KguIFInYpCuA/zh-cn_image_0000002566099115.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=F44B6DB4FB7035FD00E3667F40574AE62DC9F0CE242A99882A51D39DEA3E5847)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/C68DqtFrRqagDyrUj2iudw/zh-cn_image_0000002535139304.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=C251D0CB9677D14F5E499E13354A6FE725EF20E29709BA65EAC73823AB39F967)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Depl9PHfR32yFfoXrKfK0g/zh-cn_image_0000002535299242.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=9C3A162F56D76169AC3B8DBFDC0919AFB45131C44EF640EF4B55F9CC3B68F6BA)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/A2bCoNW2TfS3yukArocxEg/zh-cn_image_0000002566019105.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=96BDBFCFD3C5182540FEA022FC94F7ABCDB5615E0CDD90D162CBA95AA712AD3F)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/b3MpNhvKSuukt3BEPnU99g/zh-cn_image_0000002566099117.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=1039E8987C27A2E60EE337CD7D43174EB520DB7B2972A0A10BCFAF4DEAF1C9A8)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/FssV8HBBSTe6UaOwWRW7ZQ/zh-cn_image_0000002535139306.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=61701557DFB4BDE17A2D33C9305055C42D055A95EC465B8866DDB63EB1E24DD1)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/z_f41IxjRwu7CxsjAQjSmw/zh-cn_image_0000002535299244.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=3D7137F7048FE40B00DD51F5CE2C4B892E9274847D963555B33A9FD2CFDD57FF)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/B5iqoB8VSz2FD_dvYAEh2Q/zh-cn_image_0000002566019107.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=2CE05FDBF45E6C8B18156DD53D37C05C385F47ECCFCFB198BA2BAEF7A36B3E7B)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/glrJoCq7TwKzHweXEndgiw/zh-cn_image_0000002566099119.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=C4AEA75568EEE4256222F4DD54CFB42CC418F05DB9BC5CD177C3652B26F64833)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/j9MLgnCPQIO3cwo9xHG-dw/zh-cn_image_0000002535139308.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=9B9380684CBE0CD618FC0F2F0E3D1E1E251DE73BA1ED4CADEEECFBF5F71E597E)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/2oBqnTtxRfyBxFjwJbDPFA/zh-cn_image_0000002535299246.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=DB4BE7599D49EC8349F8DE73BB17FB50B6EBB3699A550540C7237DFF84C9EF09)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/TmNBjkNzTHCwJLgUuvPaEg/zh-cn_image_0000002566019109.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=1F31AFA5ED6A739F05F9E4EF5252E12E0C99CEBD70A19F54096F826BA9A68F6F)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/BUjjEuIKSU6X8QpbtW6YUQ/zh-cn_image_0000002566099121.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=BF93FA3D19A7B8BE42EBD4E0C21C7A290FE9480C9E89F62A5189B5F9291C3852)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Pu-VglhtRneZyDe8jY4FZQ/zh-cn_image_0000002535139310.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=C4DA6B17CCD98FBDA70A0801B0FFD6A3177670F12480D5B1BD7A9F89802E5793)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/ZzrwCn-GRFu8k970TFaCfw/zh-cn_image_0000002535299248.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=D66D37AD7D008187EB8A0A6190BA7C2174889968F7AE98EC329257321A43106C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/T74ZObSwTmCeL1ZEoa9unw/zh-cn_image_0000002566019111.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=6E5D698C01CB28E777A1851F973FC977DE1EE52FB8AF743080CDBF80F7489598)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/7NXTLG5wSAevkVhcEtwnJA/zh-cn_image_0000002566099123.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=7D8EF695E7519BB90235C4F05FE9532FB4DE9003D6CA20B4B502FC6EB9FAAD53)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/S4LHbCf-QOOy4PxPdXLxzg/zh-cn_image_0000002535139312.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=E9EA475EAA181A4C0E16D3459955F0CB92E11879759C4985DA55141F21A38752) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/iZfbcs4JQMW8JsMFZLIIZQ/zh-cn_image_0000002535299250.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=FA65B731E17563329DBD8478F89AFEF92B1DEEC96F5CAD2A91488CE4F6B9F824)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/je1TpCz2RYmQCnnY_3Lfdg/zh-cn_image_0000002566019113.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=E84D22E0A771E7BD35B51C89C3C13C17FD7E075CF6B1596139FA1CC0062E2B02) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/dzRE6-YESWipA4G3BvtSNw/zh-cn_image_0000002566099125.png?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=7274FE9213BC30398F7AE66D7EC242D1C17B541C5AF3DF561EF8D77B2C2F6271)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/rJGtu4hXTkGX_qxpTWCPVA/zh-cn_image_0000002535139314.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=7048746B216727FB8DB455967544AD21969E04BE05A5111283D6D0F9AD2470DE) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/jwWpsM0MR2quWSk0ijn9Qg/zh-cn_image_0000002535299252.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023835Z&HW-CC-Expire=86400&HW-CC-Sign=19A77CCCD3B61382235EB54E08347E97CB60933C2ADB4783F14BEDC860BC3665)
