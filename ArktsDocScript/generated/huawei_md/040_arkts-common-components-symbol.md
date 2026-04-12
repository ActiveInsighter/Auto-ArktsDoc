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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/vLlPw7hrR3m2iONEa80hbg/zh-cn_image_0000002538128752.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=6E7988E946B23F198B36FDEDE5B91DDC533FB193DBD40A197D5E54FF62C0A424)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。 SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。 ```typescript Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/rTFW05CDTDeIOQ1xWg45UA/zh-cn_image_0000002538288686.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=6C3543765B5E5E189765194A2E9FAD0810E143162CA414EF503E392E9169BAF7)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。 ```typescript Row() {  Column() {  Text('48')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(48)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('72')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(72)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text('96')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ukRgf1wUTbulR3FwY-hhTQ/zh-cn_image_0000002569168449.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=AB26626FDC57B789BAFE9228328CBD1D8E766DB775D07669393952AA5A893122)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。 ```typescript Row() {  Column() {  Text('Light')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Lighter)  .fontSize(96)  }  }  Column() {  Text('Normal')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Normal)  .fontSize(96)  }  }  Column() {  Text('Bold')  Text() {  SymbolSpan($r('sys.symbol.ohos_trash'))  .fontWeight(FontWeight.Bold)  .fontSize(96)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/E1OkLC_nRYW0woW28-jcwA/zh-cn_image_0000002569128475.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=D5DDCF931868C6859A98034EFB0B5FCA1BC68CBF479C0007A56D9CADAE0702BC)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。 ```typescript Row() {  Column() {  Text('Black')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Black])  }  }  Column() {  Text('Green')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Green])  }  }  Column() {  Text('Pink')  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .fontColor([Color.Pink])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/qyMuqOmoRi2EpAaeR9XMgw/zh-cn_image_0000002538128754.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=6BC5BCD9383B9E5CCE4BAC5229E03AABA22A7C3ABFCEBCE2EF90A4459B66EECD)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。 ```typescript Row() {  Column() {  Text($r('app.string.single_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.SINGLE)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.multi_color'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)  .fontColor([Color.Black, Color.Green, Color.White])  }  }  Column() {  Text($r('app.string.hierarchical'));  Text() {  SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)  .fontColor([Color.Black, Color.Green, Color.White])  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/guKyLYwKRrSrUQFhRelTeg/zh-cn_image_0000002538288688.png?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=0EA6B885628F0FE8D351B710B1246CCB31165E15DA8ACE8428A630D421DF8F23)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。 ```typescript Row() {  Column() {  Text($r('app.string.no_action'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.NONE)  }  }  Column() {  Text($r('app.string.overall_scaling_animation_effect'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.SCALE)  }  }  Column() {  Text($r('app.string.hierarchical_animation'));  Text() {  SymbolSpan($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/iC5lTOxLRf-i5zflBc67Ug/zh-cn_image_0000002569168451.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=074EEE1437FD98A923B5983515B982882AAAB5EA47D024593121CA31D6224A0B)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。 ```typescript @State isActive: boolean = true; ``` ```typescript Column() {  Text($r('app.string.variable_color_animation'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)  Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/dDw1a7ePQ7SDmx9PLHC37A/zh-cn_image_0000002569128477.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=3F50A0F930AEC85C4AAAF77D8CE76B02199427B006A77CCFC0064D5C58C64669)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; ``` ```typescript Column() {  Text($r('app.string.bounce_animation'));  SymbolGlyph($r('sys.symbol.ellipsis_message_1'))  .fontSize(96)  .fontColor([Color.Gray])  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/VJqTZjWsRla0EKongTuUag/zh-cn_image_0000002538128756.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=0A850E778D842A4553CE2594C56591863063CD10C668F79CCE7D433462B4DB99)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; @State renderMode: number = 1; ``` ```typescript Column() {  Text($r('app.string.disable_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))  .fontSize(96)  .renderingStrategy(this.renderMode)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/wz3iHm2IR0KPBzDmbICaVA/zh-cn_image_0000002538288690.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=06E24DE998F9B534FB8B8504826CE40435DB3D3FE86C3381608F32C33CA8694B)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。 ```typescript @State triggerValueReplace: number = 0; replaceFlag: boolean = true; ``` ```typescript Column() {  Text($r('app.string.quick_replacement_animation'));  SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))  .fontSize(96)  .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),  this.triggerValueReplace)  Button('trigger').onClick(() => {  this.replaceFlag = !this.replaceFlag;  this.triggerValueReplace = this.triggerValueReplace + 1;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/ZHrO4Mn3QcOT-QmU_YQ_6Q/zh-cn_image_0000002569168453.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=2DC420A38EA0BCE651BBFFF9ADCD3633868DBBE47C4D72536E801B06AA4603D1)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。 ```typescript @State isActive: boolean = true; options: ShadowOptions = {  radius: 10.0,  color: Color.Blue,  offsetX: 10,  offsetY: 10, }; ``` ```typescript Column() {  Text($r('app.string.shadow_ability'));  SymbolGlyph($r('sys.symbol.ohos_wifi'))  .fontSize(96)  .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)  .symbolShadow(this.options)  Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {  this.isActive = !this.isActive;  }) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/fMt3yYFyRrWmN4C48En6SQ/zh-cn_image_0000002569128479.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=C363483B5D8EDE4139E1DECE3843A397A1F37FAC484FFB5C5F56350A43B11CF9)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。 ```typescript radialGradientOptions: RadialGradientOptions = {  center: ['50%', '50%'],  radius: '20%',  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true, }; ``` ```typescript Column() {  Text($r('app.string.radial_gradient'))  .fontSize(18)  .fontColor(0xCCCCCC)  .textAlign(TextAlign.Center)  SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))  .fontSize(96)  .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)]) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Bj1xQoSITVGtYO3LAzVGiw/zh-cn_image_0000002538128758.jpg?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=BF07DDACEA136FB2D70B539873E6EE7B812B288E80FDDCA1A72DA2BD29EB294F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/PzfJzZK-QGWalMVgl_iIug/zh-cn_image_0000002538288692.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=A274E3CCD5554963455D54869935F72CE0013488E24B5522C70C116BDE8E523C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zZQZ8cQPQDmAH4AYdsAdVg/zh-cn_image_0000002569168455.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025307Z&HW-CC-Expire=86400&HW-CC-Sign=D6F401600CFBFB0290E9064865884898095D3F863788B3BB44190D0E2CB353DF)
