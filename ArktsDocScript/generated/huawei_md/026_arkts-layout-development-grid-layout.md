# 栅格布局 (GridRow/GridCol)-构建布局-组件布局-UI开发 (ArkTS声明式开发范式)-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
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
- 栅格容器通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。 例如，通过断点设置将应用宽度分成6个区间，通过columns配置各断点下栅格容器的栅格列数。 ```typescript @Entry @Component struct WindowRefGridLayout {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text(this.currentBp)  GridRow({  columns: {  xs: 2,  sm: 4,  md: 8,  lg: 12,  xl: 12,  xxl: 12  },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'],  reference: BreakpointsReference.WindowSize  }  }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }.backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ey5rtsylQv-yIwZomZk6Iw/zh-cn_image_0000002563865715.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=C15CA81547799EEFD8992F2C7A08439F19F38CCBAB554D42262BB89564F4A9C0)

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

- API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
- API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。 ```typescript @Entry @Component struct GridColumnsWithDefaults {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)', 'rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)'];  build() {  GridRow() {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  } } ``` API version 20之前布局显示： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/BGwkSro1Rl6HMP9yt1Klpw/zh-cn_image_0000002563785761.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=456619F2D1CEAA22D56CADCB9424DC1741C2AF07EF52956B6EE7086F6C2A070C) API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/3vPchDiKR2WamHN6BxiFCQ/zh-cn_image_0000002532905866.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=A5179DD21CFFD9AADEDF5F9D736B5DCF312DC1DA9B35F4A7D99D85B3DC09EF3B)

columns支持number和[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)两种类型, 可按两种方式设置栅格布局的总列数。

- 当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下： ```typescript @Entry @Component struct FixedFourColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：4').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 4 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ```typescript @Entry @Component struct FixedEightColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：8').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ovr7AJc4RjChyOzNgIy0KQ/zh-cn_image_0000002533065814.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=BFB8479D3E1DA6D3BFF2D5DAE5573E724B6A8EE89025B20337903CAC91425A3B)
- 当columns类型为[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。 ```typescript @Entry @Component struct GridRowColumnOptionLayout {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({  columns: { sm: 4, md: 8 },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp']  }  }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` API version 20之前布局显示（xs设备未配置栅格列数，取默认列数12）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/NwFEC8EiShujCWiYfYljxQ/zh-cn_image_0000002563865717.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=8080BCADF21C1F49EC65CB664979393F6D0A3CB21CED31200DD75B4E8F9D035B) API version 20及以后布局显示（xs设备继承sm设备栅格列数）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/6AAk9hctRcWIp0iLRHouFw/zh-cn_image_0000002563785763.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=D7BEC1AE1B20E30CFB0A21CE76B80EE2DB962376BAF1BB5A4CDD812D856C7855) 仅部分设置sm、md的栅格列数，未配置的xs、lg、xl、xxl设备根据[栅格列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)取默认值。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).Row（从左往右排列）或[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

- 子组件默认从左往右排列。 ```typescript GridRow({ direction: GridRowDirection.Row }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/3RCePnwkRIqxeUWWr7VONQ/zh-cn_image_0000002532905868.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=A297289A4FCB7EAD909B923D062A2C5FC778A4029156BC67A07E0F44AAA43906)
- 子组件从右往左排列。 ```typescript GridRow({ direction: GridRowDirection.RowReverse }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/SxAwAiXkSI22CRYsZp27fA/zh-cn_image_0000002533065816.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=6A3A16BB0D9A88CE3BD3C085E40C51D9669F690DB9862951704CE1A43390A52F)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

- 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。 ```typescript GridRow({ gutter: 10 }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/fswqBY9zSA27AIR48DWsJA/zh-cn_image_0000002563865719.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=EDF3E480571531C54991788039945D7FD82056DC88D5AA6B0D717F8CE392DFEE)
- 当gutter类型为[GutterOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gutteroption)时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。 ```typescript GridRow({ gutter: { x: 20, y: 50 } }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/U8_7ZT_rQumrkv98IuFBhQ/zh-cn_image_0000002563785765.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=440539A7B490498A87818AEB413A03523820621D11DA31B282A3753853BC53A1)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

- 设置span。 ```typescript let gSpan:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ span: 2 }){} GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){} GridCol(){}.span(2) GridCol(){}.span(gSpan) ```
- 设置offset。 ```typescript let gOffset:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ offset: 2, span: 1 }){} GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 }, span: 1 }){} GridCol({ span: 1 }){}.offset(gOffset) ```
- 设置order。 ```typescript let gOrder:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ order: 2, span: 1 }){} GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }){} GridCol({ span: 1 }){}.order(2) GridCol({ span: 1 }){}.order(gOrder) ```

### span

子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。

span支持number和[GridColColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。

- 当span类型为number时，子组件在所有尺寸设备下占用的列数相同。 ```typescript @Entry @Component struct SpanNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 2 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/XWMbxptXRv61RGmRJf20sA/zh-cn_image_0000002532905870.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=C1A6557D4B342FA923CC27D030F72514F631629A571DFAE7C7BA79D6DC78278B)
- 当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据[列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)取默认值。 ```typescript @Entry @Component struct SpanColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  span: {  xs: 1,  sm: 2,  md: 3,  lg: 4  }  }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/CNrjmrzKSVyYlIGfiwZa9w/zh-cn_image_0000002533065818.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=2149C3B2B688694E524E9BDF112B684B293EAC240AF09A198588753852FEDF91)

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

- 当offset类型为number时，子组件偏移相同列数。 ```typescript @Entry @Component struct OffsetNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column() {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ offset: 2, span: 1 }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  Blank().width('100%').height(150)  }.border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ptVfLKYoT6yFPlnUhMtdZw/zh-cn_image_0000002563865721.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=171D9F6834A13F64E2DEC25E4B1FF090EE361C7BC1A9340C2947393C338D821A) 在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
- 当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。 ```typescript @Entry @Component struct OffsetColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  offset: {  xs: 1,  sm: 2,  md: 3,  lg: 4  },  span: 1  }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/y_e-xVTGTOiM4JRB3zMVtg/zh-cn_image_0000002563785767.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=1DE77190C1E16B34C956B6B83AC3027BF65083C327A8370F3BBCCFEDDE4DC29B)

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

- 当order类型为number时，子组件在任何尺寸下排序次序一致。 ```typescript GridRow({ columns: 12 }) {  GridCol({ order: 4, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({ order: 3, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: 2, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: 1, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)') } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/BCkn0P8vStS316y7tNbWhg/zh-cn_image_0000002532905872.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=1E4D7650A94E0960F5294D59699639FDD85622F21615C5D11EA0E6077374DBCF)
- 当order类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。 ```typescript @Entry @Component struct OrderColumnOptionExample {  @State currentBp: string = 'unknown'  build() {  Column({ space: 5 }) {  GridRow({ columns: 12 }) {  GridCol({  order: { xs: 1, sm: 5, md: 3, lg: 7 }, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({  order: { xs: 2, sm: 2, md: 6, lg: 1 }, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: { xs: 3, sm: 3, md: 1, lg: 6 }, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: { xs: 4, sm: 4, md: 2, lg: 5 }, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)')  }.border({ width: 1, color: 'rgb(39,135,217)' }).height('200vp').onBreakpointChange((breakpoint) => {  this.currentBp = breakpoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Zidja7S3RAGzDPVDkkJ6YA/zh-cn_image_0000002533065820.gif?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=07615A83A0F7013634FA247D94C023F442B58E4346542937FF46E74E4EB29F34)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/ajptq--XQnCJJhhbVgPPjg/zh-cn_image_0000002563865723.png?HW-CC-KV=V1&HW-CC-Date=20260330T094447Z&HW-CC-Expire=86400&HW-CC-Sign=20BA08EE67F762A55E491E5DFD5B16F1808F11E21F527C2361FF70FDC765AD18)

综上所述，栅格组件提供了丰富的自定义能力，功能非常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。
