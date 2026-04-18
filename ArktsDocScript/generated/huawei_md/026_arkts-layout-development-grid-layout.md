# 栅格布局 (GridRow/GridCol)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout

## 概述

栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

[GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)为栅格容器组件，需与栅格子组件[GridCol](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)在栅格布局场景中联合使用。

## 栅格容器GridRow

### 栅格容器断点

栅格容器以设备的水平宽度（[像素单位](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。

栅格容器默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：

| 断点名称 | 取值范围（vp） | 设备描述 |
| --- | --- | --- |
| xs | [0, 320） | 最小宽度类型设备。 |
| sm | [320, 600) | 小宽度类型设备。 |
| md | [600, 840) | 中等宽度类型设备。 |
| lg | [840, +∞) | 大宽度类型设备。 |

在GridRow栅格组件中，允许开发者使用[BreakPoints](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#breakpoints)自定义修改断点的取值范围，最多支持6个断点，除了默认的4个断点外，还可以启用xl和xxl断点，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的布局设置。

| 断点名称 | 设备描述 |
| --- | --- |
| xs | 最小宽度类型设备。 |
| sm | 小宽度类型设备。 |
| md | 中等宽度类型设备。 |
| lg | 大宽度类型设备。 |
| xl | 特大宽度类型设备。 |
| xxl | 超大宽度类型设备。 |

- 开发者可根据实际使用场景，通过一个单调递增数组设置断点位置。由于栅格容器默认支持4个断点，在不设置断点位置时，系统为默认断点配置的单调递增数组为["320vp", "600vp", "840vp"]。开发者使用[BreakPoints](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#breakpoints)最多可支持6个断点，因此此单调递增数组最大长度为5。 假设传入的数组是[n0, n1, n2, n3, n4]，则各个断点取值如下： | 断点 | 取值范围 | | --- | --- | | xs | [0, n0) | | sm | [n0, n1) | | md | [n1, n2) | | lg | [n2, n3) | | xl | [n3, n4) | | xxl | [n4, INF) | ```typescript breakpoints: {value: ['100vp', '200vp']} breakpoints: {value: ['320vp', '600vp']} breakpoints: {value: ['320vp', '600vp', '840vp', '1440vp']} ```
- 栅格容器通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。 例如，通过断点设置将应用宽度分成6个区间，通过columns配置各断点下栅格容器的栅格列数。 ```typescript @Entry @Component struct WindowRefGridLayout {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text(this.currentBp)  GridRow({  columns: {  xs: 2,  sm: 4,  md: 8,  lg: 12,  xl: 12,  xxl: 12  },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'],  reference: BreakpointsReference.WindowSize  }  }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }.backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/TY_UkwbjS1idkv3bl_TORw/zh-cn_image_0000002572679741.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=C30A5148338B6B983095DD63A3FDF683F55B10429FFC3C3E667981785ED4B384)

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

- API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
- API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。 ```typescript @Entry @Component struct GridColumnsWithDefaults {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)', 'rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)'];  build() {  GridRow() {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  } } ``` API version 20之前布局显示： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/MSGsyTzsQka0GoFmOW49MQ/zh-cn_image_0000002541959834.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=CDCEDBFBF2BE2D392F946E7D0180B07DDA1CDB31B7FF60D7D7D47F7EC040E729) API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/qKsYASkrTc6d7IaaQjlcRw/zh-cn_image_0000002572639779.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=5B0DF4A85CCFFA013A6262271E9FD32578942D9D6BF94D44E7F7FC54DCD0D8CC)

columns支持number和[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)两种类型, 可按两种方式设置栅格布局的总列数。

- 当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下： ```typescript @Entry @Component struct FixedFourColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：4').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 4 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ```typescript @Entry @Component struct FixedEightColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：8').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/9N5Ak6rKQN-WJzfKHawg8g/zh-cn_image_0000002542119472.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=9ADC6D8B3EE2BBD0180527505C6360987A921941CF6E92931021DF6F91B24F08)
- 当columns类型为[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。 ```typescript @Entry @Component struct GridRowColumnOptionLayout {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({  columns: { sm: 4, md: 8 },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp']  }  }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` API version 20之前布局显示（xs设备未配置栅格列数，取默认列数12）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/iWtPdJDlRUalbByL3_58WQ/zh-cn_image_0000002572679743.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=2E07F8A31927DE20154152E7802C9E47303763A42CA15C198BEEEDE304BBD427) API version 20及以后布局显示（xs设备继承sm设备栅格列数）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/kmeXlQStTRWoK4mlPJAPbA/zh-cn_image_0000002541959836.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=F0704C1763DC88AAFA1051D296BB94EED040645558394D4528BB37581BCE3648) 仅部分设置sm、md的栅格列数，未配置的xs、lg、xl、xxl设备根据[栅格列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)取默认值。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).Row（从左往右排列）或[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

- 子组件默认从左往右排列。 ```typescript GridRow({ direction: GridRowDirection.Row }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/5IUsyV0hTryTmc_gPeOqsg/zh-cn_image_0000002572639781.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=6ACF9CE3B7DBA2153743DCE1E83970325DD112AFF0FBB559C72EF5153195912D)
- 子组件从右往左排列。 ```typescript GridRow({ direction: GridRowDirection.RowReverse }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/RMvd_bAOTbuxYT6Srs7Gqw/zh-cn_image_0000002542119474.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=07F50E1CB57AC48CEEA5619C35594B998ABFC1A927F64E77C0195A42DEE20C02)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

- 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。 ```typescript GridRow({ gutter: 10 }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/uEjCXB8SQFO28US-M4gqdw/zh-cn_image_0000002572679745.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=57FFE6C79DE6E040FA0285FFC206F465ACE8B8ADC4DE538B1569E78376004AAB)
- 当gutter类型为[GutterOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gutteroption)时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。 ```typescript GridRow({ gutter: { x: 20, y: 50 } }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/LPjDYVGUQda9kGH8gqPbGQ/zh-cn_image_0000002541959838.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=BA60838D9072BA6E64A4DD527C1D9930A72637BC0C226D2F9042CC363C63AD59)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

- 设置span。 ```typescript let gSpan:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ span: 2 }){} GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){} GridCol(){}.span(2) GridCol(){}.span(gSpan) ```
- 设置offset。 ```typescript let gOffset:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ offset: 2, span: 1 }){} GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 }, span: 1 }){} GridCol({ span: 1 }){}.offset(gOffset) ```
- 设置order。 ```typescript let gOrder:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ order: 2, span: 1 }){} GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }){} GridCol({ span: 1 }){}.order(2) GridCol({ span: 1 }){}.order(gOrder) ```

### span

子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。

span支持number和[GridColColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。

- 当span类型为number时，子组件在所有尺寸设备下占用的列数相同。 ```typescript @Entry @Component struct SpanNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 2 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ND1kuxoVRv-Zngmdl2HHYg/zh-cn_image_0000002572639783.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=74A3E3661E6DD11259AABA675C37E051343265C94171A3A8F519B4C1CF182A6D)
- 当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据[列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)取默认值。 ```typescript @Entry @Component struct SpanColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  span: {  xs: 1,  sm: 2,  md: 3,  lg: 4  }  }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/5Wv6xGwWS6-XQfmzPrVXOw/zh-cn_image_0000002542119476.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=7A689DDB66D299F829E00907A4F5EB73B4DE10946A890A22C4B814E732D0FAD9)

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

- 当offset类型为number时，子组件偏移相同列数。 ```typescript @Entry @Component struct OffsetNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column() {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ offset: 2, span: 1 }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  Blank().width('100%').height(150)  }.border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/s6KNfPbKQaiTjY_1zWDd5A/zh-cn_image_0000002572679747.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=564765F839FBF3CB49E2A1844D60E6C4142B411D03C95591867D72EF86943CD8) 在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
- 当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。 ```typescript @Entry @Component struct OffsetColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  offset: {  xs: 1,  sm: 2,  md: 3,  lg: 4  },  span: 1  }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Y8WrVCMmRS6Y4gpIvKJiKQ/zh-cn_image_0000002541959840.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=B3F831EE6877559EBF5C5BCC3F0B51BDE5795465CB0A4FBF7A020DBC59A38FBF)

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

- 当order类型为number时，子组件在任何尺寸下排序次序一致。 ```typescript GridRow({ columns: 12 }) {  GridCol({ order: 4, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({ order: 3, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: 2, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: 1, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)') } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/yqX4zjdGT1W4ixwrRoo0nQ/zh-cn_image_0000002572639785.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=F1FC513CF0CED3EC372C807309E3547524F935FFF65D311AD90F69533218E2A4)
- 当order类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。 ```typescript @Entry @Component struct OrderColumnOptionExample {  @State currentBp: string = 'unknown'  build() {  Column({ space: 5 }) {  GridRow({ columns: 12 }) {  GridCol({  order: { xs: 1, sm: 5, md: 3, lg: 7 }, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({  order: { xs: 2, sm: 2, md: 6, lg: 1 }, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: { xs: 3, sm: 3, md: 1, lg: 6 }, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: { xs: 4, sm: 4, md: 2, lg: 5 }, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)')  }.border({ width: 1, color: 'rgb(39,135,217)' }).height('200vp').onBreakpointChange((breakpoint) => {  this.currentBp = breakpoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kuo5KOp_S9CRFnle2rxWCw/zh-cn_image_0000002542119478.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=D608C9D378489A42C8F5F38E75CFDD3E4499FE531605C3FBFAE899A545221BE3)

## 栅格组件的嵌套使用

栅格组件也可以嵌套使用，完成一些复杂的布局。

以下示例中，栅格把整个空间分为12份。第一层GridRow嵌套GridCol，分为中间大区域以及“footer”区域。第二层GridRow嵌套GridCol，分为“left”和“right”区域。子组件空间按照上一层父组件的空间划分，粉色的区域是屏幕空间的12列，绿色和蓝色的区域是父组件GridCol的12列，依次进行空间的划分。

```typescript
@Entry
@Component
struct GridRowExample {
  build() {
    GridRow({ columns: 12 }) {
      GridCol({ span: 12 }) {
        GridRow({ columns: 12 }) {
          GridCol({ span: 2 }) {
            Row() {
              Text('left').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff41dbaa')

          GridCol({ span: 10 }) {
            Row() {
              Text('right').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff4168db')
        }
        .backgroundColor('#19000000')
      }

      GridCol({ span: 12 }) {
        Row() {
          Text('footer').width('100%').textAlign(TextAlign.Center)
        }.width('100%').height('10%').backgroundColor(Color.Pink)
      }
    }.width('100%').height(300)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/SGpQNT3vSYG0A1VFouFW_A/zh-cn_image_0000002572679749.png?HW-CC-KV=V1&HW-CC-Date=20260418T024117Z&HW-CC-Expire=86400&HW-CC-Sign=0E1148FB53E17CCD715CA65E06A942775F450A940628A09EF80E542F45DF11A9)

综上所述，栅格组件提供了丰富的自定义能力，功能非常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。
