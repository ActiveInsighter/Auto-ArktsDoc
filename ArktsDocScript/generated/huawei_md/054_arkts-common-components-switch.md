# 切换按钮 (Toggle)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch

Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)。

## 创建切换按钮

Toggle通过调用[ToggleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#toggleoptions18对象说明)来创建，具体调用形式如下：

```typescript
Toggle(options: { type: ToggleType, isOn?: boolean })
```

其中，ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态。

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

接口调用有以下两种形式：

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/invAGEEAR8ma22jjjRbQOw/zh-cn_image_0000002538288736.png?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=D0A66E541693063FB1C5F5CFAD094A7361C51748A5EDE2947D8BD32001F73466) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SIgiwr9_SSS3K2VFuQu8aw/zh-cn_image_0000002569168499.png?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=22F53B987BDC40EE3874817D4BE8EB31B78E51BA8CD6003CE1B35600E77EA53E)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/BZhzpJhOQpefQp8wMS0HtQ/zh-cn_image_0000002569128525.png?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=8E27051C3213C3A629635C387A5F421EE8E512CD8F1A361236902F25902C9F1B)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/TDL0fS2BQCeCDU9S3NWh1w/zh-cn_image_0000002538128804.png?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=2C1C28BB5A835074F23C657961922839109D39898483ED86B3EE113C3D0B7A5A)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink) Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/uEv5rbFtRquJy-ddD1xeag/zh-cn_image_0000002538288738.png?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=7A0225CCAF34E113460C35BD40C1DE6F1F7662A3A3AFEAEC417664C7BEB03685)

## 添加事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```typescript
Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
    if(isOn) {

    }
  })
```

## 场景示例

Toggle用于切换蓝牙开关状态。

```typescript
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct ToggleSample {
  @State message: string = 'off';
  pathStack: NavPathStack = new NavPathStack();

  build() {

      Column({ space: 8 }) {
        Column({ space: 8 }) {
          Text('Bluetooth Mode: ' + this.message)
            .id('message')
          Row() {
            Text('Bluetooth')
            Blank()
            Toggle({ type: ToggleType.Switch })
              .id('toggle')
              .onChange((isOn: boolean) => {
                if (isOn) {
                  this.message = 'on';
                  promptAction.openToast({ 'message': 'Bluetooth is on.' });
                } else {
                  this.message = 'off';
                  promptAction.openToast({ 'message': 'Bluetooth is off.' });
                }
              })
          }.width('100%')
        }
        .alignItems(HorizontalAlign.Start)
        .backgroundColor('#fff')
        .borderRadius(12)
        .padding(12)
        .width('100%')
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })

    .backgroundColor('#f1f2f3')

    .title($r('app.string.ToggleCaseExample_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/TLjZ6Y61SG20bjCgEoCZTQ/zh-cn_image_0000002569168501.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025321Z&HW-CC-Expire=86400&HW-CC-Sign=034726D1D618536047EBDD2148685B2ED97FB97E437AD5C8DE88C16D41F6D546)
