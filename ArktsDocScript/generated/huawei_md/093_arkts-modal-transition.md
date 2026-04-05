# 模态转场
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-transition

模态转场是新的界面覆盖在旧的界面上，旧的界面不消失的一种转场方式。

**表1** 模态转场接口

| 接口 | 说明 | 使用场景 |
| --- | --- | --- |
| [bindContentCover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition#bindcontentcover) | 弹出全屏的模态组件。 | 用于自定义全屏的模态展示界面，结合转场动画和共享元素动画可实现复杂转场动画效果，如缩略图片点击后查看大图。 |
| [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet) | 弹出半模态组件。 | 用于半模态展示界面，如分享框。 |
| [bindMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu11) | 弹出菜单，点击组件后弹出。 | 需要Menu菜单的场景，如一般应用的“+”号键。 |
| [bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12) | 弹出菜单，长按或者右键点击后弹出。 | 长按浮起效果，一般结合拖拽框架使用，如桌面图标长按浮起。 |
| [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup) | 弹出Popup弹框。 | Popup弹框场景，如点击后对某个组件进行临时说明。 |
| [if](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse) | 通过if新增或删除组件。 | 用来在某个状态下临时显示一个界面，这种方式的返回导航需要由开发者监听接口实现。 |

## 使用bindContentCover构建全屏模态转场效果

[bindContentCover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition#bindcontentcover)接口用于为组件绑定全屏模态页面，在组件出现和消失时可通过设置转场参数ModalTransition添加过渡动效。

1. 定义全屏模态转场效果[bindContentCover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition#bindcontentcover)。
2. 定义模态展示界面。 ```typescript @Builder MyBuilder() {  Column() {  Text('my model view')  }  .transition(TransitionEffect.translate({ y: 1000 }).animation({ curve: curves.springMotion(0.6, 0.8) })) } ```
3. 通过模态接口调起模态展示界面，通过转场动画或者共享元素动画去实现对应的动画效果。 ```typescript @State isPresent: boolean = false; Button('Click to present model view')  .bindContentCover(this.isPresent, this.MyBuilder(), {  modalTransition: ModalTransition.NONE,  onDisappear: () => {  if (this.isPresent) {  this.isPresent = !this.isPresent;  }  }  })  .onClick(() => {  this.isPresent = !this.isPresent;  }) ```

完整示例代码和效果如下。

```typescript
import { curves } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

interface PersonList {
  name: string,
  cardNum: string
}

@Entry
@Component
struct BindContentCoverDemo {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private personList: Array<PersonList> = [
    { name: this.context.resourceManager.getStringByNameSync('modal_transition_text1'), cardNum: '1234***********789' },
    { name: this.context.resourceManager.getStringByNameSync('modal_transition_text2'), cardNum: '2345***********789' },
    { name: this.context.resourceManager.getStringByNameSync('modal_transition_text3'), cardNum: '3456***********789' },
    { name: this.context.resourceManager.getStringByNameSync('modal_transition_text4'), cardNum: '4567***********789' }
  ];

  @State isPresent: boolean = false;

  @Builder
  MyBuilder() {
    Column() {
      Row() {
        Text(this.context.resourceManager.getStringByNameSync('modal_transition_text5'))
          .fontSize(20)
          .fontColor(Color.White)
          .width('100%')
          .textAlign(TextAlign.Center)
          .padding({ top: 30, bottom: 15 })
      }
      .backgroundColor(0x007dfe)

      Row() {
        Text(this.context.resourceManager.getStringByNameSync('modal_transition_text6'))
          .fontSize(16)
          .fontColor(0x333333)
          .margin({ top: 10 })
          .padding({ top: 20, bottom: 20 })
          .width('92%')
          .borderRadius(10)
          .textAlign(TextAlign.Center)
          .backgroundColor(Color.White)
      }

      Column() {
        ForEach(this.personList, (item: PersonList, index: number) => {
          Row() {
            Column() {
              if (index % 2 === 0) {
                Column()
                  .width(20)
                  .height(20)
                  .border({ width: 1, color: 0x007dfe })
                  .backgroundColor(0x007dfe)
              } else {
                Column()
                  .width(20)
                  .height(20)
                  .border({ width: 1, color: 0x007dfe })
              }
            }
            .width('20%')

            Column() {
              Text(item.name)
                .fontColor(0x333333)
                .fontSize(18)
              Text(item.cardNum)
                .fontColor(0x666666)
                .fontSize(14)
            }
            .width('60%')
            .alignItems(HorizontalAlign.Start)

            Column() {
              Text(this.context.resourceManager.getStringByNameSync('modal_transition_text7'))
                .fontColor(0x007dfe)
                .fontSize(16)
            }
            .width('20%')
          }
          .padding({ top: 10, bottom: 10 })
          .border({ width: { bottom: 1 }, color: 0xf1f1f1 })
          .width('92%')
          .backgroundColor(Color.White)
        })
      }
      .padding({ top: 20, bottom: 20 })

      Text(this.context.resourceManager.getStringByNameSync('modal_transition_text8'))
        .width('90%')
        .height(40)
        .textAlign(TextAlign.Center)
        .borderRadius(10)
        .fontColor(Color.White)
        .backgroundColor(0x007dfe)
        .onClick(() => {
          this.isPresent = !this.isPresent;
        })
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor(0xf5f5f5)

    .transition(TransitionEffect.translate({ y: 1000 }).animation({ curve: curves.springMotion(0.6, 0.8) }))
  }

  build() {
    Column() {
      Row() {
        Text(this.context.resourceManager.getStringByNameSync('modal_transition_text9'))
          .fontSize(20)
          .fontColor(Color.White)
          .width('100%')
          .textAlign(TextAlign.Center)
          .padding({ top: 30, bottom: 60 })
      }
      .backgroundColor(0x007dfe)

      Column() {
        Row() {
          Column() {
            Text('00:25')
            Text(this.context.resourceManager.getStringByNameSync('modal_transition_text10'))
          }
          .width('30%')

          Column() {
            Text('G1234')
            Text(this.context.resourceManager.getStringByNameSync('modal_transition_text11'))
          }
          .width('30%')

          Column() {
            Text('08:26')
            Text(this.context.resourceManager.getStringByNameSync('modal_transition_text12'))
          }
          .width('30%')
        }
      }
      .width('92%')
      .padding(15)
      .margin({ top: -30 })
      .backgroundColor(Color.White)
      .shadow({ radius: 30, color: '#aaaaaa' })
      .borderRadius(10)

      Column() {
        Text(this.context.resourceManager.getStringByNameSync('modal_transition_text13'))
          .fontSize(18)
          .fontColor(Color.Orange)
          .fontWeight(FontWeight.Bold)
          .padding({ top: 10, bottom: 10 })
          .width('60%')
          .textAlign(TextAlign.Center)
          .borderRadius(15)

          .bindContentCover(this.isPresent, this.MyBuilder(), {
            modalTransition: ModalTransition.DEFAULT,
            onDisappear: () => {
              if (this.isPresent) {
                this.isPresent = !this.isPresent;
              }
            }
          })
          .onClick(() => {

            this.isPresent = !this.isPresent;
          })
      }
      .padding({ top: 60 })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/gBl4ey5rRhKewVmMhEKa3g/zh-cn_image_0000002566708359.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=C999ABC1B01584253694029ECE89DEEFEAF964D0DAB3587051566106569E8C92)

## 使用bindSheet构建半模态转场效果

[bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)属性可为组件绑定半模态页面，在组件出现时可通过设置自定义或默认的内置高度确定半模态大小。构建半模态转场动效的步骤基本与使用[bindContentCover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition#bindcontentcover)构建全屏模态转场动效相同。

完整示例和效果如下。

```typescript
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct BindSheetDemo {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  @State isShowSheet: boolean = false;
  private menuList: string[] = [this.context.resourceManager.getStringByNameSync('modal_transition_text14'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text15'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text16'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text17'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text18'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text19'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text20')];

  @Builder
  mySheet() {
    Column() {
      Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
        ForEach(this.menuList, (item: string) => {
          Text(item)
            .fontSize(16)
            .fontColor(0x333333)
            .backgroundColor(0xf1f1f1)
            .borderRadius(8)
            .margin(10)
            .padding(15)
        })
      }
      .padding({ top: 18 })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }

  build() {
    Column() {
      Text(this.context.resourceManager.getStringByNameSync('modal_transition_text21'))
        .fontSize(28)
        .padding({ top: 30, bottom: 30 })
      Column() {
        Row() {
          Row()
            .width(10)
            .height(10)
            .backgroundColor('#a8a8a8')
            .margin({ right: 12 })
            .borderRadius(20)

          Column() {
            Text(this.context.resourceManager.getStringByNameSync('modal_transition_text22'))
              .fontSize(16)
              .fontWeight(FontWeight.Medium)
          }
          .alignItems(HorizontalAlign.Start)

          Blank()

          Row()
            .width(12)
            .height(12)
            .margin({ right: 15 })
            .border({
              width: { top: 2, right: 2 },
              color: 0xcccccc
            })
            .rotate({ angle: 45 })
        }
        .borderRadius(15)
        .shadow({ radius: 100, color: '#ededed' })
        .width('90%')
        .alignItems(VerticalAlign.Center)
        .padding({ left: 15, top: 15, bottom: 15 })
        .backgroundColor(Color.White)

        .bindSheet(this.isShowSheet, this.mySheet(), {
          height: 300,
          dragBar: false,
          onDisappear: () => {
            this.isShowSheet = !this.isShowSheet;
          }
        })
        .onClick(() => {
          this.isShowSheet = !this.isShowSheet;
        })
      }
      .width('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xf1f1f1)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/PQetg3tBTJ6DFArNNNyFNg/zh-cn_image_0000002535788564.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=4A0DBADE0B161F6BDF4D77025806F2E82FF6C7D344859650AF28D65AF6D39DF5)

## 使用bindMenu实现菜单弹出效果

[bindMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu)为组件绑定弹出式菜单，通过点击触发。完整示例和效果如下。

```typescript
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0xF811;
const TAG = '[Sample_Animation]';

class BMD {
  public value: ResourceStr = '';
  public action: () => void = () => {
  };
}

@Entry
@Component
struct BindMenuDemo {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  @State items: BMD[] = [
    {
      value: this.context.resourceManager.getStringByNameSync('modal_transition_text23'),
      action: () => {
        hilog.info(DOMAIN, TAG, 'handle Menu1 select');
      }
    },
    {
      value: this.context.resourceManager.getStringByNameSync('modal_transition_text24'),
      action: () => {
        hilog.info(DOMAIN, TAG, 'handle Menu2 select');
      }
    },
  ]

  build() {
    Column() {
      Button('click')
        .backgroundColor(0x409eff)

        .bindMenu(this.items)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height(437)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/HAOakwLISbePTOVM0kubbA/zh-cn_image_0000002535948510.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=7BAAA297E4F4E1D56FA1D18ECC1A5764BC7AAF82EEAD6EE7B0E0174B8024E024)

## 使用bindContextMenu实现菜单弹出效果

[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu8)为组件绑定弹出式菜单，通过长按或右键点击触发。

完整示例和效果如下。

```typescript
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct BindContextMenuDemo {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private menu: string[] = [this.context.resourceManager.getStringByNameSync('modal_transition_text25'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text26'),
    this.context.resourceManager.getStringByNameSync('modal_transition_text27')];

  private pics: Resource[] = [$r('app.media.icon_1'), $r('app.media.icon_2')];

  @Builder
  myMenu() {
    Column() {
      ForEach(this.menu, (item: string) => {
        Row() {
          Text(item)
            .fontSize(18)
            .width('100%')
            .textAlign(TextAlign.Center)
        }
        .padding(15)
        .border({ width: { bottom: 1 }, color: 0xcccccc })
      })
    }
    .width(140)
    .borderRadius(15)
    .shadow({ radius: 15, color: 0xf1f1f1 })
    .backgroundColor(0xf1f1f1)
  }

  build() {
    Column() {
      Row() {
        Text(this.context.resourceManager.getStringByNameSync('modal_transition_text28'))
          .fontSize(20)
          .fontColor(Color.White)
          .width('100%')
          .textAlign(TextAlign.Center)
          .padding({ top: 20, bottom: 20 })
      }
      .backgroundColor(0x007dfe)

      Column() {
        ForEach(this.pics, (item: Resource) => {
          Row() {
            Image(item)
              .width('100%')
              .draggable(false)
          }
          .padding({
            top: 20,
            bottom: 20,
            left: 10,
            right: 10
          })
          .bindContextMenu(this.myMenu, ResponseType.LongPress)
        })
      }
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/UlE9hf87TM6W69cc7AByMw/zh-cn_image_0000002566868343.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=26A5302745369F9C9E3F72021862917BDB41689E39CD10DCF4544518F4D33CE6)

## 使用bindPopup实现气泡弹窗效果

[bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)属性可为组件绑定弹窗，并设置弹窗内容，交互逻辑和显示状态。

完整示例和代码如下。

```typescript
@Entry
@Component
struct BindPopupDemo {

  @State customPopup: boolean = false;

  @Builder
  popupBuilder() {
    Column({ space: 2 }) {
      Row().width(64)
        .height(64)
        .backgroundColor(0x409eff)
      Text('Popup')
        .fontSize(10)
        .fontColor(Color.White)
    }
    .justifyContent(FlexAlign.SpaceAround)
    .width(100)
    .height(100)
    .padding(5)
  }

  build() {
    Column() {

      Button('click')

        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .backgroundColor(0xf56c6c)

        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.Top,
          maskColor: 0x33000000,
          popupColor: 0xf56c6c,
          enableArrow: true,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height(437)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/LGg2cWODTzSqiWkv8Jw6ow/zh-cn_image_0000002566708361.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=FF98FC2C66855BE161F69F74A3F543EAC5C40638CF49E0B3A7F6781101BA1EDF)

## 使用if实现模态转场

上述模态转场接口需要绑定到其他组件上，通过监听状态变量改变调起模态界面。同时，也可以通过if范式，通过新增/删除组件实现模态转场效果。

完整示例和代码如下。

```typescript
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ModalTransitionWithIf {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  private listArr: ResourceStr[] = ['WLAN', this.context.resourceManager.getStringByNameSync('modal_transition_text29'),

    this.context.resourceManager.getStringByNameSync('modal_transition_text30'),

    this.context.resourceManager.getStringByNameSync('modal_transition_text31')];

  private shareArr: ResourceStr[] = [this.context.resourceManager.getStringByNameSync('modal_transition_text32'),

    this.context.resourceManager.getStringByNameSync('modal_transition_text33'), 'VPN',

    this.context.resourceManager.getStringByNameSync('modal_transition_text34'), 'NFC'];

  @State isShowShare: boolean = false;

  private shareFunc(): void {
    this.getUIContext()?.animateTo({ duration: 500 }, () => {
      this.isShowShare = !this.isShowShare;
    })
  }

  build() {

    Stack() {
      Column() {
        Column() {

          Text($r('app.string.modal_transition_text35'))
            .fontSize(28)
            .fontColor(0x333333)
        }
        .width('90%')
        .padding({ top: 30, bottom: 15 })
        .alignItems(HorizontalAlign.Start)

        TextInput({ placeholder: $r('app.string.modal_transition_text36') })
          .width('90%')
          .height(40)
          .margin({ bottom: 10 })
          .focusable(false)

        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.listArr, (item: string, index: number) => {
            ListItem() {
              Row() {
                Row() {
                  Text(`${item.slice(0, 1)}`)
                    .fontColor(Color.White)
                    .fontSize(14)
                    .fontWeight(FontWeight.Bold)
                }
                .width(30)
                .height(30)
                .backgroundColor('#a8a8a8')
                .margin({ right: 12 })
                .borderRadius(20)
                .justifyContent(FlexAlign.Center)

                Column() {
                  Text(item)
                    .fontSize(16)
                    .fontWeight(FontWeight.Medium)
                }
                .alignItems(HorizontalAlign.Start)

                Blank()

                Row()
                  .width(12)
                  .height(12)
                  .margin({ right: 15 })
                  .border({
                    width: { top: 2, right: 2 },
                    color: 0xcccccc
                  })
                  .rotate({ angle: 45 })
              }
              .borderRadius(15)
              .shadow({ radius: 100, color: '#ededed' })
              .width('90%')
              .alignItems(VerticalAlign.Center)
              .padding({ left: 15, top: 15, bottom: 15 })
              .backgroundColor(Color.White)
            }
            .width('100%')
            .onClick(() => {

              if (item.slice(-2) === this.context.resourceManager.getStringByNameSync('modal_transition_text37')) {
                this.shareFunc();
              }
            })
          }, (item: string): string => item)
        }
        .width('100%')
      }
      .width('100%')
      .height('100%')
      .backgroundColor(0xfefefe)

      if (this.isShowShare) {
        Column() {
          Column() {
            Row() {
              Row() {
                Row()
                  .width(16)
                  .height(16)
                  .border({
                    width: { left: 2, top: 2 },
                    color: 0x333333
                  })
                  .rotate({ angle: -45 })
              }
              .padding({ left: 15, right: 10 })
              .onClick(() => {
                this.shareFunc();
              })

              Text($r('app.string.modal_transition_text31'))
                .fontSize(28)
                .fontColor(0x333333)
            }
            .padding({ top: 30 })
          }
          .width('90%')
          .padding({ bottom: 15 })
          .alignItems(HorizontalAlign.Start)

          List({ space: 12, initialIndex: 0 }) {
            ForEach(this.shareArr, (item: string) => {
              ListItem() {
                Row() {
                  Row() {
                    Text(`${item.slice(0, 1)}`)
                      .fontColor(Color.White)
                      .fontSize(14)
                      .fontWeight(FontWeight.Bold)
                  }
                  .width(30)
                  .height(30)
                  .backgroundColor('#a8a8a8')
                  .margin({ right: 12 })
                  .borderRadius(20)
                  .justifyContent(FlexAlign.Center)

                  Column() {
                    Text(item)
                      .fontSize(16)
                      .fontWeight(FontWeight.Medium)
                  }
                  .alignItems(HorizontalAlign.Start)

                  Blank()

                  Row()
                    .width(12)
                    .height(12)
                    .margin({ right: 15 })
                    .border({
                      width: { top: 2, right: 2 },
                      color: 0xcccccc
                    })
                    .rotate({ angle: 45 })
                }
                .borderRadius(15)
                .shadow({ radius: 100, color: '#ededed' })
                .width('90%')
                .alignItems(VerticalAlign.Center)
                .padding({ left: 15, top: 15, bottom: 15 })
                .backgroundColor(Color.White)
              }
              .width('100%')
            }, (item: string): string => item)
          }
          .width('100%')
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xffffff)

        .transition(TransitionEffect.OPACITY
          .combine(TransitionEffect.translate({ x: '100%' }))
          .combine(TransitionEffect.scale({ x: 0.95, y: 0.95 })))
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/b1GHZRfZRX2jBqUN55Ya_Q/zh-cn_image_0000002535788566.gif?HW-CC-KV=V1&HW-CC-Date=20260405T024817Z&HW-CC-Expire=86400&HW-CC-Sign=9660E48D8F92A9295C74BC32CA27254CA609EDA05475309CD05F3B667C6A0E20)
