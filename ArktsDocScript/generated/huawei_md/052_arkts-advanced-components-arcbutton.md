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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/DB7qhRIWQ4iOPB_BQagJcQ/zh-cn_image_0000002535299414.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=C2B308B3F241490BE85499EEB7820550FD6B4C092756144450FC6F260770E48D)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

- 下弧形按钮（默认类型）。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM_EDGE，可以将按钮设置为下弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/GzKO4RckQyGtkYv6n66S3w/zh-cn_image_0000002566019277.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=862C736A6E57FB1E18D95F6BF262F912B403427ED6BF37AAF57BB2DED7047B1A)
- 上弧形按钮。 通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP_EDGE，可以将按钮设置为上弧形按钮。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/lJpUztPdT2STct6StosYlQ/zh-cn_image_0000002566099289.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=0668452ACE435ACB6AC867341F10C160144FA5DF8AD511EB32505AEDADAC4270)

## 自定义样式

- 设置背景色。 使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/NuNqBQqjQReCNELOQHJEVw/zh-cn_image_0000002535139478.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=DC45BF9D80B2BDA563A02D7171066129910E604936BA77E68F0C7F8C9026987F)
- 设置文本颜色。 使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  styleMode: ArcButtonStyleMode.CUSTOM,  backgroundColor: ColorMetrics.resourceColor('#E84026'),  fontColor: ColorMetrics.resourceColor('#707070')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/18TyKJ5US3-ul3_q6PYQyA/zh-cn_image_0000002535299416.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=6615C69A767DA3F36BDF4BC97A077AC59B69D6D8D4EC51D1D34B411125C6AB7E)
- 设置阴影颜色。 使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。 ```typescript ArcButton({  options: new ArcButtonOptions({  label: 'OK',  shadowEnabled: true,  shadowColor: ColorMetrics.resourceColor('#ffec1022')  }) }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/CgDnLWaOTyOqFBM0lwenIw/zh-cn_image_0000002566019279.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=C1C6152DECC019576F2ED07379A11EE541A28625FEF73C49DC9ACB4BB2ED1B8F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/fBuo73Z7T1-IOqGfQqBt3w/zh-cn_image_0000002566099291.png?HW-CC-KV=V1&HW-CC-Date=20260403T023933Z&HW-CC-Expire=86400&HW-CC-Sign=E1CCC3B4075033B4467A12A52F014F2B1FA1612CA6B5A9F73C2BDD03CE914ABB)
