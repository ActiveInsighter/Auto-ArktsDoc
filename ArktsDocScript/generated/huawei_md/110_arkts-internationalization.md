# UI国际化
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization

本文介绍如何实现应用程序UI界面的国际化，包含资源配置和镜像布局，关于应用适配国际化的详细参考，请参考[Localization Kit（本地化开发服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-l10n)。

## 利用资源限定词配置国际化资源

在开发阶段，通过DevEco Studio，可以为应用在对应语言和地区的资源限定词目录下配置不同的资源，来实现UI国际化。详细介绍请参考[资源分类与访问](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access)。

## 使用镜像能力

不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语和希腊语则采用从右到左（RTL）的顺序。为满足不同用户的阅读习惯，ArkUI提供了镜像能力。在特定情况下将显示内容在X轴上进行镜像反转，由从左到右显示变成从右到左显示。

| 镜像前 | 镜像后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Dy8R2_ZHRda4uy1cMV-nbg/zh-cn_image_0000002565210423.png?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=C3315F73840F68ABAC10BBE4282F9BD72E26F5E9CB2E71C0AB6314B9B4615ABC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/hGxlxVfIRBme7p3j7q9qQg/zh-cn_image_0000002534250600.png?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=553D5DB266666E602B3D421C211B1318343D17F76A1D77ABD111E24BB8E257C8) |

当组件满足以下任意条件时，镜像能力生效：

1. 组件的direction属性设置为Direction.Rtl。
2. 组件的direction属性设置为Direction.Auto，且当前的系统语言（如维吾尔语）的阅读习惯是从右到左。

### 基本概念

- LTR：顺序为从左到右。
- RTL：顺序为从右到左。

### 使用约束

ArkUI 如下能力已默认适配镜像：

| 类别 | 名称 |
| --- | --- |
| 基础组件 | [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)、[Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)、[TabContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)、[CalendarPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker)、[CalendarPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog)、[TextPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)、[TextPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-textpicker-dialog)、[DatePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker)、[DatePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)、[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar)、[AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer)、[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)、[SideBarContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer)、[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)、[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)、[Rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating)、[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)、[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)、[Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)、[Counter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter)、[Chip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip)、[SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)、[bindMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu)、[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu8)、[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)、[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)、[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)、[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)、[GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)、[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)、[Select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)、[Marquee](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-marquee)、[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)、[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)、[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)、[RelativeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer)、[ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup) |
| 高级组件 | [SelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu) 、[TreeView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeview) 、[Filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-filter)、[SplitLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout)、[ToolBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbar)、[ComposeListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composelistitem)、[EditableTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar)、[ProgressButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbutton)、[SubHeader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader) 、[Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup)、[Dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog)、[SwipeRefresher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-swiperefresher) |
| 通用属性 | [position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)、[markAnchor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#markanchor)、[offset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#offset)、[alignRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#alignrules12)、[borderWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderwidth)、[borderColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#bordercolor)、[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)、[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)、[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin) |
| 接口 | [AlertDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box)、[ActionSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-action-sheet)、[promptAction.showDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#promptactionshowdialogdeprecated)、[promptAction.showToast](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#promptactionshowtoastdeprecated) |

但如下三种场景还需要进行适配：

1. 界面布局、边框设置：关于方向类的通用属性，如果需要支持镜像能力，使用泛化的方向指示词 start/end入参类型替换 left/right、x/y等绝对方向指示词的入参类型，来表示自适应镜像能力。
2. Canvas组件只有限支持文本绘制的镜像能力。
3. XComponent组件不支持组件镜像能力。

### 界面布局和边框设置

目前，以下三类通用属性需要使用新入参类型适配：

位置设置：[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)、[markAnchor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#markanchor)、[offset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#offset)、[alignRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#alignrules12)

边框设置：[borderWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderwidth)、[borderColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#bordercolor)、[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)

尺寸设置：[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)、[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)

以position为例，需要把绝对方向x、y描述改为新入参类型start、end的描述，其他属性类似。

```typescript
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct InterfaceLayoutBorderSettings {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Stack({ alignContent: Alignment.TopStart }) {
        Column()
          .width(100)
          .height(100)
          .backgroundColor(Color.Red)
          .position({
            start: LengthMetrics.px(200),
            top: LengthMetrics.px(200)
          })

      }.backgroundColor(Color.Blue)
    }.width('100%').height('100%').border({ color: '#880606' })
  }
}
```

### 自定义绘制Canvas组件

Canvas组件的绘制内容和坐标均不支持镜像能力。已绘制到Canvas组件上的内容并不会跟随系统语言的切换自动做镜像效果。

[CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)的文本绘制支持镜像能力，在使用时需要与Canvas组件的通用属性direction（组件显示方向）和CanvasRenderingContext2D的属性direction（文本绘制方向）协同使用。具体规格如下：

1. 优先级：CanvasRenderingContext2D的direction属性 > Canvas组件通用属性direction > 系统语言决定的水平显示方向。
2. Canvas组件本身不会自动跟随系统语言切换镜像效果，需要应用监听到系统语言切换后自行重新绘制。
3. CanvasRenderingContext2D绘制文本时，只有符号等文本会对绘制方向生效，英文字母和数字不响应绘制方向的变化。

```typescript
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Entry
@Component
struct CustomizeCanvasComponentDrawing {
  @State message: string = 'Hello world';
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  aboutToAppear(): void {

    let subscriber: commonEventManager.CommonEventSubscriber | null = null;
    let subscribeInfo2: commonEventManager.CommonEventSubscribeInfo = {
      events: ['usual.event.LOCALE_CHANGED'],
    }
    commonEventManager.createSubscriber(subscribeInfo2,
      (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => {
        if (err) {
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
          return;
        }

        subscriber = data;
        if (subscriber !== null) {
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              return;
            }

            this.drawText();
          })
        } else {
          console.error(`MayTest Need create subscriber`);
        }
      })
  }

  drawText(): void {
    console.error('MayTest drawText')
    this.context.reset()
    this.context.direction = 'inherit'
    this.context.font = '30px sans-serif'
    this.context.fillText('ab%123&*@', 50, 50)
  }

  build() {
    Row() {
      Canvas(this.context)
        .direction(Direction.Auto)
        .width('100%')
        .height('100%')
        .onReady(() =>{
          this.drawText()
        })
        .backgroundColor(Color.Pink)
    }
    .height('100%')
  }

}
```

| 镜像前 | 镜像后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/HFWqJ2lpSg6olOGgqJzjpA/zh-cn_image_0000002534410546.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=8115EE84A6F7DED706A353D06C7772CA7B9B4718F0FFCEA3B185A4A79647BA07) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/LhPhIO9vR6K1Htl7hJ2Z6w/zh-cn_image_0000002565290445.jpg?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=2EB3D3AAF63D9E34EAD28F3987A4CE2FB3C2668B41303CFD9C2F10E15B073DD0) |

### 镜像状态字符对齐

[Direction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#direction)是指文字的方向，即文本在屏幕上呈现时字符的顺序。在从左到右（LTR）文本中，显示顺序是从左向右；在从右到左（RTL）文本中，显示顺序是从右到左。

[TextAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#textalign)是将文本作为一个整体，在布局上的影响，具体位置会受Direction影响，以TextAlign为start为例，当Direction为LTR时，布局位置靠左；当Direction为RTL时，布局位置靠右。

在LTR与RTL文本混排时，如一个英文句子中包含阿拉伯语的单词或短语，显示顺序将变得复杂。下图为数字和维吾尔语混合时对应的字符逻辑顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/1KGP1qrgSG6IQezQdNWGnQ/zh-cn_image_0000002565210425.png?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=EB14CE66BD7233B167C9A8AFFBC46A29AF847BF0FB8B1EDA62E00E911B3CC84E)

此时，文本渲染引擎会采用名为“双向算法”或“Unicode双向算法”（Unicode Bidirectional Algorithm）的方法来确定字符的显示顺序。下图展示了LTR与RTL文本混合时对应的字符显示顺序，确定字符方向的基本原则如下：

1. 强字符的方向性：强字符具有明确的方向性，例如，中文为LTR，阿拉伯语为RTL，这类字符的方向性会影响其周围的中性字符。
2. 弱字符的方向性：弱字符不具备明确的方向性，这些字符不会影响其周围中性字符的方向。
3. 中性字符的方向性：中性字符无固定方向性，它们会继承其最近的强字符的方向；若附近无强字符，则采用全局方向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/FDO2P-rdQEWfOIx2ej_L6Q/zh-cn_image_0000002534250602.png?HW-CC-KV=V1&HW-CC-Date=20260330T121640Z&HW-CC-Expire=86400&HW-CC-Sign=851B82A6FEE647086E47ED8E2B72D44152AD3643EB94C8E64CE6BD2F46F59E28)
