# 弧形列表 (ArcList)（圆形屏幕推荐使用）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist

从API version 18开始支持弧形列表。弧形列表是一种专为圆形屏幕设备设计的特殊列表，它能够以结构化、可滚动的形式高效展示信息。具体用法可参考[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)。

使用弧形列表可以通过在[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件中按垂直方向线性排列子组件[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)，可以为弧形列表中的每一项提供独立视图。此外，可以使用[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)来迭代一组列表项，或结合任意数量的单个视图与[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)结构，构建复杂的弧形列表。[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件支持多种[渲染控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-overview)方式，包括条件渲染、循环渲染和懒加载，以生成子组件。

## 创建弧形列表

[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)可通过调用以下接口来创建。

```typescript
ArcList({
  initialIndex: 2
}) {
  ArcListItem() {

  }
  ArcListItem() {

  }

}
```

> **说明**
> [ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)的子组件必须是[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)，[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)必须配合[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)来使用。

## 在弧形列表中显示数据

弧形列表视图垂直展示项目集合，当列表项超出屏幕范围时，提供滚动功能，这使得它非常适合展示大型数据集合。在最简单的弧形列表形式中，[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)静态创建其列表项[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)的内容。

```typescript
import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
export struct ArcListShow {
  build() {
    NavDestination() {
      Column({ space: 12 }) {

          ArcList({ initialIndex: 2 }) {
            ArcListItem() {
              Row() {
                Image($r('app.media.wlan')).width('99px').height('99px')
                  .borderRadius('50px').margin({ left: 7 })
                Column() {
                  Text($r('app.string.ArcListStyles_waln')).fontSize('38px').fontColor('#FFFFFFFF')
                  Text($r('app.string.ArcListStyles_open')).fontSize('20px').fontColor('#FFFFFFFF')
                }.width('190px')

                Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
                  .borderRadius('50px')
              }
            }
            .borderRadius('65px')
            .width('414px')
            .height('129px')
            .backgroundColor('#26FFFFFF')

            ArcListItem() {
              Row() {
                Image($r('app.media.blueTooth')).width('99px').height('99px')
                  .borderRadius('50px').margin({ left: 7 })
                Column() {
                  Text($r('app.string.ArcListStyles_blue')).fontSize('38px').fontColor('#FFFFFFFF')
                  Text($r('app.string.ArcListStyles_open')).fontSize('20px').fontColor('#FFFFFFFF')
                }.width('190px')

                Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
                  .borderRadius('50px')
              }
            }
            .borderRadius('65px')
            .width('414px')
            .height('129px')
            .backgroundColor('#26FFFFFF')

            ArcListItem() {
              Row() {
                Image($r('app.media.mobileData')).width('99px').height('99px')
                  .borderRadius('50px').margin({ left: 7 })
                Column() {
                  Text($r('app.string.ArcListStyles_net')).fontSize('38px').fontColor('#FFFFFFFF')
                }.width('190px')

                Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
                  .borderRadius('50px')
              }
            }
            .borderRadius('65px')
            .width('414px')
            .height('129px')
            .backgroundColor('#26FFFFFF')

            ArcListItem() {
              Row() {
                Image($r('app.media.ic_settings_more_connections')).width('99px').height('99px')
                  .borderRadius('50px').margin({ left: 7 })
                Column() {
                  Text($r('app.string.ArcListStyles_connect')).fontSize('38px').fontColor('#FFFFFFFF')
                }.width('190px')

                Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
                  .borderRadius('50px')
              }
            }
            .borderRadius('65px')
            .width('414px')
            .height('129px')
            .backgroundColor('#26FFFFFF')

            ArcListItem() {
              Row() {
                Image($r('app.media.displayAndBrightness')).width('99px').height('99px')
                  .borderRadius('50px').margin({ left: 7 })
                Column() {
                  Text($r('app.string.ArcListStyles_light')).fontSize('38px').fontColor('#FFFFFFFF')
                }.width('190px')

                Image($r('app.media.ic_settings_arrow')).width('92px').height('92px')
                  .borderRadius('50px')
              }
            }
            .borderRadius('65px')
            .width('414px')
            .height('129px')
            .backgroundColor('#26FFFFFF')
          }
          .width('466px')
          .height('466px')
          .space(LengthMetrics.px(10))
          .borderRadius('233px')
          .backgroundColor(Color.Black)
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.ArcListShow_title'))
  }
}
```

**图1** 显示弧形列表数据

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/c_LVl5_hRoajdNnE2RZIiw/zh-cn_image_0000002565290177.png?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=88CA7E4FC423C26C870D9A4393C9C4F10D009A54565760588D69E15F5CD465F2)

## 迭代弧形列表内容

通常，应用会通过数据集合动态创建列表。采用[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)的方式，可以从数据源中迭代获取数据，在每次迭代过程中创建相应的组件，从而降低代码的复杂度。

ArkTS通过[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)提供了组件的循环渲染能力。以简单的联系人列表为例，将联系人名称和头像数据以Contact类结构存储到contacts数组中，使用[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)中嵌套的[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)来代替多个平铺的、内容相似的[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)，从而减少重复代码，使代码更加简洁高效。

```typescript
import { ArcList, ArcListAttribute, ArcListItemAttribute, ArcListItem, LengthMetrics } from '@kit.ArkUI';
import { util } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: ResourceStr;
  icon: Resource;

  constructor(name: ResourceStr, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
export struct ArcListContents {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State private contacts: Array<object> = [

    new Contact($r('app.string.name_xiaohong'), $r('app.media.ic_contact')),
    new Contact($r('app.string.name_xiaolan'), $r('app.media.ic_contact')),
    new Contact($r('app.string.name_xiaowang'), $r('app.media.ic_contact')),
    new Contact($r('app.string.name_xiaoli'), $r('app.media.ic_contact')),
    new Contact($r('app.string.name_xiaoming'), $r('app.media.ic_contact'))
  ];

  build() {
    NavDestination() {
      Column({ space: 12 }) {

          ArcList({ initialIndex: 2 }) {
            ForEach(this.contacts, (item: Contact) => {
              ArcListItem() {
                Row() {
                  Image(item.icon)
                    .width(40)
                    .height(40)
                    .margin(10)
                    .backgroundColor('#FF9CC998')
                    .borderRadius(20)
                  Text(item.name).fontSize('38px').fontColor('#FFFFFFFF')
                }
                .width('100%')
                .justifyContent(FlexAlign.Start)
              }
              .borderRadius('65px')
              .width('410px')
              .height('130px')
              .backgroundColor('#26FFFFFF')
            }, (item: Contact) => JSON.stringify(item))
          }
          .space(LengthMetrics.px(10))
          .width('466px')
          .height('466px')
          .borderRadius('233px')
          .backgroundColor(Color.Black)
        }

    }
    .backgroundColor('#f1f2f3')

    .title($r('app.string.ArcListContents_title'))
  }
}
```

**图2** 迭代弧形列表内容

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/qKnnWSFoQcauwbbKWAG05A/zh-cn_image_0000002565210171.png?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=4455455F5E2C94B10A07B25C5FACE50B9BADCEF0D99B5E47B30A214104B9DD89)

## 自定义弧形列表样式

### 自定义弧形列表标题

可以通过[header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#arklistoptions)参数为弧形列表添加自定义标题。

1. 首先，需要构造自定义标题组件customHeader。 ```typescript @Builder function customHeader() {  Column() {  Text($r('app.string.ArcListCrown_set'))  .fontColor('#FFFFFFFF')  .fontSize('19fp')  } } ```
2. 由于[header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#arklistoptions)参数的类型是[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)，所以需要对自定义标题组件进行封装。 ```typescript context: UIContext = this.getUIContext(); arcListHeader: ComponentContent<Object> = new ComponentContent(this.context, wrapBuilder(customHeader)); ```
3. 最后，通过[header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#arklistoptions)参数将arcListHeader设置到弧形列表中。 ```typescript ArcList({ header: this.arcListHeader }) {  ArcListItem() {  }  ArcListItem() {  } } ```

**图3** 自定义弧形列表标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/KX6_nM-AT_KZhYmib6Ow6Q/zh-cn_image_0000002534250348.png?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=D8EF8A4F380BBE8E9D36C16E817EE48521B2FFB5B328CFCBA376562E4206F33A)

### 设置弧形列表项间距

在初始化列表时，若需在列表项之间添加间距，可以通过[space](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#space)属性实现。例如，为在每个列表项的垂直方向上增加30px的间距。

```typescript
ArcList({ initialIndex: 2 }) {

}
.space(LengthMetrics.px(30))
```

**图4** 设置弧形列表项间距

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xTRNgsPASVGw3qngN_XGjw/zh-cn_image_0000002534410294.png?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=1A2DEE8C57C137EA091B8AF3BB43B955C2B32546F2844D728DF18157369792C6)

### 列表项关闭自动缩放

在弧形列表中，列表项默认具有在接近上下两端时自动缩放的效果。然而，在某些情况下，可能不希望有这种缩放效果。此时，可以通过设置[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)的[autoScale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem#autoscale)属性为false来禁用该效果。例如，如图5所示，“网络”和“显示”两个列表项，在关闭了自动缩放属性后，无论它们所处的位置如何，都不会出现缩放效果。

```typescript
ArcListItem() {

}
.autoScale(false)
```

**图5** 列表项关闭自动缩放

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/M5vwim9VSUWPbjAMdO9_ZA/zh-cn_image_0000002565290193.png?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=569950EF57D5F47939CC359EB3806E39FFF9DDFA8410FBE3F6DBA6B0D4ABE902)

### 添加内置滚动条

当列表项的高度超过屏幕高度时，弧形列表能够沿垂直方向滚动。若用户需要快速定位，可拖动滚动条以迅速滑动列表，如图6所示。

在使用[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件时，可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#scrollbar)属性来控制弧形列表滚动条的显示。scrollBar的取值类型为[BarState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#barstate)，当设置为BarState.Auto时，表示滚动条将按需显示。在这种模式下，当用户触摸到滚动条区域时，滚动条会显示出来，支持上下拖拽以快速浏览内容，且在拖拽过程中滚动条会变粗。若用户不进行任何操作，滚动条将在2秒后自动消失。此外，还可以通过[scrollBarWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#scrollbarwidth)属性来设置滚动条在按压状态下的宽度，以及通过[scrollBarColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#scrollbarcolor)属性来设置滚动条的颜色。

```typescript
ArcList({ header: this.arcListHeader }) {

}
.scrollBar(BarState.Auto)
.scrollBarWidth(LengthMetrics.px(10))
.scrollBarColor(ColorMetrics.resourceColor(Color.White))
```

**图6** 弧形列表的内置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/b0lKgcn4SHm4iSwwIOvCTw/zh-cn_image_0000002565210173.gif?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=D1164C7F20A1934D25CE79AC5A86C780DD10630A0D7C7239B5E7F98A098D4D14)

## 添加外置滚动条ArcScrollBar

弧形列表[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)可与[ArcScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar)组件配合使用，为弧形列表添加外置滚动条。两者通过绑定同一个[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)滚动控制器对象实现联动。

1. 首先，需要创建一个[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)类型的对象arcListScroller。 ```typescript private arcListScroller: Scroller = new Scroller(); ```
2. 然后，弧形列表通过[scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#arklistoptions)参数绑定滚动控制器。 ```typescript ArcList({ scroller: this.arcListScroller, header: this.arcListHeader }) { } ```
3. 最后，弧形滚动条通过[scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar#arcscrollbaroptions)参数绑定滚动控制器。 ```typescript ArcScrollBar({ scroller: this.arcListScroller }) ```

**图7** 弧形列表的外置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DqdcNTz-TgCMdMqkDwdU9g/zh-cn_image_0000002534250350.gif?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=57DA02F2C0999EC00424A9401A91FA8C1835AA060E35D922E8EFEC8BEECAD5FF)

> **说明**
> 弧形滚动条组件[ArcScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar)，还可配合其他可滚动组件使用，如[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)。

## 与弧形索引条ArcAlphabetIndexer联动

许多应用需要监测列表的滚动位置变动并作出响应，或通过调整滚动位置实现列表的快速定位。例如，在联系人列表滚动时，当列表滚动至不同首字母开头的联系人，外部索引条应更新至相应的字母位置。当用户选择外部索引条上的索引项时，列表应跳转至对应位置。为此，需使用弧形索引条组件[ArcAlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)。

如图8所示，当列表从联系人A滚动到联系人B时，外侧索引条也需要同步从选中A状态变成选中B状态，此场景可以通过监听[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件的[onScrollIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#onscrollindex)事件来实现；当点击索引项C时，列表也需要跳转到联系人C，此场景可以通过监听[ArcAlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)的[onSelect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer#onselect)事件来实现。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引条对应字母的位置selectedIndex。由于[ArcAlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)组件通过[selected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer#selected)属性设置了选中项索引值，当selectedIndex变化时会触发[ArcAlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)组件重新渲染，从而显示为选中对应字母的状态。

在选中索引项时，根据此时选中项的索引值index，重新计算列表联系人对应的位置，然后通过列表绑定的滚动控制器arcListScroller的[scrollToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolltoindex)方法控制列表跳转到对应的联系人位置。弧形列表[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)可通过[scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#arklistoptions)参数绑定[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)（滚动控制器）。

```typescript
import { ArcList, ArcListAttribute, ArcListItemAttribute, ArcListItem, LengthMetrics } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

const alphabets: string[] = [
  '#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
];

@Entry
@Component
export struct ArcListArcIndexerBar {

  @State indexerIndex: number = 0;

  private arcListScroller: Scroller = new Scroller();

  build() {

          Stack({alignContent: Alignment.End}) {
            ArcList({ initialIndex: 0, header:this.tabBar1, scroller:this.arcListScroller }) {

            }

            .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {

              this.indexerIndex = centerIndex + 1;
            })

            ArcAlphabetIndexer({ arrayValue: alphabets, selected: this.indexerIndex})
              .selected(this.indexerIndex!!)
              .onSelect((index: number) => {

                this.indexerIndex = index
                this.arcListScroller.scrollToIndex(this.indexerIndex - 1)
              })

          }

  }
}
```

**图8** 弧形列表与弧形索引条联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/RHSRT6RDT26yVF_awq3gHA/zh-cn_image_0000002534410296.gif?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=C2D3E74392AE2FACDED5995D665FFF7BEFAF8C8C62F77958A5CB6AA1D56F9182)

## 响应列表项侧滑

[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)的[swipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem#swipeaction)属性可用于实现列表项的左右滑动功能。[swipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem#swipeaction)属性方法初始化时存在必填[SwipeActionOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeactionoptions9对象说明)参数start和end。其中，start表示设置列表项右滑时起始端滑出的组件，end表示设置列表项左滑时尾端滑出的组件。

在联系人列表中，end参数表示设置[ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据数据索引来删除列表项对应的数据，从而实现侧滑删除功能。

1. 首先，实现尾端滑出组件的构建。 ```typescript @Builder itemEnd(item: Contact) {  Button({ type: ButtonType.Circle }) {  Image($r('app.media.ic_public_delete_filled'))  .width(20)  .height(20)  }  .width(20)  .height(20)  .backgroundColor(Color.Black)  .onClick(() => {  this.getUIContext()?.animateTo({  duration: 1000,  curve: Curve.Smooth,  iterations: 1,  playMode: PlayMode.Normal,  }, () => {  let index = this.contacts.indexOf(item);  this.contacts.splice(index, 1);  })  }) } ```
2. 然后，绑定[swipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem#swipeaction)属性到可左滑的ArcListItem上。 ```typescript ArcListItem() { } .swipeAction({  end: {  builder: () => {  this.itemEnd(item);  },  } }) ```

**图9** 侧滑删除列表项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Df80FT_ORuymE0LHngKepQ/zh-cn_image_0000002565290195.gif?HW-CC-KV=V1&HW-CC-Date=20260401T025238Z&HW-CC-Expire=86400&HW-CC-Sign=A1DC2D4E014022571D3CD12A9A1757B927BFD649B472BA68F319605CE492D984)

## 处理长列表

[循环渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。关于长列表按需加载优化的具体实现可参考[数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)章节中的示例。

当使用懒加载方式渲染列表时，为了减少列表滑动时出现白块，[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)组件提供了[cachedCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#cachedcount)属性，该属性用于设置列表项缓存数，只在懒加载[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)中生效。

```typescript
ArcList() {

}.cachedCount(3)
```

> **说明**
> - cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
> - 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。

## 响应旋转表冠

手表设备上弧形列表在获焦的情况下可对旋转表冠做出响应，用户可通过旋转表冠的操作滑动列表，浏览列表项数据。弧形列表可通过下列[焦点控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus)相关属性成为所在页面的默认焦点。

```typescript
ArcList({
  initialIndex: 2,
}) {

}

.focusable(true)

.focusOnTouch(true)

.defaultFocus(true)
```

还可以通过[digitalCrownSensitivity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist#digitalcrownsensitivity)属性设置表冠响应事件的灵敏度，以应对不同量级的列表项数据。列表项数据较多时可以设置更高的响应事件灵敏度，数据较少时可以设置较低的响应事件灵敏度。

```typescript
ArcList({
  initialIndex: 2,
}) {

}

.digitalCrownSensitivity(CrownSensitivity.MEDIUM)
```
