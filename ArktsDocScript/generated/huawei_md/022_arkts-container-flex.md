# 子组件
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex

Flex是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。

具体指南请参考[弹性布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout)。

> **说明**
> 该组件从API version 7开始支持。后续版本如有新增内容将采用上角标单独标记该内容的起始版本。
> Flex组件在渲染时存在二次布局过程，因此在对性能有严格要求的场景下建议使用
> Column
> 、
> Row
> 代替。最佳实践请参考
> 布局优化指导-合理使用布局组件
> 。
> Flex组件主轴不设置长度时默认撑满父容器，
> Column
> 、
> Row
> 组件主轴不设置长度时默认跟随子节点大小。
> Flex、Column、Row组件在没有子节点且不设置宽高时，默认宽高为-1。
> 主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受constraintSize属性以及父容器传递的最大最小长度限制，且constraintSize属性优先级更高。

## 子组件

可以包含子组件。

## 接口

Flex(value?: FlexOptions)

Flex布局容器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明) | 否 | 弹性布局子组件参数。 |

## FlexOptions对象说明

设置Flex子组件的排列对齐方式。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [FlexDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexdirection) | 否 | 是 | 子组件在Flex容器上排列的方向，即主轴的方向。 默认值：FlexDirection.Row 异常值按默认值处理。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| wrap | [FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap) | 否 | 是 | Flex容器是单行/列还是多行/列排列。 默认值：FlexWrap.NoWrap 异常值按默认值处理。 **说明：** 在多行布局时，通过交叉轴方向，确认新行堆叠方向。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| justifyContent | [FlexAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexalign) | 否 | 是 | 所有子组件在Flex容器主轴上的对齐格式。 默认值：FlexAlign.Start 异常值按默认值处理。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignItems | [ItemAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#itemalign) | 否 | 是 | 所有子组件在Flex容器交叉轴上的对齐格式。 默认值：ItemAlign.Start 异常值按默认值处理。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignContent | [FlexAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexalign) | 否 | 是 | 当交叉轴存在额外空间时，多行内容之间的对齐方式。仅在wrap为Wrap或WrapReverse下生效。 默认值：FlexAlign.Start 异常值按默认值处理。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| space12+ | [FlexSpaceOptions12+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexspaceoptions12) | 否 | 是 | 所有子组件在Flex容器主轴或交叉轴的间距。 默认值：{main: LengthMetrics.px(0), cross: LengthMetrics.px(0)} 非法值：按默认值处理。 space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## FlexSpaceOptions12+

设置Flex容器的子组件在主轴或交叉轴的间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | [LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12) | 否 | 是 | Flex容器主轴上的space。 默认值：LengthMetrics.px(0) |
| cross | [LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12) | 否 | 是 | Flex容器交叉轴上的space。 默认值：LengthMetrics.px(0) |

## 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

## 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## 示例

### 示例1（子组件排列方向）

该示例通过设置direction实现不同的子组件排列方向效果。

```typescript
@Entry
@Component
struct FlexExample1 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.Row }) {
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('4').width('20%').height(50).backgroundColor(0xD2B48C)
        }
        .height(70)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.RowReverse }) {
          Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
          Text('4').width('20%').height(50).backgroundColor(0xD2B48C)
        }
        .height(70)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.Column }) {
          Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)
          Text('2').width('100%').height(40).backgroundColor(0xD2B48C)
          Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)
          Text('4').width('100%').height(40).backgroundColor(0xD2B48C)
        }
        .height(160)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ direction: FlexDirection.ColumnReverse }) {
          Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)
          Text('2').width('100%').height(40).backgroundColor(0xD2B48C)
          Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)
          Text('4').width('100%').height(40).backgroundColor(0xD2B48C)
        }
        .height(160)
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Qod6lh2OQDiAZmiskKa8Ew/zh-cn_image_0000002531105844.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=A6853DE7AA3E94E8F3D405B856BDA84815D417B5FA1F84AB9C8F913F9090E377)

### 示例2（子组件单/多行排列）

该示例通过设置wrap实现子组件单行或多行的排列效果。

```typescript
@Entry
@Component
struct FlexExample2 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('Wrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.Wrap }) {
          Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
        }
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('NoWrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.NoWrap }) {
          Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
        }
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('WrapReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.WrapReverse , direction:FlexDirection.Row }) {
          Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
        }
        .width('90%')
        .height(120)
        .padding(10)
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/mLyRrCgyQza7eYzXsWh8Rg/zh-cn_image_0000002531225778.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=208773C1CBCD6AA5944817462A4769F4091BA1D9B267731FF650C33C7297A731)

### 示例3（子组件在主轴上的对齐格式）

该示例通过设置justifyContent实现子组件在主轴上不同的对齐效果。

```typescript
@Component
struct JustifyContentFlex {
  justifyContent : number = 0;

  build() {
    Flex({ justifyContent: this.justifyContent }) {
      Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
      Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
      Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
    }
    .width('90%')
    .padding(10)
    .backgroundColor(0xAFEEEE)
  }
}

@Entry
@Component
struct FlexExample3 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('justifyContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.Start })

        Text('justifyContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.Center })

        Text('justifyContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.End })

        Text('justifyContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.SpaceBetween })

        Text('justifyContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.SpaceAround })

        Text('justifyContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')
        JustifyContentFlex({ justifyContent: FlexAlign.SpaceEvenly })
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/15-v2Eh4SCyHAsy8HvxPLw/zh-cn_image_0000002562025761.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=BCC70F9984518611F78C510B6FCB33DA5D5C0557BF7829357AAF0C8C25515436)

### 示例4（子组件在交叉轴上的对齐方式）

该示例通过设置alignItems实现子组件在交叉轴上的不同的对齐效果。

```typescript
@Component
struct AlignItemsFlex {
  alignItems : number = 0;

  build() {
    Flex({ alignItems: this.alignItems }) {
      Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)
      Text('2').width('33%').height(40).backgroundColor(0xD2B48C)
      Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
    }
    .size({width: '90%', height: 80})
    .padding(10)
    .backgroundColor(0xAFEEEE)
  }
}

@Entry
@Component
struct FlexExample4 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('alignItems:Auto').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.Auto })

        Text('alignItems:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.Start })

        Text('alignItems:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.Center })

        Text('alignItems:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.End })

        Text('alignItems:Stretch').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.Stretch })

        Text('alignItems:Baseline').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignItemsFlex({ alignItems: ItemAlign.Baseline })
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/OzV2VtXJRJKuIxmSDXf2iw/zh-cn_image_0000002562145747.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=B094D65B13701CA3FF77C4E06C694B4ED526A80FC23E33E7338C4781F5955333)

### 示例5（多行内容的对齐方式）

该示例通过设置alignContent实现多行内容的不同对齐效果。

```typescript
@Component
struct AlignContentFlex {
  alignContent: number = 0;

  build() {
    Flex({ wrap: FlexWrap.Wrap, alignContent: this.alignContent }) {
      Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)
      Text('2').width('50%').height(20).backgroundColor(0xD2B48C)
      Text('3').width('50%').height(20).backgroundColor(0xD2B48C)
    }
    .size({ width: '90%', height: 90 })
    .padding(10)
    .backgroundColor(0xAFEEEE)
  }
}

@Entry
@Component
struct FlexExample5 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('alignContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignContentFlex({ alignContent: FlexAlign.Start })

        Text('alignContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignContentFlex({ alignContent: FlexAlign.Center })

        Text('alignContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignContentFlex({ alignContent: FlexAlign.End })

        Text('alignContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignContentFlex({ alignContent: FlexAlign.SpaceBetween })

        Text('alignContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')
        AlignContentFlex({ alignContent: FlexAlign.SpaceAround })

        Text('alignContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({
          wrap: FlexWrap.Wrap,
          alignContent: FlexAlign.SpaceEvenly
        }) {
          Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)
          Text('2').width('50%').height(20).backgroundColor(0xD2B48C)
          Text('3').width('50%').height(20).backgroundColor(0xF5DEB3)
          Text('4').width('50%').height(20).backgroundColor(0xD2B48C)
          Text('5').width('50%').height(20).backgroundColor(0xF5DEB3)
        }
        .size({ width: '90%', height: 100 })
        .padding({ left: 10, right: 10 })
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/JyQVxt15Rsyg6jeam5l_mQ/zh-cn_image_0000002531105846.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=A5DD9F4E848560718667546D5AF04EB1FD47980D9B4C53D9F472D5DA2528BCD4)

### 示例6（子组件单/多行排列时的主/交叉轴间距）

该示例通过设置space为单/多行排列的子组件确定在主/交叉轴上的间距。

```typescript
import {LengthMetrics} from '@kit.ArkUI';

@Entry
@Component
struct FlexExample2 {
  build() {
    Column() {
      Column({ space: 5 }) {
        Text('Wrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.Wrap, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) {
          Text('1').width('40%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('40%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('40%').height(50).backgroundColor(0xD2B48C)
        }
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('NoWrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.NoWrap, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) {
          Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
        }
        .width('90%')
        .padding(10)
        .backgroundColor(0xAFEEEE)

        Text('WrapReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
        Flex({ wrap: FlexWrap.WrapReverse, direction:FlexDirection.Row, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) {
          Text('1').width('40%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('40%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('40%').height(50).backgroundColor(0xD2B48C)
        }
        .width('90%')
        .height(120)
        .padding(10)
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/9qOP2OR_Q8qBrcZ59-AMnw/zh-cn_image_0000002531225780.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=2B5344EB380F7DB7D43CBA69C66EB16FDE8B4F88644A68CE9CEB75FA34FA146B)

### 示例7（宽度自适应的Flex容器）

该示例实现了Flex在宽度设置auto后可以自适应子组件布局的能力。

```typescript
@Component
struct Demo {
  @Require @Prop text: string

  build() {
    Button() {
      Flex() {
        Image($r('sys.media.ohos_ic_public_voice'))
          .width(16)
          .height(16)

        Row() {
          Text(this.text)
            .margin({
              left: 6,
              right: 6
            })
            .fontSize(14)
            .maxLines(1)
            .textOverflow({ overflow: TextOverflow.Ellipsis })
        }

        Image($r('sys.media.ohos_ic_public_sound'))
          .width(16)
          .height(16)
      }.width('auto')
    }
    .backgroundColor(0xAFEEEE)
    .height(36)
    .padding({ left: 16, right: 16 })
    .constraintSize({ maxWidth: 156 })
    .width('auto')
  }
}

@Entry
@Component
struct Index {
  build() {
    Column({ space: 12 }) {
      Text('Width does not reach max length').fontSize(11).fontColor(0XCCCCCC).width('50%')
      Demo({ text: '123' })
      Text('Width reaches max length').fontSize(11).fontColor(0XCCCCCC).width('50%')
      Demo({ text: '1234567890-1234567890-1234567890-1234567890' })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/ITRe5Wz5TX21VwcP-5rhrw/zh-cn_image_0000002562025763.png?HW-CC-KV=V1&HW-CC-Date=20260320T122153Z&HW-CC-Expire=86400&HW-CC-Sign=0D4B89E2EACD44BD0AE13B3ED3749CBCA284304A9532E446F47CEEA90B510467)
