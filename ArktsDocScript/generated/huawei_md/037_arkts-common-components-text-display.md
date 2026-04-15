# 文本显示 (Text/Span)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)组件的API文档。

常见问题请参考[文本显示（Text/Span）常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

- string字符串。 ```typescript Text('我是一段文本') ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/QuDOIGLJT4iYk_dJ46l81Q/zh-cn_image_0000002540771078.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=745FACA76EEDEB641C00A6B2514422527556B38AA7CCC33FC89D0A9C2BE8D12E)

- 引用Resource资源。 资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下： ```typescript {  "string": [  {  "name": "module_desc",  "value": "模块描述"  }  ] } ``` ```typescript Text($r('app.string.module_desc'))  .baselineOffset(0)  .fontSize(30)  .border({ width: 1 })  .padding(10)  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sAlroCZtRU6Jaz5GRCtNPw/zh-cn_image_0000002571291375.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=BA96B025B20F6B2BA9608E43D4B8C6F4E246AE69ABD6350099227D538E09134F)

## 添加子组件

[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)只能作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

- 创建Span。 Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。 ```typescript Text($r('app.string.TextSpan_textContent_text')) {  Span($r('app.string.TextSpan_textContent_span')) } .padding(10) .borderWidth(1) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/2-dB-f5BToWG8-QA-jq1sQ/zh-cn_image_0000002540611428.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=DE2636148628373C87106EB38A8F39CD3B6D522C8EF2EC038BA561F5A376A65E)
- 设置文本装饰线及颜色。 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置文本装饰线及颜色。 ```typescript Text() {  Span($r('app.string.TextSpan_textContent_span_one'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })  Span($r('app.string.TextSpan_textContent_span_two'))  .fontColor(Color.Blue)  .fontSize(16)  .fontStyle(FontStyle.Italic)  .decoration({ type: TextDecorationType.Underline, color: Color.Black })  Span($r('app.string.TextSpan_textContent_span_three'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.Overline, color: Color.Green }) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/zv9xlPUOQ-y3WNsmeZPOIg/zh-cn_image_0000002571171423.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=260C99E8ABD40507A78C0B323EEDAECC0BF902729A45E8E46C6CAC72114C6C64)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textcase)设置文字一直保持大写或者小写状态。 ```typescript Text() {  Span('I am Upper-span').fontSize(12)  .textCase(TextCase.UpperCase) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/eCn1tmP-SriB3AYrRFWdpw/zh-cn_image_0000002540771080.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=652826D111F7349C281AFC789832B40300715883798E38DBE2CECA5C1335BCD2)
- 添加事件。 由于Span组件无尺寸信息，仅支持添加点击事件[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、悬浮事件[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover#onhover)。 ```typescript import { hilog } from '@kit.PerformanceAnalysisKit'; @Entry @Component export struct TextSpanOnHover {  @State textStr1: string = '';  @State textStr2: string = '';  build() {  NavDestination() {  Row() {  Column() {  Text() {  Span('I am Upper-span')  .textCase(TextCase.UpperCase)  .fontSize(30)  .onClick(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');  this.textStr1 = 'Span onClick is triggering';  })  .onHover(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');  this.textStr2 = 'Span onHover is triggering';  })  }  Text('onClick：' + this.textStr1)  .fontSize(20)  Text('onHover：' + this.textStr2)  .fontSize(20)  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/AyzNxdBZStmpCEL1TiW0xw/zh-cn_image_0000002571291377.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=E44C8E7D31EDC23355A502CE8FF1DE81250B1F03DA2C5EEC3618F6BB6D01A1EE)

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

- 通过[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)属性设置文本对齐样式。 ```typescript Text($r('app.string.TextAlign_Start'))  .width(300)  .textAlign(TextAlign.Start)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_Center'))  .width(300)  .textAlign(TextAlign.Center)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_End'))  .width(300)  .textAlign(TextAlign.End)  .border({ width: 1 })  .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/EZHRAfYFQrGdWtk0oTw3YA/zh-cn_image_0000002540611430.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=8FF019254E7B5A1295051FE9A879F2706D5337A9F3BAD60D5F9455EACC0C2FF6)
- 通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。 ```typescript Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +  'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +  'of textOverflow to None text content.')  .width(250)  .textOverflow({ overflow: TextOverflow.None })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_epsis'))  .width(250)  .textOverflow({ overflow: TextOverflow.Ellipsis })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq_def'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .marqueeOptions({  start: true,  fromStart: true,  step: 6,  loop: -1,  delay: 0,  fadeout: false,  marqueeStartPolicy: MarqueeStartPolicy.DEFAULT  }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Cbt6Zy-8R56sk76iQNghUg/zh-cn_image_0000002571171425.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=569E90391B4154A46A224EEFBEBC0387E2CFADDADFE57FCB376BD6BEF9D69ADE)
- 通过[lineHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#lineheight)属性设置文本行高。 ```typescript Text('This is the text with the line height set. This is the text with the line height set.')  .width(300).fontSize(12).border({ width: 1 }).padding(10) Text('This is the text with the line height set. This is the text with the line height set.')  .width(300)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .lineHeight(20) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/uh54xs3tS8an8O3im9hhTg/zh-cn_image_0000002540771082.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=0473CCF3F0431FA6B51A3395D6A51B813A7A563A0A58EBDACBCF3A9BE6FFAC3B)
- 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性设置文本装饰线样式、颜色及其粗细。 ```typescript Text('This is the text')  .decoration({  type: TextDecorationType.LineThrough,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Overline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DASHED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOTTED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOUBLE  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.WAVY,  thicknessScale: 4  })  .borderWidth(1).padding(15).margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Stt-RxEwQaG8I_pGtiE31Q/zh-cn_image_0000002571291379.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=B8B583CD8FC85E24323FB286CC0B80CBF4723834A96D45C9E226FAFCA9B856E6)
- 通过[baselineOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#baselineoffset)属性设置文本基线的偏移量。 ```typescript Text('This is the text content with baselineOffset 0.')  .baselineOffset(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset 30.')  .baselineOffset(30)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset -20.')  .baselineOffset(-20)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/tGhqEM7FTJaRZ-R1RXRFxQ/zh-cn_image_0000002540611432.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=EFE5C3BE5C54CE74A8253AB829A8A358A9A634AF33DDB6F235E80B0AE5F8FD0C)
- 通过[letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#letterspacing)属性设置文本字符间距。 ```typescript Text('This is the text content with letterSpacing 0.')  .letterSpacing(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing 3.')  .letterSpacing(3)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing -1.')  .letterSpacing(-1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/sgOXedxdSKGaEZ6QCRtD9A/zh-cn_image_0000002571171427.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=91A50F352E558D2388F1153879BE39E3F0799A60A695CF8E0C110ED3F167756A)
- 通过[minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#minfontsize)与[maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxfontsize)自适应字体大小。 minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。 ```typescript Text($r('app.string.CustomTextStyle_textContent_one_style'))  .width(250)  .maxLines(1)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_two_style'))  .width(250)  .maxLines(2)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_no_max'))  .width(250)  .height(50)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_high'))  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/tHBeYb67Rg6xHqrJq7s5aQ/zh-cn_image_0000002540771084.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=8DEB6F3AA13DA331112B1F02DA70894E95DBB96263D95AA70B3DBE56C8E9FDD7)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcase)属性设置文本大小写。 ```typescript Text('This is the text content with textCase set to Normal.')  .textCase(TextCase.Normal)  .padding(10)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to LowerCase.')  .textCase(TextCase.LowerCase)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to UpperCase.')  .textCase(TextCase.UpperCase)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Y8oao-ouT1aCdQoHNqJxDw/zh-cn_image_0000002571291381.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=B124FC0C179D7349DCE5B7337EA1EE699C4F86016CC04879B9AAA0D696D599F4)
- 通过[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性设置文本是否可复制粘贴。 ```typescript Text($r('app.string.CustomTextStyle_textContent_incopy'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/4S4he3UuS_WoZxHZe7C5MQ/zh-cn_image_0000002540611434.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=B49514905F98A8DBBFD99763B9C1704ECC43F0505C82CB58C8B3C74C1ABD451A)
- 通过[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。 ```typescript Text('This is the text content with fontFamily')  .fontSize(30)  .fontFamily('HarmonyOS Sans') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3q_YZbmlTn6NHwZkAYKPvQ/zh-cn_image_0000002571171429.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=AA3940C4CAA0962F54CBF5C0671C746AC7770257EAB283BB966D6AF2952DAE9B)
- 从API version 20开始，支持通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#contenttransition20)属性设置数字翻牌效果。 ```typescript @Entry @Component export struct ContentTransition {  private static readonly INITIAL_SCORE: number = 98;  @State number: number = ContentTransition.INITIAL_SCORE;  @State numberTransition: NumericTextTransition =  new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });  build() {  NavDestination() {  Column() {  Text(this.number + '')  .borderWidth(1)  .fontSize(40)  .contentTransition(this.numberTransition)  Button('chang number')  .onClick(() => {  this.number++  })  .margin(10)  }  .width('100%')  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/mJoe0SEOTImZuNHGd0iEtA/zh-cn_image_0000002540771086.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=879ABF91800BEE2F42D20B1BA41796F959A506B092FCFBB1D19881A591F88531)
- 从API version 20开始，支持通过[optimizeTrailingSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。 ```typescript Column() {  Text('Trimmed space enabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(true)  .textAlign(TextAlign.Center)  Text('Trimmed space disabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(false)  .textAlign(TextAlign.Center) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/H-TwxpN6TQOkiBSHF3q_fg/zh-cn_image_0000002571291383.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=D0BF94F656CA6C50F90B481C5C9E7B43A14B10C6B0FEDDFEBC94816199A28C98)
- 从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。 ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Extend(Text) function style() {  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 }) } @Entry @Component export struct LineSpacing {  build() {  NavDestination() {  Column() {  Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })  .style()  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/nuNnNARAS3eJCfPSLVyRuQ/zh-cn_image_0000002540611436.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=EC5FA1266314F01A366FAD8BEE40B48D806BF6D1F393F35E090D97CD7BC22C2F)
- 从API version 20开始，支持通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enableautospacing20)设置是否开启中文与西文的自动间距。 ```typescript @Entry @Component export struct EnableAutoSpacing {  @State enableSpacing: boolean = false;  build() {  NavDestination() {  Column() {  Row({ space: 20 }) {  Button($r('app.string.Enable_automatic_spacing'))  .onClick(() => this.enableSpacing = true)  .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')  .fontColor(this.enableSpacing ? Color.White : Color.Black)  Button($r('app.string.off_automatic_spacing'))  .onClick(() => this.enableSpacing = false)  .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')  .fontColor(!this.enableSpacing ? Color.White : Color.Black)  }  .width('100%')  .justifyContent(FlexAlign.Center)  .margin({ top: 30, bottom: 20 })  Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))  .fontSize(16)  .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')  .margin({ bottom: 20 })  Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))  .fontSize(24)  .padding(15)  .backgroundColor('#F5F5F5')  .width('90%')  .enableAutoSpacing(this.enableSpacing)  }  .width('100%')  .height('100%')  .padding(20)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/7bU9bHHdTh2a63lFpsQDOA/zh-cn_image_0000002571171431.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=E00393C6691A7B5CE4705D48AFE84AA654C6F2AF465F5CF79D6550BA585048F6)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#shaderstyle20)设置渐变色。 ```typescript @Entry @Component export struct ShaderStyle {  @State message: string = 'Hello World';  @State linearGradientOptions: LinearGradientOptions =  {  direction: GradientDirection.LeftTop,  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true,  };  build() {  NavDestination() {  Column({ space: 5 }) {  Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)  .margin({ top: 40, left: 40 })  Text(this.message)  .fontSize(50)  .width('80%')  .height(50)  .shaderStyle(this.linearGradientOptions)  }  .height('100%')  .width('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/jPxEmayaSxupq_4uPyukQw/zh-cn_image_0000002540771088.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=351428F27947D2BDD532C386D516EA2A5EE430E5B712E42C3672A895B9602CF2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/dZdb00jxQ_SB7sVyf0hJWw/zh-cn_image_0000002571291385.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=E1516F460388EC53DE42D74689E6F0C244008622ED83396AC2449F63E04FCE58)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)属性实现文本段落在垂直方向的对齐。

- 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。 ```typescript Text() {  Span('Hello')  .fontSize(50)  ImageSpan($r('app.media.startIcon'))  .width(30).height(30)  .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)  Span('World') } .textVerticalAlign(TextVerticalAlign.CENTER) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Fkr_N6rSRZCFKOCwUTUsiA/zh-cn_image_0000002540611438.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=A4739D99187FD64B7BF313E80B06DBCEF14635C1A8B52B37E79FCCDFD9D8B1EB)

## 设置选中菜单

### 弹出选中菜单

- 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。 Text组件需要设置[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性才可以被选中。 ```typescript Text($r('app.string.selected_menu'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Jlqzf5QKReujsktUakhjFg/zh-cn_image_0000002571171433.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=010756875A358133E170CD46FD17F6CFC4BB8AE1A692DC838F67D248720B52AE)
- Text组件通过设置[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)属性绑定自定义选择菜单。 ```typescript controller: TextController = new TextController(); options: TextOptions = { controller: this.controller }; ``` ```typescript Text($r('app.string.show_selected_menu'), this.options)  .fontSize(30)  .copyOption(CopyOptions.InApp)  .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {  onAppear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));  },  onDisappear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));  }  }) ``` ```typescript @Builder RightClickTextCustomMenu() {  Column() {  Menu() {  MenuItemGroup() {  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })  .onClick(() => {  this.controller.closeSelectionMenu();  })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })  }  }.backgroundColor('#F0F0F0')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/-CWkPDL3T8ybidH-JVhR3g/zh-cn_image_0000002540771090.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=81265DD00BBFF27E8E72E623206B7EE051A9FD37CA936CE082BF9D4591344CC6)
- Text组件通过设置[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。 ```typescript Text($r('app.string.show_selected_menu'))  .fontSize(20)  .copyOption(CopyOptions.LocalDevice)  .editMenuOptions({  onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick  }) ``` ```typescript onCreateMenu = (menuItems: Array<TextMenuItem>) => {  let item1: TextMenuItem = {  content: 'customMenu1',  icon: $r('app.media.app_icon'),  id: TextMenuItemId.of('customMenu1'),  };  let item2: TextMenuItem = {  content: 'customMenu2',  id: TextMenuItemId.of('customMenu2'),  icon: $r('app.media.app_icon'),  };  menuItems.push(item1);  menuItems.unshift(item2);  return menuItems; } onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {  if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')  .id) + textRange.start + '; end:' +  textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.COPY)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +  textRange.start + '; end:' + textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +  textRange.start + '; end:' +  textRange.end);  return false;  }  return false; }; ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Y8k9JKCOTCyy7EzqQsKwBA/zh-cn_image_0000002571291387.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=6502534A3725DA535AB33C370F882C516C4B28A488182319F37A540C282A7ED7)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

- 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
- 在Text组件区域外点击空白处，前提是Text组件设置[selection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#selection11)属性，具体示例如下： ```typescript @Entry @Component export struct SelectionChange {  @State text: string =  'This is set selection to Selection text content This is set selection to Selection text content.';  @State start: number = 0;  @State end: number = 20;  build() {  NavDestination() {  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {  Text(this.text)  .fontSize(12)  .border({ width: 1 })  .lineHeight(20)  .margin(30)  .copyOption(CopyOptions.InApp)  .selection(this.start, this.end)  .onTextSelectionChange((selectionStart, selectionEnd) => {  this.start = selectionStart;  this.end = selectionEnd;  })  }  .height(600)  .width(335)  .borderWidth(1)  .onClick(() => {  this.start = -1;  this.end = -1;  })  }  } } ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/XztZ58tBSzSMku55r0Qs6w/zh-cn_image_0000002540611440.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=A0329554FA1AE5CE51A723A13C5E2CD7F51670516A9E997FF7E4F048CE473F02)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/KZFGFH_qSoasLMJ8tfmgXA/zh-cn_image_0000002571171435.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=287135CF09276F6DFA4BFF99C3773E33BB705C927D8D59AB494D5B3E9FC63E5B)

### 屏蔽系统服务类菜单

- 从API version 20开始，支持通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct ServiceMenuItems {  aboutToAppear(): void {  TextMenuController.disableSystemServiceMenuItems(true);  }  aboutToDisappear(): void {  TextMenuController.disableSystemServiceMenuItems(false);  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false;  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/BkAa6IjQSH6aNtgdNXKjjQ/zh-cn_image_0000002540771092.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=BE555FF1FD5AA2CA8564B7001DCAF67237F6DB895807C1194D8B80C32FB11885)
- 从API version 20开始，支持通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct DisableMenuItems {  aboutToAppear(): void {  TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])  }  aboutToDisappear(): void {  TextMenuController.disableMenuItems([])  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/CmJZCtdZSEmn0FcDwrMTRg/zh-cn_image_0000002571291391.jpg?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=EA36E539D54D4A3716D5A8D4A68C30DEC289908EAAB0B1F2636CFA071CC161DA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/t38hmQp2QJiZ2Sz4vrR0CQ/zh-cn_image_0000002540611442.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=A651F7246BA6192037B7DDD70433FEEFB70A32DB102BC55EBE1C0FFCE238523E)

## 设置AI菜单

Text组件通过[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)和[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

> **说明**
> 从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)设置为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。
>
> 该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

- 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true。
- 如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示： ```typescript Text($r('app.string.AIMenu_Text_One'))  .fontSize(16)  .copyOption(CopyOptions.LocalDevice)  .enableDataDetector(true)  .dataDetectorConfig({  types: [], onDetectResultUpdate: (result: string) => {  }  }) ```
- 如果需要调整识别出的样式，可以通过[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11对象说明)配置项。
- 如果需要调整菜单的位置，可以通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例12文本扩展自定义菜单)。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/GOdAHaU0Ry-L1yFPjMCI9g/zh-cn_image_0000002571171437.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=D1E556DC5EF92236147D6716F668A42397DDF9EEB12EBA8D119D186E37E5581B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/LyobuQ43QS2fOjEcuWp9FQ/zh-cn_image_0000002540771094.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=613C221FEBBC4DEA05BB6487FDF04A3225E8D2580E2098CD10AAAC777FB2A28E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/dtpdQ-wGSPW-3u40NCpHng/zh-cn_image_0000002571291393.png?HW-CC-KV=V1&HW-CC-Date=20260415T024819Z&HW-CC-Expire=86400&HW-CC-Sign=FE59DC7A2A0EE9790E1C01C76D15CE962CC99BF478EDF70FDBFF7D62DC3A1028)

## 示例代码

- [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
