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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/bQbijb_UTgaam_X00owyZg/zh-cn_image_0000002538128918.png?HW-CC-KV=V1&HW-CC-Date=20260411T023455Z&HW-CC-Expire=86400&HW-CC-Sign=48A825312FA6372CCFD70DCC56267967AEAE0B290DF23CBBA007951E317F6594)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/NwSfIoDsQQObJ285RBjAow/zh-cn_image_0000002538288852.png?HW-CC-KV=V1&HW-CC-Date=20260411T023455Z&HW-CC-Expire=86400&HW-CC-Sign=286B16527533501C0068C99868A0F66086CBD2E46C6947EAD88939C9CBE1A23B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/t69wUXInQuyQexLXCIWdWQ/zh-cn_image_0000002569168615.png?HW-CC-KV=V1&HW-CC-Date=20260411T023455Z&HW-CC-Expire=86400&HW-CC-Sign=1CEB649D4BBAAC11B51D93C45A2C1AA3BD5CD190240124BE40E0141FD29FC9A6)
