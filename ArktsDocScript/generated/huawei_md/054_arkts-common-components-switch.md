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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/b2AS9BFjTfuSI6hBZF8Fsg/zh-cn_image_0000002542119610.png?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=FD95C279052475036FE726C5886F52CA7F7382FB143B83545F2188F75FFD16FA) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/j3yLcHWXR0WzGYnYPlTCgQ/zh-cn_image_0000002572679881.png?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=2E94505EDEF0605086AEE9DB59C49FC38CF8C5565239EAA568CE58C0A90C58B7)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') // 请开发者替换为实际的id Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/B1PfX54CSe-5gKWmWSXxAg/zh-cn_image_0000002541959974.png?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=60C3E1796792630678312305BACF0B51B99AC327305F03B385BF3C974243B502)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink) // ···  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  // ···  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/oMfGT511Tfif_N4VZ0PJ4A/zh-cn_image_0000002572639919.png?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=E0D05701BBFF7726ABED67BA6C4E7CE007DB2C0F64B70EC947D4080CB01A9D1E)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink)  // ··· Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/tFeRqvSHRHCGv1O8wCPY4g/zh-cn_image_0000002542119612.png?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=4D7F263B567946E7019A51F07DB12CD2E2287F21C0530EAF285B99A17021B7C3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/yBHMFmWEQ363BjUsy-m0_g/zh-cn_image_0000002572679883.gif?HW-CC-KV=V1&HW-CC-Date=20260420T025840Z&HW-CC-Expire=86400&HW-CC-Sign=F59188D85E7ECC632C72F96CCF645BE45BF175B3BCEA19893D5DF1604CBA30E8)
