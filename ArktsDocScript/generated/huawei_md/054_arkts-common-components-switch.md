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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/b2AS9BFjTfuSI6hBZF8Fsg/zh-cn_image_0000002542119610.png?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=7EE34D04C8161082E0418046FF6D072C791C1B433DEB73C6288BC75BC8CF1862) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/j3yLcHWXR0WzGYnYPlTCgQ/zh-cn_image_0000002572679881.png?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=28CBEBC2FC3D1B2FF2827BF0E9FBA739AF772DD1076FBCE3C1891A4C3F39285A)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/B1PfX54CSe-5gKWmWSXxAg/zh-cn_image_0000002541959974.png?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=4B007B92AE8CEAC6A11467F3E62536E342AE8ACC34C281E76DAE434292CEE8F5)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/oMfGT511Tfif_N4VZ0PJ4A/zh-cn_image_0000002572639919.png?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=7EDECFA7F78A5840863B463DF84B1CBAFA15F8C4DC240502EC29EE35C7354203)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink) Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/tFeRqvSHRHCGv1O8wCPY4g/zh-cn_image_0000002542119612.png?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=BA621A7DF27FA4338DCD87DF6DA72416091EB83CEECF49C610837C4403AB3B1F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/yBHMFmWEQ363BjUsy-m0_g/zh-cn_image_0000002572679883.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025755Z&HW-CC-Expire=86400&HW-CC-Sign=3C662279D999A3A885C49E1AF25D240A42A844259093E160E44D2FA74EF6C159)
