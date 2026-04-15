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

- 导航点使用默认样式 ```typescript ArcSwiper() {  Text('0')  .width(233)  .height(233)  .backgroundColor(Color.Gray)  .textAlign(TextAlign.Center)  .fontSize(30)  Text('1')  .width(233)  .height(233)  .backgroundColor(Color.Green)  .textAlign(TextAlign.Center)  .fontSize(30)  Text('2')  .width(233)  .height(233)  .backgroundColor(Color.Pink)  .textAlign(TextAlign.Center)  .fontSize(30) } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/zceTagMrQyG-cqL_GaelkA/zh-cn_image_0000002571291459.png?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=04469CA77D80ECD989ACFB6EC5C77D360BB99D46442357C670199312A4AE6889)
- 自定义导航点样式 导航点位于ArcSwiper组件6点钟方向，导航点颜色设为红色，被选中导航点颜色为蓝色。 ```typescript ArcSwiper() { } .indicator(  new ArcDotIndicator()  .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION)  .itemColor(Color.Red)  .selectedItemColor(Color.Blue) ) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3HM9PJETR9CgWfCPoeYEdw/zh-cn_image_0000002540611510.png?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=EB60C31806D9E34D22A84ABFD86FFC0183448066CFB5D4A02019E4DEC872B557)

## 控制页面切换方式

ArcSwiper支持滑动手指、点击导航点、旋转表冠和控制控制器四种方式切换页面。以下示例展示通过控制控制器和旋转表冠翻页的方法。

- 控制控制器翻页。 ```typescript import {  ArcButton,  ArcButtonOptions,  ArcButtonStatus,  ArcButtonStyleMode,  ArcButtonPosition,  ArcSwiper,  ArcSwiperAttribute,  ArcSwiperController, } from '@kit.ArkUI'; @Component export struct ArcSwiperToggle {  private wearableSwiperController: ArcSwiperController = new ArcSwiperController();  build() {  Column({ space: 12 }) {  Stack() {  ArcSwiper(  this.wearableSwiperController  ) {  }  .vertical(true)  .indicator(false)  Column() {  ArcButton({  options: new ArcButtonOptions({  label: 'previous',  position: ArcButtonPosition.TOP_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  onClick: () => {  this.wearableSwiperController.showPrevious();  }  })  })  Blank()  ArcButton({  options: new ArcButtonOptions({  label: 'next',  position: ArcButtonPosition.BOTTOM_EDGE,  styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,  onClick: () => {  this.wearableSwiperController.showNext();  }  })  })  }.width('100%').height('100%')  }  }  } } ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/EzfbujRVSvyIC6nZsUG3Bg/zh-cn_image_0000002571171505.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=C7F00164A067539752165C2C9E8EA5149FA77C514E09D355FE9E978AC80EEF9A)
- 旋转表冠翻页。 ArcSwiper在获得焦点时能够响应旋转表冠的操作，用户可以通过旋转表冠来滑动ArcSwiper，从而浏览数据。 ```typescript ArcSwiper( ) { } .focusable(true) .focusOnTouch(true) .defaultFocus(true) ``` 还可以通过设置[digitalCrownSensitivity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#digitalcrownsensitivity)属性来调整表冠对事件响应的灵敏度，以适应不同规模的数据处理。在处理大量数据时，可以提高响应事件的灵敏度；而在处理少量数据时，则可以降低灵敏度设置。 ```typescript ArcSwiper( ) { } .digitalCrownSensitivity(CrownSensitivity.MEDIUM) ```

## 设置轮播方向

ArcSwiper支持水平和垂直方向上进行轮播，主要通过[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。 ```typescript ArcSwiper() { } .indicator(true) .vertical(false) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/i-MHPYMzQ3-C8KinBurKZQ/zh-cn_image_0000002571291459.png?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=5563D5D63D1B2F71248C9534E345257443E88983B7039351F0024D31AB389110)
- 设置垂直方向轮播，导航点设为3点钟方向。 ```typescript ArcSwiper() { } .indicator(new ArcDotIndicator()  .arcDirection(ArcDirection.THREE_CLOCK_DIRECTION)) .vertical(true) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/9gxPIj77Qfq_4KL0POz6OA/zh-cn_image_0000002540771162.png?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=78333855B0A1350CE2A6CBDB84282F1910C8CC568EE0661A480208C4D42FA052)

## 自定义切换动画

ArcSwiper支持通过[customContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#customcontenttransition)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性，从而实现自定义切换动画效果。

```typescript
import { Decimal } from '@kit.ArkTS';
import {
  ArcSwiper,
  ArcSwiperAttribute,
} from '@kit.ArkUI';

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Scfey_tCSaevpIi6epTlDA/zh-cn_image_0000002571291461.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=43431F092018388FE7DA1B52A6160D70EF43A04DC27AB49109D4D826792D5390)

## 实现侧滑返回

ArcSwiper的滑动事件会与侧滑返回冲突，可以通过[onGestureRecognizerJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement#ongesturerecognizerjudgebegin)去判断ArcSwiper是否滑动到开头去拦截ArcSwiper的滑动手势，实现再次左滑返回上一页的功能。

```typescript
import {
  ArcSwiper,
  ArcSwiperAttribute,
} from '@kit.ArkUI';

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/uR0mSBblTqGF7fzkd57Y-g/zh-cn_image_0000002540611512.gif?HW-CC-KV=V1&HW-CC-Date=20260415T024827Z&HW-CC-Expire=86400&HW-CC-Sign=F889CE78ECB8FE50B902A3E103E27FEB1AB8D5B1D80FB3BCF061298554F0216B)
