# 图标小符号 (SymbolGlyph/SymbolSpan)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)和[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)组件的API文档。

## 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

```typescript
SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
  .fontSize(96)
  .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  .fontColor([Color.Black, Color.Green, Color.White])
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/_vggVhQGQbyDJs7jUMSr-A/zh-cn_image_0000002572639867.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=033D216DCA224AD98E962F3EBDC6565524D1012E030F4CCD9936FA50B48BB309)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。 SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。 ```typescript Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/u2LSs-e2SkaYbwekA-Hf1g/zh-cn_image_0000002542119560.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=557FFD18CEE09CE8FE4C61FE3374BBB8EE4863B967C35224C1A711FAC7934344)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。 ```typescript Row() {  Column() {  Text('48')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(48)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('72')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(72)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('96')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/DxRqAPGPRC6v3giEW9muNA/zh-cn_image_0000002572679831.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=6E0A820DD973BE6923259558B8FF623A0F8018D51BDB6DC0D11EA7845750AAC9)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。 ```typescript Row() {  Column() {  Text('Light')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Lighter)  .fontSize(96)  }  }  Column() {  Text('Normal')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96)  }  }  Column() {  Text('Bold')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Bold)  .fontSize(96)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jMMS5ft7RD2xjhTxVlfOkQ/zh-cn_image_0000002541959924.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=76D0BFF866133F73DEEC067ED2F3A8FB925082B98C709E887366E530B98B1560)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。 ```typescript Row() {  Column() {  Text('Black')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Black])  }  }  Column() {  Text('Green')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Green])  }  }  Column() {  Text('Pink')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Pink])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/NEj78jNcRumEraH8xcOo1Q/zh-cn_image_0000002572639869.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=E37B6123EE25D7A0C36CBDAD06E45C0A7A6819862EB1B0962FA6423C34308FA5)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。 ```typescript Row() {  Column() {  Text($r('app.string.single_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.multi_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.hierarchical'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ejSRi-K-SKCBpP8TZ6qY_A/zh-cn_image_0000002542119562.png?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=17BC111D3BEA87B1FB5C8D3D14F677BCA42CCB4F72C52544956D939DAAB30359)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。 ```typescript Row() {  Column() {  Text($r('app.string.no_action'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.NONE)  }  }  Column() {  Text($r('app.string.overall_scaling_animation_effect'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.SCALE)  }  }  Column() {  Text($r('app.string.hierarchical_animation'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/NailFqHYSUGi8sOLrz4qoA/zh-cn_image_0000002572679833.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=816EA8EF5C8A82642D1A36690D65D575617745CA2E84724E949EDFD8CCFE1084)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。 ```typescript @State isActive: boolean = true; ``` ```typescript Column() {  Text($r('app.string.variable_color_animation'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/_Va0BnOlRhugXMnKEB-KGw/zh-cn_image_0000002541959926.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=EB970C5C397CD6E4E5785C10A92DD280A7E72587BF339732E55DD7258696D8B0)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; ``` ```typescript Column() {  Text($r('app.string.bounce_animation'));  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))  .fontSize(96)  .fontColor([Color.Gray])  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JqmEo6OPQl-aAPZ61AW7vQ/zh-cn_image_0000002572639871.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=183139C481F4BE6FA14B028F0284FCCD2A7C6076336975550666BC1C2F0573D2)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; @State renderMode: number = 1; ``` ```typescript Column() {  Text($r('app.string.disable_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))  .fontSize(96)  .renderingStrategy(this.renderMode)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/tr1UGoZ3R0yjsCuJDsQ3Pg/zh-cn_image_0000002542119564.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=4EADE6465864BB2559592DC018B670B7F5E124DBBC5A9DF443CEC5E5D061721F)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; ``` ```typescript Column() {  Text($r('app.string.quick_replacement_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))  .fontSize(96)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Tw4nH1jtRBGX6pVMNMYrBw/zh-cn_image_0000002572679835.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=9DA060B4594980FC12178CDA143FB22B1976A4D416919D0DDB4F6F1484D44A1E)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。 ```typescript @State isActive: boolean = true; options: ShadowOptions = {  radius: 10.0,  color: Color.Blue,  offsetX: 10,  offsetY: 10, }; ``` ```typescript Column() {  Text($r('app.string.shadow_ability'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)  .symbolShadow(this.options)  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Vt12t2UDRwynWgf6YXeQSA/zh-cn_image_0000002541959928.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=77379E80ABF75E2B9A89F5B76A2FAC07AE308AA588F0F626017EBE841E97713D)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。 ```typescript radialGradientOptions: RadialGradientOptions = {  center: ['50%', '50%'],  radius: '20%',  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true, }; ``` ```typescript Column() {  Text($r('app.string.radial_gradient'))  .fontSize(18)  .fontColor(0xCCCCCC)  .textAlign(TextAlign.Center)  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)]) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/eTVclebKRtC1Z1DGfeAoow/zh-cn_image_0000002572639873.jpg?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=7920DB896F1C1E510CC40A6D53C524942A44096C9635F62AFC7C50C2DF43D889)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/e62dkHBuSxC9ifT0oIdKag/zh-cn_image_0000002542119566.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=FC8B1CA693AACEA5F50780743A51207DFA400DC3C8F5A32401F5290AF0E615EF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/MtYSpCMnSM-1AAxNX_ETcw/zh-cn_image_0000002572679837.gif?HW-CC-KV=V1&HW-CC-Date=20260418T024133Z&HW-CC-Expire=86400&HW-CC-Sign=9419D8AEE08B31166049E42E4298FA2D98EDD5E09BDE5D2960F1C4BD4FD2EB5A)
