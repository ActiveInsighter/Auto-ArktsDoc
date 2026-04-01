# 图标小符号 (SymbolGlyph/SymbolSpan)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)和[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)组件的文档。

## 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

```typescript
SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
  .fontSize(96)
  .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  .fontColor([Color.Black, Color.Green, Color.White])
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/bMy3N2DURyGgHp3_PzO09A/zh-cn_image_0000002534410348.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=1D4A9A8D264EB3460DA5FCB564D8B8D91204E56C426C7499EBD47C83D22A4785)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。 SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。 ```typescript Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/XvkqE5AYQXq5v09TWnSxGg/zh-cn_image_0000002565290247.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=AFAFE2A256604204706E79E760AE6ECA69FEDE47F0A0CF5D08EC3A599C91CA90)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。 ```typescript Row() {  Column() {  Text('48')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(48)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('72')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(72)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('96')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/P8YCyf7bSuahPv3cLU_lAA/zh-cn_image_0000002565210227.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=D13375872E894B3E7AFF9C2655969C756A1D1A64E446439DD620D3BF51E5949C)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。 ```typescript Row() {  Column() {  Text('Light')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Lighter)  .fontSize(96)  }  }  Column() {  Text('Normal')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96)  }  }  Column() {  Text('Bold')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Bold)  .fontSize(96)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JbNHAxyWRHmgpvBqLE8PzQ/zh-cn_image_0000002534250404.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=9948CBD085A39749BCE3024C9F0406D19EA6A0E0A367C606B0F495B4FEEEA44C)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。 ```typescript Row() {  Column() {  Text('Black')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Black])  }  }  Column() {  Text('Green')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Green])  }  }  Column() {  Text('Pink')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Pink])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/kyLTf-_wRGaPc-eyCSX-Yg/zh-cn_image_0000002534410350.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=CCBD8F662F4118EA66B588019F9D00C8D24A1DA9D9C7965BD30561E29CB4184F)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。 ```typescript Row() {  Column() {  Text($r('app.string.single_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.multi_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.hierarchical'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Hw2BP99XSKm_OrEfSOPgQQ/zh-cn_image_0000002565290249.png?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=A1AD36F288516E64FE1D7482C0380E44105A38DA721B4828C668895BB15C70A5)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。 ```typescript Row() {  Column() {  Text($r('app.string.no_action'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.NONE)  }  }  Column() {  Text($r('app.string.overall_scaling_animation_effect'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.SCALE)  }  }  Column() {  Text($r('app.string.hierarchical_animation'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/h03t-OOhRCaIQ4n74881Eg/zh-cn_image_0000002565210229.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=40653B8BAE7C21D99E31D5EFBBA9F18124EE31FF0FE56F302444AFEE09D52842)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。 ```typescript @State isActive: boolean = true; ``` ```typescript Column() {  Text($r('app.string.variable_color_animation'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/wvxqmijISTy6pJutjkXTgg/zh-cn_image_0000002534250406.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=B0C8AE23757540B7A606B1E682A08F8A2DA9996A09AF2661061FB5BE7AEDC6E9)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; ``` ```typescript Column() {  Text($r('app.string.bounce_animation'));  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))  .fontSize(96)  .fontColor([Color.Gray])  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/KbJLR2lDSzyaCd0WfNWLNQ/zh-cn_image_0000002534410352.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=8A4ABC62DC34F83D573E8F6910C722E8E170A08CE88B579A20635B365C4B6BCF)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; @State renderMode: number = 1; ``` ```typescript Column() {  Text($r('app.string.disable_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))  .fontSize(96)  .renderingStrategy(this.renderMode)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ndRPj4nhRFmmXvUNNoR2gA/zh-cn_image_0000002565290251.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=D0DFB1D6C78E1AF063533AEF72F3536DFB17F2C2DBBE8F57EBBAA02EABDF8479)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; ``` ```typescript Column() {  Text($r('app.string.quick_replacement_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))  .fontSize(96)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/n1zUyHLDTUy4K5RYCX_efw/zh-cn_image_0000002565210231.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=F20B4F03A0198F8557E05A45A873CADA25C8B093D366E04300476E7B21FCE64E)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。 ```typescript @State isActive: boolean = true; options: ShadowOptions = {  radius: 10.0,  color: Color.Blue,  offsetX: 10,  offsetY: 10, }; ``` ```typescript Column() {  Text($r('app.string.shadow_ability'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)  .symbolShadow(this.options)  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/dSRXD66xT1utcPjZRqa0lg/zh-cn_image_0000002534250408.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=9B20B97A39F127585492054E05C6596B9584909A8C3CED480BCCD1C7E91DE304)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。 ```typescript radialGradientOptions: RadialGradientOptions = {  center: ['50%', '50%'],  radius: '20%',  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true, }; ``` ```typescript Column() {  Text($r('app.string.radial_gradient'))  .fontSize(18)  .fontColor(0xCCCCCC)  .textAlign(TextAlign.Center)  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)]) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/4wXqECKMTL2nMwqu2Hj4xA/zh-cn_image_0000002534410354.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=AAAEE9DA930AF9B32FA3491C8E55F990AD0D91EBCBABD6AE443CAEEC0D000869)

## 添加事件

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

```typescript
@State wifiColor: ResourceColor = Color.Black;
```

```typescript
SymbolGlyph($r('sys.symbol.ohos_wifi'))
  .fontSize(96)
  .fontColor([this.wifiColor])
  .onClick(() => {
    this.wifiColor = Color.Gray;
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/LESQnFRcRGObPul3mVdwog/zh-cn_image_0000002565290253.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=F452B058966791792803B2773F0FC72FDA0C0086695E1A6C4F5FB4EA04DF30CD)

## 场景示例

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

```typescript
import resourceGetString from '../../common/resource';

@Entry
@Component
struct SymbolMusicDemo {
  @State triggerValueReplace: number = 0;
  @State symbolSources: Resource[] =
    [$r('sys.symbol.repeat'), $r('sys.symbol.repeat_1'), $r('sys.symbol.arrow_left_arrow_right')];
  @State symbolSourcesIndex: number = 0;
  @State symbolText: string[] = [

    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_order').id),

    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_single_repeat').id),

    this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.shuffle_play').id),
  ];
  @State symbolTextIndex: number = 0;
  @State fontColorValue: ResourceColor = Color.Grey;
  @State fontColorValue1: ResourceColor = '#E8E8E8';

  build() {
    Column({ space: 10 }) {
      Row() {
        Text() {

          Span(this.getUIContext()
            .getHostContext()!.resourceManager.getStringSync($r('app.string.current_playlist').id))
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
          Span('（101）')
        }
      }

      Row() {
        Row({ space: 5 }) {
          SymbolGlyph(this.symbolSources[this.symbolSourcesIndex])
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
            .fontSize(20)
            .fontColor([this.fontColorValue])
          Text(this.symbolText[this.symbolTextIndex])
            .fontColor(this.fontColorValue)
        }
        .onClick(() => {
          this.symbolTextIndex++;
          this.symbolSourcesIndex++;
          this.triggerValueReplace++;
          if (this.symbolSourcesIndex > (this.symbolSources.length - 1)) {
            this.symbolSourcesIndex = 0;
            this.triggerValueReplace = 0;
          }
          if (this.symbolTextIndex > (this.symbolText.length - 1)) {
            this.symbolTextIndex = 0;
          }
        })
        .width('75%')

        Row({ space: 5 }) {
          Text() {
            SymbolSpan($r('sys.symbol.arrow_down_circle_badge_vip_circle_filled'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.heart_badge_plus'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }

          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontColor([this.fontColorValue])
              .fontSize(20)
          }
        }
        .width('25%')
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.song_again'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.again_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.song_repeat'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.repeat_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.song_play'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Row() {
        Row() {

          Text($r('app.string.play_song'))
        }.width('82%')

        Row({ space: 5 }) {
          SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
          SymbolGlyph($r('sys.symbol.trash'))
            .fontColor([this.fontColorValue])
            .fontSize(20)
        }
      }

      Divider().width(5).color(this.fontColorValue1).width('98%')
      Column() {

        Text($r('app.string.off'))
      }
      .alignItems(HorizontalAlign.Center)
      .width('98%')
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .height(400)
    .padding({
      left: 10,
      top: 10
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/EDt1EHJCRh6w6BD6CCuyMQ/zh-cn_image_0000002565210233.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132822Z&HW-CC-Expire=86400&HW-CC-Sign=0BE960D649C9684BF56DCB45BEB9E1C9F24683CB248C05E91DC7C77EF1DBB056)
