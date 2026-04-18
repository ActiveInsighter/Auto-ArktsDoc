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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/rAWLXcxTT4Wc_pDsY_OhIw/zh-cn_image_0000002572639913.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=244D7D864C81DE639A1D7B37C8CB856C04A1E3E5C6B71357805A258CBB2D3FB6)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

- 下弧形按钮（默认类型）。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM_EDGE，可以将按钮设置为下弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/q1yzPGEnQG-o5ld0P6V0dA/zh-cn_image_0000002542119606.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=EA82B96197ADF570894C378BD5B657D04DA8CD5B2353463B0D9F2E0A9D78D7ED)
- 上弧形按钮。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP_EDGE，可以将按钮设置为上弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/x2X_xzSXQ1CRug9a0blOnw/zh-cn_image_0000002572679877.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=5988BD8540752FB36A60B4B0605BF5236E09D780A98A136F4A64EA1F29987F51)

## 自定义样式

- 设置背景色。 使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/rhBVg7kSQjCONFpncOtPYA/zh-cn_image_0000002541959970.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=0001AC5C15CA20AA87685ECB52D7D17396937B171786D42D009188525B4B20C0)
- 设置文本颜色。 使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#E84026'),  fontColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/9rz7eZxwQm6A5mnl1Lcjdg/zh-cn_image_0000002572639915.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=CCF478A978A8CF09896C6C97425A92C713F79FC9863DF82AF3660B7D1C8613D7)
- 设置阴影颜色。 使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  shadowEnabled: true,  shadowColor: ColorMetrics.resourceColor('#ffec1022')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/mJh6qsYvTM6HUQE1oSnD-A/zh-cn_image_0000002542119608.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=5D75A9095579915C00AD7C55D68B5B3E1B1B1D6F9D28E535318AE67F68023E82)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/mnX_cQdiSDyo50BdcpTJTA/zh-cn_image_0000002572679879.png?HW-CC-KV=V1&HW-CC-Date=20260418T024146Z&HW-CC-Expire=86400&HW-CC-Sign=460036728F18E1C6EE0A01CB00F2E32CE88C2DC1C06E3295DC9F441D2C2D8466)
