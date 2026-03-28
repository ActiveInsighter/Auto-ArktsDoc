# Blank
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank

空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。仅当父组件为[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)/[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)/[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)时生效。

> **说明**
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

不支持设置子组件。

## 接口

Blank(min?: number | string)

创建空白填充组件。

从API version 10开始：

- Blank在父容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)主轴方向上未设置大小时会自动拉伸、压缩，设置了大小或容器自适应子节点大小时不会自动拉伸、压缩。
- Blank设置主轴方向大小（size）与min时约束关系为max(min, size)。
- Blank在父容器交叉轴上设置大小时不会撑满父容器交叉轴，交叉轴不设置大小时alignSelf默认值为ItemAlign.Stretch，会撑满容器交叉轴。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| min | number | string | 否 | 空白填充组件在容器主轴上的最小大小。 默认值：0，number类型单位为vp, string类型可以显式指定[像素单位](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)，如'10px'。不指定像素单位时，默认单位vp，如'10'，等同于10vp。 非法值：按默认值处理。 **说明：** 不支持设置百分比。负值使用默认值。当最小值大于容器可用空间时，使用最小值作为自身大小并超出容器。 |

## 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

### color

color(value: ResourceColor)

设置空白填充的填充颜色，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 是 | 空白填充的填充颜色。 默认值：Color.Transparent 非法值：按默认值处理。 |

## 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## 示例

### 示例1（占满空余空间）

Blank组件在横竖屏占满空余空间效果。

```typescript
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.width('100%').backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })
    }.backgroundColor(0xEFEFEF).padding(20)
  }
}
```

竖屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ZmrtFj1_R6SOKVhiJeBRZA/zh-cn_image_0000002563867049.gif?HW-CC-KV=V1&HW-CC-Date=20260328T073419Z&HW-CC-Expire=86400&HW-CC-Sign=9654673E1F654013974779491C92BA1108252DD5420AACE71FD16E84205DCBCB)

横屏状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/f_SDMz-QQl2XMnn6UPRVYQ/zh-cn_image_0000002563787095.gif?HW-CC-KV=V1&HW-CC-Date=20260328T073419Z&HW-CC-Expire=86400&HW-CC-Sign=BC9D76F747F3EE64695947923337665AABD4293ECD3B4E23D51D1AE3EC742CA4)

### 示例2（填充固定宽度）

Blank组件的父组件未设置宽度时，min参数的使用效果。

```typescript
@Entry
@Component
struct BlankExample {
  build() {
    Column({ space: 20 }) {

      Row() {
        Text('Bluetooth').fontSize(18)
        Blank().color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

      Row() {
        Text('Bluetooth').fontSize(18)

        Blank('160').color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

Blank父组件未设置宽度时，子组件间无空白填充，使用min参数设置填充尺寸

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/xBQucRGaR5-7PlN1uZ9xVQ/zh-cn_image_0000002532907200.png?HW-CC-KV=V1&HW-CC-Date=20260328T073419Z&HW-CC-Expire=86400&HW-CC-Sign=FC5EA76C627EBA6C021ECD90C472B1C8E9EED2FF4CD4296754F7A025E7E18CCE)
