# 文本显示 (Text/Span)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)组件的使用说明。

常见问题请参考[文本显示（Text/Span）常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

- string字符串。 ```typescript Text('我是一段文本') ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Ox60uyViSrG9ckTqqANt0g/zh-cn_image_0000002565290203.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=4A367910F00A629B860B5D01C7027B492F5AD4DDDABA3B69B2C2E2389DD40FCD)

- 引用Resource资源。 资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下： ```typescript {  "string": [  {  "name": "module_desc",  "value": "模块描述"  }  ] } ``` ```typescript Text($r('app.string.module_desc'))  .baselineOffset(0)  .fontSize(30)  .border({ width: 1 })  .padding(10)  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Kz6Eu297RKCvlcFOKs74-w/zh-cn_image_0000002565210183.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=EF3B673E45FDF1E81BBAE7F25B8A38B9BE40BB3E4A7738C797D0546F84704444)

## 添加子组件

[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)只能作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

- 创建Span。 Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。 ```typescript Text($r('app.string.TextSpan_textContent_text')) {  Span($r('app.string.TextSpan_textContent_span')) } .padding(10) .borderWidth(1) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Y-7VPaUeTwSkQNJCrxXZaw/zh-cn_image_0000002534250360.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=A7A38D96618A8FA5910F2E0EA13409170D3975F561150808E4A53B160E29FAEB)
- 设置文本装饰线及颜色。 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置文本装饰线及颜色。 ```typescript Text() {  Span($r('app.string.TextSpan_textContent_span_one'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })  Span($r('app.string.TextSpan_textContent_span_two'))  .fontColor(Color.Blue)  .fontSize(16)  .fontStyle(FontStyle.Italic)  .decoration({ type: TextDecorationType.Underline, color: Color.Black })  Span($r('app.string.TextSpan_textContent_span_three'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.Overline, color: Color.Green }) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/pqxXraSdQVqetzXmYotmEw/zh-cn_image_0000002534410306.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=F02F65349424582D61A3202B43E951E875A50B426670AB4F23F27A1C04D5B17C)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textcase)设置文字一直保持大写或者小写状态。 ```typescript Text() {  Span('I am Upper-span').fontSize(12)  .textCase(TextCase.UpperCase) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/YDCbg0r8QPiRCFu-ZyHY1w/zh-cn_image_0000002565290205.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=5EC2171E83D1E9B2C3D23AA98EE01F6513F5CB4635104770B3537D6914BC850A)
- 添加事件。 由于Span组件无尺寸信息，仅支持添加点击事件[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、悬浮事件[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover#onhover)。 ```typescript import { hilog } from '@kit.PerformanceAnalysisKit'; @Entry @Component export struct TextSpanOnHover {  @State textStr1: string = '';  @State textStr2: string = '';  build() {  NavDestination() {  Row() {  Column() {  Text() {  Span('I am Upper-span')  .textCase(TextCase.UpperCase)  .fontSize(30)  .onClick(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');  this.textStr1 = 'Span onClick is triggering';  })  .onHover(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');  this.textStr2 = 'Span onHover is triggering';  })  }  Text('onClick：' + this.textStr1)  .fontSize(20)  Text('onHover：' + this.textStr2)  .fontSize(20)  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/8ojBgr9DQUKGx7xKWJncVg/zh-cn_image_0000002565210185.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=91D3DBA9B92289BD9D26A4CE60CDFC0543F2967D89BB9DAFABED3FD63F1B611B)

## 创建自定义文本样式

Text组件支持创建自定义文本样式，以下为修改文本样式的主要属性。

| 属性名称 | 功能描述 |
| --- | --- |
| baselineOffset | 设置文本基线的偏移量。 |
| contentTransition | 设置数字翻牌效果。 |
| copyOption | 设置文本是否可复制粘贴。 |
| decoration | 设置文本装饰线样式，如类型、颜色及其粗细。 |
| enableAutoSpacing | 设置是否开启中文与西文的自动间距。 |
| enableDataDetector | 设置是否进行文本特殊实体识别。 |
| font | 设置文本字体相关属性。 |
| fontColor | 设置文本字体颜色。 |
| fontFamily | 设置文本字体族。 |
| fontFeature | 设置文字特性效果，比如数字等宽的特性。 |
| fontSize | 设置文本字体大小。 |
| fontStyle | 设置文本字体风格。 |
| fontWeight | 设置文本字体粗细。 |
| halfLeading | 设置文本是否将行间距平分至行的顶部与底部。 |
| heightAdaptivePolicy | 设置文本自适应布局调整字号的方式。 |
| letterSpacing | 设置文本字符间距。 |
| lineHeight | 设置文本行高。 |
| lineSpacing | 设置文本的行间距。 |
| marqueeOptions | 设置跑马灯配置项，如开关、步长、循环次数、方向等。 |
| maxFontSize | 设置自适应字体最大尺寸。 |
| maxLines | 设置文本最大显示行数。 |
| minFontSize | 设置自适应字体最小尺寸。 |
| optimizeTrailingSpace | 控制每行末尾空格的优化。 |
| privacySensitive | 设置是否支持卡片敏感隐私信息。 |
| shaderStyle | 设置文本渐变色样式。 |
| textCase | 设置文本大小写转换。 |
| textAlign | 设置文本段落在水平方向的对齐方式。 |
| textIndent | 设置首行文本缩进。 |
| textOverflow | 控制文本超长处理方式。 |
| textSelectable | 设置文本是否可选择。 |
| textVerticalAlign | 设置文本段落在垂直方向的对齐方式。 |
| wordBreak | 设置断行规则。 |

下面对常用的接口进行举例说明。

- 通过[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)属性设置文本对齐样式。 ```typescript Text($r('app.string.TextAlign_Start'))  .width(300)  .textAlign(TextAlign.Start)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_Center'))  .width(300)  .textAlign(TextAlign.Center)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_End'))  .width(300)  .textAlign(TextAlign.End)  .border({ width: 1 })  .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/3sMUA7JXQWmKeeUykcdItw/zh-cn_image_0000002534250362.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=CEFC49BBBD169403A9E2824CBC54A55AA1D10BADD0AAE33878709DD780400FBF)
- 通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。 ```typescript Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +  'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +  'of textOverflow to None text content.')  .width(250)  .textOverflow({ overflow: TextOverflow.None })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_epsis'))  .width(250)  .textOverflow({ overflow: TextOverflow.Ellipsis })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq_def'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .marqueeOptions({  start: true,  fromStart: true,  step: 6,  loop: -1,  delay: 0,  fadeout: false,  marqueeStartPolicy: MarqueeStartPolicy.DEFAULT  }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/MVkoGk4EQKOIKw494E4kgw/zh-cn_image_0000002534410308.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=15C5E3D9B321B4ED87E8A276484D214E2CC754220971839D53C5E1DE5239249B)
- 通过[lineHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#lineheight)属性设置文本行高。 ```typescript Text('This is the text with the line height set. This is the text with the line height set.')  .width(300).fontSize(12).border({ width: 1 }).padding(10) Text('This is the text with the line height set. This is the text with the line height set.')  .width(300)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .lineHeight(20) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/BH00T14kR0GFc3aeaWXdRw/zh-cn_image_0000002565290207.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=9BAB73A5310982FE8BB96E63FE9FF27896D472327C58429990D0C925E86619CC)
- 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性设置文本装饰线样式、颜色及其粗细。 ```typescript Text('This is the text')  .decoration({  type: TextDecorationType.LineThrough,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Overline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DASHED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOTTED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOUBLE  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.WAVY,  thicknessScale: 4  })  .borderWidth(1).padding(15).margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/xw9DPWqQQwCFvyucjMpgDw/zh-cn_image_0000002565210187.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=A0A1A09EA1CAD2413482F4315F860C0ACC868AE924F7B95B048B1B1CBB6A2431)
- 通过[baselineOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#baselineoffset)属性设置文本基线的偏移量。 ```typescript Text('This is the text content with baselineOffset 0.')  .baselineOffset(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset 30.')  .baselineOffset(30)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset -20.')  .baselineOffset(-20)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/5XkypCJXQTmLNe6asnbA3Q/zh-cn_image_0000002534250364.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=2A709FE0941CDC7D0D3CA18BD799DF24C0F81EE25537EB79B3216BF5DF9235C2)
- 通过[letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#letterspacing)属性设置文本字符间距。 ```typescript Text('This is the text content with letterSpacing 0.')  .letterSpacing(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing 3.')  .letterSpacing(3)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing -1.')  .letterSpacing(-1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/cE2T8R_yQ7O7yYIHQUamRQ/zh-cn_image_0000002534410310.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=04C812CF49577F39369A2A9E953BDE612FE99DD7F966369157F9BEFC6953F709)
- 通过[minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#minfontsize)与[maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxfontsize)自适应字体大小。 minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。 ```typescript Text($r('app.string.CustomTextStyle_textContent_one_style'))  .width(250)  .maxLines(1)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_two_style'))  .width(250)  .maxLines(2)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_no_max'))  .width(250)  .height(50)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_high'))  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Fa03cdbPSwyXNPWleTOFEQ/zh-cn_image_0000002565290209.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=B00D8F35BE7561702629B9171ADB7F067A7AEDF4E5A453F2F3343033CBB8FF90)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcase)属性设置文本大小写。 ```typescript Text('This is the text content with textCase set to Normal.')  .textCase(TextCase.Normal)  .padding(10)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to LowerCase.')  .textCase(TextCase.LowerCase)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to UpperCase.')  .textCase(TextCase.UpperCase)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/cKE8DbyFS-6izaSpCtiqag/zh-cn_image_0000002565210189.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=483405F93139911088531B3AB2F404ED909D1A19828AC6592958B35C9B9AFAD8)
- 通过[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性设置文本是否可复制粘贴。 ```typescript Text($r('app.string.CustomTextStyle_textContent_incopy'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/3YpiTmNmT7WK_bwA8FxkMw/zh-cn_image_0000002534250366.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=78FA5ABDC27FB63F0C036CED7504BFDFAE88B5509B1FD0CB6BE9D993DE665AFB)
- 通过[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。 ```typescript Text('This is the text content with fontFamily')  .fontSize(30)  .fontFamily('HarmonyOS Sans') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/IFyDyCSNR-SJI-B2WAwR5w/zh-cn_image_0000002534410312.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=2786854B83CB2FA83A6206B66D6ACE3C215B17001865CC650FEEE5E82F5629DF)
- 从API version 20开始，支持通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#contenttransition20)属性设置数字翻牌效果。 ```typescript @Entry @Component export struct ContentTransition {  private static readonly INITIAL_SCORE: number = 98;  @State number: number = ContentTransition.INITIAL_SCORE;  @State numberTransition: NumericTextTransition =  new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });  build() {  NavDestination() {  Column() {  Text(this.number + '')  .borderWidth(1)  .fontSize(40)  .contentTransition(this.numberTransition)  Button('chang number')  .onClick(() => {  this.number++  })  .margin(10)  }  .width('100%')  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/2MUtzUW2T2aaAfIaxfiZWQ/zh-cn_image_0000002565290211.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=9043033BA963121A433549995D7A993838203C5FF7F248AAB5190B20C48BF2D8)
- 从API version 20开始，支持通过[optimizeTrailingSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。 ```typescript Column() {  Text('Trimmed space enabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(true)  .textAlign(TextAlign.Center)  Text('Trimmed space disabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(false)  .textAlign(TextAlign.Center) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/X4NA2dgvTpWnBOUExloD0g/zh-cn_image_0000002565210191.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=BEA38A55197CAEC4736B30CADAC7023A58BD112FF1CF1E2734FA74F6563BC6EB)
- 从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。 ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Extend(Text) function style() {  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 }) } @Entry @Component export struct LineSpacing {  build() {  NavDestination() {  Column() {  Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })  .style()  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/d06Bc0VFTpSQO3he7y5RRw/zh-cn_image_0000002534250368.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=267DEF6D2A21291AC7BE7B7166F5E071352DD5F6E20B17C274472D7FE37E4494)
- 从API version 20开始，支持通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enableautospacing20)设置是否开启中文与西文的自动间距。 ```typescript @Entry @Component export struct EnableAutoSpacing {  @State enableSpacing: boolean = false;  build() {  NavDestination() {  Column() {  Row({ space: 20 }) {  Button($r('app.string.Enable_automatic_spacing'))  .onClick(() => this.enableSpacing = true)  .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')  .fontColor(this.enableSpacing ? Color.White : Color.Black)  Button($r('app.string.off_automatic_spacing'))  .onClick(() => this.enableSpacing = false)  .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')  .fontColor(!this.enableSpacing ? Color.White : Color.Black)  }  .width('100%')  .justifyContent(FlexAlign.Center)  .margin({ top: 30, bottom: 20 })  Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))  .fontSize(16)  .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')  .margin({ bottom: 20 })  Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))  .fontSize(24)  .padding(15)  .backgroundColor('#F5F5F5')  .width('90%')  .enableAutoSpacing(this.enableSpacing)  }  .width('100%')  .height('100%')  .padding(20)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ldl-SlLDTQKs5TGzDy-PTw/zh-cn_image_0000002534410314.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=890FE84D096EA46FB90F55C101DB07EC4B38D7C5E7BEF1D8A172B6292893A056)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#shaderstyle20)设置渐变色。 ```typescript @Entry @Component export struct ShaderStyle {  @State message: string = 'Hello World';  @State linearGradientOptions: LinearGradientOptions =  {  direction: GradientDirection.LeftTop,  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true,  };  build() {  NavDestination() {  Column({ space: 5 }) {  Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)  .margin({ top: 40, left: 40 })  Text(this.message)  .fontSize(50)  .width('80%')  .height(50)  .shaderStyle(this.linearGradientOptions)  }  .height('100%')  .width('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/239qwoZ1R9u4NRHbzMerEQ/zh-cn_image_0000002565290213.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=DBC6EB4A55ADBF5B692D75B8603D26579FC389CEBFDD0E9D70AEA924F42A1117)

## 添加事件

Text组件可以添加通用事件，可以绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
export struct GeneralEvents {
  @State textStr1: string = '';
  @State textStr2: string = '';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('This is a text component.')
            .fontSize(30)
            .onClick(() => {
              hilog.info(0x0000, 'Sample_TextComponent', 'Text onClick is triggering');
              this.textStr1 = 'Text onClick is triggering';
            })
            .onTouch(() => {
              hilog.info(0x0000, 'Sample_TextComponent', 'Text onTouch is triggering');
              this.textStr2 = 'Text onTouch is triggering';
            })
          Text('onClick：' + this.textStr1)
            .fontSize(20)
          Text('onTouch：' + this.textStr2)
            .fontSize(20)
        }.width('100%')
      }
      .height('100%')
    }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/yzS1NmUZRBKjzopPiCa8RQ/zh-cn_image_0000002565210193.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=768E5FDC57CB95A1B4312AA9DBCBB2E094E1B4CCB9C99166D5B183E5B3299DD7)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)属性实现文本段落在垂直方向的对齐。

- 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。 ```typescript Text() {  Span('Hello')  .fontSize(50)  ImageSpan($r('app.media.startIcon'))  .width(30).height(30)  .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)  Span('World') } .textVerticalAlign(TextVerticalAlign.CENTER) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/vCMLHqkoR0G-6rN3R-FusQ/zh-cn_image_0000002534250370.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=F254F71536F595862E464DB223370181C106E1DE0C1BCC5DDFC4B3260E0627D4)

## 设置选中菜单

### 弹出选中菜单

- 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。 Text组件需要设置[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性才可以被选中。 ```typescript Text($r('app.string.selected_menu'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vbRJ65CrTxWlEjCHpFcVtA/zh-cn_image_0000002534410316.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=835B73A014611A8BBAA846455951F5DE876D6CE5EBA571D3B4D5FA046206B1A9)
- Text组件通过设置[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)属性绑定自定义选择菜单。 ```typescript controller: TextController = new TextController(); options: TextOptions = { controller: this.controller }; ``` ```typescript Text($r('app.string.show_selected_menu'), this.options)  .fontSize(30)  .copyOption(CopyOptions.InApp)  .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {  onAppear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));  },  onDisappear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));  }  }) ``` ```typescript @Builder RightClickTextCustomMenu() {  Column() {  Menu() {  MenuItemGroup() {  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })  .onClick(() => {  this.controller.closeSelectionMenu();  })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })  }  }.backgroundColor('#F0F0F0')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qHhSOeaQST2o2Q2z_k_VuA/zh-cn_image_0000002565290215.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=665260BC1C80ED4209DD2B19AAA6E1A25519696591BE0103DE944CF7A495DD3C)
- Text组件通过设置[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。 ```typescript Text($r('app.string.show_selected_menu'))  .fontSize(20)  .copyOption(CopyOptions.LocalDevice)  .editMenuOptions({  onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick  }) ``` ```typescript onCreateMenu = (menuItems: Array<TextMenuItem>) => {  let item1: TextMenuItem = {  content: 'customMenu1',  icon: $r('app.media.app_icon'),  id: TextMenuItemId.of('customMenu1'),  };  let item2: TextMenuItem = {  content: 'customMenu2',  id: TextMenuItemId.of('customMenu2'),  icon: $r('app.media.app_icon'),  };  menuItems.push(item1);  menuItems.unshift(item2);  return menuItems; } onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {  if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')  .id) + textRange.start + '; end:' +  textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.COPY)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +  textRange.start + '; end:' + textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +  textRange.start + '; end:' +  textRange.end);  return false;  }  return false; }; ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/kA-T0ZP6TYCvFkr-lDC0cA/zh-cn_image_0000002565210195.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=22F7A7A07AA73BF72B127978F1C722680F86579C9AE17BA2396BE69FDE23A01D)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

- 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
- 在Text组件区域外点击空白处，前提是Text组件设置[selection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#selection11)属性，具体示例如下： ```typescript @Entry @Component export struct SelectionChange {  @State text: string =  'This is set selection to Selection text content This is set selection to Selection text content.';  @State start: number = 0;  @State end: number = 20;  build() {  NavDestination() {  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {  Text(this.text)  .fontSize(12)  .border({ width: 1 })  .lineHeight(20)  .margin(30)  .copyOption(CopyOptions.InApp)  .selection(this.start, this.end)  .onTextSelectionChange((selectionStart, selectionEnd) => {  this.start = selectionStart;  this.end = selectionEnd;  })  }  .height(600)  .width(335)  .borderWidth(1)  .onClick(() => {  this.start = -1;  this.end = -1;  })  }  } } ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/xVOKswI9QZC2eQPwjxhYpQ/zh-cn_image_0000002534250372.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=4155A9FE1CCBEA2836CE4D975BC981F8C4483DC8985F2E8999DB024D8612241E)

### 屏蔽系统菜单回调和自定义扩展菜单

从API version 12开始，支持通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)屏蔽系统菜单回调和自定义扩展菜单项。

```typescript
@Entry
@Component
export struct CustomAndBlockMenus {
  private static readonly CREATE_MENU_ITEM_ID_1: string = 'create1';
  private static readonly CREATE_MENU_ITEM_ID_2: string = 'create2';
  private static readonly PREPARE_MENU_ITEM_ID: string = 'prepare1';
  @State private text: string = 'Text editMenuOptions';
  @State private endIndex: number = 0;
  @State blockCallbackText: string = '';

  private createMenuItem(id: string, content: string): TextMenuItem {

    return {
      content: content,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of(id)
    };
  }

  private findMenuItemIndex(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): number {
    return menuItems.findIndex((item: TextMenuItem) => item.id.equals(menuItemId));
  }

  private onCreateMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const createItem1: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_1,
      'create1'
    );

    const createItem2: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2,
      'create2'
    );

    menuItems.push(createItem1);
    menuItems.unshift(createItem2);

    this.removeMenuItemById(menuItems, TextMenuItemId.AI_WRITER);
    this.removeMenuItemById(menuItems, TextMenuItemId.TRANSLATE);

    return menuItems;
  }

  private removeMenuItemById(menuItems: Array<TextMenuItem>, menuItemId: TextMenuItemId): void {
    const targetIndex: number = this.findMenuItemIndex(menuItems, menuItemId);
    if (targetIndex !== -1) {
      menuItems.splice(targetIndex, 1);
    }
  }

  private onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange): boolean => {
    const menuItemId: TextMenuItemId = menuItem.id;

    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.CREATE_MENU_ITEM_ID_2))) {
      let msg = '拦截 id: create2 start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.of(CustomAndBlockMenus.PREPARE_MENU_ITEM_ID))) {
      let msg = '拦截 id: prepare1 start:' + textRange.start + '; end:+' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.COPY)) {
      let msg = '拦截 COPY start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return true;
    }

    if (menuItemId.equals(TextMenuItemId.SELECT_ALL)) {
      let msg = '不拦截 SELECT_ALL start:' + textRange.start + '; end:' + textRange.end;
      this.blockCallbackText = msg
      return false;
    }

    return false;
  }

  private onPrepareMenu = (menuItems: Array<TextMenuItem>): Array<TextMenuItem> => {
    const prepareItem: TextMenuItem = this.createMenuItem(
      CustomAndBlockMenus.PREPARE_MENU_ITEM_ID,
      `prepare1_${this.endIndex}`
    );

    menuItems.unshift(prepareItem);
    return menuItems;
  }

  @State private editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  private onTextSelectionChange = (selectionStart: number, selectionEnd: number): void => {
    this.endIndex = selectionEnd;
  }

  build() {
    NavDestination() {
      Column() {
        Text(this.text)
          .fontSize(20)
          .copyOption(CopyOptions.LocalDevice)
          .editMenuOptions(this.editMenuOptions)
          .margin({ top: 100 })
          .onTextSelectionChange(this.onTextSelectionChange)
        Text(this.blockCallbackText).borderWidth(1)
      }
      .width('90%')
      .margin('5%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/YIG_JRntRnqN4pH_l7xkxg/zh-cn_image_0000002534410318.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=62BEB4EE6D1BBA17FBBCEF456364218AD26362A47656E986CDC1C0EB5507B2A8)

### 屏蔽系统服务类菜单

- 从API version 20开始，支持通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct ServiceMenuItems {  aboutToAppear(): void {  TextMenuController.disableSystemServiceMenuItems(true);  }  aboutToDisappear(): void {  TextMenuController.disableSystemServiceMenuItems(false);  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false;  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/BCM0fSBBTVGzpPYyc7b4zg/zh-cn_image_0000002565290217.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=6113BC671C101498C2F635B155C09931B63C55E4E8E050B68EF7108FFF2959FE)
- 从API version 20开始，支持通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct DisableMenuItems {  aboutToAppear(): void {  TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])  }  aboutToDisappear(): void {  TextMenuController.disableMenuItems([])  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/EXpRMSpoQAqa9g1SdSdhsw/zh-cn_image_0000002565210197.jpg?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=F66397CE8E9C8D6F159A200A3B966FC65492678FB8B08C44F47B64CB95335621)

### 默认菜单支持自定义刷新能力

从API version 20开始，当文本选择区域变化后显示菜单之前触发[onPrepareMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#属性-1)回调，可在该回调中进行菜单数据设置。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0000;
@Entry
@Component

export struct PrepareMenu {
  @State text: string = 'Text editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: create2 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept id: prepare1 start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'intercept COPY start:' + textRange.start + '; end:' + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'No interception SELECT_ALL start:' + textRange.start + '; end:' + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    NavDestination() {
    Column() {
      Text(this.text)
        .fontSize(20)
        .copyOption(CopyOptions.LocalDevice)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width('90%')
    .margin('5%')
    }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/wzbO1fQwThOMNNGaGFjYWA/zh-cn_image_0000002534250374.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=91B985E0D90AF117D6DF452C8216203062BE5BE3E935E79848DCF6F0B029AA68)

## 设置AI菜单

Text组件通过[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)和[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

> **说明**
> 从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)设置为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。
>
> 该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

- 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true。
- 如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示： ```typescript Text($r('app.string.AIMenu_Text_One'))  .fontSize(16)  .copyOption(CopyOptions.LocalDevice)  .enableDataDetector(true)  .dataDetectorConfig({  types: [], onDetectResultUpdate: (result: string) => {  }  }) ```
- 如果需要调整识别出的样式，可以通过[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11对象说明)配置项。
- 如果需要调整菜单的位置，可以通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例12文本扩展自定义菜单)。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SGNQyF7_T66IfYzhS7wscw/zh-cn_image_0000002534410320.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=F5A66A9BE055EE85974B21163FC5E49257867CED5DB349A948C8C42D2E7B465D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/HbSRnloUSAKz3C-QZs4b0Q/zh-cn_image_0000002565290219.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=AED922F32D1A90B21F3899D723826E4CA29C1AC66ECB71339E29DC26A650CF73)

## 实现热搜榜

该示例通过[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)、[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)、[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)、[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)属性展示了热搜榜的效果。

```typescript
import { ComponentCard } from '../../common/Card';

@Entry
@Component
export struct TextHotSearch {
  build() {
    NavDestination() {
      Column({ space: 12 }) {

          Column() {
            Row() {
              Text('1').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })

              Text($r('app.string.TextHotSearch_textContent_one'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .fontWeight(300)

              Text($r('app.string.TextHotSearch_textContent_two'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0x770100)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('2').fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })

              Text($r('app.string.TextHotSearch_textContent_three'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })

              Text($r('app.string.TextHotSearch_textContent_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('3').fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })

              Text($r('app.string.TextHotSearch_textContent_five'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .maxLines(1)
                .constraintSize({ maxWidth: 200 })
                .textOverflow({ overflow: TextOverflow.Ellipsis })

              Text($r('app.string.TextHotSearch_textContent_four'))
                .margin({ left: 6 })
                .textAlign(TextAlign.Center)
                .fontSize(10)
                .fontColor(Color.White)
                .fontWeight(600)
                .backgroundColor(0xCC5500)
                .borderRadius(5)
                .width(15)
                .height(14)
            }.width('100%').margin(5)

            Row() {
              Text('4').fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })

              Text($r('app.string.TextHotSearch_textContent_six'))
                .fontSize(12)
                .fontColor(Color.Blue)
                .fontWeight(300)
                .constraintSize({ maxWidth: 200 })
                .maxLines(1)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
            }.width('100%').margin(5)
          }.width('100%')

      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/DWCQVTX_QQ6ydTXcvqFmMg/zh-cn_image_0000002565210199.png?HW-CC-KV=V1&HW-CC-Date=20260401T132821Z&HW-CC-Expire=86400&HW-CC-Sign=11E8E2F7897B3EFC39B10818191D0CDD90A1D58E34338A74559FBF8EB7F7D410)

## 示例代码

- [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
