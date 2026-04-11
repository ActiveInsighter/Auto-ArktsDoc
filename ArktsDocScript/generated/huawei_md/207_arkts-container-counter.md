# Counter
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter

计数器组件，提供相应的增加或者减少的计数操作。

> **说明**
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

可以包含子组件。

## 接口

Counter()

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性。

### enableInc10+

enableInc(value: boolean)

设置增加按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 增加按钮禁用或使能。 默认值：true，true表示可以增加按钮，false表示禁止增加按钮。 |

### enableDec10+

enableDec(value: boolean)

设置减少按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 减少按钮禁用或使能。 默认值：true，true表示可以减少按钮，false表示禁止减少按钮。 |

## 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

### onInc

onInc(event: VoidCallback)

监听数值增加事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 是 | Counter数值增加的回调函数。 |

### onDec

onDec(event: VoidCallback)

监听数值减少事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 是 | Counter数值减少的回调函数。 |

## 示例

该示例展示了Counter组件的基本使用方法。点击+、-按钮可以修改value值。

```typescript
@Entry
@Component
struct CounterExample {
  @State value1: number = 0;
  @State value2: number = 0;

  build() {
    Column({ space: 50 }) {
      Counter() {
        Text(this.value1.toString())
      }
      .onInc(() => {
        this.value1++;
      })
      .onDec(() => {
        this.value1--;
      })

      Counter() {
        Text(this.value2.toString())
      }
      .onInc(() => {
        this.value2++;
      })
      .onDec(() => {
        this.value2--;
      })
      .enableInc(true)
      .enableDec(false)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9Vt1KgZbRe63U87G9WWdaQ/zh-cn_image_0000002538289912.gif?HW-CC-KV=V1&HW-CC-Date=20260411T023700Z&HW-CC-Expire=86400&HW-CC-Sign=F153E3CCA5BF9AB236080801F3C904A188B888D1C1BE89787977E465BC31D9B9)
