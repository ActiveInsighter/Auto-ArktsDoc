# 禁用反色能力
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-allow-force-dark

设置组件是否使用反色能力，反色能力是在深浅色切换时自动对颜色值进行反色或变换，开发者可以通过主动设置不启用反色算法，以保持在深浅色切换时的原有逻辑。

> **说明**
> 本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记该接口的起始版本。

## allowForceDark

allowForceDark(value: boolean): T

设置组件是否使用反色能力。

> **说明**
> - 当组件主动设置不使用反色能力时，组件及其所有子组件均不使用反色能力，不受父组件或祖先组件主动设置使用反色能力的影响。
> - 该接口仅在开启了反色能力的情况下生效，开启反色能力可参考[利用反色能力快速适配深色模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation#利用反色能力快速适配深色模式)。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 组件是否使用反色能力。true：组件使用反色能力；false：组件不使用反色能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

```typescript
// 组件添加allowForceDark(false)属性后，说明对当前组件不使用反色相关能力。
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Column() {
        Text("Hello World")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            console.info(`Text is clicked`);
          })
      }
      .allowForceDark(false) // Column及其子组件Text不生效反色能力，不受父组件Column使用反色能力的影响。
      Row() {
        Button('BUTTON')
          .backgroundColor(Color.Grey)
          .allowForceDark(true)
          .onClick(() => {
            console.info(`Button is clicked`);
          })
      }
      .allowForceDark(false) // Row及其子组件Button不生效反色能力，不受父组件Column使用反色能力的影响。
    }
    .allowForceDark(true)
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/fRDwejYXRpKXG4iZirl4GQ/zh-cn_image_0000002534411180.png?HW-CC-KV=V1&HW-CC-Date=20260401T025410Z&HW-CC-Expire=86400&HW-CC-Sign=B8496DC20F8842C59D53E88A5EBA19666468CFBE3582EB3F424D62DE8E834EDE)
