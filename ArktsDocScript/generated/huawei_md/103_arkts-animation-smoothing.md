# 动画衔接
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-smoothing

UI界面除了运行动画之外，还承载着与用户进行实时交互的功能。当用户行为根据意图变化发生改变时，UI界面应做到即时响应。例如用户在应用启动过程中，上滑退出，那么启动动画应该立即过渡到退出动画，而不应该等启动动画完成后再退出，从而减少用户等待时间。对于桌面翻页类从跟手到离手触发动画的场景，离手后动画的初始速度应继承手势速度，避免由于速度不连续导致停顿感的产生。针对以上场景，系统已提供动画与动画、手势与动画之间的衔接能力，保证各类场景下动画平稳光滑地过渡的同时，尽可能降低开发难度。

假设对于某一可动画属性，存在正在运行的动画。当UI侧行为改变该属性终点值时，开发者仅需在[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)动画闭包中改变属性值或者改变[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)接口作用的属性值，即可产生动画。系统会自动衔接之前的动画和当前的动画，开发者仅需要关注当前单次动画的实现。

示例如下。通过点击Click，红色方块的缩放属性会发生变化。当连续快速点击Click时，缩放属性的终点值连续发生变化，当前动画也会平滑过渡到朝着新的缩放属性终点值运动。

```typescript
import { curves } from '@kit.ArkUI';

class SetAnimationVariables {
  isAnimation: boolean = true

  set(): void {
    this.isAnimation = !this.isAnimation;
  }
}

@Entry
@Component
struct AnimationToAnimationDemo {

  @State animationController: SetAnimationVariables = new SetAnimationVariables();

  build() {
    Column() {
      Text('ArkUI')
        .fontWeight(FontWeight.Bold)
        .fontSize(12)
        .fontColor(Color.White)
        .textAlign(TextAlign.Center)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)
        .width(100)
        .height(100)
        .scale({

          x: this.animationController.isAnimation ? 2 : 1,
          y: this.animationController.isAnimation ? 2 : 1
        })
        .animation({ curve: curves.springMotion(0.4, 0.8) })

      Button('Click')
        .margin({ top: 200 })
        .onClick(() => {

          this.animationController.set()
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/-i4k84xvSV-bzSfIa0Qx7w/zh-cn_image_0000002538128914.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025408Z&HW-CC-Expire=86400&HW-CC-Sign=6665B3416BA11819ADA4E4B6737A45E4058990FE4FABD97DF9F6ECEC409C9C8E)

## 手势与动画的衔接

使用滑动、捏合、旋转等手势的场景中，跟手过程中一般会触发属性的改变。离手后，这部分属性往往会继续发生变化，直到到达属性终点值。

离手阶段的属性变化初始速度应与离手前一刻的属性改变速度保持一致。如果离手后属性变化速度从0开始，就好像正在运行的汽车紧急刹车，造成观感上的骤变是用户和开发者都不希望看到的。

针对在[TapGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture)和[动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation)之间进行衔接的场景（如列表滑动），可以在跟手阶段每一次更改组件属性时，都使用跟手弹簧曲线的属性动画。离手时再用离手弹簧曲线产生离手阶段的属性动画。对于采用[springMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curvesspringmotion9)曲线的动画，离手阶段动画将自动继承跟手阶段动画的速度，并以跟手动画当前位置为起点，运动到指定的属性终点。

示例代码如下，小球跟手运动。

```typescript
import { curves } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG: string = '[AnimatorTest]';

@Entry
@Component
struct SpringMotionDemo {

  @State positionX: number = 100;
  @State positionY: number = 100;
  diameter: number = 50;

  build() {
    Column() {
      Row() {
        Circle({ width: this.diameter, height: this.diameter })
          .fill(Color.Blue)
          .position({ x: this.positionX, y: this.positionY })
          .onTouch((event?: TouchEvent) => {

            if (event) {
              if (event.type === TouchType.Move) {

                this.getUIContext()?.animateTo({ curve: curves.responsiveSpringMotion() }, () => {

                  this.positionX = event.touches[0].windowX - this.diameter / 2;
                  this.positionY = event.touches[0].windowY - this.diameter / 2;
                  hilog.info(DOMAIN, TAG, `move, animateTo x:${this.positionX}, y:${this.positionY}`);
                })
              } else if (event.type === TouchType.Up) {

                this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                  this.positionX = 100;
                  this.positionY = 100;
                  hilog.info(DOMAIN, TAG, `touchUp, animateTo x:100, y:100`);
                })
              }
            }
          })
      }
      .width('100%').height('80%')
      .clip(true)
      .backgroundColor(Color.Orange)

      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Center }) {

        Text($r('app.string.drag')).fontSize(16)
      }
      .width('100%')

      Row() {

        Text($r('app.string.location') + ' [x: ' + Math.round(this.positionX) + ', y:' + Math.round(this.positionY) + ']').fontSize(16)
      }
      .padding(10)
      .width('100%')
    }.height('100%').width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/aMe9RJnLTXSsYk9XmFhb_w/zh-cn_image_0000002538288848.gif?HW-CC-KV=V1&HW-CC-Date=20260412T025408Z&HW-CC-Expire=86400&HW-CC-Sign=3024EFA7D8C791506957B16D8E13D6AD81696806B7A590B9BD37F6E608973EFE)
