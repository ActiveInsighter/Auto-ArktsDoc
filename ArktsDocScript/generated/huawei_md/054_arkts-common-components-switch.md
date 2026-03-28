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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/wsNi3QixQ-ajSHi_cGCpsw/zh-cn_image_0000002533065952.png?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=A7433C52033E15E42DA78F904953D0ED7C203E6BDEEE5CE7D0EB4A650F81B338) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/CGXmPSjKR8ez50vF94wTag/zh-cn_image_0000002563865855.png?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=CE3B4DFAB8F8B89AEA8DB34D19204DFB7C1A9FA19741848C7035B8127D002C3C)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Z9p8bV0dSFyLRjmG1YOnrw/zh-cn_image_0000002563785901.png?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=99B2B0A28FEA4BD55582C3CACB4820819B3A848DA237944A90BAA20C91398255)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/L1YR64TUTDya39-D-JH8Pw/zh-cn_image_0000002532906006.png?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=B6FB974FA5C59559AB7C9D0C1D6C4DF08A5C2D5FA77B0D5CDDE796CCE8138813)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink) Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/mykZ5jxRQeSNyOITxhYgxQ/zh-cn_image_0000002533065954.png?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=753AD4E4A8D634FA91A778268668A0D1EB4110B46F571A68C5914F9688CDCD97)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/GaCjc_CcRNOYFQY6_9Ae0Q/zh-cn_image_0000002563865857.gif?HW-CC-KV=V1&HW-CC-Date=20260328T140938Z&HW-CC-Expire=86400&HW-CC-Sign=4ECDD25F3617A69E18474115AF5DB56148148DEABAC01406D83D5EE83F049872)
