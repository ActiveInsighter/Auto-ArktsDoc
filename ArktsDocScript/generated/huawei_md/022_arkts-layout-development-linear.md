# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2kDCh7CRQd2c9RHiV4K33A/zh-cn_image_0000002533065768.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B3585592690B8D8B0A0F9E923E12D68F785D193B6CE94AD6013C90A1858AF2DB)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KVAii1ufSx-bTC91qvVSUA/zh-cn_image_0000002563865671.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=FB3DA2C0FCCE01DE423A113BB5CB741E2B426CE4A890FCD456CC9DF3D07A801A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/D21NY5gRTLuE4xGjp1FSxg/zh-cn_image_0000002563785717.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2930D673B3520303B850CEB576A4AE1004709F370B949150D71CC2A50F92D4FC)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/QlKU6i6nQYC5g4VfHgpn1w/zh-cn_image_0000002532905822.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=48422D1E5E05A254F1CFFF6840C42037C6BB03678F1B9F45207971A66EBFD622)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/K9h5auCTR56UKh8sq-tooQ/zh-cn_image_0000002533065770.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BEFC9A3DE355FCADCED6762FCA25A7C753A32754FEA721D5FD278DD0722391A7)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Q1nG2SLYSpSKFkJBnlzF_g/zh-cn_image_0000002563865673.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BF5A0E1EBF4136C9ECBB0C9DCADB4FD41AC4885C1F2D77D2BD63D495EF44BAA7)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/NHSJpvh4SjSx6ojQ4O2mDA/zh-cn_image_0000002563785719.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=757C5B38A68C47E9CAC7A5C5E6C9F54B36B1E7359EDF4D62AC4A49F23B8C65CA)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/xrY7nOCYRh6hhkmvcpHBIA/zh-cn_image_0000002532905824.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=F5C9C39AD9317485EDDAC346DCBD7AA06D567A06E23D5B979EC4487FE4387D61)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xGznUek8S5OrLCtfsHRpvA/zh-cn_image_0000002533065772.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C2825D5FAD183CAFE6AD9E84F12A5302765B96CBC01D030F4A01F9195A2770EF)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/0189OcYlQCyHHDQBLhqEmQ/zh-cn_image_0000002563865675.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2EB79533D4D8FE9DDAC69F836D16477D4222A74610B5896B0BEBC40DF741F062)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/uraiwTPoRPuyTjHw0k1rkw/zh-cn_image_0000002563785721.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=9EC5F1961C24A309929F94A187230864D9014C264FE5767418F43AE0D4A845C5)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BwKA-RxeSLOhlzB48cw41w/zh-cn_image_0000002532905826.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5001AA446E64E12B6E2027969B28109751F8343362C0D9212EF5BB8B29CB4391)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/1Y3RdVbHQ0S_pgMasvHQzg/zh-cn_image_0000002533065774.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=9FC273CDCFD0093BF7A3E2F1922927F0FA3E89AD220C0EC9B928669F140CAB58)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-NZO93ovSKWW_3b0b25KGQ/zh-cn_image_0000002563865677.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=83F4869D4F52117F545E23F584FCACF19F1331C9278B68389804F06E32796804)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/PXeZlwzAQ6yKKbyhUyB-7A/zh-cn_image_0000002563785723.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=73CD75191C68BA6AD59CA201E3390965E9E46D243B84AD00F92740A11A52793A)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Bre_MGGuRGGpps-pFtX3aw/zh-cn_image_0000002532905828.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C80FB1CD6C7875A078E19FBBE5D7EEFE6841E386938EA8817323C2D60E71AEB1)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/aSFiu_mtRN-aTAgkz3B_KQ/zh-cn_image_0000002533065776.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=6F29DAED8975EC24AFF6A72F834A09402B57117D07FC5E2606D316698DABBB52)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/bznWYxisROKEzHOPpoG7MA/zh-cn_image_0000002563865679.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=85971E7E20280A28AFC6683182290A9BCC135E9BD92052B23CEBC201771B0FB1)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/_3LP6XEfSriqUnHfAjCftA/zh-cn_image_0000002563785725.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A0143D1231E543521A151329D121FA3ECED2FEBC99DA9C8A4E5AAAE1B72F1DE3)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/encSzqJJRiCYuPsnY_0rsw/zh-cn_image_0000002532905830.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BA6B27E5D37227B6A0B17CC9970430A2FDD8921553071797129145004566D06D)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/vh8VwOU4TLSvkxMKUK_yuw/zh-cn_image_0000002533065778.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C04BCE1B1A669146090C4BB873585BBFF90BDD99372FDE633ADF36E103003B7D)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/A8MA4xqVTbKvLd9FriHqEw/zh-cn_image_0000002563865681.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=938FC730A1590DAC21F169BB3E8F61D40196ABFCE3217937358EE03E18B57A49)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/fC-g1K4OShOFjfG-zWQ2YA/zh-cn_image_0000002563785727.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=0B25559D8CB7C6DEE839893C1EAA0EB9ED05960ECF3E60282C57FFADA2DBB3E6)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/3kbAzY7XTlCt3HGhxsTOHw/zh-cn_image_0000002532905832.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=62EE0623AECC4367DB03186908F964AB5E7F774FC66F74D1F4ABFEF2C1CD5EF5)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/bddDaCClQjyfqVTFNnwlfg/zh-cn_image_0000002533065780.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A7BDB97F18ACB027824A91CFFA6708F18F486FA9DBEFB10F047A4337F1119E82)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/4bXtGpF9QYCPgoYtBZ275g/zh-cn_image_0000002563865683.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=49C447EB7C3425EE56A5C2BEDB8D6DAF1F3E0E9484AE5C80CDBB2D78DE2C4C45)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NRYsAuiaQmikpzMiwriR4w/zh-cn_image_0000002563785729.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2A24EFB239CC3414CD022D4CE5C74203B1CB4770B1EAC5D2E15C11BD83346213)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zJzaKxwzTXyCn_Z1QcSsJw/zh-cn_image_0000002532905834.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=D77BD5BB7405CDF06AEF77A55ACA0955FEB1B3D0C1669077C670E0C8172841A9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/_UCCmaJqRxaBiErx49WHJA/zh-cn_image_0000002533065782.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4CBB2752D40079D7345BFA4FD2A96E782949C30A3CF5CF51824110277BBA4047)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/DWsZS7sLT-OD-s4HPSJO9w/zh-cn_image_0000002563865685.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=93AE2C171DCA7A9B1E84B10D1F4192BDB3D6F3BCBAFEC3A26759E2E4CBA04DAE)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Zbn96dLfTwKSxGLrIaeXFg/zh-cn_image_0000002563785731.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=D58A773B01F19054A8A11C530BCFE4021F70BB14795B49A80D5791CD10A3EE0E) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yU6tUNUjTO2svPXE1OlJQg/zh-cn_image_0000002532905836.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=0DA7436F1ADD38AA48974FD3294491398BEDF11A13057532716CBD0ADD16B2C8)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-OZWkKiJR2mj9MnC2mwffg/zh-cn_image_0000002533065784.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BC923BB2452937AC9CF207A3BAB883405A65F0865335BE9E7FD9631F62CB171C) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/3AZzpvQ9SWeTxjmybjhX9w/zh-cn_image_0000002563865687.png?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2C15A3F47A38153588FEE2ED01F165486841F3FEAB3F24A642D8E3A5A6E1E8A6)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/v7BIM8M3QtG7dVVfzJin7g/zh-cn_image_0000002563785733.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4021E16B09C0D7B554135729814724D5234BB3FBD06300CE2E1DBFA140A697A4) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/IFmP0kw5TsibVgJ05Ia46w/zh-cn_image_0000002532905838.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024435Z&HW-CC-Expire=86400&HW-CC-Sign=00ED7C5147D1BBA6E766FD198E99AF7B801109220B56462FD656020329114A25)
