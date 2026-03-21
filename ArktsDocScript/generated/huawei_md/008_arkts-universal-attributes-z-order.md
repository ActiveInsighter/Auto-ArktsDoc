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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/WwxsiWuvRruSyVZAJ-6wWA/zh-cn_image_0000002562145641.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=E268A77FA97EA0DBCF1183EA98AF7E577FCA288B34654EEC5F26331A1392B83B)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/YRbteeSOSD-IrDzGVO-8uw/zh-cn_image_0000002531105740.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=6B31F36151F9042A962F81F0E2DD6886E51A95D17E00B423500948C793071626)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/2iao0nqRRGegseXl2ThiqQ/zh-cn_image_0000002531225674.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=7D312254B3A45CAD83E1A34AC5FF327330291860E9B810288F48BBA9F1451CF3)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/i14XBaP0QCm51NTuaoJVTg/zh-cn_image_0000002562025657.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=2E31F0C56ED00B482BA632FCF9D511E132E7B715B3C806BE8C08BF47F0C25B6A)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/OHZR0ZnnRW6HK38xGR02IA/zh-cn_image_0000002562145643.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=08C5CDBCC6944960676F40C217A56B4CF288F21985AE0C23EACC5E709E995FC5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/kCnmBOxqRqOeOh8cOjdOQQ/zh-cn_image_0000002531105742.png?HW-CC-KV=V1&HW-CC-Date=20260321T021255Z&HW-CC-Expire=86400&HW-CC-Sign=447AABE4DAD692723926A28B7E9C1C1E067AEBFE3B3A9370BC2915DD3F5337CC)
