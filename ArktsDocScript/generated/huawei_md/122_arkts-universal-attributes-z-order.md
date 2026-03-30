# Z序控制
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/TLqVI5BhRyex4UdgfxrNRA/zh-cn_image_0000002532906782.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=73BF56647ED3512E3B94AABE6620630540D340559E5410333158196C126133A5)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/bZCrexacSRSI0PhdqRRIjQ/zh-cn_image_0000002533066730.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=40462CFBAECC2460FAB36AB92A3A9A90B090DF66C10AE93087FEF9FD67DDA7BD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/YykxW3ooQxOMKyZZGtQdJQ/zh-cn_image_0000002563866633.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=44F69415FE6BAB760422BA81E110258C733235858EC8A201ECA22B1E30D96310)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/VtPReHi4RvmIoqU7Qi6BDw/zh-cn_image_0000002563786679.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=6F36C6344E7006F4E6DCFF4E371913F29473D5078E090B8F38FE526F5A90CBDA)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/AjvCjKWvRkKA7MSaWl-0Og/zh-cn_image_0000002532906784.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=8D1EE21BD61EC3459BCBC9D596ACCBEA2443699E1173C3253E9D03EDD07FD2E7)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/FWU-CqAWQbe6Bbh5rJTiQw/zh-cn_image_0000002533066732.png?HW-CC-KV=V1&HW-CC-Date=20260330T024900Z&HW-CC-Expire=86400&HW-CC-Sign=43064A7E3F9C4E793AFCA978E3560FE6408691A99E75C06654235F539353319D)
