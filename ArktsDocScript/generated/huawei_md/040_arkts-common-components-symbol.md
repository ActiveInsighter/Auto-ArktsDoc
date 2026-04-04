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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/sPrX1KzUQGGtg2A14IGqkg/zh-cn_image_0000002566708187.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=15C3AA843DF8389A3FB12F5D5291CDD997C140BC3454D815E09C09FDC9ABAC1B)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。 SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。 ```typescript Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/pR6G1of1SFWtTAjjy6eAow/zh-cn_image_0000002535788390.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=A4F85D2DAF681E89834034C1B8C40C4D7636CB94DE247B7A417F1C5B98A754E5)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。 ```typescript Row() {  Column() {  Text('48')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(48)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('72')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(72)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('96')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ZiASXD8uQfiAF33aFyhl4A/zh-cn_image_0000002535948336.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=F1B7471A19E72B6D9DCA0F9E01CB7D7484361E8E181DA97E203A800E85BAB643)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。 ```typescript Row() {  Column() {  Text('Light')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Lighter)  .fontSize(96)  }  }  Column() {  Text('Normal')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96)  }  }  Column() {  Text('Bold')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Bold)  .fontSize(96)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JC0Xuf7pSaav2HzO3v83bw/zh-cn_image_0000002566868169.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=46ADD002AD3DFE640EE137EE64E99B59B821823519D7B24893DC8095754201CF)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。 ```typescript Row() {  Column() {  Text('Black')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Black])  }  }  Column() {  Text('Green')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Green])  }  }  Column() {  Text('Pink')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Pink])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1ZLfkZVaT-S5ohssZjCY2A/zh-cn_image_0000002566708189.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=32544FE844F23F38180D8B0DA17F95DDF7CAB3E6A3100B70C341E06CF7F006C6)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。 ```typescript Row() {  Column() {  Text($r('app.string.single_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.multi_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.hierarchical'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/7yEAj5CDTVSUlxP4aumhiA/zh-cn_image_0000002535788394.png?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=81CB2B893CBC0F6415A65AFE7CDCBCB147A1B679F4BF0F9CD7EA4410051D4955)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。 ```typescript Row() {  Column() {  Text($r('app.string.no_action'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.NONE)  }  }  Column() {  Text($r('app.string.overall_scaling_animation_effect'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.SCALE)  }  }  Column() {  Text($r('app.string.hierarchical_animation'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/-3LKfrzcQKWLZgfpqVETzw/zh-cn_image_0000002535948340.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=35FDD97762BC043C4F9D6EBCB18CDA1151C8E12E791BAB7ED44B04226ECF2414)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。 ```typescript @State isActive: boolean = true; ``` ```typescript Column() {  Text($r('app.string.variable_color_animation'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/3XYLuxhPTN2D1BJDCtVDdw/zh-cn_image_0000002566868171.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=8D1F256A5E26492773A8259C0E00D546CA314137D113A091C02643A598B1DA64)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; ``` ```typescript Column() {  Text($r('app.string.bounce_animation'));  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))  .fontSize(96)  .fontColor([Color.Gray])  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/iCZiA4GARAitl9I5rr3nbg/zh-cn_image_0000002566708191.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=C0E05CC756ABC2C008C6B22ADB73ED6A3238F9ED2EC3238EE737F4C25DDDE4EE)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; @State renderMode: number = 1; ``` ```typescript Column() {  Text($r('app.string.disable_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))  .fontSize(96)  .renderingStrategy(this.renderMode)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/V9NPxbCSQkapwHYocqz8KQ/zh-cn_image_0000002535788396.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=1A4B12CF40B2FCBDC496AB9FD6B6831329F289420BDF8F594285C191246DC649)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; ``` ```typescript Column() {  Text($r('app.string.quick_replacement_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))  .fontSize(96)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/XqvrA_-1QHaI91AaSw7KzQ/zh-cn_image_0000002535948342.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=91D8CF9532DFE18384263CCC92BFBFCB310FC36F7133593F15102396E7D90DBF)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。 ```typescript @State isActive: boolean = true; options: ShadowOptions = {  radius: 10.0,  color: Color.Blue,  offsetX: 10,  offsetY: 10, }; ``` ```typescript Column() {  Text($r('app.string.shadow_ability'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)  .symbolShadow(this.options)  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/BsF7bOhCSiGScR6xRVDq9w/zh-cn_image_0000002566868175.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=651F9B164431ECA680C33938D95B83893EFD9C95D87292BD635347AD29CBA926)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。 ```typescript radialGradientOptions: RadialGradientOptions = {  center: ['50%', '50%'],  radius: '20%',  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true, }; ``` ```typescript Column() {  Text($r('app.string.radial_gradient'))  .fontSize(18)  .fontColor(0xCCCCCC)  .textAlign(TextAlign.Center)  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)]) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/HcePVFrySMm0nNW0HoB-rA/zh-cn_image_0000002566708195.jpg?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=445A2AA97B653D537D91D73B2B7E05B8FA8EDA8E88EE842D0E527E9FB1F0252A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xffhuqXLRWuLaFp4nTUXRg/zh-cn_image_0000002535788400.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=C22A10822F1FFE6030E30B57E76189E9C4A4F828685E6A48BAB94367F7E1C321)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-x20uNusT7aw71Opk-o2gw/zh-cn_image_0000002535948346.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023010Z&HW-CC-Expire=86400&HW-CC-Sign=B3784129717E2319B448C6800063D74C673739EA62FDC33F666F06A5ED889A51)
