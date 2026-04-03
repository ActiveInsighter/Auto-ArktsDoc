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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/LqZpf7XbS0m9DDqDieJ-yw/zh-cn_image_0000002535299368.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=10FD1D68976500ACE525BC275CB4C00A0086233BDF4CC1CB9DDEE526635E5EBE)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。 SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。 ```typescript Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_3MNmkRdTbyefObJEv892w/zh-cn_image_0000002566019231.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=14BADA6335365B0F084F495AB5938A3433687DFB513F1D675A112FCF256E242E)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。 ```typescript Row() {  Column() {  Text('48')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(48)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('72')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(72)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('96')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/i_DkRajzTAukNzYs30QSXg/zh-cn_image_0000002566099243.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=4B6860D7C618EBA1C7E1232D705738C22C1B0556610BEA903C93190146C2BF7A)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。 ```typescript Row() {  Column() {  Text('Light')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Lighter)  .fontSize(96)  }  }  Column() {  Text('Normal')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96)  }  }  Column() {  Text('Bold')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Bold)  .fontSize(96)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/fC_HMRX-Tn6yk7Hd_kx66g/zh-cn_image_0000002535139432.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=5217E824D2011D35A68AD69C8D5A767F69F0FCFBF8C7CDC42DF618C26186E85D)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。 ```typescript Row() {  Column() {  Text('Black')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Black])  }  }  Column() {  Text('Green')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Green])  }  }  Column() {  Text('Pink')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Pink])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/47n_Zbi-Rdi2zuukGX-FqQ/zh-cn_image_0000002535299370.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=F7B2AEFE73082B78AC15F140D08D3DB46964A5D053808A61BBA91AE807DE88B0)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。 ```typescript Row() {  Column() {  Text($r('app.string.single_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.multi_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.hierarchical'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/A82yweAOSOWTT4I311tBiA/zh-cn_image_0000002566019233.png?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=D34160E203E9A184561081465908185744461C56C858230841F1C7EA87490729)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。 ```typescript Row() {  Column() {  Text($r('app.string.no_action'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.NONE)  }  }  Column() {  Text($r('app.string.overall_scaling_animation_effect'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.SCALE)  }  }  Column() {  Text($r('app.string.hierarchical_animation'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/YNmNI-TkSfC5PzSB6Z1xGg/zh-cn_image_0000002566099245.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=774507BE2F33C31AE823AEEAA81D2A398435EFF56714DA66338DD1A309EBABEF)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。 ```typescript @State isActive: boolean = true; ``` ```typescript Column() {  Text($r('app.string.variable_color_animation'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/uHNTMwTASiiNspAMY1_DDQ/zh-cn_image_0000002535139434.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=7A298481D1DACE95F6129A32FCD0F48AE8D698EFC6B0965E1E8F8E48EAD4F303)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; ``` ```typescript Column() {  Text($r('app.string.bounce_animation'));  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))  .fontSize(96)  .fontColor([Color.Gray])  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/HwHrBoJJSD64yo0z3QugRg/zh-cn_image_0000002535299372.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=642DD69B00309A95E01F64476DB4D49310AD0673A674FBE97FD3200B19E27D60)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; @State renderMode: number = 1; ``` ```typescript Column() {  Text($r('app.string.disable_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))  .fontSize(96)  .renderingStrategy(this.renderMode)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/c4Ki3oOWSwitfnulnOy_Aw/zh-cn_image_0000002566019235.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=F2F2320DB54BD7933A2FCA6E5B8ACF5C5F21327FC0DCD91CA94C475FD7B2C878)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; ``` ```typescript Column() {  Text($r('app.string.quick_replacement_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))  .fontSize(96)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/h4aUaEjBTnag-Np35ZUlPg/zh-cn_image_0000002566099247.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=53B092312083AB57509DC0CB84F3DF40C6D5D71262572BAC7B020644D99B9D4F)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。 ```typescript @State isActive: boolean = true; options: ShadowOptions = {  radius: 10.0,  color: Color.Blue,  offsetX: 10,  offsetY: 10, }; ``` ```typescript Column() {  Text($r('app.string.shadow_ability'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)  .symbolShadow(this.options)  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/fpWdjx8kR5eeS4BdkaMYQg/zh-cn_image_0000002535139436.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=C6C43FE6CD13AE8A621D3C8FBD1158F3297F6EC30F1B37384AB767BDE9603823)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。 ```typescript radialGradientOptions: RadialGradientOptions = {  center: ['50%', '50%'],  radius: '20%',  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true, }; ``` ```typescript Column() {  Text($r('app.string.radial_gradient'))  .fontSize(18)  .fontColor(0xCCCCCC)  .textAlign(TextAlign.Center)  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)]) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/JFpfI5MPSGCxXvyajveUwA/zh-cn_image_0000002535299374.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=4CC80757F407B984375A409506E04948F57EF0780C6A585D3BB945F5F00A3FBF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/PYR_zmQoQG-9WLJ4n7vO4A/zh-cn_image_0000002566019237.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=937C934B7C4E873D98236330F35E516B5EE46C7D53C78EB961846717A7660A4E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-Ws05PAoQ_WDKq0-htqTKA/zh-cn_image_0000002566099249.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023921Z&HW-CC-Expire=86400&HW-CC-Sign=EA131036611D2AD5964E2136114ECA71E9BFB26289D720CA4DFB69AED14B7AA6)
