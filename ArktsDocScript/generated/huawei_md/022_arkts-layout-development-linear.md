# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/qVk3GigcS1SPxajhQcyOxg/zh-cn_image_0000002535788226.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=AE28897AC1DA050627F68F42C2EB784CDF942D336E15E7E60A6623158FC09CD3)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/gWuJG5QjT4yQu4om5TKrnQ/zh-cn_image_0000002535948172.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=BD4AC3B6C7CE84E4251DD35C4424956EDC4DAE09908B999778468B49793D9A85)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/lkhVJ4kvTLqk9qrPxxXv6Q/zh-cn_image_0000002566868005.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=161EF843BAEB7DF0CFB7CF95733330D151DD72E3FA9BB12C34D212DE62E1B3A5)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/j0L8xvFoQpibVzpqbLKF3g/zh-cn_image_0000002566708023.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=A646900C6D9AB33CD58D15CE1D181153A7843E8D9D59EC80F59928546490B209)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/XUYZiXKbRku10GY78wsKGg/zh-cn_image_0000002535788228.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=287AE26788FE08114261CA8009FE5A4D68A337AE5639E1EA2FE8EE0F136422F9)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/qzIeP7gAT62bwDQf6p3y5A/zh-cn_image_0000002535948174.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=24A9AE4A04D24C98533B0F4FB5E5389AB23A074B040F8E7948D48EA62363251F)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/sGdYu_wBT0OgeAPY7IYE-A/zh-cn_image_0000002566868007.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=6AEF9FD8473D5253CF5521CE3DB425546B5D0B3096D42329EDC6B646D86778F9)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/fmYzsqxUStmaWUQKteeF1g/zh-cn_image_0000002566708025.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=C94176FD0E18A78D6622BEC6828EE581BD85149934840F7F9220EA0DA0706945)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/a-z7CeMoSiuxpI0Saoe86g/zh-cn_image_0000002535788230.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=3BD4478E4C8EFA38A946B0989EFF12F2FF5FC02E0611CAEF25ABF7C978EEB5A0)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7606B_RERgO-YIxdqu0Q9g/zh-cn_image_0000002535948176.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=E62FFF45425454D2F69794D8E98EF1CD6216B7C0BEFD2626EDDFA103384F1614)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/UJh0UpqcQ16QnHPIiyt41w/zh-cn_image_0000002566868009.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=B141D7F8E7CBCDCCD3418CD6CEF1AB8E706CD0F1FD66E4076743096DD93907A0)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/M-kMuIM3SUuPEidwd0TRUg/zh-cn_image_0000002566708027.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=002E987E9EDBEF689613081213981181A0AF33C411903063A8DC411B8BC074C8)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Tqlc6rkTS_aIuyjYGCLaCg/zh-cn_image_0000002535788232.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=8B0D441D68843D23FAEC9CA19EF94E5FB87054DD7C7023065F33A88E6999F91D)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/H7c4Vn6FRe6GfV_TmF7v4A/zh-cn_image_0000002535948178.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=DD4DA825F00CADD7A6AE05A85C4AFECC69683964BC6C3DD810B9D5BCD92F3814)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/b9QOjKoaQoyGKp4kXVygdQ/zh-cn_image_0000002566868011.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=D4C7AB37A10222CFB71026DD0C7D5F1004ACF0E0553AC475F5C683D8529C234F)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/O8di_DnXRIOa3W7p8icg8A/zh-cn_image_0000002566708029.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=4A2343EC6F0DC29C059B6BA6CEBEA42A2680BA2642409F29D42C988CE3B9B167)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ycZQOYZFSTKkG95-qui5-g/zh-cn_image_0000002535788234.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=D4C3DCA4D8ECE34372BFA2A122B93D03A139B84EE9EF77B86601097FBCC1FB7F)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Q0gmn6M0QUqqQFh_iZx45A/zh-cn_image_0000002535948180.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=859DFA0B29DCDCE33205610F4C6328955BA4B9CD7AB9D1F45ED50B09D67B8D14)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/XJPDdfXPRlOLLvj7RcsbtQ/zh-cn_image_0000002566868013.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=D6F2DBE6D06237487683E50F43A0AB5E99B04A94DBF71C370D359C08B64DF6E2)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/p_gE8u2QS7O4AyFCa0DjgA/zh-cn_image_0000002566708031.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=CEF1B381F7B5D9BF557ACF5F4076472778B7D2BC5F840DA3406818DAA932C56B)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/x7ZHbUH7Rcam9XJvFw88Zg/zh-cn_image_0000002535788236.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=207011384C61E71B3EA2F64FE9496B5213F31E4F01DC9ED392428C054316C462)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SBhcHewgTK6IPEmYoOzn8w/zh-cn_image_0000002535948182.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=8ED171D65C65FB483D0E025AA83D130878E0444624282C6E7520BB41511400DB)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/x91NIM62R4OSwZKADW5MCg/zh-cn_image_0000002566868015.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=A7B2A35A537F0773AE57003B49FB35E760FE323D2454DB334E360300E3146055)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/zjKtZbyGSgq-aa_wchEjvA/zh-cn_image_0000002566708033.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=B6D3E13D1D8D84FC110439E0A71D25228705163D615E1E984E61FE1C9592C186)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2GPkDx88TmyPTAKWIAHziA/zh-cn_image_0000002535788238.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=8AEDEAB9A5FF8562802C4E545980A5F19F60A0F72C8FB4C73860BBE06BD35FAE)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wIOFwA1zTNqiazHVoL9-gw/zh-cn_image_0000002535948184.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=75BAEF0419937A198CD2F8333E38C274C2EDBD377F06E608EDFD715BA5ABA3AF)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/iJrWwHeiSFOuz_kYWYKPbQ/zh-cn_image_0000002566868017.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=237903822736B5486859FAF74B1A0A0F87858D737709B6BB5E528CAD9F7D9611)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/mP2yLfCtR-eMzxXH5KKekA/zh-cn_image_0000002566708035.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=3E676BA9284E08D6F162DE98BC2C2795E77B987DC512F7FA97DD1EA364E9DA6A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/N4t_7_k-RdGa858Y_rkOtg/zh-cn_image_0000002535788240.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=22D915B02D68EBEA224A54A54E56A1108B919C3493A85A5AC9930845FBE7D37D)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/zuNvoYgUTFSGf695apcz5A/zh-cn_image_0000002535948186.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=7DFF383978172CAA14840102514D86FF016F0CCC444C7DBB58396F1C3CAE0E3D)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0xBxm-gUQrKa79CBm5erPw/zh-cn_image_0000002566868019.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=14C1F4D408274715A70904198D0ECC34542FDA0D7A68CC9D054DE80CB32755CF) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/OGuwx87pTTScYh1LjtKmTA/zh-cn_image_0000002566708037.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=396E941B6CE2A2B319588C9FF9975B69FAD659E3F58601A6C1B6BC91E4CD95D7)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/KTncWomnSuOW9WIa6fao7Q/zh-cn_image_0000002535788242.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=3706B6DCC50F1D9AEEB73819BFA75D3730FEA8D2338A869EDA22F0CAD73A0298) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/BLpXJCeoRz2BdtNS-qoqlQ/zh-cn_image_0000002535948188.png?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=DAF9663F5D0F65FBA3F7DDC5ACCC586E568188F643BAD9FA1CBDEED3FC10F87D)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/rr5w9Fa1R0urt12vAEzzHw/zh-cn_image_0000002566868021.gif?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=04EEF9242CC69E42AC92F65C51BC652C0C66FA55425ACD17C2BA8F883A635FD2) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lmL-tyBmRiOcaA98URlspw/zh-cn_image_0000002566708039.gif?HW-CC-KV=V1&HW-CC-Date=20260406T024831Z&HW-CC-Expire=86400&HW-CC-Sign=6B59C247D9661BDBE882EF22ECE1A725B398D660BB2285A63B44E89D7994BD62)
