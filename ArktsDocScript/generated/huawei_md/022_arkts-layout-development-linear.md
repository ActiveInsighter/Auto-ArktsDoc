# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Nv87f5k0QnWLGKfAWlcZqA/zh-cn_image_0000002568172523.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=8EFE73472DDDD7675D5A7E752679A948CEE6881311352F64ECB09B6A5E167728)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/dbLXr5FrR_SibL_nUwskhQ/zh-cn_image_0000002568252517.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=ECAEDC9BE1754BD8C6D87112171F4278419EDB7FF3671047F9CD79664D0D1B09)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/0zVu-dE0RDqTtMxF9OzRmA/zh-cn_image_0000002537172806.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=7D292B011F209A364FA9EDC85EA2D1DE99A71F296650C69C413FB07FF80FE919)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SIWiL_GxRneFnNebb0SWIQ/zh-cn_image_0000002537332728.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=E285A87A9F4BFBAB473748B8516C48195C96A695A2E1D93F1EACA68FCCB4BA9E)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/4t0lVZc3QcWzUQDMYcN-cQ/zh-cn_image_0000002568172525.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=C53165B3DD766764C3120A6419C40DB05A9C086895F5AEBA27A34C379DC88471)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DEfKdkN7QZKEEtAC9V3I-w/zh-cn_image_0000002568252519.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=6502FE792F55408C57E74713A2340D0C345704E66CACC50E74BCFF352DC44402)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/QDBrnwtjS_qzdQE6Vk4FrQ/zh-cn_image_0000002537172808.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=9B88F44F6347B7B662516957B3F5181EE62E83FBCC76048E6482B097C858C712)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/dkZsdCNeRfqv0AnIrwKoZQ/zh-cn_image_0000002537332730.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=53A03C2E33601F5BAE1DA95847CA378AD85576421645999A3919B4C15038226B)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/sRxhKDApSn-EW_py5_xoyg/zh-cn_image_0000002568172527.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=96CF8BA8D30D74CE1F601D90ABE416DA18532369DB4C5249214C945AA08577B9)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/MhPo8jlDTke_dFjqzbipiA/zh-cn_image_0000002568252521.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=99D61231B0AE8F8CE1E4CD0E2F75B45B816D43D9F1F4C97C4A27F5EEC2F30371)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/CqkKLkuuS_GoGhnC8Br30Q/zh-cn_image_0000002537172810.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=9ACD2F0254538F2D7594BDB172FAC072FA5C37BC9225F4426581AF8A8F3981B8)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/j_jtgAFASA2vGci-6bn3Cw/zh-cn_image_0000002537332732.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=AB198941164F657EC91B2D6C05874F6157E261DE2930A9028ACFC37BF50B1FC8)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/TAy7MWShQIGZqGFKB5O8HA/zh-cn_image_0000002568172529.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=5E59CC0AF97B482E1861052CEEB9AF9FD2A7C28E3AF4399023B80E5C319CE9DB)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/47rZqjm0TjC6muBD6a3Q0A/zh-cn_image_0000002568252523.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=5E407565BC8762C5595416955F69C0DAD7C767536B1E4AACB1481024149FC4C8)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lzo3EAQPSbqNmIWsc4dDLQ/zh-cn_image_0000002537172812.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=3C46E0AFE43CFFC35D46482275A3CB36A2E9E374E90167D40962CA7E8831EDEB)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/4hjXlzgmTy-waPRTA2W4Aw/zh-cn_image_0000002537332734.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=F5A1B0FEB41A8A29F10F24B64156DDB2E1BA2B32C329B42DC3D1C18A86E98D63)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/L-dpLQunTV6qekQ7iaRdGQ/zh-cn_image_0000002568172531.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=170F3C9BB8FDE97464F97D70EC29B5364A8D3BD1BD645F08791C305F5C038FCE)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/SiSsPWP3Qy6AeKq9vTjiFg/zh-cn_image_0000002568252525.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=93EBEE909125B9980CC1CEFE0B75087074C7AC705821837877FA08B975F9FF13)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/if5Xk6kQST21OudR1ixYew/zh-cn_image_0000002537172814.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=2B0BA9FCF73256E978742D15EF1DD1AEB9DAEDD58B3035AACCF1EDBC5F3E2C57)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/sUUADssTRLC1aYI5Mpfk7A/zh-cn_image_0000002537332736.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=5ABF39DE8639BB73775C895D8561F69DF8BB2C960BD64C1AC64E5B2B8D8BCA53)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/zO6kDFmgRr66RuoM_nWXdg/zh-cn_image_0000002568172533.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=00CFBAB25D743821F80B2E69ED3947D128CEF03B72E1C016F308D7D9FD0177C3)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/TKjkBNf5SHS5uSXFcft8TA/zh-cn_image_0000002568252527.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=D8DB86B5E1294E2BEA454497E87263174B0D23CC9F5BA91C73A1D23DC7F252E0)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/qzwZ1-ciQOiNHr_4XzO-Uw/zh-cn_image_0000002537172816.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=27022106D241F3EA1CB248F3F4EAAB19722F9062CB5DE63F3945C68B643FD850)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/kPw65zENTKySp6LC5WBaqg/zh-cn_image_0000002537332738.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=E3761CFF6941882F816FD311C3A62A80DBCF45C7AF69F5784208E3A8713B8F12)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/P_mmObwqT-WW-vvhtmDyvQ/zh-cn_image_0000002568172535.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=FCE035C879BFDADC8F2EBFF27A02331A75A12A13C58C87983A5FB83EDC6855BB)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/fSctByJGQ2K8SHsPHJKvmg/zh-cn_image_0000002568252529.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=34EDAC7CB6235EA305B8F70B4983892F3A12D9E7FDF18A1DF2E5F318CE83D9A4)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/-Ztg3V8qT5OYXwpSqaKXlg/zh-cn_image_0000002537172818.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=AC181FAC526CAE8867FCB59FA13883257A405AD8F406F83205D29B5372F69F7D)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/UTvTt4UNSx-_FK2-kUCJmA/zh-cn_image_0000002537332740.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=9DB1C7FFE66A9EA52D7A474B94D40B1FB9C49294C89EB5652EAFD24AE394F614)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5UxhgH90SCKguUbu9eQeqg/zh-cn_image_0000002568172537.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=A715FA839F48C8C085CD5C7CB17FA2116EDA104365050B96840B36AF5DC19756)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/VIx4qyFxQTOjjcXSJMYCfg/zh-cn_image_0000002568252531.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=E9E91B764DE54BB0571C2A68598067414F10D43280B4B802F76288FF488E5D14)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3LDo4CeRQ0KQFPps6QJ5sA/zh-cn_image_0000002537172820.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=6E9CB054C610FC2C0A3DF5F93AAD95D2EC7D6316E2921C4D078EA9220D28B859) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/WhFxHA3jT-iudX-FFIxkQA/zh-cn_image_0000002537332742.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=DABD8AA0FC2E90AB5597FE43030C67F37F45C0A646C045F01C3F352C238AF8EF)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oV9Bc42VSxaQmNWW7sCVPw/zh-cn_image_0000002568172539.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=B9CAB03D9A23834C9AE5E661FDC4E5C3894B874C1D89B4CCC6C71C1D9FBDAE75) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/18He-hxhTYOlSAp1UBBHZw/zh-cn_image_0000002568252533.png?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=084DF3C2459B0D035287E4DC8EBBB9136C1551DA876028E9FA3BF14F23D85365)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/B3DvJ4o4TFOgphnZ1kFh9A/zh-cn_image_0000002537172822.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=BD803BA07448CBA41ACEE546A5E73250BA106CEBBACC3FFB167A9F0F38DA009E) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NfckZ_LaTiOYUT1F2D72LQ/zh-cn_image_0000002537332744.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023652Z&HW-CC-Expire=86400&HW-CC-Sign=AA0B8F005DA265AE97917F7D3863C95F5769FD306F38CAA3462124C453E81A8D)
