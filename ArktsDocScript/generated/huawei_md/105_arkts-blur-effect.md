# 模糊
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-blur-effect

动画效果可以丰富界面的细节，提升UI界面的真实感和品质感。例如，模糊和阴影效果可以让物体看起来更加立体，使得动画更加生动。ArkUI提供了丰富的效果接口，开发者可快速打造出精致、个性化的效果。本章主要介绍常用的模糊、阴影和色彩效果等接口。

模糊效果可以体现界面空间的纵深感，区分前后元素的层级关系。

| 接口 | 说明 |
| --- | --- |
| [backdropBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backdropblur) | 为当前组件添加背景模糊效果，入参为模糊半径。 |
| [blur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#blur) | 为当前组件添加内容模糊效果，入参为模糊半径。 |
| [backgroundBlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundblurstyle9) | 为当前组件添加背景模糊效果，入参为模糊样式。 |
| [foregroundBlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-blur-style#foregroundblurstyle) | 为当前组件添加内容模糊效果，入参为模糊样式。 |
| [motionBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-motionblur#motionblur) | 为当前组件添加由缩放大小或位移变化引起的运动过程中的动态模糊效果，入参为模糊半径和锚点坐标。 |

> **说明**
> 以上接口均为实时模糊接口，每帧执行实时渲染，性能负载较大。当模糊内容与模糊半径均无需变动时，推荐采用静态模糊接口[blur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-effectkit#blur)。最佳实践请参考：[图像模糊动效优化-使用场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519)。

## 使用backdropBlur为组件添加背景模糊

```typescript
@Entry
@Component
struct BlurEffectsExample {
  build() {
    Column({ space: 10 }) {
      Text('backdropBlur')
        .width('90%')
        .height('90%')
        .fontSize(20)
        .fontColor(Color.White)
        .textAlign(TextAlign.Center)
        .backdropBlur(10)

        .backgroundImage($r('app.media.bg'))
        .backgroundImageSize({ width: 400, height: 300 })
    }
    .width('100%')
    .height('50%')
    .margin({ top: 20 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/NaIh-bYIRx2R5N2YOkGRRQ/zh-cn_image_0000002569168611.png?HW-CC-KV=V1&HW-CC-Date=20260411T023454Z&HW-CC-Expire=86400&HW-CC-Sign=AB9B0190377AC7DABE3AE81F52AFC79C562A2DB8894366A70DB622C3F07ECDA5)

## 使用blur为组件添加内容模糊

```typescript
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State radius: number = 0;
  @State text: string = '';
  @State y: Resource | string = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text1').id);

  aboutToAppear() {

    this.text = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text2').id) +
    "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text3').id) + this.y +
      "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text4').id) + this.radius;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
      Text(this.text)
        .height(200)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .fontFamily("cursive")
        .fontStyle(FontStyle.Italic)

      Image($r("app.media.bg"))
        .blur(this.radius)
        .height('100%')
        .width("100%")
        .objectFit(ImageFit.Cover)
    }.height('100%')
    .width("100%")
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type === TouchType.Move) {
          this.y = Number(event.touches[0].y.toString()).toString();
          this.radius = Number(this.y) / 10;
        }
        if (event.type === TouchType.Up) {
          this.radius = 0;

          this.y = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text1').id);
        }
      }

      this.text = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text2').id) + "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text3').id) + this.y +
        "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text4').id) + this.radius;
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/MUwS85cNSbaAIfT_IYtOeA/zh-cn_image_0000002569128637.gif?HW-CC-KV=V1&HW-CC-Date=20260411T023454Z&HW-CC-Expire=86400&HW-CC-Sign=32497C111501ACBCF610114ACED56B9843E58B133F1285889BFF61CD9898E945)

## 使用backgroundBlurStyle为组件添加背景模糊效果

```typescript
@Entry
@Component
struct BackDropBlurStyleDemo {
  build() {
    Grid() {
      GridItem() {
        Column() {
          Column() {

            Text($r('app.string.originalImage'))
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))

          Text($r('app.string.originalImage'))
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .margin({ top: 20 })
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Thin')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))

          .backgroundBlurStyle(BlurStyle.Thin, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Thin')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .margin({ top: 20 })
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Regular')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.Regular, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Regular')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Thick')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.Thick, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Thick')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_THIN')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.BACKGROUND_THIN, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_THIN')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_REGULAR')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.BACKGROUND_REGULAR, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_REGULAR')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_THICK')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.BACKGROUND_THICK, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_THICK')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_ULTRA_THICK')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .backgroundBlurStyle(BlurStyle.BACKGROUND_ULTRA_THICK, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_ULTRA_THICK')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)
    }
    .columnsTemplate('1fr 1fr')
    .rowsTemplate('1fr 1fr 1fr 1fr')
    .width('100%')
    .height('100%')
    .margin({ top: 40 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Hbto031MT4Of3Uu1lovQrA/zh-cn_image_0000002538128916.png?HW-CC-KV=V1&HW-CC-Date=20260411T023454Z&HW-CC-Expire=86400&HW-CC-Sign=C99E32236EBE63C2B8F821F24A1A7ADC8F63A47CCEA7852156B1A05B7B7D2E28)

## 使用foregroundBlurStyle为组件添加内容模糊效果

```typescript
@Entry
@Component
struct ForegroundBlurStyleDemo {
  build() {
    Grid() {
      GridItem() {
        Column() {
          Column() {

            Text($r('app.string.originalImage'))
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))

          Text($r('app.string.originalImage'))
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Thin')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))

          .foregroundBlurStyle(BlurStyle.Thin, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Thin')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Regular')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.Regular, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Regular')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('Thick')
              .fontSize(20)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.Thick, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('Thick')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_THIN')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.BACKGROUND_THIN, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_THIN')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_REGULAR')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.BACKGROUND_REGULAR, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_REGULAR')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_THICK')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.BACKGROUND_THICK, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_THICK')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)

      GridItem() {
        Column() {
          Column() {
            Text('BACKGROUND_ULTRA_THICK')
              .fontSize(12)
              .fontColor(Color.White)
              .textAlign(TextAlign.Center)
              .width('100%')
              .height('100%')
          }
          .height(100)
          .aspectRatio(1)
          .borderRadius(10)

          .backgroundImage($r('app.media.bg'))
          .foregroundBlurStyle(BlurStyle.BACKGROUND_ULTRA_THICK, {
            colorMode: ThemeColorMode.LIGHT,
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.1
          })

          Text('BACKGROUND_ULTRA_THICK')
            .fontSize(12)
            .fontColor(Color.Black)
        }
        .height('100%')
        .justifyContent(FlexAlign.Start)
      }
      .width(200)
      .height(200)
    }
    .columnsTemplate('1fr 1fr')
    .rowsTemplate('1fr 1fr 1fr 1fr')
    .width('100%')
    .height('100%')
    .margin({ top: 40 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/3SpYFtVLQ4iJQI9JOEH70g/zh-cn_image_0000002538288850.png?HW-CC-KV=V1&HW-CC-Date=20260411T023454Z&HW-CC-Expire=86400&HW-CC-Sign=C18533F23D78D195BD0BC5C91EBD0B7E02B2F9ED3C97716656D41BA311A15BB1)

## 使用motionBlur为组件添加运动模糊效果

```typescript
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct motionBlurTest {
  @State widthSize: number = 300;
  @State heightSize: number = 240;
  @State flag: boolean = true;
  @State radius: number = 0;
  @State x: number = 0.5;
  @State y: number = 0.5;

  build() {
    Column() {
      Column() {

        Image($r('app.media.testImg'))
          .width(this.widthSize)
          .height(this.heightSize)
          .scale({ x: this.flag ? 1 : 0.8,y: this.flag ? 1 : 0.8 ,centerX: '50%', centerY: '50%' })
          .onClick(() => {
            this.radius = 50;
            this.x = 0.5;
            this.y = 0.5;
            this.flag = !this.flag;
          })
          .animation({
            duration: 2000,
            iterations: 1,
            playMode: PlayMode.Alternate,
            onFinish: () => {
              this.radius = 0;
            }
          })
          .motionBlur({ radius: this.radius, anchor: { x: this.x, y: this.y } })
      }
    }.width('100%').margin({ top: 50 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/twwy4RdJSkuHG6H_KPcMaA/zh-cn_image_0000002569168613.gif?HW-CC-KV=V1&HW-CC-Date=20260411T023454Z&HW-CC-Expire=86400&HW-CC-Sign=355A266099B7FE407F61E2BF89A9D58BDF56061685E0D0245FF0006317A92AC3)
