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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/VqlVOVOaRjqcN-C2P8wd-g/zh-cn_image_0000002535788462.png?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=011F4D13B7FEF236899B6F80FD5B102FC48B0863BFE8B605FC63DDB0D1777E06) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Q-_t3vMzRn6JU55XqfML2w/zh-cn_image_0000002535948410.png?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=57EAD983FF50862146CDB645E27FFEF70974ADE1DFB451A4E724B2F963CD622B)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') // 请开发者替换为实际的id Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/5n74oi2ySD-FryYMhZLdCQ/zh-cn_image_0000002566868241.png?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=5CFE7C5ECEDD8F3EC9B77DD11D4AEF738A3BFDB57902F7A1497539892E9DDF5F)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink) // ···  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  // ···  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/AGkZmrJVR1aBmXBT6zoYkw/zh-cn_image_0000002566708261.png?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=8D3F35B521585B29D1694AADF68B72A0922426811F7CCBF84B8776BA5867FE35)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink)  // ··· Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/euAHQozJSLmDppUOevH6NQ/zh-cn_image_0000002535788466.png?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=469C496055DEAE6FE1FC09331A7510BDA14805EDA86FE127382D06901DBB48D2)

## 添加事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```typescript
Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
    if(isOn) {
      // 需要执行的操作
      // ···
    }
  })
```

## 场景示例

Toggle用于切换蓝牙开关状态。

```typescript
// xxx.ets
import { promptAction } from '@kit.ArkUI';
@Entry
@Component
export struct ToggleSample {
  @State message: string = 'off';
  pathStack: NavPathStack = new NavPathStack();
  build() {
    // ···
      Column({ space: 8 }) {
        Column({ space: 8 }) {
          Text('Bluetooth Mode: ' + this.message)
            .id('message')
          Row() {
            Text('Bluetooth')
            Blank()
            Toggle({ type: ToggleType.Switch })
              .id('toggle') // 请开发者替换为实际的id
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
    // ···
    .backgroundColor('#f1f2f3')
    // 请将$r('app.string.ToggleCaseExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"toggle蓝牙示例"
    .title($r('app.string.ToggleCaseExample_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/afguYZHZSgmh-nV1maUcZg/zh-cn_image_0000002535948412.gif?HW-CC-KV=V1&HW-CC-Date=20260406T024904Z&HW-CC-Expire=86400&HW-CC-Sign=3A517FC1B1934DEE004D8897129894331954EDAE320FF649CD8ACA12EADDDB24)
