# 色彩
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-color-effect

## 色彩

通过颜色渐变接口，可以设置组件的背景颜色渐变效果，实现在两个或多个指定的颜色之间进行平稳的过渡。

| 接口 | 说明 |
| --- | --- |
| [linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color#lineargradient) | 为当前组件添加线性渐变的颜色渐变效果。 |
| [sweepGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color#sweepgradient) | 为当前组件添加角度渐变的颜色渐变效果。 |
| [radialGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color#radialgradient) | 为当前组件添加径向渐变的颜色渐变效果。 |

## 为组件添加线性渐变效果

```typescript
@Entry
@Component
struct LinearGradientDemo {
  build() {
    Grid() {
      GridItem() {
        Column() {
          Text('angle: 180')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .linearGradient({

          colors: [
            [0xf56c6c, 0.0],
            [0xffffff, 1.0],
          ]
        })
      }

      GridItem() {
        Column() {
          Text('angle: 45')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .linearGradient({
          angle: 45,
          colors: [
            [0xf56c6c, 0.0],
            [0xffffff, 1.0],
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: true')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .linearGradient({
          repeating: true,
          colors: [
            [0xf56c6c, 0.0],
            [0xE6A23C, 0.3],
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: false')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .linearGradient({
          colors: [
            [0xf56c6c, 0.0],
            [0xE6A23C, 0.3],
          ]
        })
      }
    }
    .columnsGap(10)
    .rowsGap(10)
    .columnsTemplate('1fr 1fr')
    .rowsTemplate('1fr 1fr 1fr')
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/PqnAhLG-RwqlwT--t5YFiA/zh-cn_image_0000002532906120.png?HW-CC-KV=V1&HW-CC-Date=20260330T024846Z&HW-CC-Expire=86400&HW-CC-Sign=10758BB89291ACAA646650953700E2984E8A367A497C9A999E54CBFF8FBD9C33)

## 为组件添加角度渐变效果

```typescript
@Entry
@Component
struct SweepGradientDemo {
  build() {
    Grid() {
      GridItem() {
        Column() {
          Text('center: 50')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 360,
          repeating: true,
          colors: [

            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('center: 0')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .sweepGradient({
          center: [0, 0],
          start: 0,
          end: 360,
          repeating: true,
          colors: [

            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: true')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 360,
          repeating: true,
          colors: [
            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: false')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 360,
          repeating: false,
          colors: [
            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }
    }
    .columnsGap(10)
    .rowsGap(10)
    .columnsTemplate('1fr 1fr')
    .rowsTemplate('1fr 1fr 1fr')
    .width('100%')
    .height(437)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/f9Wmaxw-TzqhKrcSYXiUSw/zh-cn_image_0000002533066068.png?HW-CC-KV=V1&HW-CC-Date=20260330T024846Z&HW-CC-Expire=86400&HW-CC-Sign=DF850D739DC5E3F1520D59CC6F63AF6EE76D886132B6F6B2D2C3B0ADB3E7779A)

## 为组件添加径向渐变效果

```typescript
@Entry
@Component
struct RadialGradientDemo {
  build() {
    Grid() {
      GridItem() {
        Column() {
          Text('center: 50')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .radialGradient({
          center: [50, 50],
          radius: 100,
          repeating: true,
          colors: [

            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('center: 0')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .radialGradient({
          center: [0, 0],
          radius: 100,
          repeating: true,
          colors: [
            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: true')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .radialGradient({
          center: [50, 50],
          radius: 100,
          repeating: true,
          colors: [
            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }

      GridItem() {
        Column() {
          Text('repeat: false')
            .fontSize(15)
        }
        .width(100)
        .height(100)
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .radialGradient({
          center: [50, 50],
          radius: 100,
          repeating: false,
          colors: [
            [0xf56c6c, 0],
            [0xffffff, 0.125],
            [0x409EFF, 0.25]
          ]
        })
      }
    }
    .columnsGap(10)
    .rowsGap(10)
    .columnsTemplate('1fr 1fr')
    .rowsTemplate('1fr 1fr 1fr')
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Bu9fWD08TbGvUA0p9A5Lxw/zh-cn_image_0000002563865971.png?HW-CC-KV=V1&HW-CC-Date=20260330T024846Z&HW-CC-Expire=86400&HW-CC-Sign=70EEEC0E2E1D3AE20434F7FF6763A0AA03FCA6F2F1A6CF43C3439A5CC809BDD0)
