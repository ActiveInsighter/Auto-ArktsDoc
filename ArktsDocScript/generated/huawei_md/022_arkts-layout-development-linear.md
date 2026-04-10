# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Nv87f5k0QnWLGKfAWlcZqA/zh-cn_image_0000002568172523.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=6CCA2196437600A2D1E12DCEF090C106A00BDCA836B1DB28F089EA26C9DA58E6)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/dbLXr5FrR_SibL_nUwskhQ/zh-cn_image_0000002568252517.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=C76FDFF3ED457654401E4472E43276B4765302F70834A037BC1542EE6E4EF9DD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/0zVu-dE0RDqTtMxF9OzRmA/zh-cn_image_0000002537172806.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=BAD6042530AA8872B0D55ED6F8D74702DE0468367583727466CBC346B826037B)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SIWiL_GxRneFnNebb0SWIQ/zh-cn_image_0000002537332728.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=7A0B7881B0482ED289F1899B1EA81AB171E812A3F9333C241B1727E3889499A0)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/4t0lVZc3QcWzUQDMYcN-cQ/zh-cn_image_0000002568172525.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=A24FF6581C3D519D46C2D1FE632EB7ECD69D6BCA01B3AF7BDCE3AB7DB468E144)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DEfKdkN7QZKEEtAC9V3I-w/zh-cn_image_0000002568252519.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=5BBF3ED2E6FAD9E9EF4C9E258B9437808AC11F7A2AA300AB3B50B9098FA7B7A4)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/QDBrnwtjS_qzdQE6Vk4FrQ/zh-cn_image_0000002537172808.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=975759A9AC7F405D1FD03C47BD31C02999179894C8673B7DDBC2A29DF1F4CF1B)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/dkZsdCNeRfqv0AnIrwKoZQ/zh-cn_image_0000002537332730.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=02FB12CDF928488AB723B9214679DF664633B5026DDF919F65BE081EF01A7A98)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/sRxhKDApSn-EW_py5_xoyg/zh-cn_image_0000002568172527.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=DDB6D7B05085C7D0BC9839836C08E86A2044C256096300B6EE23276D2BE0ADC3)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MhPo8jlDTke_dFjqzbipiA/zh-cn_image_0000002568252521.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=B29D8C86387E758BD42CD170295158F48D12B52C2471750C3D195FF5BFD270CC)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/CqkKLkuuS_GoGhnC8Br30Q/zh-cn_image_0000002537172810.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=B59B929F9393CEE16ACADA1CA2FE97FCB2E500475D81BE25015DD59A2FEE5FF1)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/j_jtgAFASA2vGci-6bn3Cw/zh-cn_image_0000002537332732.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=B065DD022A6C8834D7A3691C400E05AD9848B6DE4B03F8A33FE8BC11F8CF1198)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/TAy7MWShQIGZqGFKB5O8HA/zh-cn_image_0000002568172529.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=0CB90C083703853017C15DFC1B15F8F30A8A9D6226290B2C6D574178059297AD)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/47rZqjm0TjC6muBD6a3Q0A/zh-cn_image_0000002568252523.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=8EC4FC31FFBA453B87381FFF5298F55DAAC4ED508E26F04E224477F782B3B047)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lzo3EAQPSbqNmIWsc4dDLQ/zh-cn_image_0000002537172812.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=126F30991FD04BF118925D5B81338B4E347E10EE4658C9D03E456862A832D115)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/4hjXlzgmTy-waPRTA2W4Aw/zh-cn_image_0000002537332734.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=733014CF6B9CC9DC9393AC7544047D085A84256E9F11C06F3A86925F79D6E4FF)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/L-dpLQunTV6qekQ7iaRdGQ/zh-cn_image_0000002568172531.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=B4C8E8F2CB58004F95E785214D68539244A57B63162A25C0A5F5D97228248D53)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/SiSsPWP3Qy6AeKq9vTjiFg/zh-cn_image_0000002568252525.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=FFF7BC32F73458E85C942F72AE9D293558160194D5A3FB18EEF13649875A8B61)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/if5Xk6kQST21OudR1ixYew/zh-cn_image_0000002537172814.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=935ACBDAE258D2FB86E792AC067798E50F0C173275D4767AD1812866130423F3)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/sUUADssTRLC1aYI5Mpfk7A/zh-cn_image_0000002537332736.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=64F96333B970863FB742FFC08DCB52A618CB02A52BE8C3937F9CE09E12E86C9C)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/zO6kDFmgRr66RuoM_nWXdg/zh-cn_image_0000002568172533.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=6BAA293F96B6C93FCF9D7E54D54E2656026A7BEE61B2F2FB15763F36E2145DDF)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/TKjkBNf5SHS5uSXFcft8TA/zh-cn_image_0000002568252527.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=FA03879D01A85BC79DE8408C7E327CDFB101670C2B96DC2AD5836C4398D815B1)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/qzwZ1-ciQOiNHr_4XzO-Uw/zh-cn_image_0000002537172816.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=DEC7A0488A4502AE8B474A264BF3E859ECC4027E308F15F7A5A39557AF8329DA)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/kPw65zENTKySp6LC5WBaqg/zh-cn_image_0000002537332738.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=4D0C736FB6B297AB22DCDFAA7279D1FFED5B01F08978E186E4CF8F6D20209E52)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/P_mmObwqT-WW-vvhtmDyvQ/zh-cn_image_0000002568172535.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=EB7B30E406FA6C598880A5AFD53AB796C53FC6C50CC809D45E4BA05DB9E4ACB2)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/fSctByJGQ2K8SHsPHJKvmg/zh-cn_image_0000002568252529.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=19ED213187997E02EE0E349051D9841B6D6D26ECF71D1323E45F34AD1D455CC6)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/-Ztg3V8qT5OYXwpSqaKXlg/zh-cn_image_0000002537172818.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=0373BF7AADD3BF094F2FAA117CED667EC5B8BDAC40D709C61F2A90E381FAB6B2)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/UTvTt4UNSx-_FK2-kUCJmA/zh-cn_image_0000002537332740.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=DF067A3A0ED288F136FBF454A6F2903992D9B8CC7690D89319BBAD05AEFE8907)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5UxhgH90SCKguUbu9eQeqg/zh-cn_image_0000002568172537.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=5C92D62772BD35918B76DE09B30D5935C7EA47EE6F591487AB57ADE5AEF26E7C)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/VIx4qyFxQTOjjcXSJMYCfg/zh-cn_image_0000002568252531.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=C7EEC81F0AB7D11464BAC6C114ABF0D71BDE0139DBE6CE0A670F7E03D3295AA5)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3LDo4CeRQ0KQFPps6QJ5sA/zh-cn_image_0000002537172820.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=0A747CA624D0569A6B37FE30FA3174A1F9D5F64C12522B3AAF7A529E06CA19DF) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/WhFxHA3jT-iudX-FFIxkQA/zh-cn_image_0000002537332742.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=79EEE48B5E9449A3B6432D8DEEB984B104FCCC11884E36C1A6A95A38D8294612)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oV9Bc42VSxaQmNWW7sCVPw/zh-cn_image_0000002568172539.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=A3A032AFEB8631D9F9CA6090165E38A754805654A372B7E56457E529E76C3F68) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/18He-hxhTYOlSAp1UBBHZw/zh-cn_image_0000002568252533.png?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=4768F468349A9968CE523C214EE26CAD5E6F14B3DFA495DA2FBCA64F0547F1DE)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/B3DvJ4o4TFOgphnZ1kFh9A/zh-cn_image_0000002537172822.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=FF0644469AB3F0B43F97ACD873385F9043D1204AB76D93AA6012A273383FC53A) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NfckZ_LaTiOYUT1F2D72LQ/zh-cn_image_0000002537332744.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025217Z&HW-CC-Expire=86400&HW-CC-Sign=B9704E1EC0470050103035E3272D8617E706690944AA79B99A4C754FBAAE0C05)
