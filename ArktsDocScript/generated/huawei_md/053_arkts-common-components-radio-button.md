# 单选框 (Radio)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-radio-button

Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。具体用法请参考[Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)。

## 创建单选框

Radio通过调用[RadioOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio#radiooptions对象说明)来创建，以RadioOptions中的value和group为例：

```typescript
Radio(options: {value: string, group: string})
```

其中，value是单选框的名称，group是单选框的所属群组名称。checked属性可以设置单选框的状态，状态分别为false和true，设置为true时表示单选框被选中。

Radio支持设置选中状态和非选中状态的样式。

```typescript
Radio({ value: 'Radio1', group: 'radioGroup' })
  .checked(false)
Radio({ value: 'Radio2', group: 'radioGroup' })
  .checked(true)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/CZoPYNr_RpW_2-y4GXu7PQ/zh-cn_image_0000002569128523.png?HW-CC-KV=V1&HW-CC-Date=20260413T025744Z&HW-CC-Expire=86400&HW-CC-Sign=ECF6463019471D676082B48B9ED6B046BF379402B8E233DD5DBBE867038A3E54)

## 添加事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，Radio还用于选中后触发某些操作，可以绑定onChange事件来响应选中操作后的自定义行为。

```typescript
Radio({ value: 'Radio1', group: 'radioGroup' })
  .onChange((isChecked: boolean) => {
    if(isChecked) {

    }
  })
Radio({ value: 'Radio2', group: 'radioGroup' })
  .onChange((isChecked: boolean) => {
    if(isChecked) {

    }
  })
```

## 场景示例

通过点击Radio切换声音模式。

```typescript
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct RadioExample {
  @State rst: promptAction.ShowToastOptions = { 'message': 'Ringing mode.' };
  @State vst: promptAction.ShowToastOptions = { 'message': 'Vibration mode.' };
  @State sst: promptAction.ShowToastOptions = { 'message': 'Silent mode.' };

  build() {

      Row() {
        Column() {
          Radio({ value: 'Ringing', group: 'radioGroup' }).checked(true)
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {

                this.getUIContext().getPromptAction().openToast(this.rst);
              }
            })
          Text('Ringing')
        }

        Column() {
          Radio({ value: 'Vibration', group: 'radioGroup' })
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {

                this.getUIContext().getPromptAction().openToast(this.vst);
              }
            })
          Text('Vibration')
        }

        Column() {
          Radio({ value: 'Silent', group: 'radioGroup' })
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {

                this.getUIContext().getPromptAction().openToast(this.sst);
              }
            })
          Text('Silent')
        }
      }.height('100%').width('100%').justifyContent(FlexAlign.Center)

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/QS3z3GqbThOQuRacShqwTg/zh-cn_image_0000002538128802.gif?HW-CC-KV=V1&HW-CC-Date=20260413T025744Z&HW-CC-Expire=86400&HW-CC-Sign=AA588FD744611816B9F4CFB5778DDB66AE70C51DCF9EF06DF42171918CB470E6)
