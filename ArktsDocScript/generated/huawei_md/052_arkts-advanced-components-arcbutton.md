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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/mbZpy9KKQTuhEM2jC-6gww/zh-cn_image_0000002537332906.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=BDEF10B279922472BA37C7623CCDB7B95627CA35C8146D1DD1B193E5115F462B)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

- 下弧形按钮（默认类型）。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM_EDGE，可以将按钮设置为下弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/n9ijNZi1TRuLN0Gjo29qsg/zh-cn_image_0000002568172703.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=F5E8AEB2A721D7952D797376D1E3D4BE808C325452F6D82AAC6EBF98BAF48D40)
- 上弧形按钮。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP_EDGE，可以将按钮设置为上弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/3VpiHYeURJSDYOydN_U8hQ/zh-cn_image_0000002568252699.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=AAC4FFFA41797C72FD5B29E697BA0A937C5C8E857A4BA66D88383528CA2FD315)

## 自定义样式

- 设置背景色。 使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/UeHW6Y5CT9uZ2Vo8chHUYw/zh-cn_image_0000002537172986.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=C2C69019168D15E23A37DE3EC013D20A0DA16D84AC0EA21E133A1B6F56F9600C)
- 设置文本颜色。 使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#E84026'),  fontColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/BqOBrz0qQeqPiamJgnJvBQ/zh-cn_image_0000002537332908.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=AD72C6455D9D0B3B38EADC364F95A813B7671B1E8BAD12EC6291BA0B8ACF00EE)
- 设置阴影颜色。 使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  shadowEnabled: true,  shadowColor: ColorMetrics.resourceColor('#ffec1022')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/UlPbXVfTTWuN4jup2aGt0A/zh-cn_image_0000002568172705.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=483BB65DE53E4318FFF27B08AEAA918E5EB59A4338DED735C8D398A84E15A0EF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/r6H5OBCNRjCnIbCldSJLyg/zh-cn_image_0000002568252701.png?HW-CC-KV=V1&HW-CC-Date=20260409T023741Z&HW-CC-Expire=86400&HW-CC-Sign=9C82F23E0A5F6C3583E63B5DBD8FB0EC585AF08D26059DCFA133133977C8AFF4)
