# 线性布局 (Row/Column)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

> **说明**
> 在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Ki209M5FQJ-LXlo0fQTcog/zh-cn_image_0000002565290113.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=902A27A8E6CF98FD90D13EF7B38D10248FA1B6DFCF8924C4AE85070BA97C59F6)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/kbx4DNNkTBOiAWAKj7B1Pg/zh-cn_image_0000002565210093.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=34C3ADAF1A11A0EF747CA83D7DDF5C854DC48363961E38DF89564243E174E613)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/acDdjGObQkOimZZkFrn33w/zh-cn_image_0000002534250270.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=7E45EC08BAAA0413F205F0C9EAC47CCF3812654BAB061F75E62AC125CF2E7232)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Lcj60nk2SWO0OwKDIxX9Pg/zh-cn_image_0000002534410216.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=5C137126143FB89D2A8B9FFB0BCDE36F9AC4F25F92BB060AC28BF620E121C6B4)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jWsO-So2QLq1afMZaEAB-w/zh-cn_image_0000002565290115.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=336BED1C39E6CD729B48805AE0BDFF9756B8385AC38755D3028AA0C0E21152C0)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/r_zM-6gPTCCb0GEUrlzM_g/zh-cn_image_0000002565210095.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=F56194B9A92C781CF5B9B0D8066AD8A4FA1C31122A526A2950CE73935D06CED3)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/pioQb2rhSteHEnk11zdJsg/zh-cn_image_0000002534250272.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=A98C160F529D45AF00185B4B5FB6EDC4CA233C0F9CDD5A0CCB92B4B6EBC705E0)

- justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/BueN-n2VQrCywc75IQICSA/zh-cn_image_0000002534410218.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=E25DDEC14B89317D43A18C99B1E5AF43594F8C34CC95BDECB0457A7566EC7A32)
- justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Swhour3lR_qD2oZDqdgnAg/zh-cn_image_0000002565290117.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=D6D0FE4E67D4426BE983DB53E0F14749EA7E5AF952FA34CE1878B0E073BFBD15)
- justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/KWevPbfnQkSwLk7uszEn7g/zh-cn_image_0000002565210097.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=2D6C400E7B6A6A223398E8CF9C623A70C7B99EE33E5C27E2E004C1B7E7374183)
- justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/eY_vwaOZTbGIYi3sTMkfmQ/zh-cn_image_0000002534250274.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=CE14760F8FC60D8F5F463A827164547EAEA9B6A4023F0828A7D69C6A8CFA1A1A)
- justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/JbqcQTvmSGWAKpB20N9ZrA/zh-cn_image_0000002534410220.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=1535BEB722A704F5993E3B6D5EFAB47D3F91B5C53C3849AC35315A76EE9FF3C2)
- justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/7ajTYI-FQJu_wkkRZF63zA/zh-cn_image_0000002565290119.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=3B7395A8181457D169A2A7E5175B4AFEE8D8BA9BB9507074D3C6B1CE7D12031E)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/rBeZZhSWQ8GD7FeDriI-Hw/zh-cn_image_0000002565210099.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=42C76835A2E52DF44A92EEE4B5F1584662CC4CF1DB26B53E2EE0C21F221ECFCD)

- justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/0NOMD6qBSoGLp4jFqi_pQw/zh-cn_image_0000002534250276.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=47F812D9CD6BBACC976838339EA70ACA1FF699953AAA9739FEF840F449A3B50E)
- justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0SukhdGaQ36rzPX-zF43Rg/zh-cn_image_0000002534410222.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=DA4A4A50F23A90D5461EC86EEF0F4082D0307C92B30B40F3CA45E84201D594DF)
- justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Hoty_ZQUSPKnqMih2Wo0Sg/zh-cn_image_0000002565290121.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=847B4B1DD40B1D5DAFEB1FC3E2646FDB010B9D073322F8C422FB6BE9A32642ED)
- justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/LfAD4Z67QdS5rpxxU7IeRQ/zh-cn_image_0000002565210101.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=64E2E2BD5AF66FFF3B03FF7A52837A8265686AAF7C884643D35087FD09CFD670)
- justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/3okV0dxnRECYY96SCUnrlg/zh-cn_image_0000002534250278.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=9299911410F7A2152BA562E983FA3AEBA538A3D904D4923B57CBA9EDE6342E6A)
- justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/BZb1bn5CRfC8Z8dSmZM2OA/zh-cn_image_0000002534410224.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=22ADF3352985391CA35233DDA28E7F96C51375A51562A7D92EBDE9DC4CE759B1)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/D7GVJGkIQWSFvcLZv3Ha4g/zh-cn_image_0000002565290123.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=0A841D607ADF90B330EBD8CE77E6616D714B0C7B77959B267DD128E53DBA4048)

- HorizontalAlign.Start：子元素在水平方向左对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/BH_S6eZDS2G70ILWT0tSmQ/zh-cn_image_0000002565210103.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=7AEE512308C4B7F5A9B8285E0EF5E945385453EC49FCC3E6A73398237CEEFA0D)
- HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jVKuW524ScOALwKmoU49mQ/zh-cn_image_0000002534250280.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=D9571E5EC281F942817376C1C6173A52687240D454D4AD4576240984A01C3B12)
- HorizontalAlign.End：子元素在水平方向右对齐。 ```typescript Column({}) {  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3)  Column() {  }.width('80%').height(50).backgroundColor(0xD2B48C)  Column() {  }.width('80%').height(50).backgroundColor(0xF5DEB3) }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Rm6eQFUQTuaOQKael3VsUw/zh-cn_image_0000002534410226.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=74D816CC5AFA7312A2840B63B3C7E8789CCAE0CCE9DCE10B967071322545E171)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/B5stXtF8Qp6BL--8JOAPGQ/zh-cn_image_0000002565290125.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=84F167784CB3555053591F328A6365F0CBB74EED4C399DE391400FED6C334D0E)

- VerticalAlign.Top：子元素在垂直方向顶部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9K5ip4kiRVC8LQodAh9row/zh-cn_image_0000002565210105.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=4CA067960B4352D18FF4F49B8AAB66423C68CB11E84C21A96DB541EE36539137)
- VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/Q8WqzTD7Q5Ge7vuA95Hrww/zh-cn_image_0000002534250282.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=44BF41AD324566CD68F59D4DDD19C24AD774B0CD2CAABA3BCDA2BF6C2D92F1A1)
- VerticalAlign.Bottom：子元素在垂直方向底部对齐。 ```typescript Row({}) {  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3)  Column() {  }.width('20%').height(30).backgroundColor(0xD2B48C)  Column() {  }.width('20%').height(30).backgroundColor(0xF5DEB3) }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/U4LjIcOkQ_-F81K69yXV_A/zh-cn_image_0000002534410228.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=AA744169EFEC89DB8753D84F2AE75E42787F29F3440819AE45FA9A17E357B080)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/bvPF_AKqQsmQWAPcgVbotw/zh-cn_image_0000002565290127.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=0DAE9440DCB593A1443AF55845B05685888D0019F4CE4918178F66FEFD435D82)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/-ZvaaDgCSNahZQ04m27mxQ/zh-cn_image_0000002565210107.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=4241A312EEC5DB9159EE8E77BB74585DB26EEA87441A524A5B47406B49CC8035)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。 ```typescript @Entry @Component struct LayoutWeightExample {  build() {  Column() {  Text('1:2:3').width('100%')  Row() {  Column() {  Text('layoutWeight(1)')  .textAlign(TextAlign.Center)  }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  Text('2:5:3').width('100%')  Row() {  Column() {  Text('layoutWeight(2)')  .textAlign(TextAlign.Center)  }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('layoutWeight(5)')  .textAlign(TextAlign.Center)  }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')  Column() {  Text('layoutWeight(3)')  .textAlign(TextAlign.Center)  }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图11** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ga5MGdkmRZiZoaEPT0iUKg/zh-cn_image_0000002534250284.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=26C415CF0B3EEA49B9396C4AA55BD3F433B6504226F1D6A472839FE26A7AB588) **图12** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/nbrAqzfdSdqxR-pq45m5ew/zh-cn_image_0000002534410230.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=2652C47C323FD9FE4B0F65C99A797B527E6DC7052F93B404591AF23CBD7D2DC7)
- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。 ```typescript @Entry @Component struct WidthExample {  build() {  Column() {  Row() {  Column() {  Text('left width 20%')  .textAlign(TextAlign.Center)  }.width('20%').backgroundColor(0xF5DEB3).height('100%')  Column() {  Text('center width 50%')  .textAlign(TextAlign.Center)  }.width('50%').backgroundColor(0xD2B48C).height('100%')  Column() {  Text('right width 30%')  .textAlign(TextAlign.Center)  }.width('30%').backgroundColor(0xF5DEB3).height('100%')  }.backgroundColor(0xffd306).height('30%')  }  } } ``` **图13** 横屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/bE0SXL-iQcy6HDW278s2kg/zh-cn_image_0000002565290129.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=461325B547A6904B9027AEC182C3933EF2408278DB30381834A3819C6F7E8060) **图14** 竖屏 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/1U8ozqOKTY2zXu6s1Btzhg/zh-cn_image_0000002565210109.png?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=A349C73DAE21A2E87544BD14223DD3DE7C105CCEC04A3E3A842DB9B957C075AD)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

- [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
- 使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。 垂直方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollVerticalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Column() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .width('90%')  .height(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ top: 10 })  }  }, (item:number) => item.toString())  }.width('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Vertical)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/v9Xpw_JmSp-brybo_odjpA/zh-cn_image_0000002534250286.gif?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=87D7F40B387C6D7D8B3C057EFE4991B78B1ECE1176B2B5D11F7BC0D84F2E578A) 水平方向布局中使用Scroll组件： ```typescript @Entry @Component struct ScrollHorizontalExample {  scroller: Scroller = new Scroller();  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];  build() {  Scroll(this.scroller) {  Row() {  ForEach(this.arr, (item?:number|undefined) => {  if(item != undefined){  Text(item.toString())  .height('90%')  .width(150)  .backgroundColor(0xFFFFFF)  .borderRadius(15)  .fontSize(16)  .textAlign(TextAlign.Center)  .margin({ left: 10 })  }  })  }.height('100%')  }  .backgroundColor(0xDCDCDC)  .scrollable(ScrollDirection.Horizontal)  .scrollBar(BarState.On)  .scrollBarColor(Color.Gray)  .scrollBarWidth(10)  .edgeEffect(EdgeEffect.Spring)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/zPYSge-uTaqtZ6u4__3oHw/zh-cn_image_0000002534410232.gif?HW-CC-KV=V1&HW-CC-Date=20260331T024024Z&HW-CC-Expire=86400&HW-CC-Sign=6FABC5AD5D88C48FDBC7378E239F812DE509AEA9F63F5733F859F911DF9A137E)
