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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/MN-iSNU9QMedbvmy_MMJLA/zh-cn_image_0000002537172968.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=770348B39B46B28BBE57C6625F636D9B1BE2C85817972197454BE13A812FDE7A)

- loop为false

```typescript
  Swiper() {

  }

  .loop(false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/FjwGLUgGSUWayg4sunt9zA/zh-cn_image_0000002537332890.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=5529D65CC168972CD3DAC9CD388B0DB10F8C5E416B2C9A5D4B660F48108A3730)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XYOmMxnkSnu-KrEUrp4XFg/zh-cn_image_0000002568172687.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=26D8AF06BD343D2C4B6CDA3429C64CAE69586FA0AC497EC26361A07DEE4C7948)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/uDDFo9xkTTyMJE-VIhf9-A/zh-cn_image_0000002568252683.png?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=91774A1F95DD426D7B556F73D45436E57F39E93322A8A3A9BEE0A17B9C5BEA8E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/nOspY8prSxubUMAIvqn5bQ/zh-cn_image_0000002537172970.png?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=5AEAA66C8E3512D92A9C87F4B6DB45EDB68364D3B39049DE269DD089F6A501BD)

Swiper通过设置[displayArrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#displayarrow10)属性，可以控制导航点箭头的大小、位置、颜色，底板的大小及颜色，以及鼠标悬停时是否显示箭头。

- 箭头使用默认样式

```typescript
  Swiper() {

  }

  .displayArrow(true, false)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/lRHX-l2sTMiNSC4RgpXhtA/zh-cn_image_0000002537332892.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=9A2B9DBBA0A49D19E77414E560CAFAF30C01FB7F93DE4953439ABCC7C51FD760)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/CZRaJ1bIQAecYYQiGngLwQ/zh-cn_image_0000002568172689.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=1329D3BEB7E4F4983B111D726347B7297EB2B27AE03592AFD0ECD50C3CDB9071)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/shgj8oA_SQqv7CKtcSVaBg/zh-cn_image_0000002568252685.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=CD5C82FB90A6059CCA8B5B6AB26BD10A75687DA9AAEC65FE215B6675EBBE0DE2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/RDGvKA1FQ2meV2sCZpN7GA/zh-cn_image_0000002537172972.png?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=DC324A460E0D4E595D24E092B1318EE7E86958C1EC38FDC31037E9E12B66BB2A)

- 设置垂直方向轮播。

```typescript
Swiper(

) {

}

.indicator(true)
.vertical(true)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/9a9ftfWRQJCFuFtgj29xmg/zh-cn_image_0000002537332894.png?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=DA451381AF6821A7E49E00492CBA5FEFA4B49D48C9959377EEE6B1C981653994)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/3jDBPtuKTdOWm--6OjRpDQ/zh-cn_image_0000002568172691.png?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=093F2878FF8026945A072BB53F75DBE6B4CE973AC37CAF255030CCEC2BB4664B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/IBvlYEexS0ST468jQ8VTGw/zh-cn_image_0000002568252687.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=019B7B88F6A91B621F7B7BF3D07237E4E7C18D15E17C123EB0318CE01691B942)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/-1M20ku6T3K40IkZms-fLA/zh-cn_image_0000002537172974.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=802F15D123670AA21C841806440531C5AB33C4ADA113B3555DE0434881AE33A6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/mxpW5A2PR72WCQrhBSuM8g/zh-cn_image_0000002537332896.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=CD9F42B8284C334AE5F8FEC98A2EAA5C692A1640D5E96D4B0C3B85E0AE250C96)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/v_Y2fsiFRQCfnj3aOsEEuQ/zh-cn_image_0000002568172693.gif?HW-CC-KV=V1&HW-CC-Date=20260409T023735Z&HW-CC-Expire=86400&HW-CC-Sign=1C6DEF349F587DC3AEE3F80564BD70ED877359969C936B88FFD191FF792AB29C)

## 示例代码

- [短视频切换](https://gitcode.com/HarmonyOS_Samples/short-video)
