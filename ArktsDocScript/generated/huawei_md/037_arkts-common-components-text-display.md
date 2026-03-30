# 文本显示 (Text/Span)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)组件的使用说明。

常见问题请参考[文本显示（Text/Span）常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

- string字符串。 ```typescript Text('我是一段文本') ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/v0ZUk7iUTVO_Hhz5AVQS5g/zh-cn_image_0000002533065858.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=F213AB3AF8C28FCEB937F27A8E4AA731AE24DB6A5044932EEF16344DC4BFF01D)

- 引用Resource资源。 资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下： ```typescript {  "string": [  {  "name": "module_desc",  "value": "模块描述"  }  ] } ``` ```typescript Text($r('app.string.module_desc'))  .baselineOffset(0)  .fontSize(30)  .border({ width: 1 })  .padding(10)  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/5xbBfGhvQgyVSE_WfqBRVw/zh-cn_image_0000002563865761.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=972A080B3B8CA832394EC80D4A98544EAD56D51D77919D7CAB5EA2C14B28B35A)

## 添加子组件

[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)只能作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

- 创建Span。 Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。 ```typescript Text($r('app.string.TextSpan_textContent_text')) {  Span($r('app.string.TextSpan_textContent_span')) } .padding(10) .borderWidth(1) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/g9dANv4kRfmoHJsZSFEjjA/zh-cn_image_0000002563785807.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=41C57A8EBFFD44712EF9AA1A56871C0B5066060381E0634CE43AD97C273FBE78)
- 设置文本装饰线及颜色。 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置文本装饰线及颜色。 ```typescript Text() {  Span($r('app.string.TextSpan_textContent_span_one'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })  Span($r('app.string.TextSpan_textContent_span_two'))  .fontColor(Color.Blue)  .fontSize(16)  .fontStyle(FontStyle.Italic)  .decoration({ type: TextDecorationType.Underline, color: Color.Black })  Span($r('app.string.TextSpan_textContent_span_three'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.Overline, color: Color.Green }) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/D5spWnTiSBqYFhlkNUQl4A/zh-cn_image_0000002532905912.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=A1DE3692621CD934708071281BA94DFF0D061A871CA7F7BBC98DA21A466D4270)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textcase)设置文字一直保持大写或者小写状态。 ```typescript Text() {  Span('I am Upper-span').fontSize(12)  .textCase(TextCase.UpperCase) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/lWvP9QGNR3iWc60h9BTMnQ/zh-cn_image_0000002533065860.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=7424D4604111338C1AD06B3C57C43E0F75D0FD77B5FE12A67ED16DAB07BA4EAC)
- 添加事件。 由于Span组件无尺寸信息，仅支持添加点击事件[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、悬浮事件[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover#onhover)。 ```typescript import { hilog } from '@kit.PerformanceAnalysisKit'; @Entry @Component export struct TextSpanOnHover {  @State textStr1: string = '';  @State textStr2: string = '';  build() {  NavDestination() {  Row() {  Column() {  Text() {  Span('I am Upper-span')  .textCase(TextCase.UpperCase)  .fontSize(30)  .onClick(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');  this.textStr1 = 'Span onClick is triggering';  })  .onHover(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');  this.textStr2 = 'Span onHover is triggering';  })  }  Text('onClick：' + this.textStr1)  .fontSize(20)  Text('onHover：' + this.textStr2)  .fontSize(20)  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/0Poi52QrRKGZe1uTMrD1Xg/zh-cn_image_0000002563865763.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=916212B765478E1808979D4785BD49C16AE8A564FC97E2EA41F3921C4F054E81)

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

- 通过[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)属性设置文本对齐样式。 ```typescript Text($r('app.string.TextAlign_Start'))  .width(300)  .textAlign(TextAlign.Start)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_Center'))  .width(300)  .textAlign(TextAlign.Center)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_End'))  .width(300)  .textAlign(TextAlign.End)  .border({ width: 1 })  .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/YlTtfrrFTDyhINHv2CVmKA/zh-cn_image_0000002563785809.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=A65499BD4B668703B01897B5716857900046EED07A94ED5739E91768535CFAFF)
- 通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。 ```typescript Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +  'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +  'of textOverflow to None text content.')  .width(250)  .textOverflow({ overflow: TextOverflow.None })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_epsis'))  .width(250)  .textOverflow({ overflow: TextOverflow.Ellipsis })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq_def'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .marqueeOptions({  start: true,  fromStart: true,  step: 6,  loop: -1,  delay: 0,  fadeout: false,  marqueeStartPolicy: MarqueeStartPolicy.DEFAULT  }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Yk13EuCgSp2duT4U1nDFMA/zh-cn_image_0000002532905914.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=142E8F6D76B4D996777BB248FBCA3F0947A99B24BEE4035B7F2F99B1F057ACE4)
- 通过[lineHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#lineheight)属性设置文本行高。 ```typescript Text('This is the text with the line height set. This is the text with the line height set.')  .width(300).fontSize(12).border({ width: 1 }).padding(10) Text('This is the text with the line height set. This is the text with the line height set.')  .width(300)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .lineHeight(20) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Jq-DFPLYQleO1w2SPbyn5A/zh-cn_image_0000002533065862.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=C7E4C91F69793ADC87A288C1254368A27A5C5F409D964E5B399338D993536F3B)
- 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性设置文本装饰线样式、颜色及其粗细。 ```typescript Text('This is the text')  .decoration({  type: TextDecorationType.LineThrough,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Overline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DASHED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOTTED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOUBLE  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.WAVY,  thicknessScale: 4  })  .borderWidth(1).padding(15).margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/fzQGbFjgTIi4zDNt04gnbQ/zh-cn_image_0000002563865765.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=9F22EB690CF9E7691843057201DF70CAD27B746787CAB856187C57DBB0A79BA5)
- 通过[baselineOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#baselineoffset)属性设置文本基线的偏移量。 ```typescript Text('This is the text content with baselineOffset 0.')  .baselineOffset(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset 30.')  .baselineOffset(30)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset -20.')  .baselineOffset(-20)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Nv8lyhr0QsKqrAH1i90uLg/zh-cn_image_0000002563785811.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=3DC17B9FD80DCCC2490564DAA9BB819AA0D32638563F0154C910A528DD0A416B)
- 通过[letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#letterspacing)属性设置文本字符间距。 ```typescript Text('This is the text content with letterSpacing 0.')  .letterSpacing(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing 3.')  .letterSpacing(3)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing -1.')  .letterSpacing(-1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/mi9T8wmFRDOyYiVaWCo4SQ/zh-cn_image_0000002532905916.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=AAAC2C215600863C81C637244E323D155B8CB3CA180CBDA428976DA0B0AD9288)
- 通过[minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#minfontsize)与[maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxfontsize)自适应字体大小。 minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。 ```typescript Text($r('app.string.CustomTextStyle_textContent_one_style'))  .width(250)  .maxLines(1)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_two_style'))  .width(250)  .maxLines(2)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_no_max'))  .width(250)  .height(50)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_high'))  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/04v1yEy3QQeOWYfELt_GXg/zh-cn_image_0000002533065864.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=9EE97821AC6A473940C9A920BB1218B8147846C68760A8D507449CE29F6D4A28)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcase)属性设置文本大小写。 ```typescript Text('This is the text content with textCase set to Normal.')  .textCase(TextCase.Normal)  .padding(10)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to LowerCase.')  .textCase(TextCase.LowerCase)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to UpperCase.')  .textCase(TextCase.UpperCase)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/CgTJqqVZSzSCnuXA-pCFEw/zh-cn_image_0000002563865767.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=8D3539926847A32A410F1388EFDFBDA1705184AC2647CCF2C2533F1821F1AF62)
- 通过[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性设置文本是否可复制粘贴。 ```typescript Text($r('app.string.CustomTextStyle_textContent_incopy'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zG7QXh9nT-CZS_Vqyy8X6w/zh-cn_image_0000002563785813.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=2FF6FFB3560658E3E9E5BAD2EB2B2BD5283B3E22A239A580F7559E59A379DD87)
- 通过[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。 ```typescript Text('This is the text content with fontFamily')  .fontSize(30)  .fontFamily('HarmonyOS Sans') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/WAs0xpHWSNayqr9nkhp06Q/zh-cn_image_0000002532905918.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=D54C1DBC87315D32C3616A1400CE4FD04898CF07EDA18AE23AE1336D6650511B)
- 从API version 20开始，支持通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#contenttransition20)属性设置数字翻牌效果。 ```typescript @Entry @Component export struct ContentTransition {  private static readonly INITIAL_SCORE: number = 98;  @State number: number = ContentTransition.INITIAL_SCORE;  @State numberTransition: NumericTextTransition =  new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });  build() {  NavDestination() {  Column() {  Text(this.number + '')  .borderWidth(1)  .fontSize(40)  .contentTransition(this.numberTransition)  Button('chang number')  .onClick(() => {  this.number++  })  .margin(10)  }  .width('100%')  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/9reBKTwzTI6DqnwX2vCKpg/zh-cn_image_0000002533065866.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=3EFCDF31DCD02565CBCFD1843227B7DE3DDFA13A48FA94E32CB5B1E6D586FF69)
- 从API version 20开始，支持通过[optimizeTrailingSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。 ```typescript Column() {  Text('Trimmed space enabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(true)  .textAlign(TextAlign.Center)  Text('Trimmed space disabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(false)  .textAlign(TextAlign.Center) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/NlhOF0v6Qn29nO_54ok-kQ/zh-cn_image_0000002563865769.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=D401CBC941D37D28EEB2949780DE146A5ACDC2112F6363C85FCEF59586D8F9CF)
- 从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。 ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Extend(Text) function style() {  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 }) } @Entry @Component export struct LineSpacing {  build() {  NavDestination() {  Column() {  Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })  .style()  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/08kBe13zSlG7HUlIt2g9GQ/zh-cn_image_0000002563785815.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=A694CFCB0C75BEFB77BC29D01CB7D3746DF17329A014E35F989F1362E2FF6F79)
- 从API version 20开始，支持通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enableautospacing20)设置是否开启中文与西文的自动间距。 ```typescript @Entry @Component export struct EnableAutoSpacing {  @State enableSpacing: boolean = false;  build() {  NavDestination() {  Column() {  Row({ space: 20 }) {  Button($r('app.string.Enable_automatic_spacing'))  .onClick(() => this.enableSpacing = true)  .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')  .fontColor(this.enableSpacing ? Color.White : Color.Black)  Button($r('app.string.off_automatic_spacing'))  .onClick(() => this.enableSpacing = false)  .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')  .fontColor(!this.enableSpacing ? Color.White : Color.Black)  }  .width('100%')  .justifyContent(FlexAlign.Center)  .margin({ top: 30, bottom: 20 })  Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))  .fontSize(16)  .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')  .margin({ bottom: 20 })  Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))  .fontSize(24)  .padding(15)  .backgroundColor('#F5F5F5')  .width('90%')  .enableAutoSpacing(this.enableSpacing)  }  .width('100%')  .height('100%')  .padding(20)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/M1AuhrxZQpe3sHyELaVUpA/zh-cn_image_0000002532905920.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=B6D064316AE767F4F942AFC9C49461A300FB09B5BEBE533BD8CFD09C49B9B8B7)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#shaderstyle20)设置渐变色。 ```typescript @Entry @Component export struct ShaderStyle {  @State message: string = 'Hello World';  @State linearGradientOptions: LinearGradientOptions =  {  direction: GradientDirection.LeftTop,  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true,  };  build() {  NavDestination() {  Column({ space: 5 }) {  Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)  .margin({ top: 40, left: 40 })  Text(this.message)  .fontSize(50)  .width('80%')  .height(50)  .shaderStyle(this.linearGradientOptions)  }  .height('100%')  .width('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/yALxcfRzQvCYR0OIi2jBEw/zh-cn_image_0000002533065868.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=E66D42D0E55C683E1629B2BA3B4AD50B82D49C002BD9278A70F61CA6F1DD3E98)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/UXzzgX15Q0KeS6BBqstFzw/zh-cn_image_0000002563865771.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=451956A05A7E61777DA048948241BE621264DF73D89AA13AE3DAEDD1B8B5B17F)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)属性实现文本段落在垂直方向的对齐。

- 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。 ```typescript Text() {  Span('Hello')  .fontSize(50)  ImageSpan($r('app.media.startIcon'))  .width(30).height(30)  .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)  Span('World') } .textVerticalAlign(TextVerticalAlign.CENTER) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ldQRVMiQRNqjmK2v0LYVMQ/zh-cn_image_0000002563785817.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=D80B27872E2DA0C20CCD054D327DF1AE71A8E5ADA783F04B19D6E11E61C35FFE)

## 设置选中菜单

### 弹出选中菜单

- 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。 Text组件需要设置[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性才可以被选中。 ```typescript Text($r('app.string.selected_menu'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/WcSKfiwiTP2IAnCg22IoMA/zh-cn_image_0000002532905922.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=6D9B794090B129E67DAF28763D25C68C5D85F00A0F46545E7833F57CF28B9391)
- Text组件通过设置[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)属性绑定自定义选择菜单。 ```typescript controller: TextController = new TextController(); options: TextOptions = { controller: this.controller }; ``` ```typescript Text($r('app.string.show_selected_menu'), this.options)  .fontSize(30)  .copyOption(CopyOptions.InApp)  .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {  onAppear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));  },  onDisappear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));  }  }) ``` ```typescript @Builder RightClickTextCustomMenu() {  Column() {  Menu() {  MenuItemGroup() {  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })  .onClick(() => {  this.controller.closeSelectionMenu();  })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })  }  }.backgroundColor('#F0F0F0')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/AL0Q7FANQtOFm5sqc4Fe2w/zh-cn_image_0000002533065870.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=BB8461E1193ACBE3F7EF40A3C4E50A7666662089C210B17C4F126D07A898B275)
- Text组件通过设置[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。 ```typescript Text($r('app.string.show_selected_menu'))  .fontSize(20)  .copyOption(CopyOptions.LocalDevice)  .editMenuOptions({  onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick  }) ``` ```typescript onCreateMenu = (menuItems: Array<TextMenuItem>) => {  let item1: TextMenuItem = {  content: 'customMenu1',  icon: $r('app.media.app_icon'),  id: TextMenuItemId.of('customMenu1'),  };  let item2: TextMenuItem = {  content: 'customMenu2',  id: TextMenuItemId.of('customMenu2'),  icon: $r('app.media.app_icon'),  };  menuItems.push(item1);  menuItems.unshift(item2);  return menuItems; } onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {  if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')  .id) + textRange.start + '; end:' +  textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.COPY)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +  textRange.start + '; end:' + textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +  textRange.start + '; end:' +  textRange.end);  return false;  }  return false; }; ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/906vqKCXTYeEtwStjxBI-A/zh-cn_image_0000002563865773.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=021A94E05073D2FD6C6A0A7D3565613AAB33D3FD79B7383E0D7B28800783E0DE)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

- 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
- 在Text组件区域外点击空白处，前提是Text组件设置[selection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#selection11)属性，具体示例如下： ```typescript @Entry @Component export struct SelectionChange {  @State text: string =  'This is set selection to Selection text content This is set selection to Selection text content.';  @State start: number = 0;  @State end: number = 20;  build() {  NavDestination() {  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {  Text(this.text)  .fontSize(12)  .border({ width: 1 })  .lineHeight(20)  .margin(30)  .copyOption(CopyOptions.InApp)  .selection(this.start, this.end)  .onTextSelectionChange((selectionStart, selectionEnd) => {  this.start = selectionStart;  this.end = selectionEnd;  })  }  .height(600)  .width(335)  .borderWidth(1)  .onClick(() => {  this.start = -1;  this.end = -1;  })  }  } } ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ZJRdy_G_TvSrYxalnU8wKw/zh-cn_image_0000002563785819.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=4C820D2481DB1D01B403EED39438131C6AA4927CC1DCA18925882FF77475F4E6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/L3fksufQSZGSsAh6IUgI1w/zh-cn_image_0000002532905924.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=E9465E1683310D84CFB24C182D9BBF728B8E3A196D9E91DB97AD5D04D60EA62E)

### 屏蔽系统服务类菜单

- 从API version 20开始，支持通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct ServiceMenuItems {  aboutToAppear(): void {  TextMenuController.disableSystemServiceMenuItems(true);  }  aboutToDisappear(): void {  TextMenuController.disableSystemServiceMenuItems(false);  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false;  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/XVSXxu2QRGK0_z54xzUGFg/zh-cn_image_0000002533065872.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=B88F897BB666DB87C01A985210AAAE740A0FD7AEB33F5E0E439693939101358A)
- 从API version 20开始，支持通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct DisableMenuItems {  aboutToAppear(): void {  TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])  }  aboutToDisappear(): void {  TextMenuController.disableMenuItems([])  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Ivg6si_CSsuXdvDn214Pig/zh-cn_image_0000002563865775.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=66AF00CA133F1CF7B1C44CB30BE63C6F82BE4309A5E603EA09C24C165910D3AE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/0QOrwthDTCqqc0TjU0vdxA/zh-cn_image_0000002563785821.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=F088CE09568F2A3B89AE48BE9AF642C52768D40D5792689A0F87E947769637FB)

## 设置AI菜单

Text组件通过[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)和[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

> **说明**
> 从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)设置为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。
>
> 该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

- 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true。
- 如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示： ```typescript Text($r('app.string.AIMenu_Text_One'))  .fontSize(16)  .copyOption(CopyOptions.LocalDevice)  .enableDataDetector(true)  .dataDetectorConfig({  types: [], onDetectResultUpdate: (result: string) => {  }  }) ```
- 如果需要调整识别出的样式，可以通过[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11对象说明)配置项。
- 如果需要调整菜单的位置，可以通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例12文本扩展自定义菜单)。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/0Ra3TChAT3CsFoF8PKC87g/zh-cn_image_0000002532905926.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=4DAA608A5791FA69409F8E60CF9D9676D9EEA06EB240793B8FA181E50843608A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/1xoV_B7oRuuLfj9PGlU6Fw/zh-cn_image_0000002533065874.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=40E4321F04180E78CF86CF3A190A76406C4CCEACAAB588D58028CC49796EE8A1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/h2PuQqbgTQO6wxN602M4kw/zh-cn_image_0000002563865777.png?HW-CC-KV=V1&HW-CC-Date=20260330T095139Z&HW-CC-Expire=86400&HW-CC-Sign=28BB97517D7F93A6FEEEEAC82125720A1B20653C0F5ED1D52C9000CFCDB19A0D)

## 示例代码

- [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
