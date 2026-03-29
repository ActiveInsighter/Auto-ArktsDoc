# 属性字符串（StyledString/MutableStyledString）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-styled-string

属性字符串StyledString/MutableStyledString（其中MutableStyledString继承自StyledString，下文统称为StyledString），可用于在字符或段落级别上设置文本样式。将StyledString应用到文本组件上，可以采用多种方式修改文本，包括调整字号、添加字体颜色、使文本具备可点击性，以及通过自定义方式绘制文本等。具体使用方法请参考[属性字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string)的API文档。

属性字符串提供多种类型样式对象，涵盖各种常见的文本样式格式，例如文本装饰线样式、文本行高样式、文本阴影样式等。也可以自行创建[CustomSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#customspan)，以应用自定义样式。

## 创建并应用StyledString和MutableStyledString

可以通过[TextController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textcontroller11)提供的[setStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#setstyledstring12)方法，将属性字符串附加到文本组件，并推荐在[onPageShow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow)或者文本组件的[onAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide#onappear)回调中触发绑定。

> **说明**
> 在[aboutToAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear)中调用setStyledString方法时，由于该方法运行阶段组件尚未完成创建并成功挂载节点树，因此无法在页面初始化时显示属性字符串。
>
> 从API version 15开始，在aboutToAppear中调用setStyledString方法，页面初始化时可以显示属性字符串。

```typescript
@Entry
@Component
struct styled_string_demo1 {

  styledString1: StyledString = new StyledString( this.getUIContext()
    .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply_Text_Forty_Five').id));

  mutableStyledString1: MutableStyledString = new MutableStyledString( this.getUIContext()
    .getHostContext()!.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five').id));
  controller1: TextController = new TextController();
  controller2: TextController = new TextController();

  async onPageShow() {

    this.controller1.setStyledString(this.styledString1);
  }

  build() {
    Column() {

      Text(undefined, { controller: this.controller1 })
      Text(undefined, { controller: this.controller2 })
        .onAppear(() => {

          this.controller2.setStyledString(this.mutableStyledString1);
        })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/sVd6qaxPSaevHO3ovnO5RA/zh-cn_image_0000002563785857.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=A4E6E001811630B8D1A6D4A4E05C8439F43E7ECC3E0ABA4DE67B5B1010A5CCDD)

## 设置文本样式

属性字符串目前提供了多种Style对象，包括[TextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#textstyle)、[TextShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#textshadowstyle)、[DecorationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#decorationstyle)、[BaselineOffsetStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#baselineoffsetstyle)、[LineHeightStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#lineheightstyle)、[LetterSpacingStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#letterspacingstyle)，用于设置文本的各类样式。

- 创建及应用文本字体样式对象（TextStyle） ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Entry @Component struct styled_string_demo2 {  @State str: string =  this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.CreateApply_Text_3')) as string;  textStyleAttrs: TextStyle =  new TextStyle({  fontWeight: FontWeight.Bolder,  fontSize: LengthMetrics.vp(24),  fontStyle: FontStyle.Italic,  strokeWidth: LengthMetrics.px(5),  strokeColor: Color.Green  });  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 2,  length: 2,  styledKey: StyledStringKey.FONT,  styledValue: this.textStyleAttrs  },  {  start: 7,  length: 4,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({  fontColor: Color.Orange, fontSize: LengthMetrics.vp(12),  superscript: SuperscriptStyle.SUPERSCRIPT  })  }  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  .margin({ top: 10 })  }  .width('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/q7JQAKo2Sc2M6Eh8FHd47g/zh-cn_image_0000002532905962.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=BFDB12639E3414470FB01B2E82087ADD5ACE205A665CFB6FEBDFD8F883A81E68)
- 创建及应用文本阴影对象（TextShadowStyle） ```typescript @Entry @Component struct styled_string_demo3 {  @State str: string =  this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five')) as string;  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 0,  length: 3,  styledKey: StyledStringKey.TEXT_SHADOW,  styledValue: new TextShadowStyle({  radius: 5,  type: ShadowType.COLOR,  color: Color.Red,  offsetX: 10,  offsetY: 10  })  }  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  }  .width('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/AFcz1mr-SqGKJfB1G2L4MA/zh-cn_image_0000002533065910.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=182A89B242380FFBB1222098A07526E1C2EDC70649334E68701199EE0FC2EE7F)
- 创建及应用文本装饰线对象（DecorationStyle） ```typescript @Entry @Component struct styled_string_demo4 {  @State str: string =  this.getUIContext()  .getHostContext()?.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five')) as string;  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 0,  length: 4,  styledKey: StyledStringKey.DECORATION,  styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Red, thicknessScale: 3 })  },  {  start: 4,  length: 2,  styledKey: StyledStringKey.DECORATION,  styledValue: new DecorationStyle(  {  type: TextDecorationType.Underline,  },  {  enableMultiType: true  }  )  },  {  start: 4,  length: 2,  styledKey: StyledStringKey.DECORATION,  styledValue: new DecorationStyle(  {  type: TextDecorationType.LineThrough,  },  {  enableMultiType: true  }  )  },  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  }  .width('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/_ChYVj4dQR-_13jDBZ_6NA/zh-cn_image_0000002563865813.jpg?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=B66C3E86165595552C24C84C690BF892C32A28D69D68B801CEF34BCC38B0E880)
- 创建及应用文本基线偏移量对象（BaselineOffsetStyle） ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Entry @Component struct styled_string_demo5 {  @State str: string =  this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five')) as string;  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 0,  length: 3,  styledKey: StyledStringKey.BASELINE_OFFSET,  styledValue: new BaselineOffsetStyle(LengthMetrics.px(20))  }  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  }  .width('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/YdShqK9uTBSArmanONnqUg/zh-cn_image_0000002563785859.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=B657F4EC2E4D128472B9080B249389F9DF6D72424E71E1A551C4FDA28AE23852)
- 创建及应用文本行高对象（LineHeightStyle） ```typescript import { LengthMetrics } from '@kit.ArkUI'; @Entry @Component struct styled_string_demo6 {  @State str: string =  this.getUIContext()  .getHostContext()?.resourceManager.getStringSync($r('app.string.StyledStringStyle_Text_5')) as string;  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 8,  length: 3,  styledKey: StyledStringKey.LINE_HEIGHT,  styledValue: new LineHeightStyle(LengthMetrics.vp(50))  }  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  }  .width('100%')  .margin({ top: 10 })  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/pkR_D-xlQASEghCljghGIw/zh-cn_image_0000002532905964.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=EBFACA45CCDF62BE1DDDD21CC6A33A7493792BD3DBEE339E987F4D270300F117)
- 创建及应用文本字符间距对象（LetterSpacingStyle） ```typescript import { LengthMetrics, LengthUnit } from '@kit.ArkUI'; @Entry @Component struct styled_string_demo7 {  @State str: string =  this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.CreateApply_Text_Third_Five')) as string;  mutableStyledString: MutableStyledString = new MutableStyledString(this.str, [  {  start: 0,  length: 2,  styledKey: StyledStringKey.LETTER_SPACING,  styledValue: new LetterSpacingStyle(new LengthMetrics(20, LengthUnit.VP))  }  ]);  controller: TextController = new TextController();  async onPageShow() {  this.controller.setStyledString(this.mutableStyledString);  }  build() {  Column() {  Text(undefined, { controller: this.controller })  }  .width('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/rL-KAB9hTy6nfWt9Rr3t7w/zh-cn_image_0000002533065912.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=F12416DD1FA7EA5985839AEA52B8940F819E09BD97467B3B28FEACECEDF9B024)

## 设置段落样式

可通过[ParagraphStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#paragraphstyle)设置段落样式布局。下图显示了如何分割文本中的段落，段落以换行符 \n 结尾。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/KR81QBHfSFqUQL3DJoeRgQ/zh-cn_image_0000002563865815.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=36A56572B7725C92FDCC0AB7BAE558A3C8D482B53ED406A5EA7FA559CE0248B5)

以下代码示例展示了如何创建ParagraphStyle并应用。如果将ParagraphStyle附加到段落开头、末尾或之间的任何位置，均会应用样式，非段落区间内则不会应用样式。

```typescript
import { LengthMetrics} from '@kit.ArkUI';

@Entry
@Component
struct Index {

  @State str: string =
    this.getUIContext()
      .getHostContext()?.resourceManager.getStringSync($r('app.string.StyledStringParagraphStyle_Text_1')) as string;
  titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });

  paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });

  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));

  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.str, [
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.titleParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: new LineHeightStyle(new LengthMetrics(50))
      }, {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
    },
      {
        start: 5,
        length: 3,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.paragraphStyleAttr1
      },
      {
        start: 5,
        length: 20,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    ]);
  controller: TextController = new TextController();

  async onPageShow() {
    this.controller.setStyledString(this.paragraphStyledString1);
  }

  build() {
    Column() {

      Text(undefined, { controller: this.controller })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/jMI7ycpCTvmCy-WZZ29kMA/zh-cn_image_0000002563785861.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=BF2310CC93BC1739149EBF4C232111E3F286123C76EF2D5BA143284C75F8B6E1)

除了可以在创建属性字符串时就预设样式，也可以后续通过[replaceStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#replacestyle)清空原样式替换新样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext();

  @State message1: string =
    this.context!.resourceManager.getStringSync($r('app.string.StyledStringParagraphStyle_Text_2').id);
  titleParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });

  paragraphStyleAttr1: ParagraphStyle = new ParagraphStyle({ textIndent: LengthMetrics.vp(15) });

  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));

  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.message1, [
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.titleParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: new LineHeightStyle(new LengthMetrics(50))
      }, {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
    },
      {
        start: 5,
        length: 3,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.paragraphStyleAttr1
      },
      {
        start: 5,
        length: 20,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    ]);
  paragraphStyleAttr3: ParagraphStyle = new ParagraphStyle({
    textAlign: TextAlign.End,
    maxLines: 1,
    wordBreak: WordBreak.BREAK_ALL,
    overflow: TextOverflow.Ellipsis
  });
  controller: TextController = new TextController();

  async onPageShow() {
    this.controller.setStyledString(this.paragraphStyledString1);
  }

  build() {
    Column() {

      Text(undefined, { controller: this.controller }).width(300)

      Button($r('app.string.Replace_paragraph_style'))
        .onClick(() => {
          this.paragraphStyledString1.replaceStyle({
            start: 5,
            length: 3,
            styledKey: StyledStringKey.PARAGRAPH_STYLE,
            styledValue: this.paragraphStyleAttr3
          });
          this.controller.setStyledString(this.paragraphStyledString1);
        })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/3smD5r2ISPWi_44Hjs72eg/zh-cn_image_0000002532905966.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=29CB51B6CC1B5D1B37D855C27396C104EB88EC4CB5C0994E39A1928F3C778CDB)

## 支持将属性字符串转换成Paragraph

可通过[getParagraphs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#getparagraphs20)将属性字符串根据文本布局选项转换成对应的[Paragraph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#paragraph)数组。

- 以下示例展示了通过[MeasureUtils](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils)的getParagraphs方法测算文本，当内容超出最大显示行数的时候，截断文本显示并展示“...全文”的效果。 ```typescript import { LengthMetrics } from '@kit.ArkUI'; import { drawing } from '@kit.ArkGraphics2D'; class MyCustomSpan extends CustomSpan {  constructor(word: string, width: number, height: number, context: UIContext) {  super();  this.word = word;  this.width = width;  this.height = height;  this.context = context;  }  onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {  return { width: this.width, height: this.height };  }  onDraw(context: DrawContext, options: CustomSpanDrawInfo) {  let canvas = context.canvas;  const brush = new drawing.Brush();  brush.setColor({  alpha: 255,  red: 0,  green: 74,  blue: 175  });  const font = new drawing.Font();  font.setSize(25);  const textBlob = drawing.TextBlob.makeFromString(this.word, font, drawing.TextEncoding.TEXT_ENCODING_UTF8);  canvas.attachBrush(brush);  canvas.drawRect({  left: options.x + 10,  right: options.x + this.context.vp2px(this.width) - 10,  top: options.lineTop + 10,  bottom: options.lineBottom - 10  });  brush.setColor({  alpha: 255,  red: 23,  green: 169,  blue: 141  });  canvas.attachBrush(brush);  canvas.drawTextBlob(textBlob, options.x + 20, options.lineBottom - 15);  canvas.detachBrush();  }  setWord(word: string) {  this.word = word;  }  public width: number = 160;  public word: string = 'drawing';  public height: number = 10;  public context: UIContext; } @Entry @Component struct Index {  @State fullText: string =  this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Full_text') as string;  @State originalText: ResourceStr = $r('app.string.Original_text');  @State afterTypesetting: ResourceStr = $r('app.string.After_typesetting');  str: string =  'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.';  mutableStr2 = new MutableStyledString(this.str, [  {  start: 0,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontSize: LengthMetrics.px(20) })  },  {  start: 3,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Brown })  }  ]);  getLineNum(styledString: StyledString, width: LengthMetrics) {  let paragraphArr = this.getUIContext().getMeasureUtils().getParagraphs(styledString, { constraintWidth: width });  let res = 0;  for (let i = 0; i < paragraphArr.length; ++i) {  res += paragraphArr[i].getLineCount();  }  return res;  }  getCorrectIndex(styledString: MutableStyledString, maxLines: number, width: LengthMetrics) {  let low = 0;  let high = styledString.length - 1;  while (low <= high) {  let mid = (low + high) >> 1;  console.info('demo: get ' + low + ' ' + high + ' ' + mid);  let moreStyledString = new MutableStyledString(this.fullText, [{  start: 4,  length: 2,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Blue })  }]);  moreStyledString.insertStyledString(0, styledString.subStyledString(0, mid));  let lineNum = this.getLineNum(moreStyledString, LengthMetrics.px(500));  if (lineNum <= maxLines) {  low = mid + 1;  } else {  high = mid - 1;  }  }  return high;  }  mutableStrAllContent = new MutableStyledString(this.str, [  {  start: 0,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontSize: LengthMetrics.px(40) })  },  {  start: 3,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Brown })  }  ]);  customSpan1: MyCustomSpan = new MyCustomSpan('Hello', 120, 10, this.getUIContext());  mutableStrAllContent2 = new MutableStyledString(this.str, [  {  start: 0,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontSize: LengthMetrics.px(100) })  },  {  start: 3,  length: 3,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Brown })  }  ]);  controller: TextController = new TextController();  controller2: TextController = new TextController();  textController: TextController = new TextController();  textController2: TextController = new TextController();  aboutToAppear() {  this.mutableStrAllContent2.insertStyledString(0, new StyledString(this.customSpan1));  this.mutableStr2.insertStyledString(0, new StyledString(this.customSpan1));  }  build() {  Scroll() {  Column() {  Text(this.originalText)  Text(undefined, { controller: this.controller }).width('500px').onAppear(() => {  this.controller.setStyledString(this.mutableStrAllContent);  })  Divider().strokeWidth(8).color('#F1F3F5')  Text(this.afterTypesetting)  Text(undefined, { controller: this.textController }).onAppear(() => {  let now = this.getCorrectIndex(this.mutableStrAllContent, 3, LengthMetrics.px(500));  if (now != this.mutableStrAllContent.length - 1) {  let moreStyledString = new MutableStyledString(this.fullText, [{  start: 4,  length: 2,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Blue })  }]);  moreStyledString.insertStyledString(0, this.mutableStrAllContent.subStyledString(0, now));  this.textController.setStyledString(moreStyledString);  } else {  this.textController.setStyledString(this.mutableStrAllContent);  }  })  .width('500px')  Divider().strokeWidth(8).color('#F1F3F5')  Text(this.originalText)  Text(undefined, { controller: this.controller2 }).width('500px').onAppear(() => {  this.controller2.setStyledString(this.mutableStrAllContent2);  })  Divider().strokeWidth(8).color('#F1F3F5')  Text(this.afterTypesetting)  Text(undefined, { controller: this.textController2 }).onAppear(() => {  let now = this.getCorrectIndex(this.mutableStrAllContent2, 3, LengthMetrics.px(500));  let moreStyledString = new MutableStyledString(this.fullText, [{  start: 4,  length: 2,  styledKey: StyledStringKey.FONT,  styledValue: new TextStyle({ fontColor: Color.Blue })  }]);  moreStyledString.insertStyledString(0, this.mutableStrAllContent2.subStyledString(0, now));  this.textController2.setStyledString(moreStyledString);  })  .width('500px')  }.width('100%')  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/AruuGofAQdC72QJjmDhFPg/zh-cn_image_0000002533065914.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=306EF678E87BC9F92E78E90C34FC3D0F3BB883523D0555BFF3581EF7F1C03F51)

## 使用图片

可通过[ImageAttachment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#imageattachment)来添加图片。

以下示例展示了如何将图片和文本附加到同一个MutableStyledString对象上，并实现图文混排。

> **说明**
> 属性字符串的构造函数[constructor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#constructor)中，当入参value的类型为ImageAttachment或CustomSpan时，styles参数不生效。需要设置styles时，通过[setStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#setstyle)、[insertStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#insertstyledstring)等方法实现。

```typescript
import { image } from '@kit.ImageKit';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringImageAttachment {
  @State abled: boolean = true;
  @State message: string = 'Hello World';
  imagePixelMap: image.PixelMap | undefined = undefined;
  @State imagePixelMap3: image.PixelMap | undefined = undefined;
  mutableStr: MutableStyledString = new MutableStyledString('123');
  controller: TextController = new TextController();
  mutableStr2: MutableStyledString = new MutableStyledString('This is set decoration line style to the mutableStr2', [{
    start: 0,
    length: 15,
    styledKey: StyledStringKey.DECORATION,
    styledValue: new DecorationStyle({
      type: TextDecorationType.Overline,
      color: Color.Orange,
      style: TextDecorationStyle.DOUBLE
    })
  }]);

  async aboutToAppear() {
    console.info('aboutToAppear initial imagePixelMap');

    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.sea'));
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent({
      bundleName: resource.bundleName,
      moduleName: resource.moduleName,
      id: resource.id
    });
    let imageSource = image.createImageSource(unit8Array?.buffer?.slice(0, unit8Array?.buffer?.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  leadingMarginValue: ParagraphStyle = new ParagraphStyle({ leadingMargin: LengthMetrics.vp(5)});

  lineHeightStyle1: LineHeightStyle= new LineHeightStyle(new LengthMetrics(24));

  boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });

  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment_Text_1').id), [
    {
      start: 0,
      length: 28,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 14,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: '#B22222' })
    },
    {
      start: 24,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontWeight: FontWeight.Lighter })
    },
    {
      start: 11,
      length: 4,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: this.lineHeightStyle1
    }
  ]);

  paragraphStyledString2: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringImageAttachment_Text_2').id), [
    {
      start: 0,
      length: 5,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: new LineHeightStyle(new LengthMetrics(60))
    },
    {
      start: 0,
      length: 7,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 1,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
    },
    {
      start: 2,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(36) })
    },
    {
      start: 4,
      length: 3,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20) })
    },
    {
      start: 7,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14)})
    }
  ]);

  build() {
    NavDestination() {
      Column({ space: 12 }) {

          Row() {
            Column({ space: 10 }) {
              Text(undefined, { controller: this.controller })
                .id('text1')
                .copyOption(CopyOptions.InApp)
                .draggable(true)
                .backgroundColor('#FFFFFF')
                .borderRadius(5)

              Button($r('app.string.StyledStringImageAttachment_Button_1'))
                .enabled(this.abled)
                .onClick(() => {
                  if (this.imagePixelMap !== undefined) {
                    this.mutableStr = new MutableStyledString(new ImageAttachment({
                      value: this.imagePixelMap,
                      size: { width: 180, height: 160 },
                      verticalAlign: ImageSpanAlignment.BASELINE,
                      objectFit: ImageFit.Fill
                    }));
                    this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
                    this.mutableStr.appendStyledString(this.paragraphStyledString1);
                    this.controller.setStyledString(this.mutableStr);
                  }
                  this.abled = false;
                })
            }
            .width('100%')
          }
          .height('100%')
          .backgroundColor('#F8F8FF')
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.StyledStringImageAttachment_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/UbjFCuBfQDi9jFyE01ZWzg/zh-cn_image_0000002563865817.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=79B42CF1E3039ADA368CA838B388D200C9F73C9512413022BA9C697F2C7A83C9)

## 设置事件

可通过[GestureStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#gesturestyle)设置onClick、onLongPress事件来使文本响应点击长按事件。

除了初始化属性字符串对象即初始样式对象，亦可通过[setStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#setstyle)接口再叠加新样式或更新已有样式，同时需要在附加的文本组件controller上主动触发更新绑定的属性字符串。

```typescript
import { drawing } from '@kit.ArkGraphics2D';

let gUIContext: UIContext;

class MyCustomSpan extends CustomSpan {
  constructor(word: string, width: number, height: number, fontSize: number) {
    super();
    this.word = word;
    this.width = width;
    this.height = height;
    this.fontSize = fontSize;
  }

  onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics {
    return { width: this.width, height: this.height };
  }

  onDraw(context: DrawContext, options: CustomSpanDrawInfo) {
    let canvas = context.canvas;

    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 0
    });
    const font = new drawing.Font();
    font.setSize(gUIContext.vp2px(this.fontSize));
    const textBlob =
      drawing.TextBlob.makeFromString(this.word.substring(0, 5), font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.attachBrush(brush);

    this.onDrawRectByRadius(context, options.x, options.x + gUIContext.vp2px(this.width), options.lineTop,
      options.lineBottom, 20);
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 255,
      blue: 255
    });
    canvas.attachBrush(brush);
    canvas.drawTextBlob(textBlob, options.x, options.lineBottom - 30);
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 228,
      blue: 196
    });
    canvas.attachBrush(brush);
    const textBlob1 =
      drawing.TextBlob.makeFromString(this.word.substring(5), font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
    canvas.drawTextBlob(textBlob1, options.x + gUIContext.vp2px(100), options.lineBottom - 30);

    canvas.detachBrush();
  }

  onDrawRectByRadius(context: DrawContext, left: number, right: number, top: number, bottom: number, radius: number) {
    let canvas = context.canvas;
    let path = new drawing.Path();

    path.moveTo(left + radius, top);
    path.lineTo(right - radius, top);
    path.arcTo(right - 2 * radius, top, right, top + 2 * radius, 270, 90);
    path.lineTo(right, bottom - radius);
    path.arcTo(right - 2 * radius, bottom - 2 * radius, right, bottom, 0, 90);

    path.lineTo(left + 2 * radius, bottom);
    path.arcTo(left, bottom - 2 * radius, left + 2 * radius, bottom, 90, 90);
    path.lineTo(left, top + 2 * radius);
    path.arcTo(left, top, left + 2 * radius, top + 2 * radius, 180, 90);

    canvas.drawPath(path);
  }

  setWord(word: string) {
    this.word = word;
  }

  public width: number = 160;
  public word: string = 'drawing';
  public height: number = 10;
  public fontSize: number = 16;
}

@Entry
@Component
export struct StyledStringGestureStyle {
  customSpan3: MyCustomSpan = new MyCustomSpan('99VIP88%off', 200, 40, 30);
  customSpanStyledString: MutableStyledString = new MutableStyledString(this.customSpan3);
  textController: TextController = new TextController();
  isPageShow: boolean = true;
  @State backgroundColor1: ResourceColor | undefined = undefined;
  gestureStyleAttr: GestureStyle = new GestureStyle({
    onClick: () => {
      this.backgroundColor1 = Color.Green;
    },
    onLongPress: () => {
      this.backgroundColor1 = Color.Grey;
    }
  });

  aboutToAppear() {
    gUIContext = this.getUIContext();
  }

  async onPageShow() {
    if (!this.isPageShow) {
      return;
    }
    this.isPageShow = false;
    this.customSpanStyledString.setStyle({
      start: 0,
      length: 1,
      styledKey: StyledStringKey.GESTURE,
      styledValue: this.gestureStyleAttr
    })
    this.textController.setStyledString(this.customSpanStyledString);
  }

  build() {
    NavDestination() {
      Column({ space: 12 }) {

          Row() {
            Column() {

              Button($r('app.string.StyledStringGestureStyle_button_content'))
                .backgroundColor(this.backgroundColor1)
                .width('80%')
                .margin(10)
              Text(undefined, { controller: this.textController })
                .id('text1')
                .copyOption(CopyOptions.InApp)
                .fontSize(30)
            }
            .width('100%')
          }
          .height('100%')
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.TStyledStringGestureStyle_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/e6j2JcoUSPGdyQiTjuz5pQ/zh-cn_image_0000002563785863.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=FDEC871C0E037CE16B3A3E58D4F7E36CA036CC7B8E265D7747449D7FC7EB7305)

## 格式转换

可以通过[toHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#tohtml14)、[fromHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#fromhtml)接口实现属性字符串与HTML格式字符串的相关转换，当前支持转换的HTML标签范围：<p>、<span>、<img>、<br>、<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>。

- 以下示例展示了如何将属性字符串转换成HTML格式，并展示了如何从HTML格式转换回属性字符串。

```typescript
import { image } from '@kit.ImageKit';
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringHtml {
  imagePixelMap: image.PixelMap | undefined = undefined;
  @State html: string | undefined = undefined;
  @State styledString: StyledString | undefined = undefined;
  controller1: TextController = new TextController;
  controller2: TextController = new TextController;
  private uiContext: UIContext = this.getUIContext();

  async aboutToAppear() {
    console.info('aboutToAppear initial imagePixelMap');
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.startIcon'));
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.uiContext.getHostContext()?.resourceManager?.getMediaContent({
      bundleName: resource.bundleName,
      moduleName: resource.moduleName,
      id: resource.id
    });
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  build() {
    NavDestination() {
      Column({ space: 12 }) {

          Column() {
            Text(undefined, { controller: this.controller1 }).height(100).id('text1')
            Row() {

              Button($r('app.string.StyledStringHtml_Button_1')).onClick(() => {

                let mutableStyledString1: MutableStyledString =
                  new MutableStyledString(this.getUIContext()
                    .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringHtml_Text_1').id), [{
                  start: 0,
                  length: 6,
                  styledKey: StyledStringKey.FONT,
                  styledValue: new TextStyle({ fontColor: Color.Green, fontSize: LengthMetrics.px(50) })
                }]);
                if (this.imagePixelMap !== undefined) {
                  let mutableStyledString2 = new MutableStyledString(new ImageAttachment({
                    value: this.imagePixelMap,
                    size: { width: 50, height: 50 },
                  }));
                  mutableStyledString1.appendStyledString(mutableStyledString2);
                }
                this.styledString = mutableStyledString1;
                this.controller1.setStyledString(mutableStyledString1);
              }).margin(5)

              Button($r('app.string.StyledStringHtml_Button_2')).onClick(() => {
                this.html = StyledString.toHtml(this.styledString);
              }).margin(5)

              Button($r('app.string.StyledStringHtml_Button_3')).onClick(async () => {
                let styledString = await StyledString.fromHtml(this.html);
                this.controller2.setStyledString(styledString);
              }).margin(5)
            }

            Text(undefined, { controller: this.controller2 }).height(100).id('text2')
            Text(this.html).id('text3')
          }.width('100%')
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.StyledStringHtml_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/zWYkNp_MSXS8lsIAp6dDnw/zh-cn_image_0000002532905968.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=E1CA388E989F7E40B5313D5759D68AC818E33258B6FB1DFF3C5B5E668E40CF32)

- 将HTML中<strong>、<b>、<a>、<i>、<em>、<s>、<u>、<del>、<sup>、<sub>标签及其style属性中的background-color转换为属性字符串并转回HTML。 ```typescript @Entry @Component struct HtmlSpanStringDemo {  @State html: string =  "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style = \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";  @State spanString: StyledString | undefined = undefined;  @State resultText: string = '';  controller: TextController = new TextController;  build() {  Column() {  Text(undefined, { controller: this.controller }).height(100).id('text1')  TextArea({ text: this.html })  .width('100%')  .height(100)  .margin(5)  Button($r('app.string.Converted_HTML_to_SpanString')).onClick(async () => {  this.spanString = await StyledString.fromHtml(this.html);  this.controller.setStyledString(this.spanString);  this.resultText = 'Converted HTML to SpanString successfully.';  }).margin(5)  Button($r('app.string.Converted_SpanString_to_HTML')).onClick(() => {  if (this.spanString) {  const newHtml = StyledString.toHtml(this.spanString);  if (newHtml !== this.html) {  this.html = newHtml;  }  this.resultText = 'Converted SpanString to HTML successfully.';  } else {  this.resultText = 'SpanString is undefined.';  }  }).margin(5)  Button($r('app.string.Converted_HTML_back_to_SpanString')).onClick(async () => {  this.spanString = await StyledString.fromHtml(this.html);  this.controller.setStyledString(this.spanString);  this.resultText = 'Converted HTML back to SpanString successfully.';  }).margin(5)  Button($r('app.string.Reset')).onClick(() => {  this.html =  "<p>This is <b>b</b> <strong>strong</strong> <em>em</em> <i>i</i> <u>u</u> <del>del</del> <s>s</s> <span style = \"foreground-color:blue\"> <a href='https://www.example.com'>www.example</a> </span> <span style=\"background-color: red;\">red span</span> <sup>superscript</sup> and <sub>subscript</sub></p>";  this.spanString = undefined;  this.controller.setStyledString(new StyledString(''));  this.resultText = 'Reset HTML and SpanString successfully.';  }).margin(5)  }.width('100%').padding(20)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/s6JoJrypRWeHNXVlAPp48Q/zh-cn_image_0000002533065916.gif?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=49DEBB54102B50BD0B0F0AC33ED8A807358679029329C459701053F37D72E32B)

## 场景示例

该示例通过ParagraphStyle、LineHeightStyle、TextStyle对象展示了会员过期提示的效果。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct StyledStringSceneExample {
  alignCenterParagraphStyleAttr: ParagraphStyle = new ParagraphStyle({ textAlign: TextAlign.Center });

  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(LengthMetrics.vp(24));

  boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });

  paragraphStyledString1: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_1').id), [
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.alignCenterParagraphStyleAttr
      },
      {
        start: 0,
        length: 4,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: new LineHeightStyle(LengthMetrics.vp(40))
      },
      {
        start: 11,
        length: 14,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontSize: LengthMetrics.vp(14), fontColor: Color.Grey })
      },
      {
        start: 11,
        length: 4,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.alignCenterParagraphStyleAttr
      },
      {
        start: 11,
        length: 4,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    ]);

  paragraphStyledString2: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_2').id), [
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.alignCenterParagraphStyleAttr
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: new LineHeightStyle(LengthMetrics.vp(60))
    },
    {
      start: 0,
      length: 6,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 1,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18) })
    },
    {
      start: 2,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(40) })
    },
    {
      start: 6,
      length: 3,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
    },
    {
      start: 6,
      length: 3,
      styledKey: StyledStringKey.DECORATION,
      styledValue: new DecorationStyle({ type: TextDecorationType.LineThrough, color: Color.Grey })
    }
  ]);

  paragraphStyledString3: MutableStyledString =
    new MutableStyledString(this.getUIContext()
      .getHostContext()!.resourceManager.getStringSync($r('app.string.StyledStringSceneExample_Text_3').id), [
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.alignCenterParagraphStyleAttr
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: new LineHeightStyle(LengthMetrics.vp(30))
    },
    {
      start: 1,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
    },
    {
      start: 4,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: '#FFD700', fontWeight: FontWeight.Bold })
    }
  ]);
  controller: TextController = new TextController();

  build() {
    NavDestination() {
      Column({ space: 12 }) {

          Row() {
            Column({ space: 5 }) {
              Text(undefined, { controller: this.controller })
                .id('text1')
                .width(240)
                .copyOption(CopyOptions.InApp)
                .draggable(true)
                .onAppear(() => {
                  this.paragraphStyledString2.appendStyledString(this.paragraphStyledString3);
                  this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
                  this.controller.setStyledString(this.paragraphStyledString1);
                })

              Button($r('app.string.StyledStringSceneExample_Button_1'))
                .width(200)
                .fontColor(Color.White)
                .fontSize(18)
                .backgroundColor('#3CB371')
                .margin({ bottom: 10 })
            }
            .borderWidth(1).borderColor('#FFDEAD')
            .margin({ left: 10 })
          }
          .height('60%')
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.StyledStringSceneExample_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/2YgR7g1LTH-4FmVgyLWqnA/zh-cn_image_0000002563865819.png?HW-CC-KV=V1&HW-CC-Date=20260329T024454Z&HW-CC-Expire=86400&HW-CC-Sign=22F8EC5CE75045152564BA5EE4662416C3E967B0F6A0DA1E3F0E77398915C258)
