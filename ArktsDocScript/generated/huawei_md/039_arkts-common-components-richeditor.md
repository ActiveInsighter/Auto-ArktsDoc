# 富文本编辑（RichEditor）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法参考[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)。

对于仅需图文展示而不需要编辑的场景，建议使用[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件。

对于需要大量展示Html格式内容的场景，建议使用[RichText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)组件。

## 组件构成

下图展示了组件元素的构成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/hnlJu65RQeeUg3CmOGdoXw/zh-cn_image_0000002563865791.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=81A1FF8806D2E6773D3DA43CBCD346FB25957B266BD8C805FB080934AFFEF630)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/10FVer5ySdSllLct7DwlYw/zh-cn_image_0000002563785837.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=84C1F594F266CBD51156CAABDE1120A70692F3018DB9C48578B9E28D7D3BD205)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/rnrJxpyPRW-8btzaqd_PLQ/zh-cn_image_0000002532905942.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=DC12B60B48ECB6D7C376923664554FE75CA69ACDDD31631FABC1465F58F3D37F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/D5bRI1XqTLS_az-MGeVdig/zh-cn_image_0000002533065890.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=A56140486580C27BD3AC268E38D1B8EBE07E02A03CF376C7CC86F3309659BCD0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/yfZXEP3NTb2uDEisE8dhmw/zh-cn_image_0000002563865793.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=DE200DBC02F3E258AA51DABBAEDDD149C730234ED2BDC834AB4EF484D447AF2F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/sQ4NnET5QZCWuC5xd7tFwA/zh-cn_image_0000002563785839.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=0A172FE7C0AC4DAB154C6935337704D5E6386E3FAB958CDEA1C7A3B6CECF395A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/CUnuzJ8iSWyVsPo77OTLUg/zh-cn_image_0000002532905944.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=BFECC49AD56DD9928DE2E0DF90D2760E17D1BD3F662FB43D685224D8CE35555A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/IXkFBm7qTUC6pbrVUKncCg/zh-cn_image_0000002533065892.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=B9574AD09CBC2D2956E902984F60ECDF89A2C921966021758052DE0997757680)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/5npXK9O-Q26Z083y4HsBCw/zh-cn_image_0000002563865795.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=B8CA6CAB365FFC5F5047B1DB6D7585CF2F8695F95C1093670BF32143F8A33955)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/6xfPw7vFRM2FpKpHLkwtlQ/zh-cn_image_0000002563785841.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=C35059D1B01EC7AA2E88F4C290B50A9B5DC63D9D061CDE6FF25762806218ABF6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/OyhiyYy8R8mTmjCirdBptw/zh-cn_image_0000002532905946.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=302D66932C00526AB399F8EAC783CFEE5D4AEED20D709955677CF42852E3B514)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/yF_hV0lGRB2IgQMx94mqew/zh-cn_image_0000002533065894.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=DBDCF58BB65AC9D98977F9C809A995E465B8106063ECBDF77C2DB03A9CC5A80F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/DRGWx6KMRR2-9gsQICmiDA/zh-cn_image_0000002563865797.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=0B7FF48AD1DB2A4727E3674228913C4BB30923573E89A02BA561268B339B9F8C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ikJHTuhcQ9imb3Z1seAaNw/zh-cn_image_0000002563785843.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=08214B4C06EDD26A8B9548F92695E0C7A76631CA8535837E886ADEAAB73184A1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/vkr6LMwkReyzY_KX-bLLWg/zh-cn_image_0000002532905948.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=46A923097EF05E38D8AE220B27BB007D7FEA9B28C0D018F7A939FA45A0CC7514)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/LE1g3JZfRIKls34XrS9I1g/zh-cn_image_0000002533065896.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=7110A703FDB663F9E2F5E91032F3F4C7126C886492779A7A6B80150FF9255F62)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/HBSJlwCxR4agPRG9UTmKqQ/zh-cn_image_0000002563865799.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=9956773A9AD2383663F6501C3FEE3BF2289FEC56D90334D80D2774EB589DACC6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Wx_XI768T7Kx-y6HL7E0EQ/zh-cn_image_0000002563785845.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=3E1049E66245D66DE82CC5EB654531933D5513C05CA10CEEC600B716DB181E31)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/uvsxphz4SBK42uk-NS1S_g/zh-cn_image_0000002532905950.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=F699153A194F500376EB2B0BD9F0E35E9278C50C8B757CE10B3021B66A2FA772)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/lVUcON13SiujneCp-h9z5Q/zh-cn_image_0000002533065898.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=A5A678F640DA396DF84F35A39D04A7D37BD3A5DAE1E61779728B07AC55B8F54D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hGSgbo1rSqi95ZOKteveIw/zh-cn_image_0000002563865801.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=4FFCC6E5086AC16C6B36CA25D5A99F9957B4CADF02395B0926AE924001818727)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/35yqhAClQiS6ZN85gKYlpw/zh-cn_image_0000002563785847.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=31568A16818320B0DCD33C3A5324F2E25A367238F14E4C3D44A3E26A79F8DB19)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/6mRQPRYlQCay0T_mYEjNYA/zh-cn_image_0000002532905952.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=0D9EF7ACB7E18DBFA9EB60D9E451EFEC21BEDB0BD7297D6CDC960582C51B672C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/T285ttb1RH2ajfpnoN1XTQ/zh-cn_image_0000002533065900.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=35B0FFD0A15DF34AF8E063B6AC09639C5D644D4E8C847D8161E55249A148BCEE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/nHmk_8tlS-Oo2ZCTt3Em0w/zh-cn_image_0000002563865803.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=E8DB361306F8650BB834BCF54E8EE1D240E2558B702E018C074310E4DD7A9D4D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/V1F-7F7-RLOOUmINkdwMwA/zh-cn_image_0000002563785849.gif?HW-CC-KV=V1&HW-CC-Date=20260330T095140Z&HW-CC-Expire=86400&HW-CC-Sign=B51865338D1D37FEDBFA18AFBFA48E4E444A3E72674D74950A49188D2C42C563)

## 示例代码

- [内容发布器](https://gitcode.com/HarmonyOS_Samples/content-publisher)
