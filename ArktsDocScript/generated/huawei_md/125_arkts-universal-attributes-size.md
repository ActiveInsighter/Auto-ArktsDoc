# 尺寸设置
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size

设置组件的宽高、边距。

> **说明**
> - 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
> - 如果组件的尺寸通过百分比进行设置， 在计算组件尺寸的百分比大小时，参考最近设置了固定大小的祖先节点的尺寸。
> - 从API version 10开始，尺寸设置内部分属性支持使用calc计算特性，具体支持属性请参考对应的属性说明。calc计算特性是一种动态计算长度值的函数，常用于灵活设置布局尺寸（如宽度、高度、边距等）。它允许通过数学表达式组合不同单位和数值，支持通过加减乘除括号运算符组成计算表达式，实现动态响应式设计。注意，在使用calc时，运算符与数值之间需要使用空格隔开。具体使用场景可见[示例1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#示例1设置组件的宽高和边距)。

## width

width(value: Length): T

设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会超出父组件的范围。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | 是 | 要设置的组件宽度。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

> **说明**
> - 在[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)组件中，width设置auto表示自适应文本宽度。
> - 在[AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer)组件中，width设置auto表示自适应宽度最大索引项的宽度。

## height

height(value: Length): T

设置组件自身的高度，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会超出父组件的范围。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | 是 | 要设置的组件高度。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

> **说明**
> 在[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[RelativeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer)组件中，width、height设置auto表示自适应子组件。

## width15+

width(widthValue: Length | LayoutPolicy): T

设置组件自身的宽度或水平方向布局策略，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会超出父组件的范围。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| widthValue | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [LayoutPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutpolicy15) | 是 | 要设置的组件宽度。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## height15+

height(heightValue: Length | LayoutPolicy): T

设置组件自身的高度或垂直方向布局策略，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会超出父组件的范围。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| heightValue | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [LayoutPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutpolicy15) | 是 | 要设置的组件高度。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## size

size(value: SizeOptions): T

设置组件自身的宽高尺寸。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#sizeoptions) | 是 | 设置宽高尺寸。 异常值：参数为undefined时，属性设置不生效；其它异常值时，size属性恢复到不配置时的默认行为。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## padding

padding(value: Padding | Length | LocalizedPadding): T

设置组件的内边距属性。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#padding) | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [LocalizedPadding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedpadding12)12+ | 是 | 设置组件的内边距。 参数为Length类型时，四个方向内边距同时生效。 默认值：0 单位：vp padding设置百分比时，上下左右内边距均以父容器的width作为基础值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## margin

margin(value: Margin | Length | LocalizedMargin): T

设置组件的外边距属性。在计算位置时外边距视为组件大小的一部分，从而影响组件位置。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#margin) | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [LocalizedMargin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedmargin12)12+ | 是 | 设置组件的外边距。 参数为Length类型时，四个方向外边距同时生效。 默认值：0 单位：vp margin设置百分比时，上下左右外边距均以父容器的width作为基础值。在[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)交叉轴上布局时，子组件交叉轴的大小与margin的和为整体。 例如Column容器宽100，其中子组件宽50，margin left为10，right为20，子组件水平方向偏移10。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## safeAreaPadding14+

safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T

设置安全区边距属性。允许容器向自身添加组件级安全区域，供子组件延伸，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。

> **说明**
> 从API version 18开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 14开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paddingValue | [Padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#padding) | [LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12) | [LocalizedPadding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedpadding12) | 是 | 设置组件的安全区边距。 默认值：0 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

> **说明**
> 当父辈和祖先容器设置了组件级安全区域时，子组件可以感知并利用该区域，称该区域为累计安全区延伸（accumulatedSafeAreaExpand，下文简称SAE），表示子组件在四个方向上各可延伸的长度。当祖辈与更上一级祖辈的safeAreaPadding相邻接（即未被margin、border、padding分隔）时，SAE将递归地向外累积，直至不存在相邻的更外层safeAreaPadding或递归至页面容器外。系统级避让区域（如状态栏、导航条、挖孔区等，详情参见[安全区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area)中的说明）可视为页面容器特有的safeAreaPadding，同样参与该延伸范围的计算。
>
> 通过与其他属性配合使用，可对上述计算得到的组件级安全区区域加以利用。例如，对子组件设置[ignoreLayoutSafeArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#ignorelayoutsafearea20)属性，即可利用SAE延伸组件的布局范围。

## layoutWeight

layoutWeight(value: number | string): T

设置组件的布局权重，使组件在父容器（[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)/[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)/[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）的主轴方向按照权重分配尺寸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 父容器尺寸确定时，不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位，这些元素占位后在主轴留下的空间称为主轴剩余空间。设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，分配时会忽略元素本身的尺寸设置。 默认值：0 **说明：** 仅在[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)/[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)/[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)布局中生效。 可选值为大于等于0的数字，或者可以转换为数字的字符串。 如果容器中有子元素设置了layoutWeight属性，且设置的属性值大于0，则所有子元素不会再基于[flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink)和[flexGrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexgrow)布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## constraintSize

constraintSize(value: ConstraintSizeOptions): T

设置约束尺寸，组件布局时，进行尺寸范围限制。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#constraintsizeoptions) | 是 | 设置约束尺寸。constraintSize的优先级高于Width和Height。取值结果参考constraintSize取值对width/height影响。 默认值： { minWidth: 0, maxWidth: Infinity, minHeight: 0, maxHeight: Infinity } 异常值：数值开头的字符串仅解析出数字部分，非数值开头的字符串解析为0；其它异常值时，constraintSize属性恢复到不配置时的默认行为。 单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**constraintSize(minWidth/maxWidth/minHeight/maxHeight)取值对width/height影响：**

| 缺省值 | 结果 |
| --- | --- |
| \ | width=MAX(minWidth,MIN(maxWidth,width)) height=MAX(minHeight,MIN(maxHeight,height)) |
| maxWidth、maxHeight | width=MAX(minWidth,width) height=MAX(minHeight,height) |
| minWidth、minHeight | width=MIN(maxWidth,width) height=MIN(maxHeight,height) |
| width、height | 若minWidth<maxWidth，组件自身布局逻辑生效，width取值范围为[minWidth,maxWidth]；否则，width=MAX(minWidth,maxWidth)。 若minHeight<maxHeight，组件自身布局逻辑生效，height取值范围为[minHeight,maxHeight]；否则，height=MAX(minHeight,maxHeight)。 |
| width与maxWidth、height与maxHeight | width=minWidth height=minHeight |
| width与minWidth、height与minHeight | 组件自身布局逻辑生效，width取值约束为不大于maxWidth。 组件自身布局逻辑生效，height取值约束为不大于maxHeight。 |
| minWidth与maxWidth、minHeight与maxHeight | width以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。 height以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。 |
| width与minWidth与maxWidth | 使用父容器传递的布局限制进行布局。 |
| height与minHeight与maxHeight | 使用父容器传递的布局限制进行布局。 |

## LayoutPolicy15+

用于组件宽度和高度的布局策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| matchParent | [LayoutPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutpolicy15) | 是 | 否 | 当前组件自适应父组件布局时，其大小与父组件内容区相等，不包括padding，border和safeAreaPadding。 **卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| wrapContent20+ | [LayoutPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutpolicy15) | 是 | 否 | 当前组件自适应子组件（内容）时，其大小与子组件（内容）相等，并且其大小受父组件内容区大小约束。 **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| fixAtIdealSize20+ | [LayoutPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutpolicy15) | 是 | 否 | 当前组件自适应子组件（内容）时，其大小与子组件（内容）相等，并且其大小不受父组件内容区大小约束。 **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

> **说明**
> - LayoutPolicy支持设置三种布局策略：matchParent（自适应父组件布局）、wrapContent（根据内容自适应但不超过父组件尺寸的布局）和fixAtIdealSize（根据内容自适应，可能超过父组件尺寸的布局）。具体示例代码参见[设置布局策略](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#示例5设置布局策略)。
> - wrapContent和fixAtIdealSize场景，组件无法通过内容确定大小时，如果组件大小有默认值，则按照默认值进行测算；如果没有默认值，则按照宽高(0,0)进行测算。
> - 容器设置wrapContent，并且有子组件设置matchParent时（包括仅一边设置matchParent），容器先由确定大小的子组件撑大，设置matchParent的子组件再匹配容器大小；如果没有确定大小的子组件，容器和子组件大小均为0。
> - LayoutPolicy优先级低于constraintSize。
> - 从API version 15开始，仅Row和Column组件的width和height属性支持设置LayoutPolicy类型参数，其他组件设置LayoutPolicy类型参数后与不设置宽度或高度表现一致；从API version 20开始，所有基础组件均支持设置LayoutPolicy类型参数。

## 示例

### 示例1（设置组件的宽高和边距）

设置组件的宽度、高度、内边距及外边距。

```typescript
@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:').fontSize(12).fontColor(0xCCCCCC).width('90%')
      Row() {

        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor(Color.Yellow)
        }
        .width(80)
        .height(80)
        .padding({
          top: 5,
          left: 10,
          bottom: 15,
          right: 20
        })
        .margin(20)
        .backgroundColor(Color.White)
      }.backgroundColor(Color.Blue)

      Text('constraintSize')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Text('this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text')
        .width('90%')
        .constraintSize({ maxWidth: 200 })

      Text('layoutWeight')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')

      Row() {

        Text('layoutWeight(1)')
          .size({ width: '30%', height: 110 }).backgroundColor(0xFFEFD5).textAlign(TextAlign.Center)
          .layoutWeight(1)

        Text('layoutWeight(2)')
          .size({ width: '30%', height: 110 }).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
          .layoutWeight(2)

        Text('no layoutWeight')
          .size({ width: '30%', height: 110 }).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
      }
      .size({ width: '90%', height: 140 })
      .backgroundColor(0xAFEEEE)

      Text('calc:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Column() {
        Row() {
          Text('width 50%')
            .fontSize(14)
            .borderWidth(1)
            .textAlign(TextAlign.Center)
            .size({ width: '50%', height: 50 })
          Text('width 50vp')
            .fontSize(14)
            .borderWidth(1)
            .textAlign(TextAlign.Center)
            .size({ width: '50vp', height: 50 })
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)

        Text('width:calc(50% + 50vp), height:calc(50%)')
          .fontSize(14)
          .borderWidth(1)
          .fontWeight(FontWeight.Bold)
          .backgroundColor(0xFFFAF0)
          .textAlign(TextAlign.Center)
          .size({ width: 'calc(50% + 50vp)', height: 'calc(50%)' })

      }.width('100%').height(100)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/SyudadmlTOKW13g9w_QCLA/zh-cn_image_0000002542120394.png?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=23B3B59D3F74AB9E694CF0BA05227BB2B17C8046A6792D0C62AF230546524FC1)

### 示例2（LocalizedPadding和LocalizedMargin类型的使用）

使用LocalizedPadding类型和LocalizedMargin类型定义padding和margin属性。

```typescript
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Row() {

        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor(Color.Yellow)
        }
        .width(80)
        .height(80)
        .padding({
          top: LengthMetrics.vp(5),
          bottom: LengthMetrics.vp(15),
          start: LengthMetrics.vp(10),
          end: LengthMetrics.vp(20)
        })
        .margin({
          top: LengthMetrics.vp(40),
          bottom: LengthMetrics.vp(20),
          start: LengthMetrics.vp(30),
          end: LengthMetrics.vp(10)
        })
        .backgroundColor(Color.White)
      }
      .backgroundColor(Color.Blue)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```

从左至右显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/EqiOMxrWTvyuJpPty0kx5w/zh-cn_image_0000002572680665.png?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=908CDD55E2F9805CA6868A4B0BBE7751233F604951FDE4ADB08E1A2315D9748A)

从右至左显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/nUMxKDbHTS69fNUZb1RMnQ/zh-cn_image_0000002541960758.png?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=07947170B77FC81251743B7576140FF5D63D462DD5B418636034B8F746AA60C7)

### 示例3（设置组件级安全区）

对容器设置组件级安全区。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct SafeAreaPaddingExample {
  build() {
    Column() {
      Column() {
        Column()
          .width('100%')
          .height('100%')
          .backgroundColor(Color.Pink)
      }
      .width(200)
      .height(200)
      .backgroundColor(Color.Yellow)
      .borderWidth(10)
      .padding(10)
      .safeAreaPadding(LengthMetrics.vp(40))
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/jWm3KEQ7SkiSx6-1IQIpgA/zh-cn_image_0000002572640703.png?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=B47084E5B5F9FBACEEFFDD4AB095ABBDA4AD59745E6EA897049477355F7C1AD8)

### 示例4（使用attributeModifier动态设置安全区）

使用attributeModifier对容器设置组件级安全区。

```typescript
class MyModifier implements AttributeModifier<CommonAttribute> {
  applyNormalAttribute(instance: CommonAttribute): void {
    instance.safeAreaPadding({
      left: 10,
      top: 20,
      right: 30,
      bottom: 40
    })
  }
}

@Entry
@Component
struct SafeAreaPaddingExample {
  @State modifier: MyModifier = new MyModifier()

  build() {
    Column() {
      Column() {
        Column()
          .width('100%')
          .height('100%')
          .backgroundColor(Color.Pink)
      }
      .width(200)
      .height(200)
      .backgroundColor(Color.Yellow)
      .borderWidth(10)
      .padding(10)
      .attributeModifier(this.modifier)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/G1hs96HRSlOcVUKFW0ovCA/zh-cn_image_0000002542120396.png?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=9D80D015A3D0EFDFF66BA0425C95677BDFDEBBB8A84201CAC7FF3C9FC659B1FB)

### 示例5（设置布局策略）

对容器大小设置布局策略。

```typescript
@Entry
@Component
struct LayoutPolicyExample {
  build() {
    Column() {
      Column() {

        Text('matchParent')
        Flex()
          .backgroundColor('rgb(0, 74, 175)')
          .width(LayoutPolicy.matchParent)
          .height(LayoutPolicy.matchParent)
          .constraintSize({ maxWidth: 150, maxHeight: 150 })

        Text('wrapContent')
        Row() {
          Flex()
            .width(300)
            .height(300)
        }
        .backgroundColor('rgb(39, 135, 217)')
        .width(LayoutPolicy.wrapContent)
        .height(LayoutPolicy.wrapContent)
        .constraintSize({ maxWidth: 250, maxHeight: 250 })

        Text('fixAtIdealSize')

        Row() {
          Flex()
            .width(300)
            .height(300)
        }
        .backgroundColor('rgb(240, 250, 255)')
        .width(LayoutPolicy.fixAtIdealSize)
        .height(LayoutPolicy.fixAtIdealSize)
        .constraintSize({ maxWidth: 250, maxHeight: 250 })
      }
      .width(200)
      .height(200)
      .padding(10)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/5JqzL_KxRTu2s_N7WBXICg/zh-cn_image_0000002572680667.jpg?HW-CC-KV=V1&HW-CC-Date=20260420T025945Z&HW-CC-Expire=86400&HW-CC-Sign=55847E850DCAF72D030EC9B610AD74BA421C2DA4A9AE1ED8B611FBF329BA8197)
