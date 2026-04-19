# 创建轮播 (Swiper)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-looping

[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。通常，在一些应用首页显示推荐的内容时，需要用到轮播显示的能力。

针对复杂页面场景，可以使用Swiper组件的预加载机制，利用主线程的空闲时间来提前构建和布局绘制组件，优化滑动体验。

## 布局与约束

Swiper作为一个容器组件，如果设置了自身尺寸属性，则在轮播显示过程中均以该尺寸生效。如果自身尺寸属性未被设置，则分两种情况：如果设置了[prevMargin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#prevmargin10)或者[nextMargin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#nextmargin10)属性，则Swiper自身尺寸会跟随其父组件；如果未设置prevMargin或者nextMargin属性，则会自动根据子组件的大小设置自身的尺寸。

## 循环播放

通过[loop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#loop)属性控制是否循环播放，该属性默认值为true。

当loop为true时，在显示第一页或最后一页时，可以继续往前切换到前一页或者往后切换到后一页。如果loop为false，则在第一页或最后一页时，无法继续向前或者向后切换页面。

- loop为true

```typescript
  Swiper() {
    Text('0')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Gray)
      .textAlign(TextAlign.Center)
      .fontSize(30)

    Text('1')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Green)
      .textAlign(TextAlign.Center)
      .fontSize(30)

    Text('2')
      .width('90%')
      .height('100%')
      .backgroundColor(Color.Pink)
      .textAlign(TextAlign.Center)
      .fontSize(30)
  }

  .loop(true)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Y2q0pTVmRQOynyErfhAGlw/zh-cn_image_0000002541959952.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=63B6615BCDE2EAD9F838EC02AD2FEBC5EB898558AEDB7EACC10468D5F434ABA4)

- loop为false

```typescript
  Swiper() {

  }

  .loop(false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/7D0cn92pQiSckNyxwLmXKA/zh-cn_image_0000002572639897.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=AACBE3379D00A9DD76F2B44C78056861672DA523D716A0537D4259AE33CB6C0B)

## 自动轮播

Swiper通过设置[autoPlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#autoplay)属性，控制是否自动轮播子组件。该属性默认值为false。

autoPlay为true时，会自动切换播放子组件，子组件与子组件之间的播放间隔通过interval属性设置。interval属性默认值为3000，单位毫秒。

```typescript
  Swiper() {

  }

  .loop(true)
  .autoPlay(true)
  .interval(1000)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ejUCWUvfR26U8WANf45szQ/zh-cn_image_0000002542119590.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=2BBDF92C1F6D2E111C43449D1B4D8F2D14FA0A072FA422C809ABF7728344CB7F)

## 导航点样式

Swiper提供了默认的导航点样式和导航点箭头样式，导航点默认显示在Swiper下方居中位置，开发者也可以通过[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicator)属性自定义导航点的位置和样式，导航点箭头默认不显示。

通过indicator属性，开发者可以设置导航点相对于Swiper组件上下左右四个方位的位置，同时也可以设置每个导航点的尺寸、颜色、蒙层和被选中导航点的颜色。

- 导航点使用默认样式

```typescript
Swiper() {
  Text('0')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text('1')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text('2')
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/GEBBf8mYSJ6nUy62MaUA0g/zh-cn_image_0000002572679861.png?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=5B0CDE0EC029D4ECA452F74DB9297BBAA243579E44892278CA2C8B9995E0A06C)

- 自定义导航点样式

选中的导航点，直径设为30vp，且颜色为蓝色；未选中的导航点，直径设为15vp，颜色设为红色。

```typescript
  Swiper() {

  }

  .indicator(
    Indicator.dot()
      .left(0)
      .itemWidth(15)
      .itemHeight(15)
      .selectedItemWidth(30)
      .selectedItemHeight(15)
      .color(Color.Red)
      .selectedColor(Color.Blue)
  )
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/mDBw28UBTqGK0ujZMINHEg/zh-cn_image_0000002541959954.png?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=8C24BAB76E39DB1A69A654B5A42AEAB0D9B0027433BDFB80D247C45D8B187CC6)

Swiper通过设置[displayArrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#displayarrow10)属性，可以控制导航点箭头的大小、位置、颜色，底板的大小及颜色，以及鼠标悬停时是否显示箭头。

- 箭头使用默认样式

```typescript
  Swiper() {

  }

  .displayArrow(true, false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/IBSyzMrRTB6jvmZebm4DhQ/zh-cn_image_0000002572639899.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=6FBB8EF2DABFFA27D2B79ABCBFFBF05377E26F6E504BEC11F7ED79D6D1BBA306)

- 自定义箭头样式

箭头显示在组件两侧，大小为18vp，导航点箭头颜色设为蓝色。

```typescript
  Swiper() {

  }

  .displayArrow({
    showBackground: true,
    isSidebarMiddle: true,
    backgroundSize: 24,
    backgroundColor: Color.White,
    arrowSize: 18,
    arrowColor: Color.Blue
  }, false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/e8bgqFD4T6mTiLfdLvJPag/zh-cn_image_0000002542119592.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=2BE307C1CE0E799B17B1F8B8608FD0324120DC736D12E1F99327ACF4352B2BC2)

## 页面切换方式

Swiper支持手指滑动、点击导航点和通过控制器三种方式切换页面，以下示例展示通过控制器切换页面的方法。

```typescript
@Component
export struct SwiperPageSwitchMethod {
  private swiperBackgroundColors: Color[] = [Color.Blue, Color.Brown, Color.Gray, Color.Green, Color.Orange,
    Color.Pink, Color.Red, Color.Yellow];
  private swiperAnimationMode: (SwiperAnimationMode | boolean | undefined)[] = [undefined, true, false,
    SwiperAnimationMode.NO_ANIMATION, SwiperAnimationMode.DEFAULT_ANIMATION, SwiperAnimationMode.FAST_ANIMATION];
  private swiperController: SwiperController = new SwiperController();
  private animationModeIndex: number = 0;
  private animationMode: (SwiperAnimationMode | boolean | undefined) = undefined;
  @State animationModeStr: string = 'undefined';
  @State targetIndex: number = 0;

  aboutToAppear(): void {
    this.toSwiperAnimationModeStr();
  }

  build() {

          Column({ space: 5 }) {
            Swiper(this.swiperController) {
              ForEach(this.swiperBackgroundColors, (backgroundColor: Color, index: number) => {
                Text(index.toString())
                  .width(250)
                  .height(250)
                  .backgroundColor(backgroundColor)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              })
            }

            .indicator(true)

            Row({ space: 12 }) {
              Button('showNext')
                .onClick(() => {
                  this.swiperController.showNext();
                })
              Button('showPrevious')
                .onClick(() => {
                  this.swiperController.showPrevious();
                })
            }.margin(5)

            Row({ space: 12 }) {
              Text('Index:')
              Button(this.targetIndex.toString())
                .onClick(() => {
                  this.targetIndex = (this.targetIndex + 1) % this.swiperBackgroundColors.length;
                })
            }.margin(5)
            Row({ space: 12 }) {
              Text('AnimationMode:')
              Button(this.animationModeStr)
                .onClick(() => {
                  this.animationModeIndex = (this.animationModeIndex + 1) % this.swiperAnimationMode.length;
                  this.toSwiperAnimationModeStr();
                })
            }.margin(5)

            Row({ space: 12 }) {
              Button('changeIndex(' + this.targetIndex + ', ' + this.animationModeStr + ')')
                .onClick(() => {
                  this.swiperController.changeIndex(this.targetIndex, this.animationMode);
                })
            }.margin(5)
          }

  }

  private toSwiperAnimationModeStr() {
    this.animationMode = this.swiperAnimationMode[this.animationModeIndex];
    if ((this.animationMode === true) || (this.animationMode === false)) {
      this.animationModeStr = '' + this.animationMode;
    } else if ((this.animationMode === SwiperAnimationMode.NO_ANIMATION) ||
      (this.animationMode === SwiperAnimationMode.DEFAULT_ANIMATION) ||
      (this.animationMode === SwiperAnimationMode.FAST_ANIMATION)) {
      this.animationModeStr = SwiperAnimationMode[this.animationMode];
    } else {
      this.animationModeStr = 'undefined';
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2966F475SduupqfFocAuKQ/zh-cn_image_0000002572679863.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=7CFC22391C970FF323E0D99EC41D3BAED634DE0255FD70EBE507BB9E947AE943)

## 轮播方向

Swiper支持水平和垂直方向上进行轮播，主要通过[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。

```typescript
Swiper(

) {

}

.indicator(true)
.vertical(false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/smoG_wroSYiokjAhPJAODA/zh-cn_image_0000002541959956.png?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=627E19CFBA2580B8A8504FA3B37DFEBD49C11B69B40D2FFA980AAA37F1B4CD74)

- 设置垂直方向轮播。

```typescript
Swiper(

) {

}

.indicator(true)
.vertical(true)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/utqPofRIS4CFyYn6txmFDQ/zh-cn_image_0000002572639901.png?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=0BA702E69F93CA7762A0205007C636EEE01C09B605DDF1BBDA9D55B49B81FAD5)

## 每页显示多个子页面

Swiper支持在一个页面内同时显示多个子组件，通过[displayCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#displaycount8)属性设置。

```typescript
  Swiper() {
    Text('0')
      .width(250)
      .height(250)
      .backgroundColor(Color.Gray)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('1')
      .width(250)
      .height(250)
      .backgroundColor(Color.Green)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('2')
      .width(250)
      .height(250)
      .backgroundColor(Color.Pink)
      .textAlign(TextAlign.Center)
      .fontSize(30)
    Text('3')
      .width(250)
      .height(250)
      .backgroundColor(Color.Yellow)
      .textAlign(TextAlign.Center)
      .fontSize(30)
  }

  .indicator(true)
  .displayCount(2)
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/8yb5S3ufTWK-a4DY_mImsg/zh-cn_image_0000002542119594.png?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=21DF83EF1A423229DE154E28304F9139909D0A89CB8FBAE2CFC0A0C6D033468C)

## 自定义切换动画

Swiper支持通过[customContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#customcontenttransition12)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性实现自定义切换动画。

```typescript
@Component
export struct SwiperCustomAnimation {
  private DISPLAY_COUNT: number = 2;
  private MIN_SCALE: number = 0.75;
  @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
  @State opacityList: number[] = [];
  @State scaleList: number[] = [];
  @State translateList: number[] = [];
  @State zIndexList: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
      this.translateList.push(0.0);
      this.zIndexList.push(0);
    }
  }

  build() {

      Column({ space: 12 }) {

          Swiper() {
            ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
              Text(index.toString())
                .width('100%')
                .height('100%')
                .fontSize(50)
                .textAlign(TextAlign.Center)
                .backgroundColor(backgroundColor)
                .opacity(this.opacityList[index])
                .scale({ x: this.scaleList[index], y: this.scaleList[index] })
                .translate({ x: this.translateList[index] })
                .zIndex(this.zIndexList[index])
            })
          }
          .height(300)
          .indicator(false)
          .displayCount(this.DISPLAY_COUNT, true)
          .customContentTransition({
            timeout: 1000,
            transition: (proxy: SwiperContentTransitionProxy) => {
              if (proxy.position <= proxy.index % this.DISPLAY_COUNT ||
                proxy.position >= this.DISPLAY_COUNT + proxy.index % this.DISPLAY_COUNT) {

                this.opacityList[proxy.index] = 1.0;
                this.scaleList[proxy.index] = 1.0;
                this.translateList[proxy.index] = 0.0;
                this.zIndexList[proxy.index] = 0;
              } else {

                if (proxy.index % this.DISPLAY_COUNT === 0) {
                  this.opacityList[proxy.index] = 1 - proxy.position / this.DISPLAY_COUNT;
                  this.scaleList[proxy.index] =
                    this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - proxy.position / this.DISPLAY_COUNT);
                  this.translateList[proxy.index] = -proxy.position * proxy.mainAxisLength +
                    (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
                } else {
                  this.opacityList[proxy.index] = 1 - (proxy.position - 1) / this.DISPLAY_COUNT;
                  this.scaleList[proxy.index] =
                    this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - (proxy.position - 1) / this.DISPLAY_COUNT);
                  this.translateList[proxy.index] = -(proxy.position - 1) * proxy.mainAxisLength -
                    (1 - this.scaleList[proxy.index]) * proxy.mainAxisLength / 2.0;
                }
                this.zIndexList[proxy.index] = -1;
              }
            }
          })

      }
      .width('100%')

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/EDsX91MuSpGB7BXSDx1dmQ/zh-cn_image_0000002572679865.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=48473D8C795A2E8F0C0A5FD078A90066A21EB85E90988D80DAB913C912E8F6E1)

## Swiper与Tabs联动

从API version 18开始，Swiper选中的元素改变时，会通过[onSelected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#onselected18)回调事件，将元素的索引值index返回。通过调用[tabsController.changeIndex(index)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#changeindex)方法来实现Tabs页签的切换。

```typescript
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Component
export struct SwiperAndTabsLinkage {
  @State fontColor: string = '#182431';
  @State selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  private list: number[] = [];
  private tabsController: TabsController = new TabsController();
  private swiperController: SwiperController = new SwiperController();
  private swiperData: MyDataSource = new MyDataSource([]);
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    for (let i = 0; i <= 9; i++) {
      this.list.push(i);
    }
    this.swiperData = new MyDataSource(this.list);
  }

  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.currentIndex === index ? 1 : 0)
    }.width('20%')
  }

  build() {

          Column() {
            Tabs({ barPosition: BarPosition.Start, controller: this.tabsController }) {
              ForEach(this.list, (index: number) =>{

                TabContent().tabBar(this.tabBuilder(index,
                  this.context.resourceManager.getStringByNameSync('swiper_text1') + this.list[index]))
              })
            }
            .onTabBarClick((index: number) => {
              this.currentIndex = index;
              this.swiperController.changeIndex(index, true);
            })
            .barMode(BarMode.Scrollable)
            .backgroundColor('#F1F3F5')
            .height(56)
            .width('100%')

            Swiper(this.swiperController) {
              LazyForEach(this.swiperData, (item: string) => {
                Text(item.toString())
                  .onAppear(()=>{
                    console.info('onAppear ' + item.toString());
                  })
                  .onDisAppear(()=>{
                    console.info('onDisAppear ' + item.toString());
                  })
                  .width('100%')
                  .height('40%')
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              }, (item: string) => item)
            }
            .loop(false)
            .onSelected((index: number) => {
              console.info('onSelected:' + index);
              this.currentIndex = index;
              this.tabsController.changeIndex(index);
            })
          }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Rw3huUwZRPe9EIt5L7NFcQ/zh-cn_image_0000002541959958.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=CDAFE42EE6C5B02E9AD3503BCBB50E86CEBDDEEB637B4343BDB3B5C41A69FE8E)

## 设置圆点导航点间距

从API version 19开始，针对圆点导航点，可以通过DotIndicator的[space](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#space19)属性来设置圆点导航点的间距。

```typescript
Swiper(

) {

}
.indicator(new DotIndicator()
  .space(this.space)

)
```

## 导航点忽略组件大小

当导航点的[bottom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#bottom)设为0之后，导航点的底部与Swiper的底部还会有一定间距。如果希望消除该间距，从API version 19开始，可通过调用[bottom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#bottom19)(bottom, ignoreSize)属性来进行设置。将ignoreSize设置为true，即可忽略导航点组件大小，达到消除该间距的目的。

- 圆点导航点忽略组件大小。

```typescript
Swiper(

) {

}
.indicator(new DotIndicator()

  .bottom(LengthMetrics.vp(0), this.ignoreSize)

)
```

- 数字导航点忽略组件大小。

```typescript
Swiper(

) {

}
.indicator(new DigitIndicator()
  .bottom(LengthMetrics.vp(0), true)
)
```

圆点导航点设置间距及忽略组件大小完整示例代码如下：

```typescript
import { LengthMetrics } from '@kit.ArkUI';

class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener() {
  }
}

@Component
export struct SwiperIgnoreComponentSize {

  @State space: LengthMetrics = LengthMetrics.vp(0);
  @State spacePool: LengthMetrics[] = [LengthMetrics.vp(0), LengthMetrics.px(3), LengthMetrics.vp(10)];
  @State spaceIndex: number = 0;

  @State ignoreSize: boolean = false;
  @State ignoreSizePool: boolean[] = [false, true];
  @State ignoreSizeIndex: number = 0;

  private swiperController1: SwiperController = new SwiperController();
  private data1: MyDataSource = new MyDataSource([]);

  aboutToAppear(): void {
    let list1: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list1.push(i);
    }
    this.data1 = new MyDataSource(list1);
  }

  build() {

          Scroll() {
            Column({ space: 20 }) {
              Swiper(
                this.swiperController1
              ) {
                LazyForEach(this.data1, (item: string) => {
                  Text(item.toString())
                    .width('90%')
                    .height(120)
                    .backgroundColor(0xAFEEEE)
                    .textAlign(TextAlign.Center)
                    .fontSize(30)
                }, (item: string) => item)
              }
              .indicator(new DotIndicator()
                .space(this.space)
                .bottom(LengthMetrics.vp(0), this.ignoreSize)
                .itemWidth(15)
                .itemHeight(15)
                .selectedItemWidth(15)
                .selectedItemHeight(15)
                .color(Color.Gray)
                .selectedColor(Color.Blue)
              )
              .displayArrow({
                showBackground: true,
                isSidebarMiddle: true,
                backgroundSize: 24,
                backgroundColor: Color.White,
                arrowSize: 18,
                arrowColor: Color.Blue
              }, false)

              Column({ space: 4 }) {
                Button('spaceIndex:' + this.spaceIndex).onClick(() => {
                  this.spaceIndex = (this.spaceIndex + 1) % this.spacePool.length;
                  this.space = this.spacePool[this.spaceIndex];
                }).margin(10)

                Button('ignoreSizeIndex:' + this.ignoreSizeIndex).onClick(() => {
                  this.ignoreSizeIndex = (this.ignoreSizeIndex + 1) % this.ignoreSizePool.length;
                  this.ignoreSize = this.ignoreSizePool[this.ignoreSizeIndex];
                }).margin(10)
              }.margin(2)
            }.width('100%')
          }

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/QKK7m7frRE2VWREWszIaSA/zh-cn_image_0000002572639903.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=D912C6F8FF14FF4EE97F9B802E3DA837F9CEC4E821508A1A096CF10C62861617)

## 保持可见内容位置不变

从API version 20开始，Swiper通过设置[maintainVisibleContentPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#maintainvisiblecontentposition20)属性，可在使用LazyForEach懒加载数据时（如通过onDataAdd新增数据），保持当前可见内容位置不变，避免因数据增删导致的视图跳动。该属性默认值为false。

maintainVisibleContentPosition为true时，显示区域上方或前方插入或删除数据时可见内容位置不变。

关于数据[LazyForEach：数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)的具体使用，可参考数据懒加载章节中的示例。

```typescript
class MyDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private dataArray: string[] = ['0', '1', '2', '3', '4', '5', '6'];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): string | undefined {
    return this.dataArray[index];
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  public deleteData(index: number): void {
    this.dataArray.splice(index, 1);
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      hilog.info(DOMAIN, 'testTag', 'add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      hilog.info(DOMAIN, 'testTag', 'remove listener');
      this.listeners.splice(pos, 1);
    }
  }
}

@Component
export struct SwiperVisibleContentPosition {
  private data: MyDataSource = new MyDataSource();
  @State index: number = 3;

  build() {

      Column({ space: 12 }) {

            Swiper() {
              LazyForEach(this.data, (item: string) => {
                Text(item.toString())
                  .width('90%')
                  .height(160)
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30)
              })
            }
            .onChange((index) => {
              this.index = index;
            })
            .index(3)
            .maintainVisibleContentPosition(true)

            Column({ space: 12 }) {
              Text('index:' + this.index).fontSize(20)
              Row() {

                Button('header data add').height(30).onClick(() => {
                  this.data.addData(0, 'header Data');
                })

                Button('header data delete').height(30).onClick(() => {
                  this.data.deleteData(0);
                })
              }
            }.margin(5)

      }.width('100%')
      .margin({ top: 5 })

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/smEEnTWVSD6-joeRF62vdw/zh-cn_image_0000002542119596.gif?HW-CC-KV=V1&HW-CC-Date=20260419T025749Z&HW-CC-Expire=86400&HW-CC-Sign=E099B61D4930E14F3C41BCE6680F8937D94003E786E1D48793C89C680C1F3108)

## 示例代码

- [短视频切换](https://gitcode.com/HarmonyOS_Samples/short-video)
