# 文本显示 (Text/Span)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display

Text是文本组件，用于展示用户视图，如显示文章的文字内容。该组件支持绑定自定义文本选择菜单，用户可根据需要选择不同功能。此外，还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于展示行内文本。

具体用法请参考[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)组件的使用说明。

常见问题请参考[文本显示（Text/Span）常见问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq#文本显示textspan常见问题)。

## 创建文本

Text可通过以下两种方式来创建：

- string字符串。 ```typescript Text('我是一段文本') ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Pk8nRBXTT9W-cuygLTnd1A/zh-cn_image_0000002566019187.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=C86A3BCE5F6F249F77FC0803B26F6800B484310F589CB9DDD5F87962E2886AD3)

- 引用Resource资源。 资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json，具体内容如下： ```typescript {  "string": [  {  "name": "module_desc",  "value": "模块描述"  }  ] } ``` ```typescript Text($r('app.string.module_desc'))  .baselineOffset(0)  .fontSize(30)  .border({ width: 1 })  .padding(10)  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/PAW7OCYUS3Cfd9wqP6ak1w/zh-cn_image_0000002566099199.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=5D64D2B3728B793189C3B3A889E01841F44C987A5786F389A260DFA42416E065)

## 添加子组件

[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)只能作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)和[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

- 创建Span。 Span组件需嵌入在Text组件中才能显示，单独使用时不会显示任何内容。Text与Span同时配置文本内容时，Span内容将覆盖Text内容。 ```typescript Text($r('app.string.TextSpan_textContent_text')) {  Span($r('app.string.TextSpan_textContent_span')) } .padding(10) .borderWidth(1) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ZkdcejybTbSZUXwBaoenjw/zh-cn_image_0000002535139388.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=7996BE167D0C252922E0A41B372DCE5A127133C47CBBB37E54559525F0E243B9)
- 设置文本装饰线及颜色。 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置文本装饰线及颜色。 ```typescript Text() {  Span($r('app.string.TextSpan_textContent_span_one'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })  Span($r('app.string.TextSpan_textContent_span_two'))  .fontColor(Color.Blue)  .fontSize(16)  .fontStyle(FontStyle.Italic)  .decoration({ type: TextDecorationType.Underline, color: Color.Black })  Span($r('app.string.TextSpan_textContent_span_three'))  .fontSize(16)  .fontColor(Color.Grey)  .decoration({ type: TextDecorationType.Overline, color: Color.Green }) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/js0xaOOxStqdIwf9cn4qMA/zh-cn_image_0000002535299326.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=CC353677EAE0C94195CAC95A5764B7440A1F47E7261BC3DAACBE12BE7AAFCDF6)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textcase)设置文字一直保持大写或者小写状态。 ```typescript Text() {  Span('I am Upper-span').fontSize(12)  .textCase(TextCase.UpperCase) } .borderWidth(1) .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/WnBa-I0rS86zM8HgW9ZwzQ/zh-cn_image_0000002566019189.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=5B177FC2951F7DB855B4E02154310AE986195E5509D57409845EBC83D8EB49FF)
- 添加事件。 由于Span组件无尺寸信息，仅支持添加点击事件[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、悬浮事件[onHover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover#onhover)。 ```typescript import { hilog } from '@kit.PerformanceAnalysisKit'; @Entry @Component export struct TextSpanOnHover {  @State textStr1: string = '';  @State textStr2: string = '';  build() {  NavDestination() {  Row() {  Column() {  Text() {  Span('I am Upper-span')  .textCase(TextCase.UpperCase)  .fontSize(30)  .onClick(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onClick is triggering');  this.textStr1 = 'Span onClick is triggering';  })  .onHover(() => {  hilog.info(0x0000, 'Sample_TextComponent', 'Span onHover is triggering');  this.textStr2 = 'Span onHover is triggering';  })  }  Text('onClick：' + this.textStr1)  .fontSize(20)  Text('onHover：' + this.textStr2)  .fontSize(20)  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/4jQZeV0LQE2VWVW_3Av-Sw/zh-cn_image_0000002566099201.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=E14842936BFE48595A66A289B26958804C3BBBCC0554BEED25502892A53AE61D)

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

- 通过[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)属性设置文本对齐样式。 ```typescript Text($r('app.string.TextAlign_Start'))  .width(300)  .textAlign(TextAlign.Start)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_Center'))  .width(300)  .textAlign(TextAlign.Center)  .border({ width: 1 })  .padding(10) Text($r('app.string.TextAlign_End'))  .width(300)  .textAlign(TextAlign.End)  .border({ width: 1 })  .padding(10) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1TixucrETXG99NiB5r9rBQ/zh-cn_image_0000002535139390.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=85E9FFE393D84A532A1FF5AC59449BA8284383828565A989999703A3B15099D3)
- 通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)属性控制文本超长处理，textOverflow需配合[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)一起使用（默认情况下文本自动折行）。从API version 18开始，文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。 ```typescript Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow ' +  'to None text content. This is the setting of textOverflow to Clip text content This is the setting ' +  'of textOverflow to None text content.')  .width(250)  .textOverflow({ overflow: TextOverflow.None })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_epsis'))  .width(250)  .textOverflow({ overflow: TextOverflow.Ellipsis })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10) Text($r('app.string.CustomTextStyle_textContent_marq_def'))  .width(250)  .textOverflow({ overflow: TextOverflow.MARQUEE })  .maxLines(1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .marqueeOptions({  start: true,  fromStart: true,  step: 6,  loop: -1,  delay: 0,  fadeout: false,  marqueeStartPolicy: MarqueeStartPolicy.DEFAULT  }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/z3RniGxaRla_oH5xx5K7aA/zh-cn_image_0000002535299328.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=F6207CBAA2FE218B3688280B4CD6A497E5EC961B550388E2D2A9EB318058EAAC)
- 通过[lineHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#lineheight)属性设置文本行高。 ```typescript Text('This is the text with the line height set. This is the text with the line height set.')  .width(300).fontSize(12).border({ width: 1 }).padding(10) Text('This is the text with the line height set. This is the text with the line height set.')  .width(300)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .lineHeight(20) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/QhcBSChbSzaI3_SZlONY7Q/zh-cn_image_0000002566019191.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=78E657F32C530F05074B33C465E45BE5A7D84816A374BB163899315873208CDF)
- 通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性设置文本装饰线样式、颜色及其粗细。 ```typescript Text('This is the text')  .decoration({  type: TextDecorationType.LineThrough,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Overline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Red  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DASHED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOTTED  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.DOUBLE  })  .borderWidth(1).padding(15).margin(5) Text('This is the text')  .decoration({  type: TextDecorationType.Underline,  color: Color.Blue,  style: TextDecorationStyle.WAVY,  thicknessScale: 4  })  .borderWidth(1).padding(15).margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/ObS0gvDCT_uEjTThnp550Q/zh-cn_image_0000002566099203.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=529DB275BDDE14F99F5F6B9D5AEF93B81A650D00579743F9A673F37443ABBEAE)
- 通过[baselineOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#baselineoffset)属性设置文本基线的偏移量。 ```typescript Text('This is the text content with baselineOffset 0.')  .baselineOffset(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset 30.')  .baselineOffset(30)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with baselineOffset -20.')  .baselineOffset(-20)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/VTGG2vzrQ9ikP_bznW7deQ/zh-cn_image_0000002535139392.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=FE78A384F424EE19420DD9CE3AF3CBECF41B62C1FF34D450B823C7EAC470FB70)
- 通过[letterSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#letterspacing)属性设置文本字符间距。 ```typescript Text('This is the text content with letterSpacing 0.')  .letterSpacing(0)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing 3.')  .letterSpacing(3)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) Text('This is the text content with letterSpacing -1.')  .letterSpacing(-1)  .fontSize(12)  .border({ width: 1 })  .padding(10)  .width('100%')  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/hgFTKD54QPGE2_qLKtqVDg/zh-cn_image_0000002535299330.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=D68A2ECB4C597D7A8D510FE6483A08B145E84A82877E011391E6C19C7737699F)
- 通过[minFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#minfontsize)与[maxFontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxfontsize)自适应字体大小。 minFontSize用于设置文本的最小显示字号，maxFontSize用于设置文本的最大显示字号。这两个属性必须同时设置才能生效，并且需要与[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性或布局大小限制配合使用，单独设置任一属性将不会产生效果。 ```typescript Text($r('app.string.CustomTextStyle_textContent_one_style'))  .width(250)  .maxLines(1)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_two_style'))  .width(250)  .maxLines(2)  .maxFontSize(30)  .minFontSize(5)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_no_max'))  .width(250)  .height(50)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) Text($r('app.string.CustomTextStyle_textContent_high'))  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/uWo2YXqmRR-a37GyKKC9eQ/zh-cn_image_0000002566019193.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=42D5B0F806532E79E46D3BAE8BE47604F72782ED18CEF11AB41506E02C5FC079)
- 通过[textCase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcase)属性设置文本大小写。 ```typescript Text('This is the text content with textCase set to Normal.')  .textCase(TextCase.Normal)  .padding(10)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to LowerCase.')  .textCase(TextCase.LowerCase)  .border({ width: 1 })  .padding(10)  .margin(5) Text('This is the text content with textCase set to UpperCase.')  .textCase(TextCase.UpperCase)  .border({ width: 1 })  .padding(10)  .margin(5) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/a4HWGxamQsar8v_8H6bxSg/zh-cn_image_0000002566099205.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=C93DE875EA1058FD96F36CB9EEDB8B1E24E71F2CA48E9AB2B96EC13E1D8C0C67)
- 通过[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性设置文本是否可复制粘贴。 ```typescript Text($r('app.string.CustomTextStyle_textContent_incopy'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uNfaQzk-QB6LXz9yK86mrA/zh-cn_image_0000002535139394.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=B37C435529AA410D130BE2E27F7F87F3E20BAECDECDB59593F92CFD52B584F1A)
- 通过[fontFamily](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfamily)属性设置字体列表。应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。 ```typescript Text('This is the text content with fontFamily')  .fontSize(30)  .fontFamily('HarmonyOS Sans') ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/DdpTOGT1RXCI-aMVfElACg/zh-cn_image_0000002535299332.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=070627778047C085AC80A65D162F36F55BEC926E9C1F19B1360BC79609ADCF96)
- 从API version 20开始，支持通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#contenttransition20)属性设置数字翻牌效果。 ```typescript @Entry @Component export struct ContentTransition {  private static readonly INITIAL_SCORE: number = 98;  @State number: number = ContentTransition.INITIAL_SCORE;  @State numberTransition: NumericTextTransition =  new NumericTextTransition({ flipDirection: FlipDirection.DOWN, enableBlur: false });  build() {  NavDestination() {  Column() {  Text(this.number + '')  .borderWidth(1)  .fontSize(40)  .contentTransition(this.numberTransition)  Button('chang number')  .onClick(() => {  this.number++  })  .margin(10)  }  .width('100%')  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/yEOGWDw8R1SlruHWK-KEfA/zh-cn_image_0000002566019195.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=EFE7AE3604204E5A80450D651810964A47EF8DE0C8B614F06114E0B167E25D6A)
- 从API version 20开始，支持通过[optimizeTrailingSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#optimizetrailingspace20)设置是否在文本布局过程中优化每行末尾的空格，可解决行尾空格影响对齐显示效果问题。 ```typescript Column() {  Text('Trimmed space enabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(true)  .textAlign(TextAlign.Center)  Text('Trimmed space disabled ')  .fontSize(30)  .fontWeight(FontWeight.Bold)  .margin({ top: 20 })  .optimizeTrailingSpace(false)  .textAlign(TextAlign.Center) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/xm9U8auXTcS_BrMSMO6mrQ/zh-cn_image_0000002566099207.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=E42A7CB11B22AF2C6363C0BC6DBA8085D8847C9709C7C508EEF0C533F8EA0CB8)
- 从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。当不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距，当onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外的行间距。 ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Extend(Text) function style() {  .width(250)  .height(100)  .maxFontSize(30)  .minFontSize(15)  .border({ width: 1 }) } @Entry @Component export struct LineSpacing {  build() {  NavDestination() {  Column() {  Text('The line spacing of this context is set to 20_px, and the spacing is effective only between the lines.')  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })  .style()  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/L1Z4pwWBR124o_55OGUmjQ/zh-cn_image_0000002535139396.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=31A06F763222B3B4FE53010B4824F3216AB617042C297C55308A9E01CEC36633)
- 从API version 20开始，支持通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enableautospacing20)设置是否开启中文与西文的自动间距。 ```typescript @Entry @Component export struct EnableAutoSpacing {  @State enableSpacing: boolean = false;  build() {  NavDestination() {  Column() {  Row({ space: 20 }) {  Button($r('app.string.Enable_automatic_spacing'))  .onClick(() => this.enableSpacing = true)  .backgroundColor(this.enableSpacing ? '#4CAF50' : '#E0E0E0')  .fontColor(this.enableSpacing ? Color.White : Color.Black)  Button($r('app.string.off_automatic_spacing'))  .onClick(() => this.enableSpacing = false)  .backgroundColor(!this.enableSpacing ? '#F44336' : '#E0E0E0')  .fontColor(!this.enableSpacing ? Color.White : Color.Black)  }  .width('100%')  .justifyContent(FlexAlign.Center)  .margin({ top: 30, bottom: 20 })  Text(this.enableSpacing ? $r('app.string.Automatic_spacing_has_been_enabled') : $r('app.string.Automatic_spacing_has_been_turned_off'))  .fontSize(16)  .fontColor(this.enableSpacing ? '#4CAF50' : '#F44336')  .margin({ bottom: 20 })  Text($r('app.string.Chinese_and_Western_Auto_Spacing_automatic_spacing'))  .fontSize(24)  .padding(15)  .backgroundColor('#F5F5F5')  .width('90%')  .enableAutoSpacing(this.enableSpacing)  }  .width('100%')  .height('100%')  .padding(20)  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/uabsgafMRG2Pm49UKjpuig/zh-cn_image_0000002535299334.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=145211F9DA748E598116E603F80788948F7529968CE0EEAE12F9CAC5A2585448)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#shaderstyle20)设置渐变色。 ```typescript @Entry @Component export struct ShaderStyle {  @State message: string = 'Hello World';  @State linearGradientOptions: LinearGradientOptions =  {  direction: GradientDirection.LeftTop,  colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],  repeating: true,  };  build() {  NavDestination() {  Column({ space: 5 }) {  Text($r('app.string.direction_LeftTop')).fontSize(18).width('90%').fontColor(0xCCCCCC)  .margin({ top: 40, left: 40 })  Text(this.message)  .fontSize(50)  .width('80%')  .height(50)  .shaderStyle(this.linearGradientOptions)  }  .height('100%')  .width('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uvrWtimsSEKf16XdmDzTMg/zh-cn_image_0000002566019197.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=44D1BA9224C316451390E2EDA45FE95AD64B2ED4B7EEA04269F88978B378F499)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/p60QcwxpS6CY2baSU-7EiQ/zh-cn_image_0000002566099209.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=4E52CC34BEE9A846D32FA70DC53D930FFF58899161AC188A399C4C0A727C96F2)

## 设置垂直居中

从API version 20开始，Text组件支持通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)属性实现文本段落在垂直方向的对齐。

- 以下示例展示了如何通过textVerticalAlign属性设置文本垂直居中对齐效果。 ```typescript Text() {  Span('Hello')  .fontSize(50)  ImageSpan($r('app.media.startIcon'))  .width(30).height(30)  .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)  Span('World') } .textVerticalAlign(TextVerticalAlign.CENTER) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ZisxELQxQd28WdMEEygMUQ/zh-cn_image_0000002535139398.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=AFFBFA259D3C7EB67BD6D0EADF185C2431DDC59B0AE2FE5FB26C70C06646D8BC)

## 设置选中菜单

### 弹出选中菜单

- 设置Text被选中时，会弹出包含复制、翻译、搜索的菜单。 Text组件需要设置[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)属性才可以被选中。 ```typescript Text($r('app.string.selected_menu'))  .fontSize(30)  .copyOption(CopyOptions.InApp) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/QuoLEutqQRSsuYwddourRQ/zh-cn_image_0000002535299336.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=B13DDB2CF5930F75FD2521847B80533A09F04EFA8B0E931975DBC9915993E9D9)
- Text组件通过设置[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#bindselectionmenu11)属性绑定自定义选择菜单。 ```typescript controller: TextController = new TextController(); options: TextOptions = { controller: this.controller }; ``` ```typescript Text($r('app.string.show_selected_menu'), this.options)  .fontSize(30)  .copyOption(CopyOptions.InApp)  .bindSelectionMenu(TextSpanType.TEXT, this.RightClickTextCustomMenu, TextResponseType.RIGHT_CLICK, {  onAppear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Ejected').id));  },  onDisappear: () => {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_Close').id));  }  }) ``` ```typescript @Builder RightClickTextCustomMenu() {  Column() {  Menu() {  MenuItemGroup() {  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu One', labelInfo: '' })  .onClick(() => {  this.controller.closeSelectionMenu();  })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Two', labelInfo: '' })  MenuItem({ startIcon: $r('app.media.app_icon'), content: 'CustomMenu Three', labelInfo: '' })  }  }.backgroundColor('#F0F0F0')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/VeEN6qRTQyq5-kQhwI0zTQ/zh-cn_image_0000002566019199.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=33E4AE11AD7575E4E5DB3F89590939A444D8305572E62D0B3B296C1540EB5994)
- Text组件通过设置[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)属性扩展自定义选择菜单，可以设置扩展项的文本内容、图标以及回调方法。 ```typescript Text($r('app.string.show_selected_menu'))  .fontSize(20)  .copyOption(CopyOptions.LocalDevice)  .editMenuOptions({  onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick  }) ``` ```typescript onCreateMenu = (menuItems: Array<TextMenuItem>) => {  let item1: TextMenuItem = {  content: 'customMenu1',  icon: $r('app.media.app_icon'),  id: TextMenuItemId.of('customMenu1'),  };  let item2: TextMenuItem = {  content: 'customMenu2',  id: TextMenuItemId.of('customMenu2'),  icon: $r('app.media.app_icon'),  };  menuItems.push(item1);  menuItems.unshift(item2);  return menuItems; } onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {  if (menuItem.id.equals(TextMenuItemId.of('customMenu2'))) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_customMenu')  .id) + textRange.start + '; end:' +  textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.COPY)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_copy').id) +  textRange.start + '; end:' + textRange.end);  return true;  }  if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {  hilog.info(0x0000, 'Sample_TextComponent',  this.getUIContext()  .getHostContext()!.resourceManager.getStringSync($r('app.string.SelectMenu_Text_SelectionAll').id) +  textRange.start + '; end:' +  textRange.end);  return false;  }  return false; }; ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/qz6qCSHYQX6Ez-f3mKtiDw/zh-cn_image_0000002566099211.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=4BC4EFCF46175DBD43742E076F41C57B436038EF8E84894004F1352A4781F389)

### 关闭选中菜单

使用Text组件时，若需要实现点击空白处关闭选中的场景，分为以下两种情况：

- 在Text组件区域内点击空白处，会正常关闭选中态和菜单；
- 在Text组件区域外点击空白处，前提是Text组件设置[selection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#selection11)属性，具体示例如下： ```typescript @Entry @Component export struct SelectionChange {  @State text: string =  'This is set selection to Selection text content This is set selection to Selection text content.';  @State start: number = 0;  @State end: number = 20;  build() {  NavDestination() {  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {  Text(this.text)  .fontSize(12)  .border({ width: 1 })  .lineHeight(20)  .margin(30)  .copyOption(CopyOptions.InApp)  .selection(this.start, this.end)  .onTextSelectionChange((selectionStart, selectionEnd) => {  this.start = selectionStart;  this.end = selectionEnd;  })  }  .height(600)  .width(335)  .borderWidth(1)  .onClick(() => {  this.start = -1;  this.end = -1;  })  }  } } ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/nMCJ04M-QuSNiwgyPIlrLA/zh-cn_image_0000002535139400.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=852591F684C5927E514A221DD9DFBFACAE4E6AE833262AC2E9ACD1EF250713AE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/A3dl8KGKT9ug1Jqcwf6FAQ/zh-cn_image_0000002535299338.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=E804E43A19C82D8B0693630486A85A434EA5D631F7AC6D1C5587E39520640DFE)

### 屏蔽系统服务类菜单

- 从API version 20开始，支持通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽文本选择菜单内所有系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct ServiceMenuItems {  aboutToAppear(): void {  TextMenuController.disableSystemServiceMenuItems(true);  }  aboutToDisappear(): void {  TextMenuController.disableSystemServiceMenuItems(false);  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false;  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/_NqxDkMKRb6UXRHcUWe4AA/zh-cn_image_0000002566019201.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=4491D7CED28C0D029E3600A01527BC27905932316FE4CF24A53CD9595B262832)
- 从API version 20开始，支持通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)屏蔽文本选择菜单内指定的系统服务菜单项。 ```typescript import { TextMenuController } from '@kit.ArkUI'; @Entry @Component export struct DisableMenuItems {  aboutToAppear(): void {  TextMenuController.disableMenuItems([TextMenuItemId.SEARCH])  }  aboutToDisappear(): void {  TextMenuController.disableMenuItems([])  }  build() {  NavDestination() {  Row() {  Column() {  Text($r('app.string.Service_MenuItems_Text'))  .height(60)  .fontStyle(FontStyle.Italic)  .fontWeight(FontWeight.Bold)  .textAlign(TextAlign.Center)  .copyOption(CopyOptions.InApp)  .editMenuOptions({  onCreateMenu: (menuItems: Array<TextMenuItem>) => {  return menuItems;  },  onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {  return false  }  })  }.width('100%')  }  .height('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/JOsGhBZnSLOn052XJid2sw/zh-cn_image_0000002566099213.jpg?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=BBA272AC4F6DA045464D2FBD2552B8B59C6AACAA9E053B491E6AF30D96D9776B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/zY5Vy9KAS3WUz9l0c4AH9g/zh-cn_image_0000002535139402.gif?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=DFD695B4575AB3068CBEB016BD41A9DCB14CA8A0C8FB212A7AADD24327946812)

## 设置AI菜单

Text组件通过[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)和[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)属性实现AI菜单的显示。AI菜单的表现形式包括：单击AI实体（指可被识别的内容，包括地址、邮箱等）弹出菜单的实体识别选项，选中文本后，文本选择菜单与鼠标右键菜单中显示的实体识别选项。

> **说明**
> 从API version 20开始，支持在文本选择菜单与鼠标右键菜单中显示实体识别选项。当[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)设置为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice时，该功能生效。菜单选项包括[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)中的url(打开链接)、email(新建邮件)、phoneNumber(呼叫)、address(导航至该位置)、dateTime(新建日程提醒)。
>
> 该功能生效时，需选中范围内，包括一个完整的AI实体，才能展示对应的选项。

- 如果需要单击AI实体弹出菜单的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true。
- 如果在单击的交互方式之外，还需要文本选择菜单与鼠标右键菜单中显示的实体识别选项，可以配置[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)为true，且[copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#copyoption9)设置为CopyOptions.LocalDevice，具体示例如下所示： ```typescript Text($r('app.string.AIMenu_Text_One'))  .fontSize(16)  .copyOption(CopyOptions.LocalDevice)  .enableDataDetector(true)  .dataDetectorConfig({  types: [], onDetectResultUpdate: (result: string) => {  }  }) ```
- 如果需要调整识别出的样式，可以通过[dataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#datadetectorconfig11)实现，具体可以参考[TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textdatadetectorconfig11对象说明)配置项。
- 如果需要调整菜单的位置，可以通过[editMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#editmenuoptions12)实现，具体可以参考示例[文本扩展自定义菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例12文本扩展自定义菜单)。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/yd-_LJG4TFiQ9-CnA7MWcg/zh-cn_image_0000002535299340.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=FED2BC56C8D0C7BD3A390BBC3BE6411B36C9942258EFF4FA4537834B64EBD542)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/DFEuR3vvTXGjSBjwC8vAzg/zh-cn_image_0000002566019203.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=1DA05B4F8232D77288B3156D702D5B99F62A0FC679358EEF9CC28D8AB0152703)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/lwJEdOuhRS-5gBe3CQttqg/zh-cn_image_0000002566099215.png?HW-CC-KV=V1&HW-CC-Date=20260403T023918Z&HW-CC-Expire=86400&HW-CC-Sign=25D4F87ABFD09AEE32C302AA22D6F726AFF645B05CA9F990F3E26B103C8224AF)

## 示例代码

- [文字特效合集](https://gitcode.com/HarmonyOS_Samples/text-effects)
