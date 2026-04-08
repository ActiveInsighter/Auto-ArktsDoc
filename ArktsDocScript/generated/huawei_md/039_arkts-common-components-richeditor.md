# 富文本编辑（RichEditor）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法参考[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的API文档。

对于仅需图文展示而不需要编辑的场景，建议使用[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件。

对于需要大量展示Html格式内容的场景，建议使用[RichText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)组件。

## 组件构成

下图展示了组件元素的构成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/-4gqvaloRbuYjQ_Ynth4bg/zh-cn_image_0000002535948318.jpg?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=3A95F738AB4D1C5565F419CEED41ADDFE20A6E41FACE5EE89F163D9E70F1EF95)

组件的元素构成包括：

| 元素 | 说明 |
| --- | --- |
| 内容区 | 内容可显示的区域。 |
| 光标 | 用于指明当前输入位置。 |
| 手柄 | 分为左手柄和右手柄，可分别进行拖动，用于调整文本选择区域范围。 |
| 菜单 | 选中内容后弹出，其中包含复制、粘贴等内容操作按钮。 |

## 创建RichEditor组件

开发者可以[创建基于属性字符串进行内容管理的RichEditor组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#创建基于属性字符串进行内容管理的richeditor组件)或[创建基于Span进行内容管理的RichEditor组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#创建基于span进行内容管理的richeditor组件)。

### 创建基于属性字符串进行内容管理的RichEditor组件

使用RichEditor(options: [RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12))接口可以创建基于属性字符串（[StyledString/MutableStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-styled-string)）进行内容管理的RichEditor组件。这种构建方式开发者可以通过在应用侧持有属性字符串对象来管理数据，通过修改属性字符串对象的内容、样式，再传递给组件，即可实现对富文本组件内容的更新。

相比于使用controller提供的接口进行内容样式更新，使用起来更加灵活便捷。同时属性字符串对象可以设置到各类支持属性字符串的文本组件中，可以快速实现内容的迁移。

```typescript
@Entry
@Component
export struct CreateRichEditor {

  fontStyle: TextStyle = new TextStyle({
    fontColor: Color.Pink
  })

  mutableStyledString: MutableStyledString =

    new MutableStyledString(this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.CreateRichEditor_Text_1').id),
    [{
      start: 0,
      length: 5,
      styledKey: StyledStringKey.FONT,
      styledValue: this.fontStyle
    }])

  controller: RichEditorStyledStringController = new RichEditorStyledStringController();
  options: RichEditorStyledStringOptions = { controller: this.controller };
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        Column({ space: 3 }) {

          RichEditor(this.options)
            .onReady(() => {
              this.controller.setStyledString(this.mutableStyledString);
            })
        }

      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.Create_RichEditor_Component_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/LBxFauTPTkuCfss8RZgeFw/zh-cn_image_0000002566868149.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=CC123AD787E0A43EB06023BC2486A6DF7A9BACC9A8D77B2481B01EF4DAEF1C3D)

### 创建基于Span进行内容管理的RichEditor组件

使用RichEditor(value: [RichEditorOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditoroptions))接口可以创建基于Span进行内容管理的RichEditor组件，通常用于复杂内容场景，开发者通过RichEditorController提供的接口实现内容、样式的管理。

```typescript
@Entry
@Component
export struct CreateRichEditor {
  controllerNoStyledString: RichEditorController = new RichEditorController();
  optionsNoStyledString: RichEditorOptions = { controller: this.controllerNoStyledString };

  build() {
    NavDestination() {
      Column({ space: 12 }) {

        Column({ space: 3 }) {

          RichEditor(this.optionsNoStyledString)
            .onReady(() => {
              this.controllerNoStyledString.addTextSpan(

                $r('app.string.CreateRichEditor_Text_2'), {
                style: {
                  fontColor: Color.Black,
                  fontSize: 15
                }
              })
            })
        }

      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.Create_RichEditor_Component_title'))
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/D284CO_4Sh2Vr3MVgTlTZg/zh-cn_image_0000002566708169.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=FBC787CE5215AA317DF5A7BB06DE4E13E03D357E61216C59DC15DBF8209A76C3)

## 添加内容

富文本组件可以通过不同的接口添加多种形式的内容。

### 添加文本内容

除了直接在组件内输入内容，也可以通过[addTextSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan)添加文本内容。

此接口可以实现文本样式多样化，例如创建混合样式文本。

如果组件是获焦状态并且光标在闪烁，那么通过addTextSpan添加文本内容后，光标位置会更新，在新添加文本内容的右侧闪烁。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {

    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan($r('app.string.AddTextContent_Text_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .border({ width: 1, color: Color.Gray })
        .constraintSize({
          maxHeight: 100
        })
        .width(300)
        .margin(10)
      Row() {

        Button($r('app.string.AddTextContent_Button_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
        .height(30)
        .fontSize(13)
        .onClick(() => {

          this.controller.addTextSpan($r('app.string.AddTextContent_Text_2'))
        })
      }.justifyContent(FlexAlign.Center).width('100%')
    }

}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/S0prhrB7RlmA4SsFDKgsTw/zh-cn_image_0000002535788374.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=4E7530C7BA486100F6F2C1F05C8D1656C3E08E2A6DB631308D05F5E992826CC9)

### 添加图片内容

通过[addImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addimagespan)添加图片内容。

此接口可用于内容丰富与可视化展示，例如在新闻中加入图片，在文档中加入数据可视化图形等。

如果组件是获焦状态并且光标在闪烁，那么通过addImageSpan添加图片内容后，光标位置会更新，在新添加图片内容的右侧闪烁。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
build() {

    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan($r('app.string.AddImageContent_Text_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(100)
      Row() {

        Button($r('app.string.AddImageContent_Button_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {

            this.controller.addImageSpan($r('app.media.startIcon'), {
              imageStyle: {
                size: ['57px', '57px']
              }
            })
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }

}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/a3JIlwRyT7-pcyrDRZfD3Q/zh-cn_image_0000002535948320.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=B0DCD8A31E8B26AEBAA7E216C82C5FCE3B53400648150FBE820A7BEBC290C100)

### 添加@Builder装饰器修饰的内容

通过[addBuilderSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addbuilderspan11)添加@Builder装饰器修饰的内容。

此接口可用于自定义复杂组件的嵌入，例如在组件内加入自定义图表。

该接口内可通过[RichEditorBuilderSpanOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorbuilderspanoptions11)设置在组件中添加builder的位置，省略或者为异常值时，则添加builder到所有内容的最后位置。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
private myBuilder: CustomBuilder = undefined;

@Builder
TextBuilder() {
  Row() {
    Image($r('app.media.startIcon')).width(50).height(50).margin(16)
    Column() {

      Text($r('app.string.AddBuilderDecoratorContent_Text_1')).fontWeight(FontWeight.Bold).fontSize(16)

      Text($r('app.string.AddBuilderDecoratorContent_Text_2')).fontColor('#8a8a8a').fontSize(12)
    }.alignItems(HorizontalAlign.Start)
  }.backgroundColor('#f4f4f4')
  .borderRadius('20')
  .width(220)
}
build() {

    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(

            $r('app.string.AddBuilderDecoratorContent_Text_3'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
      Row() {

        Button($r('app.string.AddBuilderDecoratorContent_Button_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.myBuilder = () => {
              this.TextBuilder()
            }
            this.controller.addBuilderSpan(this.myBuilder)
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }

}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/umyAvghmR7qLKWuz6CmkTA/zh-cn_image_0000002566868153.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=73324EAC558D91796399D52069204E6609A2F9EBC199185FC0CF7DA31801D2A8)

### 添加SymbolSpan内容

可通过[addSymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addsymbolspan11)添加Symbol内容。此接口可用于特殊符号的添加，例如在编辑学术论文时，此接口可用于添加各种数学符号。

添加Symbol内容时，如果组件是获焦状态并且光标在闪烁，那么添加Symbol后，光标将移动到新插入Symbol的右侧。

Symbol内容暂不支持手势、复制、拖拽处理。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {

    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan($r('app.string.AddSymbolSpanContent_Text_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(100)
      Row() {

        Button($r('app.string.AddSymbolSpanContent_Button_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {

            this.controller.addSymbolSpan($r('sys.symbol.basketball_fill'), {
              style: {
                fontSize: 30
              }
            })
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }

}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/m47Rr59TSheMxGC2gUjj7g/zh-cn_image_0000002566708173.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=D3395FFEA4284BAFFD68036E59CBAD1FA7463E97F6831FD0CD0D73E99078112E)

## 管理内容

富文本组件可以通过接口对内容进行管理，例如[获取组件内的图文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#获取组件内图文信息)、[设置无输入时的提示文本](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#设置无输入时的提示文本)或[设置组件内容的最大字符数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#设置最大长度)。

### 获取组件内图文信息

可通过[getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)获取组件内所有图文内容的信息，包括图文的内容、id、样式、位置等信息。获取内容位置信息后，可对指定范围内容进行样式的更新。

此接口适用于已有的内容样式获取与检查，例如在模板应用场景下，可利用此接口获取文本样式。此外，它还适用于内容解析与处理，例如在文本分析应用中，此接口能够获取特定范围内的文本信息。

```typescript
@Entry
@Component
export struct GetGraphicInfoInComponent {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  infoShowController: RichEditorController = new RichEditorController();
  infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

  build() {

      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {
            this.controller.addTextSpan(

              $r('app.string.GetGraphicInfoInComponent_Text_1'), {
              style: {
                fontColor: Color.Black,
                fontSize: 15
              }
            })
          })
          .width(300)
          .height(50)

        Text($r('app.string.GetGraphicInfoInComponent_Text_1')).fontSize(10).fontColor(Color.Gray).width(300);
        RichEditor(this.infoShowOptions)
          .width(300)
          .height(50)
        Row() {

          Button($r('app.string.GetGraphicInfoInComponent_Button_1'), {
            buttonStyle: ButtonStyleMode.NORMAL
          })
            .height(30)
            .fontSize(13)
            .onClick(() => {
              this.infoShowController.addTextSpan(JSON.stringify(this.controller.getSpans()), {
                style: {
                  fontColor: Color.Gray,
                  fontSize: 10
                }
              })
            })
        }.justifyContent(FlexAlign.Center).width('100%')
      }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ltikvsZ4QceGvEox1aFWIg/zh-cn_image_0000002535788376.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=87E4C0973B0137DB3E641FDF8401E606CF32BE951A581431E10BBD6BE636C405)

### 设置无输入时的提示文本

通过[placeholder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#placeholder12)设置无输入时的提示文本。

例如，在用户登录界面采用提示文本，有助于用户区分用户名与密码的输入框。又如，在文本编辑框中，使用提示文本明确输入要求，如“限输入100字以内”，以此指导用户正确操作。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)

      .placeholder(resource.resourceToString($r('app.string.SetAttributes_Text_6')), {
        fontColor: Color.Gray,
        font: {
          size: 15,
          weight: FontWeight.Normal,
          family: 'HarmonyOS Sans',
          style: FontStyle.Normal
        }
      })
      .width(300)
      .height(50)

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/v9n2PV1qRRO7N4Wq1p6IQg/zh-cn_image_0000002535948324.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=A04EC0293C6866DFF69D373A1A1E336C37145D91B66E2D421142F114A3153F13)

### 设置最大长度

通过[maxLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#maxlength18)可以设置富文本的最大可输入字符数。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)

      .placeholder(resource.resourceToString($r('app.string.SetAttributes_Text_8')))
      .maxLength(7)

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Mafl3WeGQ_S9muWN8HeotA/zh-cn_image_0000002566868155.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=6DBAF7EFF22C3285DC6BF788135B013E59941282C3D5C5090D01B6282BE49510)

## 事件回调

开发者可以通过注册事件回调，感知组件事件的触发。

### 添加图文变化前和图文变化后可触发的回调

通过[onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onwillchange12)添加图文变化前可触发的回调。此回调适用于用户实时数据校验与提醒，例如在用户输入文本时，可在回调内实现对输入内容的检测，若检测到敏感词汇，应立即弹出提示框。此外，它还适用于实时字数统计与限制，对于有字数限制的输入场景，可在回调中实时统计用户输入的字数，并在接近字数上限时提供相应的提示。

通过[onDidChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#ondidchange12)添加图文变化后可触发的回调。此回调适用于内容保存与同步，例如在用户完成内容编辑后，可使用该回调自动将最新内容保存至本地或同步至服务器。此外，它还适用于内容状态更新与渲染，例如在待办事项列表应用中，用户编辑富文本格式的待办事项描述后，可使用该回调更新待办事项在列表中的显示样式。

使用[RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12)构建的RichEditor组件不支持上述两种回调。

```typescript
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {

    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_5')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onWillChange((value: RichEditorChangeValue) => {

          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_6')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
          return true;
        })
        .onDidChange((rangeBefore: TextRange, rangeAfter: TextRange) => {

          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_7')) +
          JSON.stringify(rangeBefore) + '\nrangeAfter: ' + JSON.stringify(rangeBefore), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50);

      Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300);
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70);
    }

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/oXVvuRACSme2gog96ZiFwg/zh-cn_image_0000002566708175.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=42E0D480141086083BACE2E0BDA790C002000E623BA94518D49431712F9786FF)

### 添加输入法输入内容前和完成输入后可触发的回调

添加输入法输入内容前和完成输入后可触发的回调。

在添加输入法输入内容前，可以通过[aboutToIMEInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#abouttoimeinput)触发回调。在输入法完成输入后，可以通过[onDidIMEInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#ondidimeinput12)触发回调。

这两种回调机制适用于文本上屏过程的业务逻辑处理。例如：在用户输入的文本上屏前，利用回调提供联想词汇，在用户完成输入后，执行自动化纠错或格式转换。两种回调的时序依次为：aboutToIMEInput、onDidIMEInput。

使用[RichEditorStyledStringOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringoptions12)构建的组件不支持上述两种回调功能。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {

    Column({ space: 3 }) {

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_8')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .aboutToIMEInput((value: RichEditorInsertValue) => {
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_9')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
          return true;
        })
        .onDidIMEInput((value: TextRange) => {
          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_10')) +
          JSON.stringify(value), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)

    }

  }
  .alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Kv3Ad-EgS9OUf3pExmXbZg/zh-cn_image_0000002535788380.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=8D963A295803AD7C7A15909DD9E58E879B24D3876A7E1284411643A8A978BE2C)

### 添加完成粘贴前可触发的回调

通过[onPaste](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onpaste11)回调，来添加粘贴前要处理的流程。

此回调适用于内容格式的处理。例如，当用户复制包含HTML标签的文本时，可在回调中编写代码，将其转换为富文本组件所支持的格式，同时剔除不必要的标签或仅保留纯文本内容。

由于组件默认的粘贴行为仅限于纯文本，无法处理图片粘贴，开发者可利用此方法实现图文并茂的粘贴功能，从而替代组件原有的粘贴行为。

```typescript
import { pasteboard } from '@kit.BasicServicesKit';

@Component
struct on_cut_copy_paste {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  infoShowController: RichEditorController = new RichEditorController();
  infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

  PopDataFromPasteboard() {
    let selection = this.controller.getSelection();
    let start = selection.selection[0];
    let end = selection.selection[1];
    if (start == end) {
      start = this.controller.getCaretOffset();
      end = this.controller.getCaretOffset();
    }
    let moveOffset = 0;
    let sysBoard = pasteboard.getSystemPasteboard();
    sysBoard.getData((err, data) => {
      if (err) {
        return;
      }
      if (start != end) {
        this.controller.deleteSpans({ start: start, end: end });
      }
      let count = data.getRecordCount();
      for (let i = 0; i < count; i++) {
        const element = data.getRecord(i);
        if (element && element.plainText && element.mimeType === pasteboard.MIMETYPE_TEXT_PLAIN) {
          this.controller.addTextSpan(element.plainText,
            {
              style: { fontSize: 26, fontColor: Color.Red },
              offset: start + moveOffset
            }
          )
          moveOffset += element.plainText.length;
        }
      }
      this.controller.setCaretOffset(start + moveOffset);
    });
  }

  build() {
    Column() {

      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {

            this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_11')),
              { style: { fontColor: Color.Black, fontSize: 15 } })
          })
          .onPaste((event) => {

            this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_12')),
              { style: { fontColor: Color.Gray, fontSize: 10 } })
            if (event != undefined && event.preventDefault) {
              event.preventDefault();
            }
            this.PopDataFromPasteboard()
          })
          .width(300)
          .height(50);

        Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300);
        RichEditor(this.infoShowOptions)
          .width(300)
          .height(70);
      }.width('100%').alignItems(HorizontalAlign.Start);

    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}
```

### 添加完成剪切前可触发的回调

通过[onCut](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#oncut12)回调，来添加剪切前要处理的流程。

此回调功能适用于数据处理与存储。例如，当用户从富文本组件中剪切内容时，可在回调中临时存储被剪切的内容，确保后续的粘贴操作能够准确无误地还原内容。

由于组件默认的剪切行为仅限于纯文本，无法处理图片剪切，开发者可利用此方法实现图文并茂的剪切功能，从而替代组件原有的剪切行为。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {

    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_13')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onCut(() => {

          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_14')), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(70)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

### 添加完成复制前可触发的回调

通过[onCopy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#oncopy12)回调，来添加复制前要处理的流程。

此回调适用于内容的备份与共享，例如在用户复制内容时，可在回调中执行以下操作：将复制的内容及其格式信息保存至本地备份文件夹，或自动生成一段包含复制内容及产品购买链接的分享文案，以方便用户进行粘贴和分享。

组件默认的复制行为仅限于纯文本，无法处理图片。开发者可利用此方法实现图文并茂的复制功能，替代组件的默认行为。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {

    Column({ space: 3 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_15')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onCopy(() => {

          this.infoShowController.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_16')), {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/SWmS0Uu-R6CRxCEBQyabfQ/zh-cn_image_0000002535948326.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=5F2F0BD56005781962C85685682F142B3612EEF9E6D4973BF903736D409AC136)

更多事件使用请参考[RichEditor事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#事件)。

## 组件交互

可以通过接口配置交互元素属性，感知交互元素变化。

### 设置输入框光标和手柄的颜色

通过[caretColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#caretcolor12)设置输入框光标和手柄的颜色。

设置不同颜色的光标和手柄可以提高视觉辨识度，特别是在包含多个输入区域的复杂界面中，独特的光标颜色能帮助快速定位当前操作的输入区域。这一特性也可以提升用户体验，使光标颜色与应用页面整体的风格相协调。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)
      .onReady(() => {

        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_5')), {
          style: {
            fontColor: Color.Black,
            fontSize: 15
          }
        })
      })
      .caretColor(Color.Orange)
      .width(300)
      .height(300)

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bFN0fxRnTQaoA_Ynz-fiqg/zh-cn_image_0000002566868157.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=61E3945789E9C6966F3CE351B22D3696A137ABF7FF8D97A141A062631BBAF730)

### 添加组件内容选择区域或编辑状态下光标位置改变时可触发的回调

通过[onSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onselectionchange12)来添加组件内容选择区域或编辑状态下光标位置改变时可触发的回调。

该回调可用于实时监听组件内容选中区域变化，例如实现实时更新工具栏状态（显示字体、段落格式等）、统计选中内容长度或生成选中内容摘要。实时响应选中状态，动态联动交互元素，提升富文本编辑的操作反馈体验和功能的灵活性。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

infoShowController: RichEditorController = new RichEditorController();
infoShowOptions: RichEditorOptions = { controller: this.infoShowController };

build() {
  Column() {

    Column({ space: 3 }) {

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(resource.resourceToString($r('app.string.AddEvent_Text_2')), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .onSelectionChange((value: RichEditorRange) => {
          this.infoShowController.addTextSpan('\n' + resource.resourceToString($r('app.string.AddEvent_Text_3')) +
          value.start + ',' + value.end + ')', {
            style: {
              fontColor: Color.Gray,
              fontSize: 10
            }
          })
        })
        .width(300)
        .height(50)
      Text(resource.resourceToString($r('app.string.AddEvent_Text_4'))).fontSize(10).fontColor(Color.Gray).width(300)
      RichEditor(this.infoShowOptions)
        .width(300)
        .height(70)
    }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/-BkYyAHsRpiSmPChXLpzxw/zh-cn_image_0000002566708177.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=864C3726B0DDA8BC6BB3C2BACC6638A94DC026C68B561EC18670CCAB5AE16F88)

### 设置内容选中区范围

通过[setSelection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#setselection11)设置组件内的内容选中时部分背板高亮。

此接口可用于实现文本聚焦效果，例如当用户点击某个文本段落的标题或摘要时，可通过该接口自动选中并高亮出对应正文内容。

当组件内未获焦出现光标时，调用该接口不产生选中效果。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {

    Column({ space: 12 }) {
      RichEditor(this.options)
        .onReady(() => {

          this.controller.addTextSpan($r('app.string.BackplaneHighlighting_Text_1'), {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
        })
        .width(300)
        .height(60)
      Row() {

        Button($r('app.string.BackplaneHighlighting_Button_1'), {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.controller.setSelection(0, 2)
          })
      }.justifyContent(FlexAlign.Center).width('100%')
    }

}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/5QWH1-eCR_KvBq23EcKYYg/zh-cn_image_0000002535788382.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=0BC4783001059B6E3ADA4DDEFC7F108515DFF4940496FBE3B5D9CEEE897E1828)

## 菜单配置

通过接口可以对文本选择菜单进行配置。

### 管理选中菜单项

当富文本选择区域变化后显示菜单之前触发[onPrepareMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#属性-1)回调，可在该回调中进行菜单数据设置。

```typescript
@Component
struct PrepareMenu {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State endIndex: number | undefined = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    const idsToFilter = [
      TextMenuItemId.TRANSLATE,
      TextMenuItemId.SHARE,
      TextMenuItemId.SEARCH,
      TextMenuItemId.AI_WRITER
    ]
    const items = menuItems.filter(item => !idsToFilter.some(id => id.equals(item.id)));

    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    }
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    }
    items.push(item1);
    items.unshift(item2);
    return items;
  }

  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of('create2'))) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of('prepare1'))) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
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
    Column() {

      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('RichEditor editMenuOptions');
        })
        .editMenuOptions(this.editMenuOptions)
        .onSelectionChange((range: RichEditorRange) => {
          this.endIndex = range.end;
        })
        .height(50)
        .margin({ top: 100 })
        .borderWidth(1)
        .borderColor(Color.Red)

    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/SEPWSvvgTvKGeMWWfvkwTA/zh-cn_image_0000002535948328.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=3ADAE656B3CFAE8CAB82E6960CA28F444F083710662C600E83B86001522B6A96)

### 屏蔽系统服务类菜单项

通过[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)屏蔽富文本选择菜单内所有系统服务菜单项。

此接口保护内容安全，适用于限制文本操作的场景，例如展示保密内容或禁止复制的版权文本。屏蔽系统服务菜单项，防止用户通过系统服务菜单复制、分享文本，降低内容泄露风险。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
export struct DisableSystemServiceMenu {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  aboutToAppear(): void {

    TextMenuController.disableSystemServiceMenuItems(true);
  }

  aboutToDisappear(): void {

    TextMenuController.disableSystemServiceMenuItems(false);
  }

  build() {

      Column({ space: 12 }) {
        RichEditor(this.options).onReady(() => {

          this.controller.addTextSpan($r('app.string.Demo_richEditor'),
            {
              style:
              {
                fontSize: 30
              }
            })
        })
          .height(60)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
      }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/rgIwOmhbRkGuIe8vRQ56qg/zh-cn_image_0000002566868161.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=5E24A4C59F2E7FA14BF15A17EFA394AA11D52B3623FA2A4A14BED621B3EA2DB4)

通过[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)可以屏蔽富文本选择菜单内指定的系统服务菜单项。

此接口可精确屏蔽指定的系统服务菜单项，保留应用所需的系统菜单功能，使菜单更贴合实际交互设计。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
export struct DisableMenuItem {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  aboutToAppear(): void {

    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE]);
  }

  aboutToDisappear(): void {

    TextMenuController.disableMenuItems([]);
  }

  build() {

      Column({ space: 12 }) {
        RichEditor(this.options)
          .onReady(() => {

            this.controller.addTextSpan($r('app.string.Demo_richEditor'), {
              style: {
                fontSize: 30
              }
            })
          })
          .height(60)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
      }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/CV2slYv1S4KXTFG8_1FUyA/zh-cn_image_0000002566708181.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=37BF7E1DC570B0567B19BFBAB7AB4B4DA7B48C5428DA9481E55C9E388511D585)

### 设置自定义选择菜单

通过[bindSelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#bindselectionmenu)设置自定义选择菜单。

组件原本具有默认的文本选择菜单，包含复制、剪切和全选的功能。用户可使用该属性设定自定义菜单，例如翻译英文、加粗字体等丰富的菜单功能。

当自定义菜单超长时，建议内部嵌套Scroll组件使用，避免键盘被遮挡。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };
sliderShow: boolean = false;
private theme: SelectionMenuTheme = defaultTheme;

build() {
  Column() {

    RichEditor(this.options)
      .onReady(() => {

        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_4')), {
          style: {
            fontColor: Color.Black,
            fontSize: 18
          }
        })
      })
      .bindSelectionMenu(RichEditorSpanType.TEXT, this.SystemMenu, ResponseType.LongPress, {
        onDisappear: () => {
          this.sliderShow = false
        }
      })

      .width(300)
      .height(300)

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}

@Builder
SystemMenu() {
  Column() {
    Menu() {
      if (this.controller) {
        MenuItemGroup() {
          MenuItem({
            startIcon: this.theme.cutIcon,

            content: resource.resourceToString($r('app.string.SetAttributes_Text_1')),
            labelInfo: 'Ctrl+X'
          })
          MenuItem({
            startIcon: this.theme.copyIcon,

            content: resource.resourceToString($r('app.string.SetAttributes_Text_2')),
            labelInfo: 'Ctrl+C'
          })
          MenuItem({
            startIcon: this.theme.pasteIcon,

            content: resource.resourceToString($r('app.string.SetAttributes_Text_3')),
            labelInfo: 'Ctrl+V'
          })
        }
      }
    }
    .radius(this.theme.containerBorderRadius)
    .clip(true)
    .backgroundColor(Color.White)
    .width(this.theme.defaultMenuWidth)
  }
  .width(this.theme.defaultMenuWidth)
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/7E6prlbNTUWN6CCui5qywg/zh-cn_image_0000002535788384.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=472C55B777978F692DD873B66A2415D0853E37D296C6D668DBAF85EE4B8D0AE8)

## 布局配置

组件支持通过接口配置布局规则，开发者可以根据业务场景定制合适的布局规则。

### 设置最大行数

通过[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#maxlines18)可以设置富文本组件内可显示文本的最大行数。

此接口控制组件内文本的显示范围，防止文本过长影响页面布局，确保不同设备和场景下的文本显示效果一致，提升界面兼容性和美观度。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)
      .onReady(() => {
        this.controller.addTextSpan(resource.resourceToString($r('app.string.SetAttributes_Text_7')),
          {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          })
      })
      .maxLines(2)

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/pYDzA82XTTahLvU5XAA9tg/zh-cn_image_0000002535948332.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=2280214FE634AAC1B220025259CF2DD304F455A13A9EC3FBD8A9D522E36D1645)

## 样式设置

组件支持对内容设置复杂的样式。

### 设置用户预设的文本样式

通过[setTypingStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#settypingstyle11)可以设置用户预设的文本样式。

此接口可用于个性化的写作体验，例如可以使用此接口让输入的不同层级标题自动应用相应格式（如一级、二级标题）。

```typescript
@Entry
@Component
export struct SetUserPresetTextStyles {

  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {

      Column({ space: 12 }) {
        RichEditor(this.options)
          .onReady(() => {

            this.controller.addTextSpan($r('app.string.SetUserPresetTextStyles_Text_1'),
              {
                style: {
                  fontColor: Color.Black,
                  fontSize: 15
                }
              })
          })
          .width(300)
          .height(60)
        Row() {

          Button($r('app.string.SetUserPresetTextStyles_Button_1'), {
            buttonStyle: ButtonStyleMode.NORMAL
          })
            .height(30)
            .fontSize(13)
            .onClick(() => {
              this.controller.setTypingStyle({
                fontWeight: 'medium',
                fontColor: Color.Pink,
                fontSize: 15,
                fontStyle: FontStyle.Italic,
                decoration: {
                  type: TextDecorationType.Underline,
                  color: Color.Gray
                }
              })
            })
        }.justifyContent(FlexAlign.Center).width('100%')
      }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/s12e-7moTMi8-3p-TQYRkg/zh-cn_image_0000002566868163.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=C866FBE18EFFD03A57AE3C42A8B3E9C84E6EBF436A300E125F9ADF2C22E0018F)

### 设置装饰线

通过[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#decoration)设置富文本组件中文本装饰线的样式、颜色和粗细。

设置文本装饰线可突出关键信息、区分文本状态、增强视觉层次。例如，为重要标题或关键词添加装饰线，帮助用户快速获取信息。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)
      .onReady(() => {

        this.controller.addTextSpan($r('app.string.Demo_oneText'), {
          style: {
            fontSize: 25,
            decoration: {
              type: TextDecorationType.LineThrough,
              color: Color.Blue,

              thicknessScale: 6
            }
          }
        })
      })

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/bACq0PtaRhGjAE9gIxHsrA/zh-cn_image_0000002566708183.jpg?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=7E1E13ECD8D7C3D3C977D579DFE6289677A6599C93DD131D3CD0E6D2B6333511)

通过[DecorationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#decorationoptions20)中的enableMultiType设置多装饰线，比如同时设置下划线和中划线。

此接口适用于复杂业务场景，满足文本装饰的多样化需求。在文档协作过程中，多人编辑时，可以通过使用不同的装饰线组合来区分文本状态，从而提高协作效率。

```typescript
RichEditor({ controller: this.styledStringController });

Button($r('app.string.Demo_SetStyledStringButton'))
  .fontSize(20)
  .onClick(() => {
    let mutString: MutableStyledString = new MutableStyledString(

      resource.resourceToString($r('app.string.Demo_styledString')), [
      {
        start: 0,
        length: 9,
        styledKey: StyledStringKey.FONT,
        styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
      },
      {
        start: 0,
        length: 5,
        styledKey: StyledStringKey.DECORATION,
        styledValue: new DecorationStyle(
          {
            type: TextDecorationType.Underline,
          },
          {

            enableMultiType: true
          })
      },
      {
        start: 2,
        length: 4,
        styledKey: StyledStringKey.DECORATION,
        styledValue: new DecorationStyle(
          {
            type: TextDecorationType.LineThrough,
          },
          {

            enableMultiType: true
          })
      }
    ])
    this.styledStringController.setStyledString(mutString);
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/x_J_CTnhRX2tcbn8Khkifg/zh-cn_image_0000002535788388.jpg?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=4789F688778D3FC34AD63154A5694016A6831475E9DA9997305FD8BE2C4D41F0)

### 设置垂直居中

通过[textVerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textverticalalign20)设置文本段落在垂直方向的对齐方式。

此接口优化多元素排版，使组件内容与图片、图标等在垂直方向对齐时，整体布局更协调。

```typescript
controller: RichEditorController = new RichEditorController();
options: RichEditorOptions = { controller: this.controller };

build() {
  Column() {

    RichEditor(this.options)
      .onReady(() => {

        this.controller.addImageSpan($r('app.media.startIcon'), {
          imageStyle: {
            size: [100, 100]
          }
        })

        this.controller.addTextSpan($r('app.string.Demo_verticalAlignString'), {
          style: {
            fontColor: Color.Pink,
            fontSize: '32'
          },
          paragraphStyle: {
            textAlign: TextAlign.Start,
            textVerticalAlign: TextVerticalAlign.CENTER,
            leadingMargin: 16
          }
        })
      })

  }.alignItems(HorizontalAlign.Start)
  .backgroundColor('#fff')
  .borderRadius(12)
  .padding(12)
  .width('100%')
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/LXRTovuESliUH-FMw-1GGA/zh-cn_image_0000002535948334.jpg?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=82BA8939FCC3EBED1D6224C17611412090ED8A10A2DD8DB34A67CE1BBE1728B1)

### 设置中西文自动间距

通过[enableAutoSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#enableautospacing20)设置是否开启中文与西文的自动间距。

此接口优化文本排版，提升组件内文本的可读性。设置自动间距后，中文与西文间产生适当空隙，便于区分不同语种，减少视觉干扰。

```typescript
@Component
struct EnableAutoSpacing {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State
  enableAutoSpace:boolean = false;

  build() {
    Column() {

      Column({ space: 3 }) {
        RichEditor(this.options)
          .onReady(() => {

            this.controller.addTextSpan($r('app.string.Demo_autoSpacingString'),
              {
                style:
                {
                  fontColor: Color.Orange,
                  fontSize: 20
                }
              })
          })
          .enableAutoSpacing(this.enableAutoSpace)

        Button($r('app.string.Demo_autoSpacingButton'))
          .fontSize(20)
          .onClick(() => {
            this.enableAutoSpace = true;
          })
      }

    }.alignItems(HorizontalAlign.Start)
    .backgroundColor('#fff')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/lwosLbMoQDyK-O0wpOx31g/zh-cn_image_0000002566868167.gif?HW-CC-KV=V1&HW-CC-Date=20260408T024038Z&HW-CC-Expire=86400&HW-CC-Sign=CE0DF59035404666DBDFD83FDC8DD006FD12DB84211C03D9BEE8E140EC8D3E9F)

## 示例代码

- [内容发布器](https://gitcode.com/HarmonyOS_Samples/content-publisher)
