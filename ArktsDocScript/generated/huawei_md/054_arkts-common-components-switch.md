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

- 创建不包含子组件的Toggle。 当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle： ```typescript Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/H5d_PlnFQyWYRSVjIcGqrQ/zh-cn_image_0000002568172707.png?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=D6F2E2947994283050B29F3220EF3ADEEA1D356097F8BF87ECD9B3166BFD6358) ```typescript Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Anb8Sq5GSOeCxKVHiWF9MQ/zh-cn_image_0000002568252703.png?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=99F7D193468C5757F22862872C7EE6113346A267256846F7FECA8334B396582A)
- 创建包含子组件的Toggle。 当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。 ```typescript Toggle({ type: ToggleType.Button, isOn: false }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle5') Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12) }.width(100).id('toggle6') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ZkbFEhy3Tli1QBquhk33cg/zh-cn_image_0000002537172990.png?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=708DBD203328BF6AAE0A9E66A627AF6B8159F0AEE98EC8B204CA6B365EC1C9B3)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。 ```typescript  Toggle({ type: ToggleType.Button, isOn: true }) {  Text('status button')  .fontColor('#182431')  .fontSize(12)  }.width(100)  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Checkbox, isOn: true })  .selectedColor(Color.Pink)  Toggle({ type: ToggleType.Switch, isOn: true })  .selectedColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/9NlG-iBmS_qyC8UUDz6Baw/zh-cn_image_0000002537332912.png?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=CB8BEB12A9A263844E3B939CF1879FA8289E68B99A02F2C393300FA70F0130AA)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。 ```typescript Toggle({ type: ToggleType.Switch, isOn: false })  .switchPointColor(Color.Pink) Toggle({ type: ToggleType.Switch, isOn: true })  .switchPointColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/AyqAGxmHSSu10t-mKKI5sQ/zh-cn_image_0000002568172709.png?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=AA35D1F7632C710121010C8A8A9EE3C3BDA930A3398EA8ECE02A7F9E5F035FC1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/vPDVUXVlR1GoZ7198C7NZw/zh-cn_image_0000002568252705.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025250Z&HW-CC-Expire=86400&HW-CC-Sign=5CF576207D3F850C3AF3503B9A51AFA7185E775BB0E1DE856D03D38CFB6E84D1)
