# 富文本编辑（RichEditor）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor

RichEditor是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。具体用法参考[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件的API文档。

对于仅需图文展示而不需要编辑的场景，建议使用[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件。

对于需要大量展示Html格式内容的场景，建议使用[RichText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)组件。

## 组件构成

下图展示了组件元素的构成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Z14jMSgxSF2Cr-ml2XyS4w/zh-cn_image_0000002568252639.jpg?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=D4615F0596C1CA2655E9D1260833CEE0522EA50725A5DFE6BDD728E915E3BDCA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/U6TrcShlRVyuy22YENiwZg/zh-cn_image_0000002537172926.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=68016166CEB716F85F7C6D5D14D397096CD5E00803F922C9F7C18F87B2360CCD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/D4lf-x3_R_usbsXuh84pbQ/zh-cn_image_0000002537332848.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=BAC5237E3C5A1A5222156612F5204E9B5FB270AEADEBE7420865376939F8CF8C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Qynj2KbHQcqW8oxC0w_asw/zh-cn_image_0000002568172645.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=D09247ECA5B1E9BEF925D17EF0AD307BFCB23FBA468EA10D0C20AEF8C5E8229B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/-JbCHjVJT8qD-WoAxrxtYQ/zh-cn_image_0000002568252641.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=5DBB78D4A2E8B1D3F0F51BD91C825B4AB0057420A877CE026CB43B1848CE0E7B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/OX51kTIGT3i2OmK3I7taLQ/zh-cn_image_0000002537172928.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=6C719B50154EBDED89AC67350A4675BE1FE4BD6B04FA5C392093A007D79A4AAE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/HvPmOmyMSMyyUkXdrEqCAw/zh-cn_image_0000002537332850.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=F3695D4EEE1A0EE01498E7DFBBB55DB956DC074482692D178111794CB8195B52)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/7ruLOM-xQ-Sdrg3IyW2Rfg/zh-cn_image_0000002568172647.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=8C38070409794F29249FECF857CD4AEE9B03B43EE6E8B3C233443B2204D63FE8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/a81SG4dWTgms_i_UMdF7Mg/zh-cn_image_0000002568252643.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=AE296ADE4231459E2E84D8B50800630CF37EFBA41030A46CA030E8CEE8253106)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ZWKgjaBuSO-uEvIm1JoKnQ/zh-cn_image_0000002537172930.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=3901D1EAFF612EA506E4BEF14C5B091DCE2A71440CC84A92227362F7A3EA2390)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/u5LuedDCQ7WCrcEyUc64cw/zh-cn_image_0000002537332852.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=6D88DA27BB7683C299FF8CDB0E408C305BB44914420FCECE772BFFD5BB99EB08)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/GQcgzES3QziYiXgcxwMtCA/zh-cn_image_0000002568172649.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=8E53EF134B2F41F706EB938B3CD6C47442B6B120A571B3583391967966E524F1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/0F23GzNWTHCCenM--WHLSA/zh-cn_image_0000002568252645.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=A87714CFC19133C124930B1B4C864E29D0950FF5ED358B54D3CB8630F33965E2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Ysfxx6oPSDSI7naUUQnAgQ/zh-cn_image_0000002537172932.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=408E0E7A4A092780D139634407CEE8F9A7B0F68CC62FB0FB6821F2F6D1C88354)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/_lr8DyBgT4aeHZhhgGjItQ/zh-cn_image_0000002537332854.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=BBE8C2B33CA8EE4AA91905165F8757722A882DF7B721F52E007F747FD8E16DC8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/NucdqQoHR3yVZpcYoFV1ug/zh-cn_image_0000002568172651.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=61B380953FADD8CCC18741A7951A18062FDC8F9B5B260FF425E94363B87A023C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2kvr-DTMSkGGP2C3jMmdrQ/zh-cn_image_0000002568252647.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=36907120B1E5B9B2D824B8192974E576E39F9946BB296F67A31D645C136CE1B7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/JdqQvv9aSTibVYLJbkRgfg/zh-cn_image_0000002537172934.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=03F6CE3E0F5DB4A052191498CB10043814BABED6DAE1E34DB49F6F5222F5B468)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/kSEqSCZ9Rtu5S1O9bkA5AA/zh-cn_image_0000002537332856.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=DB8977B66B1DD38263FC3116C8710DA1F0217F615766006CD5EDB43EF4D4CC80)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/XCQctlRRRkG2GeXGkaICfw/zh-cn_image_0000002568172653.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=55F9F67C2890077581F43D999202BFB261C24C94058DF341EE0DE0CC239C80CC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/x6Ks-xxBQMmRWS3nZwlvMQ/zh-cn_image_0000002568252649.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=339ECB1421A35F6BFBE13CE1F71C621BAE1927DC9F7BD0E625C1C649AA76B598)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/jUTREfpQR5Wt6fB0i6bpPg/zh-cn_image_0000002537172936.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=51A868DAF1E63A35ADC3A0B29427AA1BAB840B890E890CE089594E6307CC4EFA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/LPGqjNp_RUamdiaqLH5t_A/zh-cn_image_0000002537332858.jpg?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=2D2AE0083ABA7B7EDB84E3DE7A742F1678C9648B1CAB97EDDBFD1B666F240CA5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/SkovfGu7QNGsIm8n16WDkg/zh-cn_image_0000002568172655.jpg?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=99B5ACEB49346918B1A2F4D5FC6CE5A09B0758359B4CD25F3955FBDCB784AF8B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/4QWXMPXDTLi4nn5qB_o7-A/zh-cn_image_0000002568252651.jpg?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=1315008D56EDD0B7BFB84E5BCC50ED5B01F4BE42DC1DB1B1B47F4296CD6DDD94)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/bZTLUnlOQL-tw3A9D2airQ/zh-cn_image_0000002537172938.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023727Z&HW-CC-Expire=86400&HW-CC-Sign=4F1AEDE86470F990C9892D0219B390AE967B3ABCA7B605DBDB5CA86F1CC3E6C3)

## 示例代码

- [内容发布器](https://gitcode.com/HarmonyOS_Samples/content-publisher)
