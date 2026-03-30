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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/S8HQcaupS2y15tQRU6gXWg/zh-cn_image_0000002534250452.png?HW-CC-KV=V1&HW-CC-Date=20260330T121545Z&HW-CC-Expire=86400&HW-CC-Sign=C9AA4966E4187AB173E474BD432F68394DE2D4FE8BC061DD170DE48AC1BF0DF1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/l8IAY2TgSNCaUbaSsL3j2A/zh-cn_image_0000002534410398.gif?HW-CC-KV=V1&HW-CC-Date=20260330T121545Z&HW-CC-Expire=86400&HW-CC-Sign=43CDC539AEFE2646FF68F1CFCBA28853D879F1EE92F16CB093DDAFC4FB20FA5A)
