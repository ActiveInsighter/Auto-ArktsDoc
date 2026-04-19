# 层叠布局 (Stack)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout

## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1->Item2->Item3。

**图1** 层叠布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/EbGKNY5hQw-224yieYtTeg/zh-cn_image_0000002542119444.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=9CBE5614E824D677D10E8CF155DD11B46D2C7738FFFDEC57226B3A3F9A80C662)

> **说明**
> 过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠布局的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization#section78181114123811)。

## 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```typescript
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/y-c_FH9uTZW8CJBhf60hLg/zh-cn_image_0000002572679715.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=581A8A51F6B8A76BA4147F46C4EFB3449D228566A7B5E751B9516F0030F1D9AB)

## 对齐方式

Stack组件通过[alignContent参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack#aligncontent)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/KuRfmL3mT_quSkvxr5s7LQ/zh-cn_image_0000002541959808.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=8EEB38BF92B7EA77EAC17967FA0193BEA3A03D29306F4908358FB579083D2305)

```typescript
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

    Text($r('app.string.stack_num1')).textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)

  Column() {

    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)

  Column() {

    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/RuJoNf5EQNa8Njvyv5Zrlw/zh-cn_image_0000002572639753.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=48A273B7F3D6DAD136D379458604B6C8202BF410E4922798058A4C9D84AEE292)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1、子元素2的zIndex属性后，可以将元素展示出来。

```typescript
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {

    Text($r('app.string.stack_num1')).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

  Column() {

    Text($r('app.string.stack_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

  Column() {

    Text($r('app.string.stack_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/m-FEi2xKSJ-VBX5TC_eP6Q/zh-cn_image_0000002542119446.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=B003542F5EB87826A42741696061894F839FBDDB9B3E572316DF4F25CB28F333)

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

        Text($r('app.string.contacts')).fontSize(16)

        Text($r('app.string.setting')).fontSize(16)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ic7v_BBuRDWmym1Bg2iOZA/zh-cn_image_0000002572679717.png?HW-CC-KV=V1&HW-CC-Date=20260419T025724Z&HW-CC-Expire=86400&HW-CC-Sign=06EB3413724CE283D546A2B9D75D0D4A3B1B04109F921BFC1FA800D196F152B5)

## 示例代码

- [组件堆叠](https://gitcode.com/HarmonyOS_Samples/component-stack)
