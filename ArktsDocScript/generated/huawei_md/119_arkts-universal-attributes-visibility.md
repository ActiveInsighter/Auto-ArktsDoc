# 显隐控制
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility

控制组件是否可见。

> **说明**
> 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## visibility

visibility(value: Visibility): T

控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#visibility) | 是 | 控制当前组件显示或隐藏。根据具体场景需要可使用[条件渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)代替。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

该示例通过配置visibility的不同值，实现不同的显隐控制效果。

```typescript
@Entry
@Component
struct VisibilityExample {
  build() {
    Column() {
      Column() {

        Text('None').fontSize(9).width('90%').fontColor(0xCCCCCC)
        Row().visibility(Visibility.None).width('90%').height(80).backgroundColor(0xAFEEEE)

        Text('Hidden').fontSize(9).width('90%').fontColor(0xCCCCCC)
        Row().visibility(Visibility.Hidden).width('90%').height(80).backgroundColor(0xAFEEEE)

        Text('Visible').fontSize(9).width('90%').fontColor(0xCCCCCC)
        Row().visibility(Visibility.Visible).width('90%').height(80).backgroundColor(0xAFEEEE)
      }.width('90%').border({ width: 1 })
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Kb8rTdvGSxWqEwlr74pFww/zh-cn_image_0000002538129574.png?HW-CC-KV=V1&HW-CC-Date=20260411T023507Z&HW-CC-Expire=86400&HW-CC-Sign=E56874D0E550742D7362C38E30CD704F2D7E07F6E6BCC5AE4442C52D8EB44CF5)
