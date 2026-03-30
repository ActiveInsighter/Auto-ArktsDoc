# 实现属性动画
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-animation-apis

通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供三种动画接口[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)、[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)和[keyframeAnimateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。

> **说明**
> 本章节讨论的属性动画不是狭义的[属性动画接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)，而是通过给定新的可动画属性终值，对属性产生动画的方式。

| 动画接口 | 作用域 | 原理 | 使用场景 |
| --- | --- | --- | --- |
| animateTo | 闭包内改变属性引起的界面变化。 | 通用函数，对闭包前界面和闭包中的状态变量引起的界面之间的差异做动画。 支持多次调用，支持嵌套。 | 适用对多个可动画属性配置相同动画参数的动画。 需要嵌套使用动画的场景。 如果需要实现多段动画循环的效果，建议通过设置[AnimateParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation#animateparam对象说明)的playMode和iterations属性实现，或使用keyframeAnimateTo实现。 |
| animation | 组件通过属性接口绑定的属性变化引起的界面变化。 | 识别组件的可动画属性变化，自动添加动画。 组件的接口调用是从下往上执行，animation只会作用于在其之上的属性调用。 组件可以根据调用顺序对多个属性设置不同的animation。 | 适用于对多个可动画属性配置不同参数动画的场景。 |
| keyframeAnimateTo | 多个闭包内改变属性引起的分段属性动画。 | 通用函数，每一段闭包中的状态变量与前一次的差异做动画。 支持多次调用，不推荐嵌套。 | 适用于同一属性需要做连续多个动画的场景。 |

## 使用animateTo产生属性动画

```typescript
animateTo(value: AnimateParam, event: () => void): void
```

[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)接口参数中，value指定[AnimateParam对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation#animateparam对象说明)（包括时长、曲线等）event为动画的闭包函数，闭包内变量改变产生的属性动画将遵循相同的动画参数。

> **说明**
> 直接使用animateTo可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface)的问题，建议使用[getUIContext()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api#getuicontext)获取[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)实例，并使用[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)调用绑定实例的animateTo。

```typescript
import { curves } from '@kit.ArkUI';
@Entry
@Component
struct attrAnimateToDemo2 {
  @State animate: boolean = false;

  @State rotateValue: number = 0;
  @State translateX: number = 0;
  @State opacityValue: number = 1;

  build() {
    Row() {

      Column() {
      }
      .rotate({ angle: this.rotateValue })
      .backgroundColor('#317AF7')
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .borderRadius(30)
      .onClick(() => {
        this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
          this.animate = !this.animate;

          this.rotateValue = this.animate ? 90 : 0;

          this.opacityValue = this.animate ? 0.6 : 1;

          this.translateX = this.animate ? 50 : 0;
        })
      })

      Column() {
      }
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .backgroundColor('#D94838')
      .borderRadius(30)
      .opacity(this.opacityValue)
      .translate({ x: this.translateX })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/uml-rix_Tk-2tEaMlbNc5w/zh-cn_image_0000002565290391.gif?HW-CC-KV=V1&HW-CC-Date=20260330T121619Z&HW-CC-Expire=86400&HW-CC-Sign=5196D1C536168555A411796BEDB0F1A992A17D2714B2FE67795CD7C24456D4AE)

## 使用animation产生属性动画

相比于animateTo接口需要将属性修改封装在闭包中执行，[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)接口无需使用闭包，只需将其加在要做动画的可动画属性后即可。animation只要检测到其绑定的可动画属性发生变化，就会自动添加属性动画，animateTo则必须在动画闭包内改变可动画属性的值从而生成动画。

```typescript
import { curves } from '@kit.ArkUI';
@Entry
@Component
struct attrAnimationDemo3 {
  @State animate: boolean = false;

  @State rotateValue: number = 0;
  @State translateX: number = 0;
  @State opacityValue: number = 1;

  build() {
    Row() {

      Column() {
      }
      .opacity(this.opacityValue)
      .rotate({ angle: this.rotateValue })

      .animation({ curve: curves.springMotion() })
      .backgroundColor('#317AF7')
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .borderRadius(30)
      .onClick(() => {
        this.animate = !this.animate;

        this.rotateValue = this.animate ? 90 : 0;

        this.translateX = this.animate ? 50 : 0;

        this.opacityValue = this.animate ? 0.6 : 1;
      })

      Column() {
      }
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .backgroundColor('#D94838')
      .borderRadius(30)
      .opacity(this.opacityValue)
      .translate({ x: this.translateX })
      .animation({ curve: curves.springMotion() })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/IlStXeKLTa6eUCoRF9F-6A/zh-cn_image_0000002565210371.gif?HW-CC-KV=V1&HW-CC-Date=20260330T121619Z&HW-CC-Expire=86400&HW-CC-Sign=2E42A3ED7DFC1821F79054A437A92210E3F923F9C198F92E8BAFB31F7B3F2326)

## 使用keyframeAnimateTo产生属性动画

```typescript
keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void
```

[keyframeAnimateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto)接口参数中，第一个参数[KeyframeAnimateParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto#keyframeanimateparam对象说明)为关键帧动画的整体参数（包括延时、播放次数、结束回调、期望帧率），第二个参数是一个数组，每一项表示一个关键帧内的动画行为；每一段动画可单独控制动画参数（包括时长、曲线等）。

在同一属性存在多段动画过程的场景，可通过在结束回调中再创建新动画实现，但写法更复杂，且每次创建新动画需要耗时，会有衔接卡顿现象。此场景更适宜用关键帧动画实现。

以下示例主要演示如何通过keyframeAnimateTo来设置关键帧动画。

```typescript
@Entry
@Component
struct KeyframeAnimateToDemo {

  @State rotateValue: number = 0;
  @State translateX: number = 0;
  @State opacityValue: number = 1;

  build() {
    Row() {

      Column() {
      }
      .rotate({ angle: this.rotateValue })
      .backgroundColor('#317AF7')
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .borderRadius(30)
      .onClick(() => {

        this.getUIContext()?.keyframeAnimateTo({
          iterations: 1
        }, [
          {

            duration: 800,
            event: () => {
              this.rotateValue = 90;
              this.opacityValue = 0.6;
              this.translateX = 50;
            }
          },
          {

            duration: 500,
            event: () => {
              this.rotateValue = 0;
              this.opacityValue = 1;
              this.translateX = 0;
            }
          }
        ]);
      })

      Column() {
      }
      .justifyContent(FlexAlign.Center)
      .width(100)
      .height(100)
      .backgroundColor('#D94838')
      .borderRadius(30)
      .opacity(this.opacityValue)
      .translate({ x: this.translateX })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/E0ma2_I3QSehs9MGwUfVhw/zh-cn_image_0000002534250548.gif?HW-CC-KV=V1&HW-CC-Date=20260330T121619Z&HW-CC-Expire=86400&HW-CC-Sign=AE3B2A0432CDB5D6832104F8247CB9F5F88A75069A753E865E61F005BD6AA394)

> **说明**
> - 在对组件位置大小变化做动画的时候，由于布局属性的改变会触发测量布局，性能开销大。而[scale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#scale)属性的改变不会触发测量布局，性能开销小。因此，在组件位置大小持续发生变化的场景，如跟手触发组件大小变化的场景，推荐使用scale。
> - 属性动画应该作用于始终存在的组件，对于将要出现或者将要消失的组件的动画应该使用[转场动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-transition-overview)。
> - 尽量不要使用动画结束回调。属性动画是对已经发生的状态进行的动画，不需要开发者去处理结束的逻辑。如果要使用结束回调，一定要正确处理连续操作的数据管理。
> - 在设置的开发者选项中关闭过渡动画，或UIAbility从前台切换至后台，会立即执行动画结束回调。建议对此类场景进行一定的验证并避免在动画结束回调中加入时序相关的功能逻辑。
