# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/qVk3GigcS1SPxajhQcyOxg/zh-cn_image_0000002535788226.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=DB73DC6827C63B2D98C338416A28AA1FF8C30102B6C41FE09BE5FFDEE78113B2)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/gWuJG5QjT4yQu4om5TKrnQ/zh-cn_image_0000002535948172.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=6E1643B64A124ED2C72A34D24925071A4656A6F9B5953C424E5558544328BB7F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/lkhVJ4kvTLqk9qrPxxXv6Q/zh-cn_image_0000002566868005.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=58C1B163E04FD5469593C91E6E6119E44CBC89679755D6889295EFEE3CA9FDA5)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/j0L8xvFoQpibVzpqbLKF3g/zh-cn_image_0000002566708023.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=2BED06B081A2ED77CE6AE07ABE3B5E9F05227ADD8E4A921AA4E41E277D2DA65D)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/XUYZiXKbRku10GY78wsKGg/zh-cn_image_0000002535788228.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=2D9FCFF873CF4536E184DBFE392335DD112A380EA7E08CB071BD26D91596BCC2)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/qzIeP7gAT62bwDQf6p3y5A/zh-cn_image_0000002535948174.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=35E26C03E9A17E86BEAAC82A5F2BAB6E12D44360E93267C25C3DA14C02CB1737)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/sGdYu_wBT0OgeAPY7IYE-A/zh-cn_image_0000002566868007.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=8297602ADACDC013D0686B27D828A8BAC33A3AFC2C88AE310F0B3E6413D6BAFF)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/fmYzsqxUStmaWUQKteeF1g/zh-cn_image_0000002566708025.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=05223A9EAA98231406761F3FDC42376F223592469BC375FD4C440ED0F05E99FF)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/a-z7CeMoSiuxpI0Saoe86g/zh-cn_image_0000002535788230.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=BCE2C7C7D1D91F4F7D2B58F92E0DBE18D71AA471D515A40D0A2AB849E735DC50)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7606B_RERgO-YIxdqu0Q9g/zh-cn_image_0000002535948176.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=8FD10DE16C26F5964D24DAB390C6620D31EDD53E8BB627F1D19C32CA9C209190)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/UJh0UpqcQ16QnHPIiyt41w/zh-cn_image_0000002566868009.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=CEEEDF3AAD59E174638C40FBAF9073EB15DD2088D92EBF536D1500059C7A063A)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/M-kMuIM3SUuPEidwd0TRUg/zh-cn_image_0000002566708027.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=18AD3AE6F1FCC6845AB46715C07B9FB9156B846C2F3467B9C6CB4E1EBD935FA3)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Tqlc6rkTS_aIuyjYGCLaCg/zh-cn_image_0000002535788232.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=0B891C541AFBA8C785D6D1FDE4C23A0EE27C5820060C84C61A450D0B2CEA4158)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/H7c4Vn6FRe6GfV_TmF7v4A/zh-cn_image_0000002535948178.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=B658E47338875F178A7DD579006A65DCD4BC1B09567FADF88666DD583053CF39)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/b9QOjKoaQoyGKp4kXVygdQ/zh-cn_image_0000002566868011.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=43DF9AD13E1994A64DDD873DAAE18CFA9CA2713C4AB3F30905BE90A0C9535240)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/O8di_DnXRIOa3W7p8icg8A/zh-cn_image_0000002566708029.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=551F01548CCE360E8F38E0451A53DFC7773A35827EFB8B42637A8592194336D8)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ycZQOYZFSTKkG95-qui5-g/zh-cn_image_0000002535788234.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=3258F08CF0ACD068F088DB21D2852F531B6B06BE76AD0E09194A645C20E9EADA)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Q0gmn6M0QUqqQFh_iZx45A/zh-cn_image_0000002535948180.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=BAD228E44D6027766AC7185F00FCD1548801BEF185AE233AD7380CD74B01E86C)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/XJPDdfXPRlOLLvj7RcsbtQ/zh-cn_image_0000002566868013.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=78A024E6D229081E91B9D2646F18E8032F20C921B73E03510A81E78E4EB7CD48)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/p_gE8u2QS7O4AyFCa0DjgA/zh-cn_image_0000002566708031.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=C7AF4BF66F229AA9EA4625B5D633158038E9ADACA186A842B441633D06237C7B)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/x7ZHbUH7Rcam9XJvFw88Zg/zh-cn_image_0000002535788236.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=0AF6D65D54FCA83108C3731E6890D580C8181AAD687259C71C0B6E24AB5ED5F4)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SBhcHewgTK6IPEmYoOzn8w/zh-cn_image_0000002535948182.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=B09A653BAB47A55D3FDB069040D328C983F9CEEF5EBEFDCE730AB3AB03CCA475)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/x91NIM62R4OSwZKADW5MCg/zh-cn_image_0000002566868015.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=9D8581B64447C58B23BB7FDB0EC4FF8AE21FA6DCECB0BC37A239ED459BCF5B4E)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/zjKtZbyGSgq-aa_wchEjvA/zh-cn_image_0000002566708033.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=8E51E821467D4C8F2E0682FEBCEA1E05612DC9C12C45EA54E73E506494E41282)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2GPkDx88TmyPTAKWIAHziA/zh-cn_image_0000002535788238.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=A5C0D8B266A693CD231EB5D7967A28C687735F980591ED186F70B522F8CC1237)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/wIOFwA1zTNqiazHVoL9-gw/zh-cn_image_0000002535948184.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=A5183A28B1CEEBE79684709AE721F40A02D526EBF7890CDAEAB87C2A33A75E94)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/iJrWwHeiSFOuz_kYWYKPbQ/zh-cn_image_0000002566868017.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=65DC71B3628F762DABA67CE638B9951EE1DB77BD8A23EBCA84C293A26842B57A)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/mP2yLfCtR-eMzxXH5KKekA/zh-cn_image_0000002566708035.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=E07F836909FFDFCC550D6ED3755505176FE927BE1724A4567C1B47DE5477FE2D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/N4t_7_k-RdGa858Y_rkOtg/zh-cn_image_0000002535788240.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=6A5EA0920BF2D01F476EAAB4D7BF6C830CFE79D87E10E3D5DBB2668E1B8DA9E6)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/zuNvoYgUTFSGf695apcz5A/zh-cn_image_0000002535948186.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=FEB03708A57FE1D3D87FF9A047D567DE7C38A609EB5D0D18AC0DDFFC9F845631)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0xBxm-gUQrKa79CBm5erPw/zh-cn_image_0000002566868019.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=A0743A69ADBBD76A8FF04BAC4DCA8189DA26A0CD8906B2A0FD63AB78C240B997) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/OGuwx87pTTScYh1LjtKmTA/zh-cn_image_0000002566708037.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=51A1514D1CAF8B4335C499D31C5EE45B3470D8FB16F528D8B5CA20B548CC3A76)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/KTncWomnSuOW9WIa6fao7Q/zh-cn_image_0000002535788242.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=C4B70EA0BB3A2767C6217BFE7FFFE1AF390A38511C96B5534260A7D8AA90A530) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/BLpXJCeoRz2BdtNS-qoqlQ/zh-cn_image_0000002535948188.png?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=4DEEF9643BC766FA1E94FA1B638CC862538DA7FD85340C70466E6B90CFD61AEF)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/rr5w9Fa1R0urt12vAEzzHw/zh-cn_image_0000002566868021.gif?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=48C88BFCA2CE991923DE644C240C3E514B04AB10B7985F1042C1ACD3916FCE7B) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lmL-tyBmRiOcaA98URlspw/zh-cn_image_0000002566708039.gif?HW-CC-KV=V1&HW-CC-Date=20260407T023836Z&HW-CC-Expire=86400&HW-CC-Sign=318716006E68621BD588424E8135421E99CBDFFF28791D21435787B7C58A1BA9)
