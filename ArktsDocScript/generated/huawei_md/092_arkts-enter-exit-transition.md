# 出现/消失转场
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-enter-exit-transition

[transition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component#transitioneffect10对象说明)的组合使用，定义出各式效果。

**表1** 转场效果接口

| 转场效果 | 说明 | 动画 |
| --- | --- | --- |
| IDENTITY | 禁用转场效果。 | 无。 |
| OPACITY | 默认的转场效果，透明度转场。 | 出现时透明度从0到1，消失时透明度从1到0。 |
| SLIDE | 滑动转场效果。 | 出现时从窗口左侧滑入，消失时从窗口右侧滑出。 |
| translate | 通过设置组件平移创建转场效果。 | 出现时，平移参数的值从translate接口设置的值变化为默认值0，消失时从默认值0变化为translate接口设置的值。 |
| rotate | 通过设置组件旋转创建转场效果。 | 出现时，旋转参数的值从rotate接口设置的值变化为默认值0，消失时从默认值0变化为rotate接口设置的值。 |
| opacity | 通过设置透明度参数创建转场效果。 | 出现时，透明度参数的值从opacity设置的值变化为透明度默认值1，消失时从透明度默认值1变化为opacity设置的值。 |
| move | 通过[TransitionEdge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component#transitionedge10)创建从窗口哪条边缘出来的效果。 | 出现时从TransitionEdge方向滑入，消失时滑出到TransitionEdge方向。 |
| asymmetric | 通过此方法组合非对称的出现消失转场效果。 - appear：出现转场的效果。 - disappear：消失转场的效果。 | 出现时采用appear设置的TransitionEffect出现效果，消失时采用disappear设置的[TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component#transitioneffect10对象说明)消失效果。 |
| combine | 组合其他TransitionEffect。 | 组合其他TransitionEffect，一起生效。 |
| animation | 定义转场效果的动画参数： - 如果不定义会跟随[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)的动画参数。 - 不支持通过控件的animation接口配置动画参数。 - TransitionEffect中animation的onFinish不生效。 | 调用顺序是从上往下，上面TransitionEffect的animation也会作用到下面TransitionEffect。 |

1. 创建TransitionEffect。 ```typescript private effect: object =  TransitionEffect.OPACITY  .combine(TransitionEffect.scale({ x: 0, y: 0 }).animation({ curve: curves.springMotion(0.6, 1.2) }))  .combine(TransitionEffect.rotate({ angle: 90 }))  .combine(TransitionEffect.translate({ x: 150, y: 150 }))  .combine(TransitionEffect.move(TransitionEdge.END)).animation({curve: curves.springMotion()})  .combine(TransitionEffect.asymmetric(TransitionEffect.scale({  x: 0,  y: 0  }), TransitionEffect.rotate({ angle: 90 }))); ```
2. 将转场效果通过[transition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)接口设置到组件。 ```typescript Text('test')  .transition(this.effect) ```
3. 新增或者删除组件触发转场。 ```typescript @State isPresent: boolean = true; if (this.isPresent) {  Text('test')  .transition(this.effect) } this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {  this.isPresent = false; }) this.isPresent = false; ```

完整的示例代码和效果如下，示例中采用直接删除或新增组件的方式触发转场，也可以替换为在[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)闭包内改变控制变量触发转场。

```typescript
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct TransitionEffectDemo {
  @State isPresent: boolean = false;

  private effect: TransitionEffect =

    TransitionEffect.OPACITY.animation({
      curve: curves.springMotion(0.6, 0.8)
    })
      .combine(TransitionEffect.scale({
        x: 0,
        y: 0
      }))
      .combine(TransitionEffect.rotate({ angle: 90 }))
      .combine(TransitionEffect.translate({ y: 150 })
        .animation({ curve: curves.springMotion() }))
      .combine(TransitionEffect.move(TransitionEdge.END));

  build() {
    Stack() {
      if (this.isPresent) {
        Column() {
          Text('ArkUI')
            .fontWeight(FontWeight.Bold)
            .fontSize(20)
            .fontColor(Color.White)
        }
        .justifyContent(FlexAlign.Center)
        .width(150)
        .height(150)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)

        .transition(this.effect)
      }

      Column()
        .width(155)
        .height(155)
        .border({
          width: 5,
          radius: 10,
          color: Color.Black
        })

      Button('Click')
        .margin({ top: 320 })
        .onClick(() => {
          this.isPresent = !this.isPresent;
        })
    }
    .width('100%')
    .height('60%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/UFKqGrPyT4qZgqgFSoatww/zh-cn_image_0000002563865951.gif?HW-CC-KV=V1&HW-CC-Date=20260328T141016Z&HW-CC-Expire=86400&HW-CC-Sign=F151A96E0FBEB6B90028AB5ADC3DFF0784D17F9EDEB11ADF186DAA8010B096E0)

对多个组件添加转场效果时，可以在[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty#animation)动画参数中配置不同的delay值，实现组件渐次出现消失的效果：

```typescript
const ITEM_COUNTS = 9;
const ITEM_COLOR = '#ED6F21';
const INTERVAL = 30;
const DURATION = 300;

@Entry
@Component
struct Index1 {
  @State isGridShow: boolean = false;
  private dataArray: number[] = new Array(ITEM_COUNTS);

  aboutToAppear(): void {
    for (let i = 0; i < ITEM_COUNTS; i++) {
      this.dataArray[i] = i;
    }
  }

  build() {
    Stack() {
      if (this.isGridShow) {
        Grid() {
          ForEach(this.dataArray, (item: number, index: number) => {
            GridItem() {
              Stack() {
                Text((item + 1).toString())
              }
              .size({ width: 50, height: 50 })
              .backgroundColor(ITEM_COLOR)
              .transition(TransitionEffect.OPACITY
                .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }))
                .animation({ duration: DURATION, curve: Curve.Friction, delay: INTERVAL * index }))
              .borderRadius(10)
            }

            .transition(TransitionEffect.opacity(0.99))
          }, (item: number) => item.toString())
        }
        .columnsTemplate('1fr 1fr 1fr')
        .rowsGap(15)
        .columnsGap(15)
        .size({ width: 180, height: 180 })

        .transition(TransitionEffect.opacity(0.99))
      }
    }
    .size({ width: '100%', height: '100%' })
    .onClick(() => {
      this.getUIContext()?.animateTo({
        duration: DURATION + INTERVAL * (ITEM_COUNTS - 1),
        curve: Curve.Friction
      }, () => {
        this.isGridShow = !this.isGridShow;
      })
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/CFYHotRiSVSANl5DbyQfTg/zh-cn_image_0000002563785997.gif?HW-CC-KV=V1&HW-CC-Date=20260328T141016Z&HW-CC-Expire=86400&HW-CC-Sign=B3CEE06413CB13DBAD01EB03DF1CBAB3E8F0F69ED429ABB75965B0F7259C4F60)
