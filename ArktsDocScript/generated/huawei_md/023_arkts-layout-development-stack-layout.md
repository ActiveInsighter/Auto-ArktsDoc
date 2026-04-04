# 层叠布局 (Stack)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout

## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1->Item2->Item3。

**图1** 层叠布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/eWzqrKcnRsmo-AnYdYWp9w/zh-cn_image_0000002535788244.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=FCD056EE3F89EF7DB2C8FC2284A3E0F3AD6ABD55F3B79BBDEE2920EB56523EF5)

> **说明**
> 过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠布局的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization#section78181114123811)。

## 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```typescript
// xxx.ets
let mTop:Record<string,number> = { 'top': 50 }
@Entry
@Component
struct StackLayoutExample {
  build() {
    Column(){
      Stack({ }) {
        Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
        Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
        Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
      }.width('100%').height(150).margin(mTop)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/FwF3MWzrSw6tKlctJJz59Q/zh-cn_image_0000002535948190.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=2A646CF0668D7243637A278CEBC372BFB48BD08013A9AF4FF8C28A0F5C090EC2)

## 对齐方式

Stack组件通过[alignContent参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack#aligncontent)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/KrtrrXmcTwG-AX2I5a16Xg/zh-cn_image_0000002566868023.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=F6C4CF3AB1F886FA8ADE13BE1C7159BA9B7CCE63412197C8BF5C9D7AFE5BD06D)

```typescript
// xxx.ets
@Entry
@Component
struct StackAlignContentExample {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Text('Stack').width('90%').height('100%').backgroundColor('#e1dede').align(Alignment.BottomEnd)
      Text('Item 1').width('70%').height('80%').backgroundColor(0xd2cab3).align(Alignment.BottomEnd)
      Text('Item 2').width('50%').height('60%').backgroundColor(0xc1cbac).align(Alignment.BottomEnd)
    }.width('100%').height(150).margin({ top: 5 })
  }
}
```

## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

```typescript
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack_num1')).textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)
  Column() {
    // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)
  Column() {
    // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/mJ782AfHTpqnglUNg6Pc7w/zh-cn_image_0000002566708043.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=DF31E5AA4281E78430A4A42895436F5A32E5FB22C7D552ABF4E766C4D2D5840A)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1、子元素2的zIndex属性后，可以将元素展示出来。

```typescript
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack_num1')).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)
  Column() {
    // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)
  Column() {
    // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/azYK1URzQrqFT3EgyTuzlQ/zh-cn_image_0000002535788246.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=0998026AADCBD0EF68593DF7252324A8DB7D09DB2424E794358423CE181D50D2)

## 场景示例

使用层叠布局快速搭建页面。

```typescript
@Entry
@Component
struct StackSample {
  private arr: string[] = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];
  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Flex({ wrap: FlexWrap.Wrap }) {
        ForEach(this.arr, (item:string) => {
          Text(item)
            .width(100)
            .height(100)
            .fontSize(16)
            .margin(10)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }, (item:string):string => item)
      }.width('100%').height('100%')
      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // 请将$r('app.string.contacts')替换为实际资源文件，在本示例中该资源文件的value值为"联系人"
        Text($r('app.string.contacts')).fontSize(16)
        // 请将$r('app.string.setting')替换为实际资源文件，在本示例中该资源文件的value值为"设置"
        Text($r('app.string.setting')).fontSize(16)
        // 请将$r('app.string.text_message')替换为实际资源文件，在本示例中该资源文件的value值为"短信"
        Text($r('app.string.text_message')).fontSize(16)
      }
      .width('50%')
      .height(50)
      .backgroundColor('#16302e2e')
      .margin({ bottom: 15 })
      .borderRadius(15)
    }.width('100%').height('100%').backgroundColor('#CFD0CF')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/JJ0KAMiRTT2y6RvBsS0hDw/zh-cn_image_0000002535948194.png?HW-CC-KV=V1&HW-CC-Date=20260404T022954Z&HW-CC-Expire=86400&HW-CC-Sign=C7DB286AB4CD735529646984929B541C94A5F56D2C60263ABA6BF33550D9A919)

## 示例代码

- [组件堆叠](https://gitcode.com/HarmonyOS_Samples/component-stack)
