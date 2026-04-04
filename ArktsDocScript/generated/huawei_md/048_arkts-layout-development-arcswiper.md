# 创建弧形轮播 (ArcSwiper)（圆形屏幕推荐使用）
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-arcswiper

ArcSwiper是弧形轮播组件，在圆形屏幕场景下使用，提供弧形轮播显示能力。具体用法请参考[ArcSwiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper)。

在使用ArcSwiper组件之前，需要在代码中先导入ArcSwiper模块。

```typescript
import {
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';
```

## 设置导航点样式

ArcSwiper提供了默认的弧形导航点样式，导航点默认显示在ArcSwiper下方居中位置，开发者也可以通过[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#indicator)属性自定义弧形导航点的样式。

通过indicator属性，开发者可以设置弧形导航点的方向，同时也可以设置导航点和被选中导航点的颜色。

- 导航点使用默认样式 ```typescript ArcSwiper() {  Text('0')  .width(233)  .height(233)  .backgroundColor(Color.Gray)  .textAlign(TextAlign.Center)  .fontSize(30)  Text('1')  .width(233)  .height(233)  .backgroundColor(Color.Green)  .textAlign(TextAlign.Center)  .fontSize(30)  Text('2')  .width(233)  .height(233)  .backgroundColor(Color.Pink)  .textAlign(TextAlign.Center)  .fontSize(30) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Jg22-2ezQKm7RBarnNACFg/zh-cn_image_0000002535948390.png?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=2F79E3B82977290EE59E0F807BCC0ACB77F300937268B759DD9F791594A842AF)
- 自定义导航点样式 导航点位于ArcSwiper组件6点钟方向，导航点颜色设为红色，被选中导航点颜色为蓝色。 ```typescript ArcSwiper() { } .indicator(  new ArcDotIndicator()  .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION)  .itemColor(Color.Red)  .selectedItemColor(Color.Blue) ) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/mxCWGua5TliDs3DYxS4kOw/zh-cn_image_0000002566868223.png?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=51ED38D12532BD8747543B85E48FAB120B1772DF88D48DFB968042619D423861)

## 控制页面切换方式

ArcSwiper支持滑动手指、点击导航点、旋转表冠和控制控制器四种方式切换页面。以下示例展示通过控制控制器和旋转表冠翻页的方法。

- 控制控制器翻页。 ```typescript import {  ArcButton,  ArcButtonOptions,  ArcButtonStatus,  ArcButtonStyleMode,  ArcButtonPosition,  ArcSwiper,  ArcSwiperAttribute,  ArcSwiperController, } from '@kit.ArkUI'; @Entry @Component export struct ArcSwiperToggle {  private wearableSwiperController: ArcSwiperController = new ArcSwiperController();  build() {  Column({ space: 12 }) {  Stack() {  ArcSwiper(  this.wearableSwiperController  ) {  }  .vertical(true)  .indicator(false)  Column() {  ArcButton({  options: new ArcButtonOptions({  label: 'previous',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  onClick: () => {  this.wearableSwiperController.showPrevious();  }  })  })  Blank()  ArcButton({  options: new ArcButtonOptions({  label: 'next',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  onClick: () => {  this.wearableSwiperController.showNext();  }  })  })  }.width('100%').height('100%')  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/SU55bBPMTMKotaC-6WCoHQ/zh-cn_image_0000002566708243.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=CEB203145131DBE588D70BCFB1A19F0C7B327E0CD3BDEC2F1E25F9614DABA63A)
- 旋转表冠翻页。 ArcSwiper在获得焦点时能够响应旋转表冠的操作，用户可以通过旋转表冠来滑动ArcSwiper，从而浏览数据。 ```typescript ArcSwiper( ) { } .focusable(true) .focusOnTouch(true) .defaultFocus(true) ``` 还可以通过设置[digitalCrownSensitivity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#digitalcrownsensitivity)属性来调整表冠对事件响应的灵敏度，以适应不同规模的数据处理。在处理大量数据时，可以提高响应事件的灵敏度；而在处理少量数据时，则可以降低灵敏度设置。 ```typescript ArcSwiper( ) { } .digitalCrownSensitivity(CrownSensitivity.MEDIUM) ```

## 设置轮播方向

ArcSwiper支持水平和垂直方向上进行轮播，主要通过[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。 ```typescript ArcSwiper() { } .indicator(true) .vertical(false) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/5rlhMy1nRJ6auq6Tcb-HNA/zh-cn_image_0000002535948390.png?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=79CE7EF2BD6A5860F8ED9122365D33D836A43C4D145B28C22BB7DFFF11222376)
- 设置垂直方向轮播，导航点设为3点钟方向。 ```typescript ArcSwiper() { } .indicator(new ArcDotIndicator()  .arcDirection(ArcDirection.THREE_CLOCK_DIRECTION)) .vertical(true) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/-xPQZw1_RG-bCCBssvtywQ/zh-cn_image_0000002535788446.png?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=69546C4329E39C9E0F5DAF2EAC25CDFC7D3160D9E45D1B00B746833395CC271A)

## 自定义切换动画

ArcSwiper支持通过[customContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#customcontenttransition)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性，从而实现自定义切换动画效果。

```typescript
import { Decimal } from '@kit.ArkTS';
import {
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';

@Entry
@Component
export struct ArcSwiperAction {
  private MIN_SCALE: number = 0.1;
  @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
  @State opacityList: number[] = [];
  @State scaleList: number[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < this.backgroundColors.length; i++) {
      this.opacityList.push(1.0);
      this.scaleList.push(1.0);
    }
  }

  build() {

      Column({ space: 12 }) {

          ArcSwiper() {
            ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
              Text(index.toString())
                .width(233)
                .height(233)
                .fontSize(50)
                .textAlign(TextAlign.Center)
                .backgroundColor(backgroundColor)
                .opacity(this.opacityList[index])
                .scale({ x: this.scaleList[index], y: this.scaleList[index] })
            })
          }
          .customContentTransition({
            timeout: 1000,
            transition: (proxy: SwiperContentTransitionProxy) => {
              if (proxy.position <= -1 || proxy.position >= 1) {

                this.opacityList[proxy.index] = 1.0;
                this.scaleList[proxy.index] = 1.0;
              } else {
                let position: number = Decimal.abs(proxy.position).toNumber();
                this.opacityList[proxy.index] = 1 - position;
                this.scaleList[proxy.index] =
                  this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - position);
              }
            }
          })

      }
      .width('100%')

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/j1oxtCf9TEa1oyL4q84ddQ/zh-cn_image_0000002535948392.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=4A16FE765A4D235BF6D49285174E30EB160082BAF5795CDEA9CEFDAF37E6C2BF)

## 实现侧滑返回

ArcSwiper的滑动事件会与侧滑返回冲突，可以通过[onGestureRecognizerJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement#ongesturerecognizerjudgebegin)去判断ArcSwiper是否滑动到开头去拦截ArcSwiper的滑动手势，实现再次左滑返回上一页的功能。

```typescript
import {
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';

@Entry
@Component
export struct ArcSwiperSideSlip {
  @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
  innerSelectedIndex: number = 0;

  build() {

      Column({ space: 12 }) {

          ArcSwiper() {
            ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
              Text(index.toString())
                .width(233)
                .height(233)
                .fontSize(50)
                .textAlign(TextAlign.Center)
                .backgroundColor(backgroundColor)
            })
          }
          .onAnimationStart((index: number, targetIndex: number) => {
            this.innerSelectedIndex = targetIndex;
          })
          .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
            others: Array<GestureRecognizer>): GestureJudgeResult => {
            if (current) {
              let target = current.getEventTargetInfo();
              if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
                let swiperTarget = target as ScrollableTargetInfo;
                if (swiperTarget instanceof ScrollableTargetInfo &&
                  (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
                  let panEvent = event as PanGestureEvent;
                  if (panEvent && panEvent.offsetX > 0 && (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
                    return GestureJudgeResult.REJECT;
                  }
                }
              }
            }
            return GestureJudgeResult.CONTINUE;
          })

      }
      .width('100%')

  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/90LN26DkRwm6c84X2Q3LbA/zh-cn_image_0000002566868225.gif?HW-CC-KV=V1&HW-CC-Date=20260404T023017Z&HW-CC-Expire=86400&HW-CC-Sign=50DA5B4A4BC616ECB507F7BA952429AA41C3B6DE367A89441198F733D195030B)
