# Flex布局
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout

可以灵活排列、对齐和分配容器内的子组件空间，使元素根据可用空间扩展或收缩，以满足不同屏幕尺寸下的响应式布局。

> **说明**
> - 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
> - 仅[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)或[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)支持下述四种属性，[GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)仅支持设置[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)。

## flexBasis

flexBasis(value: number | string): T

设置组件的基准尺寸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 设置组件在父容器主轴方向上的基准尺寸。 默认值：'auto'（表示组件在主轴方向上的基准尺寸为组件原本的大小）。 string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'）或'auto'，不允许设置百分比字符串。 number：取值范围(0,+∞)，单位为vp。 异常值：默认为'auto'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## flexGrow

flexGrow(value: number): T

设置组件在父容器的剩余空间所占比例。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置父容器在主轴方向上的剩余空间分配给此属性所在组件的比例。 取值范围：[0, +∞) 默认值：0 设置异常值时，该属性为默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## flexShrink

flexShrink(value: number): T

设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

> **说明**
> 使用[getInspectorByKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#getinspectorbykey9)获取flexShrink属性时，如果该节点未设置flexShrink属性，默认返回1。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置父容器压缩尺寸分配给此属性所在组件的比例。 父容器为[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)时，默认值：0，取值范围[0,+∞)。 父容器为[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)时，默认值：1 [constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)限制组件的尺寸范围。[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)和[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)即使设置了[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)，在未设置主轴尺寸（[width](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#width)/[height](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#height)/[size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#size)）时仍遵守默认布局行为，在主轴上自适应子组件尺寸，此时flexShrink不生效。 设置异常值时，该属性为默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## alignSelf

alignSelf(value: ItemAlign): T

子组件在父容器交叉轴的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ItemAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#itemalign) | 是 | 子组件在父容器交叉轴的对齐格式，会覆盖[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)、[GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)布局容器中的alignItems设置。 [GridCol](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)可以绑定alignSelf属性来改变它自身在交叉轴方向上的布局。 默认值：ItemAlign.Auto |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

通过配置flexBasis/flexGrow/flexShrink/alignSelf属性设置Flex布局。

```typescript
@Entry
@Component
struct FlexExample {
  build() {
    Column({ space: 5 }) {
      Text('flexBasis').fontSize(9).fontColor(0xCCCCCC).width('90%')

      Flex() {
        Text('flexBasis(100)')
          .flexBasis(100)
          .height(100)
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
        Text(`flexBasis('auto')`)
          .flexBasis('auto')
          .width('60%')
          .height(100)
          .backgroundColor(0xD2B48C)
          .textAlign(TextAlign.Center)
      }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

      Text('flexGrow').fontSize(9).fontColor(0xCCCCCC).width('90%')

      Flex() {
        Text('flexGrow(2)')
          .flexGrow(2)
          .height(100)
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
        Text('flexGrow(1)')
          .flexGrow(1)
          .height(100)
          .backgroundColor(0xD2B48C)
          .textAlign(TextAlign.Center)
      }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

      Text('flexShrink').fontSize(9).fontColor(0xCCCCCC).width('90%')

      Flex({ direction: FlexDirection.Row }) {
        Text('flexShrink(0)')
          .flexShrink(0)
          .width('50%')
          .height(100)
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
        Text('default flexShrink')
          .width('40%')
          .height(100)
          .backgroundColor(0xD2B48C)
          .textAlign(TextAlign.Center)
        Text('flexShrink(1)')
          .flexShrink(1)
          .width('40%')
          .height(100)
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
      }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

      Text('alignSelf').fontSize(9).fontColor(0xCCCCCC).width('90%')

      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
        Text('no alignSelf,height:70')
          .width('33%')
          .height(70)
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
        Text('alignSelf End')
          .alignSelf(ItemAlign.End)
          .width('33%')
          .height(70)
          .backgroundColor(0xD2B48C)
          .textAlign(TextAlign.Center)
        Text('no alignSelf,height:100%')
          .width('34%')
          .height('100%')
          .backgroundColor(0xF5DEB3)
          .textAlign(TextAlign.Center)
      }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/5ZrZ64QpQVehCXPpkI1ukA/zh-cn_image_0000002542120402.png?HW-CC-KV=V1&HW-CC-Date=20260418T024257Z&HW-CC-Expire=86400&HW-CC-Sign=349CA751D7ACAAFA72A2EAE4DC9CF0E268B5D39781EC1FEFDDF81F9264581308)
