# 页面转场动画 (不推荐)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-transition-animation

为了实现更好的转场效果，推荐使用[组件导航(Navigation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)和[模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-transition)。

两个页面间发生跳转，一个页面消失，另一个页面出现，这时可以配置各自页面的页面转场参数实现自定义的页面转场效果。[页面转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation)效果写在pageTransition函数中，通过[PageTransitionEnter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#pagetransitionenter)和[PageTransitionExit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#pagetransitionexit)指定页面进入和退出的动画效果。

pageTransition的函数为：

```typescript
pageTransition() {
  PageTransitionEnter()
  PageTransitionExit()
}
```

PageTransitionEnter的接口为：

```typescript
PageTransitionEnter({ type?: RouteType, duration?: number, curve?: Curve | string, delay?: number })
```

PageTransitionExit的接口为：

```typescript
PageTransitionExit({ type?: RouteType, duration?: number, curve?: Curve | string, delay?: number })
```

上述接口定义了PageTransitionEnter和PageTransitionExit组件，可通过[slide](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#slide)、[translate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#translate)、[scale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#scale)、[opacity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#opacity)属性定义不同的页面转场效果。对于PageTransitionEnter而言，这些效果表示入场时起点值，对于PageTransitionExit而言，这些效果表示退场的终点值，这一点与组件转场[transition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)配置方法类似。此外，PageTransitionEnter提供了onEnter接口进行自定义页面入场动画的回调，PageTransitionExit提供了onExit接口进行自定义页面退场动画的回调。

上述接口中的参数type，表示路由生效的类型，这一点开发者容易混淆其含义。页面转场的两个页面，必定有一个页面退出，一个页面进入。如果通过[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl)操作从页面A跳转到页面B，则页面A退出，做页面退场动画，页面B进入，做页面入场动画。如果通过[back](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#back)操作从页面B返回到页面A，则页面B退出，做页面退场动画，页面A进入，做页面入场动画。即页面的PageTransitionEnter既可能是由于新增页面(push，入栈)引起的新页面的入场动画，也可能是由于页面返回(back，或pop，出栈)引起的页面栈中老页面的入场动画，为了能区分这两种形式的入场动画，提供了type参数，这样开发者能完全定义所有类型的页面转场效果。

## type配置为RouteType.None

type为RouteType.None表示对页面栈的push、pop操作均生效，type的默认值为RouteType.None。

```typescript
pageTransition() {

  PageTransitionEnter({ type: RouteType.None, duration: 1200 })
    .slide(SlideEffect.Left)

  PageTransitionExit({ type: RouteType.None, duration: 1000 })
    .slide(SlideEffect.Left)
}
```

```typescript
pageTransition() {

  PageTransitionEnter({ type: RouteType.None, duration: 1000 })
    .slide(SlideEffect.Right)

  PageTransitionExit({ type: RouteType.None, duration: 1200 })
    .slide(SlideEffect.Right)
}
```

假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作 | 页面A转场效果 | 页面B转场效果 |
| --- | --- | --- |
| pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |
| back，从页面B返回到页面A | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕 |
| pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕 |
| back，从页面A返回到页面B | 页面退出，PageTransitionExit生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |

如果希望pushUrl进入的页面总是从右侧滑入，back时退出的页面总是从右侧滑出，则上表中的第3、4种情况不满足要求，那么需要完整的定义4个页面转场效果。

## type配置为RouteType.Push或RouteType.Pop

[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#pagetransitionoptions对象说明)为[RouteType.Push](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#routetype枚举说明)表示仅对页面栈的push操作生效，type为RouteType.Pop表示仅对页面栈的pop操作生效。

```typescript
pageTransition() {

  PageTransitionEnter({ type: RouteType.Push, duration: 1200 })
    .slide(SlideEffect.Right)

  PageTransitionEnter({ type: RouteType.Pop, duration: 1200 })
    .slide(SlideEffect.Left)

  PageTransitionExit({ type: RouteType.Push, duration: 1000 })
    .slide(SlideEffect.Left)

  PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
    .slide(SlideEffect.Right)
}
```

```typescript
pageTransition() {

  PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
    .slide(SlideEffect.Right)

  PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
    .slide(SlideEffect.Left)

  PageTransitionExit({ type: RouteType.Push, duration: 1200 })
    .slide(SlideEffect.Left)

  PageTransitionExit({ type: RouteType.Pop, duration: 1200 })
    .slide(SlideEffect.Right)
}
```

以上代码则完整的定义了所有可能的页面转场样式。假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作 | 页面A转场效果 | 页面B转场效果 |
| --- | --- | --- |
| pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕 | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 |
| back，从页面B返回到页面A | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕 |
| pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕 |
| back，从页面A返回到页面B | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕 | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕 |

> **说明**
> - 由于每个页面的页面转场样式都可由开发者独立配置，而页面转场涉及到两个页面，开发者应考虑两个页面的页面转场效果的衔接，如时长尽量保持一致。
> - 如果没有定义匹配的页面转场样式，则该页面使用系统默认的页面转场样式。

## 禁用某页面的页面转场

通过设置页面转场的时长为0，可使该页面无页面转场动画。

```typescript
pageTransition() {
  PageTransitionEnter({ type: RouteType.None, duration: 0 })
  PageTransitionExit({ type: RouteType.None, duration: 0 })
}
```

## 场景示例

下面介绍了利用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl)跳转能力定义了所有的四种页面转场样式的页面转场动画示例。

```typescript
@Entry
@Component
struct PageTransitionSrc1 {
  build() {
    Column() {

      Image($r('app.media.mountain'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true)
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {

            this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template3/pageTransitionDst1' });
          })
        Button("back")
          .onClick(() => {

            this.getUIContext().getRouter().back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width('100%').height('100%')
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {

    PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Right)

    PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right)
  }
}
```

```typescript
@Entry
@Component
struct PageTransitionDst1 {
  build() {
    Column() {

      Image($r('app.media.forest'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true)
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {

            this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template3/pageTransitionSrc1' });
          })
        Button("back")
          .onClick(() => {

            this.getUIContext().getRouter().back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width('100%').height('100%')
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {

    PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Right)

    PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/E3iNcLWvQQeUvABbTaRg_w/zh-cn_image_0000002566708367.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024819Z&HW-CC-Expire=86400&HW-CC-Sign=A89BC6663E8A681950EDE021A6093FC4B28972B00ECA6A81F785531B215B5692)

下面介绍使用了type为None的页面转场动画示例。

```typescript
@Entry
@Component
struct PageTransitionSrc2 {
  build() {
    Column() {

      Image($r('app.media.mountain'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true)
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {

            this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template4/pageTransitionDst2' });
          })
        Button("back")
          .onClick(() => {

            this.getUIContext().getRouter().back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width('100%').height('100%')
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {

    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ duration: 1200 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

```typescript
@Entry
@Component
struct PageTransitionDst2 {
  build() {
    Column() {

      Image($r('app.media.forest'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true)
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {

            this.getUIContext().getRouter().pushUrl({ url: 'pages/pageTransition/template4/pageTransitionSrc2' });
          })
        Button("back")
          .onClick(() => {

            this.getUIContext().getRouter().back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width('100%').height('100%')
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {

    PageTransitionEnter({ duration: 1200 })
      .slide(SlideEffect.Left)

    PageTransitionExit({ duration: 1000 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Bn34-87QReiRTBlaMoyOmw/zh-cn_image_0000002535788572.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024819Z&HW-CC-Expire=86400&HW-CC-Sign=67357C529C0BD3D485A330B2911317EB72861DF5681167EADD1376E81A38D2E8)
