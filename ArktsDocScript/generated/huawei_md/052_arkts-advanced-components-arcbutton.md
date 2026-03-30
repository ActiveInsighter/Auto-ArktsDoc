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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/Rui6NG7lTCWEsIGYzFZbAQ/zh-cn_image_0000002532906000.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=5E36004A654988BAE4A0A48C9260A5EA2BF0F8FB850196FB0F7CA6F5055F75AA)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

- 下弧形按钮（默认类型）。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM_EDGE，可以将按钮设置为下弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/8V2eyAoYRIOv2fTzExl3Mw/zh-cn_image_0000002533065948.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=9587187AEB10ADA4F4D714622E1D33DF558837CFC190D4F32E6D4BAB31FC5461)
- 上弧形按钮。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP_EDGE，可以将按钮设置为上弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/41CZv6Q1QT2zQ_Tn67-MCg/zh-cn_image_0000002563865851.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=0CEE5432577D54BFBA56126451FA7411601A25E03650F0FB43AE431B13B63ED6)

## 自定义样式

- 设置背景色。 使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2ieIsuuCQJC4Jom6Bsityw/zh-cn_image_0000002563785897.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=2F0583706459D476AE0FA4E44F3EBCA012043EEE7192C07444F5311FFCB72C18)
- 设置文本颜色。 使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#E84026'),  fontColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/YzRSSLxDT1mU83E2wyQ4Gg/zh-cn_image_0000002532906002.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=C3CF79463156DD0FB3B26E70A9619E5B1CD89696A2F1FAEAB460E4918B8D4B05)
- 设置阴影颜色。 使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  shadowEnabled: true,  shadowColor: ColorMetrics.resourceColor('#ffec1022')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/zV5hLr4NTl6jWEhMEzRjnw/zh-cn_image_0000002533065950.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=45D2C67B128BFFEEF37B45D1979EF2954D5158EE2B82B3D04EFE07E1A21A09EE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LPLgg8o5TQKuiV7XAwEDvg/zh-cn_image_0000002563865853.png?HW-CC-KV=V1&HW-CC-Date=20260330T095155Z&HW-CC-Expire=86400&HW-CC-Sign=D81FADA38E3AF7858084AB2135C95802004DA328232505B85C66DA3CC433563F)
