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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/irxHYJGOQ_KInTTe9W3hbw/zh-cn_image_0000002565290297.png?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=671DB681E31D73F7A87D88EC43E5C83CCA6C66F42E63B08E413CEAD5C2191F6D) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/LjYOUYk1RzaCeGsxNY7f-A/zh-cn_image_0000002565210277.png?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=D39993F6267BD41084A518A9CE5A1FF3E2CF9D189BE0F5FD6449FF01AE9E2A66)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') // 请开发者替换为实际的id Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') // 请开发者替换为实际的id ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/7vUHXp_oQ8STUG-WbhJbZw/zh-cn_image_0000002534250454.png?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=002770122EE6D1E8F2D36C3FA3503906D180727341C01FE8CD65D6C4B4C694DB)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink) // ···  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  // ···  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/GCdFm_GBQVCn544uIbPRFA/zh-cn_image_0000002534410400.png?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=0DD24A0BB9B453475075141653BEE27312164845A78807B7B5CCEF137D5701B4)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink)  // ··· Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink)  // ··· ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/SpYRI3yvQHSgSDQRaV5SDQ/zh-cn_image_0000002565290299.png?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=6A6CAF10B5A4F8C46E703B1772B4F8D44F14682C9F3F95180B40F810C51E94F1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/qS1C6bHLTS-JBR6C0N33Cg/zh-cn_image_0000002565210279.gif?HW-CC-KV=V1&HW-CC-Date=20260330T121546Z&HW-CC-Expire=86400&HW-CC-Sign=1702D9BDAF93EEFD270E6E901F8D5559165CD6E5BD47E98FFBDBFF948A58C943)
