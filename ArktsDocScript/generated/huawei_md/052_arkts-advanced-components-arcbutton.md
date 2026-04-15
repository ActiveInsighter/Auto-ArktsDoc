# 弧形按钮 (ArcButton)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton

从API version 18开始支持ArcButton。ArcButton是弧形按钮组件，用于圆形屏幕。为手表用户提供强调、普通、警告等样式按钮。具体用法请参考[ArcButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton)。

## 创建按钮

ArcButton通过调用以下接口来创建。

```typescript
ArcButton({
  options: new ArcButtonOptions({
    label: 'OK',
    position: ArcButtonPosition.TOP_EDGE,
    styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,

  })
})
```

其中，[label](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮文字，[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型，[styleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/W_z-TFVQRD2tqMQUoI90YQ/zh-cn_image_0000002571171513.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=9CCAFA92057A4D6E5C4C7426C9AA098E6446214A5D5DD694DE219254AC1523F3)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

- 下弧形按钮（默认类型）。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM_EDGE，可以将按钮设置为下弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/X0BvVurkSK-GkCStp2Zh6Q/zh-cn_image_0000002540771170.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=5CF7E75E5A144B7F83BAF66F4F427CAED394CCAB1E14CF7C653A6898FE801860)
- 上弧形按钮。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP_EDGE，可以将按钮设置为上弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/BWE676e0Q_We86wUQ1PJbw/zh-cn_image_0000002571291469.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=357EFAB966C5AB7F0F25C391CC7CADBFE9433C0D1B5DB0A49D5023B7F4B218D9)

## 自定义样式

- 设置背景色。 使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/XCEskga5TNSW9l3hp4Hw0Q/zh-cn_image_0000002540611520.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=F76BFD7247611D5CFBFEDBCE0A184540BD80107C6EB26E2B76D9D9A4D04A6EA7)
- 设置文本颜色。 使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#E84026'),  fontColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/U2ALJE34THG7GX_yCUjfRA/zh-cn_image_0000002571171515.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=1EFDB47D92BE80CAC12B0DF24C27DCD8C71EF76FAA601D4D5C929F39C8679819)
- 设置阴影颜色。 使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  shadowEnabled: true,  shadowColor: ColorMetrics.resourceColor('#ffec1022')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/7mjqg_XFRomvoL2tjTojAg/zh-cn_image_0000002540771172.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=46C01CE68B932551F16427A8E95A3FE40E3C229E1CDA033800C40578A7B325C8)

## 添加事件

- 绑定onClick事件来响应点击操作后的自定义行为。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  onClick: () => {  hilog.info(DOMAIN, TAG, 'ArcButton onClick');  },  }) }) ```
- 绑定onTouch事件来响应触摸操作后的自定义行为。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  onTouch: (event: TouchEvent) => {  hilog.info(DOMAIN, TAG, 'ArcButton onTouch');  }  }) }) ```

## 场景示例

在亮度设置界面，进度条显示当前亮度为30%。点击重置后，亮度值将被重置为默认的50%。

运行该示例需要Wearable设备的支持。在src/main目录下的工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中[deviceTypes标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)内配置wearable。

```typescript
"module": {

  "deviceTypes": [
    "wearable"
  ],

}
```

```typescript
import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

const BRIGHT_NESS_VALUE = 30;
const BRIGHT_NESS_VALUE_DEFAULT = 50;

@Entry
@ComponentV2
struct BrightnessPage {
  @Local brightnessValue: number = BRIGHT_NESS_VALUE;
  private defaultBrightnessValue: number = BRIGHT_NESS_VALUE_DEFAULT;

  build() {
    RelativeContainer() {

      Text($r('app.string.Brightness'))
        .fontColor(Color.White)
        .id('id_brightness_set_text')
        .fontSize(24)
        .margin({ top: 16 })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

      Text(`${this.brightnessValue} %`)
        .fontColor(Color.White)
        .id('id_brightness_min_text')
        .margin({ left: 16 })
        .alignRules({
          start: { anchor: '__container__', align: HorizontalAlign.Start },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })

      Slider({
        value: this.brightnessValue,
        min: 0,
        max: 100,
        style: SliderStyle.InSet
      })
        .blockColor('#191970')
        .trackColor('#ADD8E6')
        .selectedColor('#4169E1')
        .width(150)
        .id('id_brightness_slider')
        .margin({ left: 16, right: 16 })
        .onChange((value: number, mode: SliderChangeMode) => {
          this.brightnessValue = value;
        })
        .alignRules({
          center: { anchor: 'id_brightness_min_text', align: VerticalAlign.Center },
          start: { anchor: 'id_brightness_min_text', align: HorizontalAlign.End }
        })

      ArcButton({
        options: new ArcButtonOptions({

          label: $r('app.string.Reset'),
          styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
          fontSize: new LengthMetrics(19, LengthUnit.FP),
          onClick: () => {
            this.brightnessValue = this.defaultBrightnessValue;
          }
        })
      })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        })
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/bPa8rN3eTsmYqyCrD66FFA/zh-cn_image_0000002571291471.png?HW-CC-KV=V1&HW-CC-Date=20260415T024833Z&HW-CC-Expire=86400&HW-CC-Sign=1747C27707BC661092DCC805812AFFCACFB776303473475764AB8E60B2F0C98B)
