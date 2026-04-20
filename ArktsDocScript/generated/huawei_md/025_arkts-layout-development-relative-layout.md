# 相对布局 (RelativeContainer)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-relative-layout

## 概述

在应用的开发过程中，经常需要设计复杂界面，此时涉及到多个相同或不同组件之间的嵌套。如果布局组件嵌套深度过深，或者嵌套组件数过多，会带来额外的开销。如果在布局的方式上进行优化，就可以有效的提升性能，减少时间开销。

RelativeContainer是一种采用相对布局的容器，支持容器内部的子元素设置相对位置关系，适用于处理界面复杂的场景，对多个子元素进行对齐和排列。子元素可以指定兄弟元素或父容器作为锚点，基于锚点进行相对位置布局。在使用锚点时，需注意子元素的相对位置关系，以避免出现错位或遮挡的情况。下图展示了一个 RelativeContainer的概念图，图中的虚线表示位置的依赖关系。

**图1** 相对布局示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/YY-BwqWwRtaLf29xlhgpjA/zh-cn_image_0000002572639771.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=44975A5618E09F5918A11EF140565611CCAE40B3D94606CC020769C26AE42879)

子元素并不完全是上图中的依赖关系。比如，Item4可以以Item2为依赖锚点，也可以以RelativeContainer父容器为依赖锚点。

## 基本概念

- 参考边界：设置当前组件的哪个边界对齐到锚点。
- 锚点：通过锚点设置当前元素基于哪个元素确定位置。
- 对齐方式：通过对齐方式，设置当前元素是基于锚点的上中下对齐，还是基于锚点的左中右对齐。
- 链：将一系列组件以首尾相连的方式对齐，可以形成一条链。通过设置链的模式，可以指定链上元素的排列方式。
- 辅助线：辅助线是在容器内虚拟出的额外水平或垂直锚点，便于统一对齐至某个偏移位置。
- 屏障：屏障是指容器内一组指定组件在特定方向上的共同最远边界，例如，一组组件下方的屏障，是指这些组件底部边缘中最底部的那个边界。

## 设置依赖关系

### 设置参考边界

设置当前组件的哪个边界对齐到锚点。容器内子组件的参考边界区分水平方向和垂直方向。

- 在水平方向上，可以按照起始（left）、居中（middle）或尾端（right）的组件边界与锚点对齐。当设置三个边界时，仅起始（left）和居中（middle）的边界设置生效。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/fMLn23MrRhSTiQxa2OENVg/zh-cn_image_0000002542119464.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=48C6CE87C2D1ED2C3B8E591974F964AB916122E09F66437FE05D1221DDA68EA9)
- 在垂直方向上，可以设置组件边界与锚点对齐，具体包括顶部（top）、居中（center）和底部（bottom）。当设置三个边界时，仅顶部（top）和居中（center）生效。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/QnMvZYzBRrWZAeb0X7-wBw/zh-cn_image_0000002572679735.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=464886BDD55D1F4BCA4DC0DD0C167D8E0BD5853745EED5A59C939B40B3278D7D)

### 设置锚点

锚点设置涉及子元素相对于其父元素或兄弟元素的位置依赖关系。具体而言，子元素可以将其位置锚定到相对布局容器（RelativeContainer）、辅助线（guideline）、屏障（barrier）或其他子元素上。

为了准确定义锚点，RelativeContainer的子元素必须拥有唯一的组件标识（id），用于指定锚点信息。父元素RelativeContainer的标识默认为“__container__”，其他子元素的组件标识（id）则通过[id](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#id)属性设置。

> **说明**
> - 未设置组件标识（id）的组件虽可显示，但无法被其他组件引用为锚点。相对布局容器会为其拼接组件标识，但组件标识（id）的规律无法被应用感知。辅助线（guideline）与屏障（barrier）的组件标识（id）需确保唯一，避免与任何组件冲突。若有重复，遵循组件 > guideline > barrier 的优先级。
> - 组件间设置锚点时应避免形成依赖循环（组件之间设置链除外），依赖循环将导致子组件缺乏定位基准，最终无法绘制。

- RelativeContainer父组件为锚点，__container__代表父容器的组件标识（id）。 ```typescript let alignRus: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {  'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },  'left': { 'anchor': '__container__', 'align': HorizontalAlign.Start } } let alignRue: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {  'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },  'right': { 'anchor': '__container__', 'align': HorizontalAlign.End } } let marginLeft: Record<string, number> = { 'left': 20 } let bwc: Record<string, number | string> = { 'width': 2, 'color': '#6699FF' } @Entry @Component struct ParentRefRelativeContainer {  build() {  RelativeContainer() {  Row() {  Text('row1')  }  .justifyContent(FlexAlign.Center)  .width(100)  .height(100)  .backgroundColor('#a3cf62')  .alignRules(alignRus)  .id('row1')  Row() {  Text('row2')  }  .justifyContent(FlexAlign.Center)  .width(100)  .height(100)  .backgroundColor('#00ae9d')  .alignRules(alignRue)  .id('row2')  }.width(300).height(300)  .margin(marginLeft)  .border(bwc)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/B66ihmy5Tgu3tUvm2fBQrQ/zh-cn_image_0000002541959828.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=53019AAF276D8D4EF09BFE7E8963B1D51F34CA57F726DFDF3457829D9225ACCD)
- 以兄弟元素为锚点。 ```typescript let alignRus001: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {  'top': { 'anchor': '__container__', 'align': VerticalAlign.Top },  'left': { 'anchor': '__container__', 'align': HorizontalAlign.Start } } let relConB: Record<string, Record<string, string | VerticalAlign | HorizontalAlign>> = {  'top': { 'anchor': 'row1', 'align': VerticalAlign.Bottom },  'left': { 'anchor': 'row1', 'align': HorizontalAlign.Start } } let marginLeft001: Record<string, number> = { 'left': 20 } let bwc001: Record<string, number | string> = { 'width': 2, 'color': '#6699FF' } @Entry @Component struct SiblingRefRelativeContainer {  build() {  RelativeContainer() {  Row() {  Text('row1')  }  .justifyContent(FlexAlign.Center)  .width(100)  .height(100)  .backgroundColor('#00ae9d')  .alignRules(alignRus001)  .id('row1')  Row() {  Text('row2')  }  .justifyContent(FlexAlign.Center)  .width(100)  .height(100)  .backgroundColor('#a3cf62')  .alignRules(relConB)  .id('row2')  }.width(300).height(300)  .margin(marginLeft001)  .border(bwc001)  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6R4zEWbKRWOtDAdisGKvJw/zh-cn_image_0000002572639773.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=6BE10A61AE3566878AF587F5423412B9661BE40BF8D3C2EAD107F8B057FECAE4)
- 子组件锚点可以任意选择，但需注意不要相互依赖。 ```typescript @Entry @Component struct ChildRefRelativeContainer {  build() {  Row() {  RelativeContainer() {  Row() {  Text('row1')  }  .justifyContent(FlexAlign.Center)  .width(100)  .height(100)  .backgroundColor('#a3cf62')  .alignRules({  top: { anchor: '__container__', align: VerticalAlign.Top },  left: { anchor: '__container__', align: HorizontalAlign.Start }  })  .id('row1')  Row() {  Text('row2')  }  .justifyContent(FlexAlign.Center)  .width(100)  .backgroundColor('#00ae9d')  .alignRules({  top: { anchor: '__container__', align: VerticalAlign.Top },  right: { anchor: '__container__', align: HorizontalAlign.End },  bottom: { anchor: 'row1', align: VerticalAlign.Center },  })  .id('row2')  Row() {  Text('row3')  }  .justifyContent(FlexAlign.Center)  .height(100)  .backgroundColor('#0a59f7')  .alignRules({  top: { anchor: 'row1', align: VerticalAlign.Bottom },  left: { anchor: 'row1', align: HorizontalAlign.Start },  right: { anchor: 'row2', align: HorizontalAlign.Start }  })  .id('row3')  Row() {  Text('row4')  }.justifyContent(FlexAlign.Center)  .backgroundColor('#2ca9e0')  .alignRules({  top: { anchor: 'row3', align: VerticalAlign.Bottom },  left: { anchor: 'row1', align: HorizontalAlign.Center },  right: { anchor: 'row2', align: HorizontalAlign.End },  bottom: { anchor: '__container__', align: VerticalAlign.Bottom }  })  .id('row4')  }  .width(300).height(300)  .margin({ left: 50 })  .border({ width: 2, color: '#6699FF' })  }  .height('100%')  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/k9MbOsqQTguptVPUrjipHg/zh-cn_image_0000002542119466.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=B8E0C9B768F31B479ECE48055C2E432B2AFB7F53FEA9B3C41452069E92225C13)

### 设置相对于锚点的对齐位置

设置了锚点之后，可以通过[alignRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#alignrules9)属性的align设置相对于锚点的对齐位置。

在水平方向上，对齐位置可以设置为HorizontalAlign.Start、HorizontalAlign.Center、HorizontalAlign.End。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/M63vytD0Q6CmIt_9pFvFZw/zh-cn_image_0000002572679737.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=FA89A2A0DE2A02251758B35DCFF6454AD49DE95362F79A94A11A7EF01FD2179B)

在垂直方向上，对齐位置可以设置为VerticalAlign.Top、VerticalAlign.Center、VerticalAlign.Bottom。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Q_s7ppSZTey2jy9W-MQgcg/zh-cn_image_0000002541959830.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=5F796A7FDF23286F85AA0F1B64F007B9E1EE27C8902D615CB3976159600520DD)

### 子组件位置偏移

子组件经过相对位置对齐后，可能尚未达到目标位置。开发者可根据需要设置额外偏移（offset）。当使用offset调整位置的组件作为锚点时，对齐位置为设置offset之前的位置。从API Version 11开始，新增了[Bias](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#bias对象说明)对象，建议API Version 11及以后的版本使用bias来设置额外偏移。使用bias的示例可以参考[示例4（设置偏移）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer#示例4设置偏移)。

```typescript
@Entry
@Component
struct ChildComponentOffsetExample {
  build() {
    Row() {
      RelativeContainer() {
        Row() {
          Text('row1')
        }
        .justifyContent(FlexAlign.Center)
        .width(100)
        .height(100)
        .backgroundColor('#a3cf62')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          left: { anchor: '__container__', align: HorizontalAlign.Start }
        })
        .id('row1')

        Row() {
          Text('row2')
        }
        .justifyContent(FlexAlign.Center)
        .width(100)
        .backgroundColor('#00ae9d')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          bottom: { anchor: 'row1', align: VerticalAlign.Center },
        })
        .offset({
          x: -40,
          y: -20
        })
        .id('row2')

        Row() {
          Text('row3')
        }
        .justifyContent(FlexAlign.Center)
        .height(100)
        .backgroundColor('#0a59f7')
        .alignRules({
          top: { anchor: 'row1', align: VerticalAlign.Bottom },
          left: { anchor: 'row1', align: HorizontalAlign.End },
          right: { anchor: 'row2', align: HorizontalAlign.Start }
        })
        .offset({
          x: -10,
          y: -20
        })
        .id('row3')

        Row() {
          Text('row4')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#2ca9e0')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row1', align: HorizontalAlign.End }
        })
        .offset({
          x: -10,
          y: -30
        })
        .id('row4')

        Row() {
          Text('row5')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#30c9f7')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
          left: { anchor: 'row2', align: HorizontalAlign.Start },
          right: { anchor: 'row2', align: HorizontalAlign.End }
        })
        .offset({
          x: 10,
          y: 20
        })
        .id('row5')

        Row() {
          Text('row6')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#ff33ffb5')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: 'row4', align: VerticalAlign.Bottom },
          left: { anchor: 'row3', align: HorizontalAlign.Start },
          right: { anchor: 'row3', align: HorizontalAlign.End }
        })
        .offset({
          x: -15,
          y: 10
        })
        .backgroundImagePosition(Alignment.Bottom)
        .backgroundImageSize(ImageSize.Cover)
        .id('row6')
      }
      .width(300).height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/9zUeIGAeQGespLi9P7yqpA/zh-cn_image_0000002572639775.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=5E6368047AB84EF06DCD9B5D34A6E5F8103EAF44D6F90EBA1F3F02EE7159F273)

## 多种组件的对齐布局

Row、Column、Flex、Stack等多种布局组件，可按照RelativeContainer组件规则进行对齐排布。

```typescript
@Entry
@Component
struct RelativeContainerExample {
  build() {
    Row() {

      RelativeContainer() {
        Row()
          .width(100)
          .height(100)
          .backgroundColor('#a3cf62')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          })
          .id('row1')

        Column()
          .width('50%')
          .height(30)
          .backgroundColor('#00ae9d')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            left: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .id('row2')

        Flex({ direction: FlexDirection.Row }) {
          Text('1').width('20%').height(50).backgroundColor('#0a59f7')
          Text('2').width('20%').height(50).backgroundColor('#2ca9e0')
          Text('3').width('20%').height(50).backgroundColor('#0a59f7')
          Text('4').width('20%').height(50).backgroundColor('#2ca9e0')
        }
        .padding(10)
        .backgroundColor('#30c9f7')
        .alignRules({
          top: { anchor: 'row2', align: VerticalAlign.Bottom },
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          bottom: { anchor: '__container__', align: VerticalAlign.Center },
          right: { anchor: 'row2', align: HorizontalAlign.Center }
        })
        .id('row3')

        Stack({ alignContent: Alignment.Bottom }) {
          Text('First child, show in bottom')
            .width('90%')
            .height('100%')
            .backgroundColor('#a3cf62')
            .align(Alignment.Top)
          Text('Second child, show in top').width('70%').height('60%').backgroundColor('#00ae9d').align(Alignment.Top)
        }
        .margin({ top: 5 })
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
          right: { anchor: 'row3', align: HorizontalAlign.End }
        })
        .id('row4')

      }
      .width(300).height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/EG0-GgYjRaGjP-8lUIO5lw/zh-cn_image_0000002542119468.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=BABDDE1417F91CB4F33A2EB6BE4A21CD9EDC393846E8B3FD044EE4D151240D91)

## 组件尺寸

当同时存在前端页面设置的子组件尺寸和相对布局规则时，子组件的绘制尺寸依据约束规则确定。从API Version 11开始，此规则有所变化，子组件自身设置的尺寸优先级高于相对布局规则中的对齐锚点尺寸。因此，若要使子组件与锚点严格对齐，应仅使用alignRules，避免使用[尺寸设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size)。

> **说明**
> - 根据约束条件和子组件自身的size属性无法确定子组件的大小，此时，不绘制该子组件。
> - 在同一方向上设置两个或更多锚点时，若这些锚点的位置顺序有误，该子组件将被视为大小为0而不予绘制。

```typescript
@Entry
@Component
struct RelativeAlignRulesExample {
  build() {
    Row() {
      RelativeContainer() {
        Row() {
          Text('row1')
        }
        .justifyContent(FlexAlign.Center)
        .width(100)
        .height(100)
        .backgroundColor('#a3cf62')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          left: { anchor: '__container__', align: HorizontalAlign.Start }
        })
        .id('row1')

        Row() {
          Text('row2')
        }
        .justifyContent(FlexAlign.Center)
        .width(100)
        .backgroundColor('#00ae9d')
        .alignRules({
          top: { anchor: '__container__', align: VerticalAlign.Top },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          bottom: { anchor: 'row1', align: VerticalAlign.Center },
        })
        .id('row2')

        Row() {
          Text('row3')
        }
        .justifyContent(FlexAlign.Center)
        .height(100)
        .backgroundColor('#0a59f7')
        .alignRules({
          top: { anchor: 'row1', align: VerticalAlign.Bottom },
          left: { anchor: 'row1', align: HorizontalAlign.End },
          right: { anchor: 'row2', align: HorizontalAlign.Start }
        })
        .id('row3')

        Row() {
          Text('row4')
        }.justifyContent(FlexAlign.Center)
        .backgroundColor('#2ca9e0')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row1', align: HorizontalAlign.End }
        })
        .id('row4')

        Row() {
          Text('row5')
        }.justifyContent(FlexAlign.Center)
        .backgroundColor('#30c9f7')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
          left: { anchor: 'row2', align: HorizontalAlign.Start },
          right: { anchor: 'row2', align: HorizontalAlign.End }
        })
        .id('row5')

        Row() {
          Text('row6')
        }
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#ff33ffb5')
        .alignRules({
          top: { anchor: 'row3', align: VerticalAlign.Bottom },
          bottom: { anchor: 'row4', align: VerticalAlign.Bottom },
          left: { anchor: 'row3', align: HorizontalAlign.Start },
          right: { anchor: 'row3', align: HorizontalAlign.End }
        })
        .id('row6')
        .backgroundImagePosition(Alignment.Bottom)
        .backgroundImageSize(ImageSize.Cover)
      }
      .width(300).height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ML_plQXnTti9gs5KJcN-_g/zh-cn_image_0000002572679739.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=5F1E41A80DEF9E37D7A0D1AE1844375F08E8F4FF982477256D133F9295D5D81A)

## 多个组件形成链

链的形成依赖于组件之间的关联关系。以组件A和组件B构成的最简水平链为例，其依赖关系为：锚点1 <-- 组件A <---> 组件B --> 锚点2，即A具有left锚点，B具有right锚点，同时A的right锚点与B的HorizontalAlign.Start对齐，B的left锚点与A的HorizontalAlign.End对齐。

- 链的方向和格式在链头组件的[chainMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#chainmode12)接口中声明；链内元素的bias属性全部失效，链头元素的bias属性作为整个链的bias生效。链头是指在满足成链规则时链的第一个组件（在水平方向上，从左边开始，镜像语言中从右边开始；在垂直方向上，从上边开始）。
- 如果链内所有元素的size超出链的锚点约束，超出部分将被均匀分配到链的两侧。在[PACKED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#chainstyle12)链中，可以通过[Bias](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#bias对象说明)设置超出部分的分布。

在以下示例代码中，通过alignRules和chainMode将九个在容器内的Row组件分为三组水平链式排列。组件row1、组件row2和组件row3顶部对齐，水平方向成SPREAD链，链内组件在锚点间均匀分布。组件row4、组件row5、组件row6垂直方向基于容器居中，水平方向成SPREAD_INSIDE链，链内除首尾2个组件对齐锚点外，其他组件在链中均匀分布。组件row7、组件row8、组件row9底部对齐，水平方向组成PACKED链，链内组件无间隙。

```typescript
@Entry
@Component
struct RelativeChainModeExample {
  build() {
    Row() {
      RelativeContainer() {
        Row() {
          Text('row1')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row2', align: HorizontalAlign.Start },
          top: { anchor: '__container__', align: VerticalAlign.Top }
        })
        .id('row1')
        .chainMode(Axis.Horizontal, ChainStyle.SPREAD)

        Row() {
          Text('row2')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row1', align: HorizontalAlign.End },
          right: { anchor: 'row3', align: HorizontalAlign.Start },
          top: { anchor: 'row1', align: VerticalAlign.Top }
        })
        .id('row2')

        Row() {
          Text('row3')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row2', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row1', align: VerticalAlign.Top }
        })
        .id('row3')

        Row() {
          Text('row4')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row5', align: HorizontalAlign.Start },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })
        .id('row4')
        .chainMode(Axis.Horizontal, ChainStyle.SPREAD_INSIDE)

        Row() {
          Text('row5')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row4', align: HorizontalAlign.End },
          right: { anchor: 'row6', align: HorizontalAlign.Start },
          top: { anchor: 'row4', align: VerticalAlign.Top }
        })
        .id('row5')

        Row() {
          Text('row6')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row5', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row4', align: VerticalAlign.Top }
        })
        .id('row6')

        Row() {
          Text('row7')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row8', align: HorizontalAlign.Start },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        })
        .id('row7')
        .chainMode(Axis.Horizontal, ChainStyle.PACKED)

        Row() {
          Text('row8')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row7', align: HorizontalAlign.End },
          right: { anchor: 'row9', align: HorizontalAlign.Start },
          top: { anchor: 'row7', align: VerticalAlign.Top }
        })
        .id('row8')

        Row() {
          Text('row9')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row8', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row7', align: VerticalAlign.Top }
        })
        .id('row9')
      }
      .width(300).height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/hN3eAxm1RpuDMzcUubBnkQ/zh-cn_image_0000002541959832.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=F86541DA0A40860EDB4B6DD1D888465990F18016215BEC5EA5DA87CE0B0A81E1)

## 使用辅助线辅助定位子组件

辅助线（guideLine）是在容器内虚拟出的额外水平或垂直锚点，便于统一对齐到特定偏移位置，从而避免为每个组件单独编写重复的偏移设置。

辅助线分为垂直（Vertical）和水平（Horizontal）两种：垂直辅助线通过start和end属性指定其距离容器左侧和右侧的距离；水平辅助线通过start和end属性指定其距离容器顶部和底部的距离。

- 如果同时设置了start和end，当两者规则冲突时，仅start属性生效。
- 若容器在某个方向的尺寸被声明为"auto"，则该方向上的guideLine位置只能使用start属性声明（不允许使用百分比）。

在以下示例代码中，定义了一条垂直辅助线guideline1，距离容器左侧50vp，以及另一条水平辅助线guideline2，距离容器顶部50vp。组件row1通过这两条辅助线来定位自身位置，无需设置bias。

```typescript
@Entry
@Component
struct RelativeGuideLineExample {
  build() {
    Row() {
      RelativeContainer() {
        Row()
          .width(100)
          .height(100)
          .backgroundColor('#a3cf62')
          .alignRules({
            left: { anchor: 'guideline1', align: HorizontalAlign.End },
            top: { anchor: 'guideline2', align: VerticalAlign.Top }
          })
          .id('row1')
      }
      .width(300)
      .height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
      .guideLine([{ id: 'guideline1', direction: Axis.Vertical, position: { start: 50 } },
        { id: 'guideline2', direction: Axis.Horizontal, position: { start: 50 } }])
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/A_nDTAFQRbKQFtKDwInLMw/zh-cn_image_0000002572639777.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=37AF081A46426EA6D30973163BBAFE05B5EF5FB86C4D76C26E6AA23747A7F46B)

## 多个组件的屏障

屏障（barrier）是容器的一种动态参考边界，它基于一组指定组件的实际位置，计算出它们在特定方向上的公共最远边界。当需要让某个组件参照多个组件的集体边界时使用，例如实现“位于这些组件右侧”或“不与其他任何组件重叠”等效果。

屏障可以有上下左右四个方向。垂直方向（TOP，BOTTOM）的屏障仅能作为组件的水平方向锚点，用作垂直方向锚点时值为0；水平方向（LEFT，RIGHT）的屏障仅能作为组件的垂直方向锚点，用作水平方向锚点时值为0。

与静态的guideline不同，barrier会随参照组件位置变化而自动更新，只需定义实际需要的方向即可。

在下列示例代码中，item1，item2，item3三个组件可以视为由一个隐形的矩形区域包围着，outer1基于这个“隐形区域”的底部边界进行布局，位于该区域的下方；outer2基于这个“隐形区域”的右侧边界进行布局，位于该区域的右侧。

```typescript
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('item 1')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item1')
        .alignRules({
          top: {
            anchor: '__container__',
            align: VerticalAlign.Top
          },
          left: {
            anchor: '__container__',
            align: HorizontalAlign.Start
          }
        })
      Text('item 2')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item2')
        .alignRules({
          top: {
            anchor: 'item1',
            align: VerticalAlign.Bottom
          },
          left: {
            anchor: 'item1',
            align: HorizontalAlign.End
          }
        })
      Text('item 3')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item3')
        .alignRules({
          bottom: {
            anchor: 'item2',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'item2',
            align: HorizontalAlign.End
          }
        })
      Text('outer 1')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#00ae9d')

        .alignRules({
          top: {
            anchor: 'barrier_bottom',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'barrier_left',
            align: HorizontalAlign.Start
          }
        })

      Text('outer 2')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#00ae9d')

        .alignRules({
          top: {
            anchor: 'barrier_top',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'barrier_right',
            align: HorizontalAlign.Start
          }
        })
    }
    .width('100%')
    .padding(10)
    .barrier([
      {
        id: 'barrier_left',
        direction: BarrierDirection.LEFT,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_right',
        direction: BarrierDirection.RIGHT,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_top',
        direction: BarrierDirection.TOP,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_bottom',
        direction: BarrierDirection.BOTTOM,
        referencedId: ['item1', 'item2', 'item3']
      },
    ])
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/wT4d0WDGQtyl4Ng49pnESg/zh-cn_image_0000002542119470.png?HW-CC-KV=V1&HW-CC-Date=20260420T025809Z&HW-CC-Expire=86400&HW-CC-Sign=2E3DC4FA24C1BB45A1DCA5837F3A5953910DFF467EE5919C278D983CC577C66C)
