# 弹出框蒙层控制
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-mask

开发者对弹出框的定制不仅限于弹出框里的内容，对弹出框蒙层的定制需求也逐渐增加。本文介绍ArkUI弹出框的蒙层控制，包括点击蒙层时是否消失、蒙层区域、蒙层颜色和蒙层动画等特性。

## 使用约束

ArkUI提供多种弹出框，不同类型的弹出框具备不同的蒙层定制能力。详情请参阅下表：

| 接口&组件 | autoCancel | maskRect | isModal | immersiveMode |
| --- | --- | --- | --- | --- |
| [openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog) | 支持 | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 | 支持 |
| [presentCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#presentcustomdialog18) | 支持 | 支持 | 支持 | 支持 |
| [updateCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#updatecustomdialog12) | 支持 | 不支持 | 不支持 | 不支持 |
| [CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog) | 支持 | 支持 | 支持 | 支持 |
| [showDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showdialog) | 不支持 | 支持 | 支持 | 支持 |
| [showAlertDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showalertdialog) | 支持 | 支持 | 支持 | 支持 |
| [showActionSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showactionsheet) | 支持 | 支持 | 支持 | 支持 |
| [showActionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showactionmenu11) | 不支持 | 不支持 | 支持 | 支持 |
| [showDatePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showdatepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog) | 不支持 | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [showTextPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtextpickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |

> **说明**
> - 设置autoCancel参数，可控制弹出框蒙层被点击时是否消失。
> - 设置maskRect参数，可定制弹出框的蒙层的大小和位置。此外，蒙层范围内的事件无法透传，而蒙层范围外的事件可以透传。
> - 设置isModal参数，可定制弹出框的模态状态：非模态弹出框无蒙层，支持与周围组件交互；模态弹出框有蒙层，禁止与周围组件交互。
> - 从API version 15开始，当levelMode属性设置为LevelMode.EMBEDDED时，设置immersiveMode参数，可定制弹出框蒙层是否延伸至状态栏及导航栏。

| 接口&组件 | maskColor | transition | maskTransition |
| --- | --- | --- | --- |
| [openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog) | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 |
| [presentCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#presentcustomdialog18) | 支持 | 支持 | 支持 |
| [updateCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#updatecustomdialog12) | 支持 | 不支持 | 不支持 |
| [CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog) | 支持 | 不支持（可由openAnimation和closeAnimation替代） | 不支持 |
| [showDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showdialog) | 不支持 | 不支持 | 不支持 |
| [showAlertDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showalertdialog) | 不支持 | 支持 | 不支持 |
| [showActionSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showactionsheet) | 不支持 | 支持 | 不支持 |
| [showActionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#showactionmenu11) | 不支持 | 不支持 | 不支持 |
| [showDatePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showdatepickerdialog) | 不支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog) | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog) | 不支持 | 不支持 | 不支持 |
| [showTextPickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtextpickerdialog) | 不支持 | 不支持 | 不支持 |

> **说明**
> - 设置maskColor参数，可定制弹出框蒙层的颜色。
> - 设置openAnimation参数，可定制弹出框的进入动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
> - 设置closeAnimation参数，可定制弹出框的退出动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
> - 设置transition参数，可定制弹出框的进入和退出动画，同时影响蒙层动画。
> - 从API version 19开始，设置maskTransition参数，可定制弹出框的蒙层动画。

## 弹出框蒙层显隐控制

通过autoCancel和isModal属性控制弹出框的蒙层显隐。

设置autoCancel为false，取消默认点击蒙层时弹窗消失。

```typescript
  autoCancelOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    autoCancel: false,
  } as promptAction.CustomDialogOptions;

  build() {
    NavDestination() {
      Column() {
        Button('openCustomDialog autoCancel:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt)
          })

      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/I9d0wBkARdCBAZbGGl-Qgg/zh-cn_image_0000002532906030.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=821D927FF1D355AED2D0C5541925A0156AAD7681C3AB54C215E16556E9C81CCA)

设置isModal为false，将默认的模态弹出框变为非模态弹出框。

```typescript
  modalOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    isModal: false,
  } as promptAction.CustomDialogOptions;

  build() {
    NavDestination() {
      Column() {

        Button('openCustomDialog isModal:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt)
          })

      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Hl8Ns8rMTtquyIYM37MBhg/zh-cn_image_0000002533065978.png?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=CC2057B1AFA630BA3435A87E5FE3A07C11295B243EE311962B929BCB6D900D35)

## 弹出框蒙层样式控制

该示例通过maskRect、immersiveMode和maskColor展示弹出框在蒙层样式控制方面的能力。

设置maskRect和maskColor，实现蒙层区域和蒙层颜色的设置。

```typescript
  maskOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    maskRect: {
      x: 0,
      y: 10,
      width: '100%',
      height: '90%'
    },
    maskColor: '#33AA0000'
  } as promptAction.CustomDialogOptions;

  build() {
    NavDestination() {
      Column() {

        Button('openCustomDialog maskOpt')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt)
          })

      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/3_esEEiaRZeNUb_3_hNZcg/zh-cn_image_0000002563865881.png?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=14C2929C424F34109428A8EE8FFCA1C681F2912D8194CAFD2B981095496CFE03)

在levelMode为LevelMode.EMBEDDED下，展示不同immersiveMode对蒙层在导航栏和状态栏的延伸效果。

```typescript
  @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;

  build() {
    NavDestination() {
      Column() {

        Button('openCustomDialog immersiveMode')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.immersiveMode =
              this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              levelMode: LevelMode.EMBEDDED,
              immersiveMode: this.immersiveMode,
            })
          })

      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ls561bkSQ8GxiW39OD0yvA/zh-cn_image_0000002563785927.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=E18049455D8276D4894440265D4C9BE5A7EE6EEADFE497D6165BAA68F4C861C4)

## 弹出框蒙层动画控制

该示例通过transition和maskTransition分别展示弹出框在蒙层动画方面的能力。

设置transition，实现弹出框与蒙层整体的动画。

```typescript
  transitionOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
  } as promptAction.CustomDialogOptions;

  build() {
    NavDestination() {
      Column() {

        Button('openCustomDialog transition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
          })

      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/j3i7voznT5i7joJRt4yqYw/zh-cn_image_0000002532906032.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=8BAF7A2E962B7294D0EEC5B467F40DBDFE03DD99EA8C462B4802B95EBDC5B888)

设置maskTransition，实现弹出框中蒙层单独的动画定制能力。

```typescript
Button('openCustomDialog maskTransition')
  .width('100%')
  .margin({ top: 10 })
  .onClick(() => {
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.myBuilder();
      },
      maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
        .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
    });
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qZY1gkz8SBCI9aDNA09yDw/zh-cn_image_0000002533065980.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=15547AD562D5A3B9172C6B0445ADA29848764345CCB2FCDE2641E661D3A48FAA)

[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog)虽然不支持transition接口，但与之对应的openAnimation和closeAnimation接口在动画的打开和关闭时可进行定制，示例代码如下：

```typescript
@CustomDialog
@Component
struct CustomDialogAnimationBuilder {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('title')
        .margin(10)
        .fontSize(20)
      Button('button1')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.controller?.close();
        })
      Button('button2')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.controller?.close();
        })
    }.width('100%')
    .height('50%')
  }
}

@Entry
@Component
export struct CustomDialogAnimation {
  animationController: CustomDialogController | null =
    new CustomDialogController({
      builder: CustomDialogAnimationBuilder(),
      closeAnimation: { duration: 2000 },
      openAnimation: { duration: 2000 }
    });

  aboutToDisappear(): void {
    this.animationController = null;
  }

  build() {
    NavDestination() {
      Column() {
        Button('CustomDialogController animate')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.animationController?.open();
          })
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/uBRX9lp7Q86mGUJ4e13V5Q/zh-cn_image_0000002563865883.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=36C9153873F758806FFA8B039A896310AFD87A191B43B206DD6D2305C4D323B6)

## 完整示例

```typescript
import { ImmersiveMode, LevelMode, promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct CustomDialogControl {
  @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;

  autoCancelOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    autoCancel: false,
  } as promptAction.CustomDialogOptions;

  modalOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    isModal: false,
  } as promptAction.CustomDialogOptions;

  maskOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    maskRect: {
      x: 0,
      y: 10,
      width: '100%',
      height: '90%'
    },
    maskColor: '#33AA0000'
  } as promptAction.CustomDialogOptions;

  transitionOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
  } as promptAction.CustomDialogOptions;

  @Builder
  myBuilder() {
    Column() {
      Text('title').margin(10).fontSize(20)
      Button('button1').margin(10).fontSize(20)
      Button('button2').margin(10).fontSize(20)
    }.width('100%').height('50%')
  }

  build() {
    NavDestination() {
      Column() {
        Button('openCustomDialog autoCancel:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt)
          })

        Button('openCustomDialog isModal:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt)
          })

        Button('openCustomDialog maskOpt')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt)
          })

        Button('openCustomDialog transition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
          })

        Button('openCustomDialog immersiveMode')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.immersiveMode =
              this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              levelMode: LevelMode.EMBEDDED,
              immersiveMode: this.immersiveMode,
            })
          })

        Button('openCustomDialog maskTransition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
                .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
            });
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ZVjRC0NjQDO6Q23VoOGhmw/zh-cn_image_0000002563785929.gif?HW-CC-KV=V1&HW-CC-Date=20260330T024810Z&HW-CC-Expire=86400&HW-CC-Sign=53BFB20FFBFF0B63FB8EF16B2DCF5B20AEE3E537FFBA2D64D6EFAFE5C40FE3F8)
