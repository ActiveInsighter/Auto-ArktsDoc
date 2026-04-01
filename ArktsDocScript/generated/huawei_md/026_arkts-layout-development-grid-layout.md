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
- 栅格容器通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。 例如，通过断点设置将应用宽度分成6个区间，通过columns配置各断点下栅格容器的栅格列数。 ```typescript @Entry @Component struct WindowRefGridLayout {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text(this.currentBp)  GridRow({  columns: {  xs: 2,  sm: 4,  md: 8,  lg: 12,  xl: 12,  xxl: 12  },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'],  reference: BreakpointsReference.WindowSize  }  }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }.backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/631eh5x1QVGc2qwqtZHsvg/zh-cn_image_0000002565210137.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=59467ABE479D8B58FBD3971715348B723318A0E3D2BE3112BB48B932A80C22FD)

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

- API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
- API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。 ```typescript @Entry @Component struct GridColumnsWithDefaults {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)', 'rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)'];  build() {  GridRow() {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  } } ``` API version 20之前布局显示： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/l0_Xyq2XRuuISJjnCU9o4g/zh-cn_image_0000002534250314.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=A1383CB24752807200A9F2BB9DF34C608615D55536FC3CB9B0670469245CADE8) API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/lobVs3fpS7STJgslYaKmvw/zh-cn_image_0000002534410260.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=48E220391B750023AADC6C74D5AD20980742A5B099D0A1A8949346CC4AD4AD2D)

columns支持number和[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)两种类型, 可按两种方式设置栅格布局的总列数。

- 当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下： ```typescript @Entry @Component struct FixedFourColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：4').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 4 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ```typescript @Entry @Component struct FixedEightColumnGrid {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  Text('columns：8').alignSelf(ItemAlign.Start)  Row() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .width('100%').height('100%')  }  .height(160)  .border({ color: 'rgb(39,135,217)', width: 2 })  .width('90%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/VNZ_XqboQiGO9QGcvW5obA/zh-cn_image_0000002565290159.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=4E69441C68E589D3116C816DCF53226CFF2D1D0003A2A87955D85EDEEE341887)
- 当columns类型为[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。 ```typescript @Entry @Component struct GridRowColumnOptionLayout {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({  columns: { sm: 4, md: 8 },  breakpoints: {  value: ['320vp', '600vp', '840vp', '1440vp', '1600vp']  }  }) {  ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {  GridCol({ span: 1 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50')  }.backgroundColor(item)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` API version 20之前布局显示（xs设备未配置栅格列数，取默认列数12）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Ycmnr1dMTFqLs1odvRJQjA/zh-cn_image_0000002565210139.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=CCBC976F4960E3144E3A0AB633146892A6DC9C3764739823E527E71AAFB2CE4F) API version 20及以后布局显示（xs设备继承sm设备栅格列数）： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/XGY4ADZBRayJURbKCYraeA/zh-cn_image_0000002534250316.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=AFEE725EE6C81EC5F74D5C9E3FC9FB514B2659EBF28A6F96F40C1994579FB391) 仅部分设置sm、md的栅格列数，未配置的xs、lg、xl、xxl设备根据[栅格列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)取默认值。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).Row（从左往右排列）或[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

- 子组件默认从左往右排列。 ```typescript GridRow({ direction: GridRowDirection.Row }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/ABOiymquR-ai77w7ramMEA/zh-cn_image_0000002534410262.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=8098C4A5298BCF766AAA834C5329154ABD5A5A14D42EA7AE10B2026F7F17226D)
- 子组件从右往左排列。 ```typescript GridRow({ direction: GridRowDirection.RowReverse }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/RxH_dKCMSy6Iz7WBJA7VxQ/zh-cn_image_0000002565290161.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=95F37D5124C16AF6D982DC5F598A069AF3FBD9FC7CA5C896046EE408D75269AE)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

- 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。 ```typescript GridRow({ gutter: 10 }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/8x4TS1xtS3eIrbmoRUrLOQ/zh-cn_image_0000002565210141.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=3F38875FACCCDF52E0822988D964F4CC1674D35B70FE63BA02F90EEBC162C861)
- 当gutter类型为[GutterOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gutteroption)时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。 ```typescript GridRow({ gutter: { x: 20, y: 50 } }) { } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/H4Y1-dzbR3C7KzKGm5j19A/zh-cn_image_0000002534250318.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=9C43BA1C9DA969088FF1B4B6C236BFF4DAA186515DC79D9782B362C5D8110813)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

- 设置span。 ```typescript let gSpan:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ span: 2 }){} GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){} GridCol(){}.span(2) GridCol(){}.span(gSpan) ```
- 设置offset。 ```typescript let gOffset:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ offset: 2, span: 1 }){} GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 }, span: 1 }){} GridCol({ span: 1 }){}.offset(gOffset) ```
- 设置order。 ```typescript let gOrder:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 } ``` ```typescript GridCol({ order: 2, span: 1 }){} GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }){} GridCol({ span: 1 }){}.order(2) GridCol({ span: 1 }){}.order(gOrder) ```

### span

子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。

span支持number和[GridColColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。

- 当span类型为number时，子组件在所有尺寸设备下占用的列数相同。 ```typescript @Entry @Component struct SpanNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ span: 2 }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/VdRBUe8YRcCOymDLB7Ov2g/zh-cn_image_0000002534410264.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=6F291556BC0175E3FD4F0A1DEE0DE37970DF040369E38E6E4DDDC076147F3B04)
- 当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据[列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)取默认值。 ```typescript @Entry @Component struct SpanColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 8 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  span: {  xs: 1,  sm: 2,  md: 3,  lg: 4  }  }) {  Row() {  Text(`${index}`)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .border({ color: 'rgb(39,135,217)', width: 2 })  .height('150vp')  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/j_H82180TjqbCA8ltubssA/zh-cn_image_0000002565290163.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=3FFCEAF60CD320FAAB86F482ED31BEBEC72536AF5BEEB6BAE21F53A8F0FEC338)

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

- 当offset类型为number时，子组件偏移相同列数。 ```typescript @Entry @Component struct OffsetNumberExample {  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column() {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({ offset: 2, span: 1 }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  Blank().width('100%').height(150)  }.border({ color: 'rgb(39,135,217)', width: 2 })  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/coe5NSvkRv-9sm7IoDYXCQ/zh-cn_image_0000002565210143.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=9F3911FBA43CBCA52C25E3993B908A720B6F38A3CD18D2A8E5BED1F975049E70) 在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
- 当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。 ```typescript @Entry @Component struct OffsetColumnOptionExample {  @State currentBp: string = "unknown"  @State bgColors: ResourceColor[] =  ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',  'rgb(255,192,0)', 'rgb(170,10,33)'];  build() {  Column({ space: 6 }) {  GridRow({ columns: 12 }) {  ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {  GridCol({  offset: {  xs: 1,  sm: 2,  md: 3,  lg: 4  },  span: 1  }) {  Row() {  Text('' + index)  }.width('100%').height('50vp')  }  .backgroundColor(color)  })  }  .height(200)  .border({ color: 'rgb(39,135,217)', width: 2 })  .onBreakpointChange((breakPoint) => {  this.currentBp = breakPoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/hvz92GlkQRaotgtLPwlECw/zh-cn_image_0000002534250320.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=6B51B7F3CC68CB8CC5F341C393AE71B04BA88F4F6CAEEE05749B35C9E8A42870)

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

- 当order类型为number时，子组件在任何尺寸下排序次序一致。 ```typescript GridRow({ columns: 12 }) {  GridCol({ order: 4, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({ order: 3, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: 2, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: 1, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)') } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/iXflaGhtSqimluvdnUhNYA/zh-cn_image_0000002534410266.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=DF691E81F28D516D3D12C4297449E83A08AC5DE24DBB10252FF0F9C9E1080DB8)
- 当order类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。 ```typescript @Entry @Component struct OrderColumnOptionExample {  @State currentBp: string = 'unknown'  build() {  Column({ space: 5 }) {  GridRow({ columns: 12 }) {  GridCol({  order: { xs: 1, sm: 5, md: 3, lg: 7 }, span: 1 }) {  Row() {  Text('1')  }.width('100%').height('50vp')  }.backgroundColor('rgb(213,213,213)')  GridCol({  order: { xs: 2, sm: 2, md: 6, lg: 1 }, span: 1 }) {  Row() {  Text('2')  }.width('100%').height('50vp')  }.backgroundColor('rgb(150,150,150)')  GridCol({ order: { xs: 3, sm: 3, md: 1, lg: 6 }, span: 1 }) {  Row() {  Text('3')  }.width('100%').height('50vp')  }.backgroundColor('rgb(0,74,175)')  GridCol({ order: { xs: 4, sm: 4, md: 2, lg: 5 }, span: 1 }) {  Row() {  Text('4')  }.width('100%').height('50vp')  }.backgroundColor('rgb(39,135,217)')  }.border({ width: 1, color: 'rgb(39,135,217)' }).height('200vp').onBreakpointChange((breakpoint) => {  this.currentBp = breakpoint  })  Text(this.currentBp)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/0YSyihXfSvyE6r7AfKpw1Q/zh-cn_image_0000002565290165.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=E016F0583165BA083C9EAD785071E20993D322A811E7BFC7C698CBE54F7D9767)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/N_vFFrDbS3SereSy1IWfmQ/zh-cn_image_0000002565210145.png?HW-CC-KV=V1&HW-CC-Date=20260401T132809Z&HW-CC-Expire=86400&HW-CC-Sign=04493587760B2A28FEE9C79F48E9F4980BA43BBFD2B2D429F6CDFBB51D927BA5)

综上所述，栅格组件提供了丰富的自定义能力，功能非常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。
