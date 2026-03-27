# 文档中心
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order

组件的Z序，设置同一容器中兄弟组件的堆叠顺序。

> **说明**
> 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## zIndex

zIndex(value: number): T

设置组件的堆叠顺序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。当不涉及新增或减少兄弟节点，动态改变zIndex时会在zIndex改变前层级顺序的基础上进行稳定排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

### 示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

```typescript
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Stack() {

        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)

        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)

        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

Stack容器内子组件不设置zIndex的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/OwwvtsHdRX2dstDjE87xEQ/zh-cn_image_0000002532086992.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=129543FAE4600E6ED5081F41B63D4914FC47C8F9FD0DD09795B8A4DD17733881)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/CvGvrp2zSGaybmJCCZ58rA/zh-cn_image_0000002532246928.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=0527A1E3E62AB6F742BEA0718764A1FF4B056E1A64668762586DF2900094F228)

### 示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

```typescript
@Entry
@Component
struct ZIndexExample {
  @State zIndex_: number = 0

  build() {
    Column() {

      Button("change Text2 zIndex")
        .onClick(() => {
          this.zIndex_ = (this.zIndex_ + 1) % 3;
        })
      Stack() {

        Text('1, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)

        Text('2, default zIndex(0), now zIndex:' + this.zIndex_)
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(this.zIndex_)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

不点击Button修改zIndex值的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/P-IG6WDRTjWqMhqeI-Yh-w/zh-cn_image_0000002563126871.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=53A331710060BA6F12D22A398697B382433A4410D7A22A2C10DCC0DF597080DA)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Qg-2aRIdQW6i-mI6UwVyHA/zh-cn_image_0000002563206893.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=16C57B2E938396D9BA6B772FAA5D03B4936087E7563173B6764DF82FC00CAD73)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/zEmHmHxRQB2_B7965-hn2A/zh-cn_image_0000002532086994.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=586544B1CC17A737F26454A266833D12EDF6AFF0F249C8791A6166DC8679D26A)

### 示例3（设置不同容器内组件的zIndex属性）

该示例在不同容器内设置zIndex属性。其中，Text1、Text2和Text3在不同的Stack容器内。虽然Text3的zIndex值最小，但Text1、Text2仍无法按照预期显示在Text3的上方。

```typescript
@Entry
@Component
struct ZIndexExample {
  build() {
    Stack() {
      Stack() {

        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)

        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
      }.width('100%').height(200)

      Stack() {

        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Wpe3Ym1aR0e0D8V8TMmHvA/zh-cn_image_0000002532246930.png?HW-CC-KV=V1&HW-CC-Date=20260327T024032Z&HW-CC-Expire=86400&HW-CC-Sign=15273ADE631724356FCA20DC55C0D52BCB789E18054567A70126EFE852940ABA)
