# 边框设置
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border

设置组件边框样式。

> **说明**
> 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## border

border(value: BorderOptions): T

设置边框样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#borderoptions) | 是 | 统一边框样式设置接口。 **说明：** 边框宽度默认值为0，即不显示边框。 从API version 9开始，父节点的border显示在子节点内容之上。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

> **说明**
> color、radius缺省时，为了保证[borderColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#bordercolor)、[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)生效，需要将[borderColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#bordercolor)、[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)设置在[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)后。

## borderStyle

borderStyle(value: BorderStyle | EdgeStyles): T

设置元素的边框线条样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#borderstyle) | [EdgeStyles](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edgestyles9)9+ | 是 | 设置元素的边框样式。 默认值：BorderStyle.Solid |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderWidth

borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T

设置边框的宽度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [EdgeWidths](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edgewidths9)9+ | [LocalizedEdgeWidths](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizededgewidths12)12+ | 是 | 设置元素的边框宽度，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderColor

borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T

设置边框的颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | [EdgeColors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edgecolors9)9+ | [LocalizedEdgeColors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizededgecolors12)12+ | 是 | 设置元素的边框颜色。 默认值：Color.Black |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderRadius

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T

设置边框的圆角半径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [BorderRadiuses](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#borderradiuses9)9+ | [LocalizedBorderRadiuses](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedborderradiuses12)12+ | 是 | 设置元素的边框圆角半径，支持百分比，百分比依据组件宽度。设置圆角后，可搭配[clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)属性进行裁剪，避免子组件超出组件自身。 设置四个不同圆角值，若某个圆角值超过高度或者宽度最小值一半时，按值的比例绘制异形圆角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderRadius22+

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T

设置边框的圆角半径和绘制圆角的模式。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length) | [BorderRadiuses](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#borderradiuses9) | [LocalizedBorderRadiuses](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedborderradiuses12) | 是 | 设置元素的边框圆角半径，支持百分比，百分比依据组件宽度。设置圆角后，可搭配[clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)属性进行裁剪，避免子组件超出组件自身。 |
| type | [RenderStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#renderstrategy22) | 否 | 设置组件绘制圆角的模式。 默认值：RenderStrategy.FAST |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

### 示例1（基本样式用法）

设置边框的宽度、颜色、圆角半径以及点、线样式。

```typescript
@Entry
@Component
struct BorderExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {

        Text('dashed')
          .borderStyle(BorderStyle.Dashed).borderWidth(5).borderColor(0xAFEEEE).borderRadius(10)
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)

        Text('dotted')
          .border({ width: 5, color: 0x317AF7, radius: 10, style: BorderStyle.Dotted })
          .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
      }.width('100%').height(150)

      Text('.border')
        .fontSize(50)
        .width(300)
        .height(300)
        .border({
          width: { left: 3, right: 6, top: 10, bottom: 15 },
          color: { left: '#e3bbbb', right: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
          style: {
            left: BorderStyle.Dotted,
            right: BorderStyle.Dotted,
            top: BorderStyle.Solid,
            bottom: BorderStyle.Dashed
          }
        }).textAlign(TextAlign.Center)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/cAuEJlu1Q8KOwAXJ0W4R5w/zh-cn_image_0000002533066748.gif?HW-CC-KV=V1&HW-CC-Date=20260328T073225Z&HW-CC-Expire=86400&HW-CC-Sign=97C161FE093E60B6D2BACB5A9CA3877BCF68A464F4E3AC833560DDF6A37D0432)

### 示例2（边框宽度类型和边框颜色）

border属性的width、radius、color属性值使用LocalizedEdgeWidths类型和LocalizedEdgeColors类型。

```typescript
import { LengthMetrics } from '@kit.ArkUI';
@Entry
@Component
struct BorderExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {

        Text('dashed')
          .borderStyle(BorderStyle.Dashed)
          .borderWidth(5)
          .borderColor(0xAFEEEE)
          .borderRadius(10)
          .width(120)
          .height(120)
          .textAlign(TextAlign.Center)
          .fontSize(16)

        Text('dotted')
          .border({ width: 5, color: 0x317AF7, radius: 10, style: BorderStyle.Dotted })
          .width(120)
          .height(120)
          .textAlign(TextAlign.Center)
          .fontSize(16)
      }.width('100%').height(150)

      Text('.border')
        .fontSize(50)
        .width(300)
        .height(300)
        .border({
          width: {
            start: LengthMetrics.vp(3),
            end: LengthMetrics.vp(6),
            top: LengthMetrics.vp(10),
            bottom: LengthMetrics.vp(15)
          },
          color: { start: '#e3bbbb', end: Color.Blue, top: Color.Red, bottom: Color.Green },
          radius: {
            topStart: LengthMetrics.vp(10),
            topEnd: LengthMetrics.vp(20),
            bottomStart: LengthMetrics.vp(40),
            bottomEnd: LengthMetrics.vp(80)
          },
          style: {
            left: BorderStyle.Dotted,
            right: BorderStyle.Dotted,
            top: BorderStyle.Solid,
            bottom: BorderStyle.Dashed
          }
        })
        .textAlign(TextAlign.Center)
    }
  }
}
```

从左至右显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/m_QJOZMtS9S6QNHMymXmlg/zh-cn_image_0000002563866651.png?HW-CC-KV=V1&HW-CC-Date=20260328T073225Z&HW-CC-Expire=86400&HW-CC-Sign=48CAFF9791FB64D6D0AFEE5836D6F523E89938B05315DEBD808BAECBCF5952B8)

从右至左显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/qPU6usQvR0m_EUZ3eY5qHA/zh-cn_image_0000002563786697.png?HW-CC-KV=V1&HW-CC-Date=20260328T073225Z&HW-CC-Expire=86400&HW-CC-Sign=2D49329A392C582F28BC90833399A40B4634E3C892A7DA8CA97DFDF83A7EB6D3)

### 示例3（设置离屏圆角）

从API version 22开始，该示例支持设置组件绘制圆角的模式。

```typescript
@Entry
@Component
struct RenderStrategyExample {
  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Stack() {
          Column()
            .width(320)
            .height(320)
            .backgroundColor(Color.Black)

          Stack() {
            Stack() {
              Scroll(new Scroller()) {
                Image($r('app.media.startIcon')).width('100%').height('200%')
              }

              Column()
                .blur(50)
                .width(300)
                .height(100)
                .position({ x: 0, y: 0 })
            }
          }
          .width(300)
          .height(300)
          .backgroundColor(Color.Pink)
          .borderRadius(50, RenderStrategy.FAST)
          .clip(true)
        }

        Stack() {
          Column()
            .width(320)
            .height(320)
            .backgroundColor(Color.Black)

          Stack() {
            Stack() {
              Scroll(new Scroller()) {
                Image($r('app.media.startIcon')).width('100%').height('200%')
              }

              Column()
                .blur(50)
                .width(300)
                .height(100)
                .position({ x: 0, y: 0 })
            }
          }
          .width(300)
          .height(300)
          .backgroundColor(Color.Pink)
          .borderRadius(50, RenderStrategy.OFFSCREEN)
          .clip(true)
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

设置在线绘制模式（上方）以及离屏绘制模式（下方）的示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Bw24b8pfSxWkkCNzU2OjVQ/zh-cn_image_0000002532906802.jpg?HW-CC-KV=V1&HW-CC-Date=20260328T073225Z&HW-CC-Expire=86400&HW-CC-Sign=0BE6AFC2D045D083C36E4A83D73F0579BD796D442D4CFC978FDAAA46E2D7CC6E)

### 示例4（设置异形圆角）

该示例通过[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)设置四个不同圆角值。当其中一个圆角值超过高度或宽度最小值的一半时，按值的比例绘制异形圆角。

```typescript
@Entry
@Component
struct BorderExample {
  build() {
    Column() {
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        Text('Text')
          .borderWidth(5)
          .borderColor(0xAFEEEE)
          .borderRadius({
            topLeft: 2000,
            topRight: 10,
            bottomLeft: 30,
            bottomRight: 50
          })
          .width(100)
          .height(100)
          .textAlign(TextAlign.Center)
          .fontSize(16)
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ypq-hJFuSVGtYW4RRpwlug/zh-cn_image_0000002533066750.png?HW-CC-KV=V1&HW-CC-Date=20260328T073225Z&HW-CC-Expire=86400&HW-CC-Sign=9369F171B094CB9298057974DB405C5172BA073858D7B89B2F0161973372EBB3)
