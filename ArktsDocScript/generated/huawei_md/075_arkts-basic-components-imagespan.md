# ImageSpan-文本与输入-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan

[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)、[ContainerSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan)组件的子组件，用于显示行内图片。

> **说明**
> 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

无

## 接口

ImageSpan(value: ResourceStr | PixelMap)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 图片的数据源，支持本地图片和网络图片。 当使用相对路径引用图片资源时，例如ImageSpan("common/test.jpg")，不支持跨包/跨模块调用该ImageSpan组件，建议使用$r方式来管理需全局使用的图片资源。 - 支持的图片格式包括png、jpg、bmp、svg、gif和heif。 - 支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。 - 支持file://data/storage路径前缀的字符串，用于读取本应用安装目录下file文件夹下的图片资源。需要保证目录包路径下的文件有可读权限。 |

## 属性

属性继承自[BaseSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#basespan)，通用属性方法支持[尺寸设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size)、[背景设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background)、[边框设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border)。

### verticalAlign

verticalAlign(value: ImageSpanAlignment)

设置图片基于行高的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageSpanAlignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagespanalignment10) | 是 | 图片基于行高的对齐方式。 默认值：ImageSpanAlignment.BOTTOM |

### objectFit

objectFit(value: ImageFit)

设置图片的缩放类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagefit) | 是 | 图片的缩放类型。 默认值：ImageFit.Cover |

### alt12+

alt(value: PixelMap)

设置图片加载过程中显示的占位图。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 设置图片加载过程中显示的占位图，支持[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型。 默认值：null |

### colorFilter14+

colorFilter(filter: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#colorfilter9) | [DrawingColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawingcolorfilter12) | 是 | 1. 给图像设置颜色滤镜效果，入参为一个4x5的RGBA转换矩阵。 矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。 当矩阵对角线值为1，其余值为0时，保持图片原有色彩。 **计算规则：** 如果输入的滤镜矩阵为： ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ZpnfOfnOTF6AZhFAqxB2Iw/zh-cn_image_0000002562715707.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=5B70CC7CC61C513BE499D0DBA130A20AA7E9475FFB2E14A11AC896200DA4BE1C) 像素点为[R, G, B, A]，色值的范围[0, 255] 则过滤后的颜色为 [R’, G’, B’, A’] ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/4QUrgkWvQmyD_sflBern7A/zh-cn_image_0000002531635836.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=D839EA23498BDA7D4F94BDE9B4BC29587930812109FF645649773138C28367B3) 2. 支持@ohos.graphics.drawing的ColorFilter类型作为入参。 **说明：** 该接口中的DrawingColorFilter类型支持在元服务中使用。其中，svg类型的图源只对stroke属性生效。 |

### supportSvg222+

supportSvg2(enable: Optional<boolean>)

开启或关闭[SVG标签解析能力增强功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities)，开启后相关SVG图片显示效果会有变化。

ImageSpan组件创建后，不支持动态修改该属性的值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional<boolean> | 是 | 控制是否开启[SVG标签解析能力增强功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities)。 true：支持SVG解析新能力；false：保持原有SVG解析能力。 默认值：false |

## 事件

通用事件仅支持[点击事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click)。还支持以下事件：

### onComplete12+

onComplete(callback: ImageCompleteCallback)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageCompleteCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#imagecompletecallback12) | 是 | 图片数据加载成功和解码成功时触发的回调。 |

### onError12+

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageerrorcallback9) | 是 | 图片加载异常时触发的回调。 |

## ImageCompleteCallback12+

type ImageCompleteCallback = (result: ImageLoadResult) => void

图片加载成功和解码成功时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [ImageLoadResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#imageloadresult12对象说明) | 是 | 图片数据加载成功和解码成功触发回调时返回的对象。 |

## ImageLoadResult12+对象说明

图片数据加载成功和解码成功触发回调时返回的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 图片的宽。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) |
| height | number | 否 | 否 | 图片的高。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) |
| componentWidth | number | 否 | 否 | 组件的宽。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) |
| componentHeight | number | 否 | 否 | 组件的高。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) |
| loadingStatus | number | 否 | 否 | 图片加载成功的状态值。 **说明：** 返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。 |
| contentWidth | number | 否 | 否 | 图片实际绘制的宽度。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) **说明：** 仅在loadingStatus返回1时有效。 |
| contentHeight | number | 否 | 否 | 图片实际绘制的高度。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) **说明：** 仅在loadingStatus返回1时有效。 |
| contentOffsetX | number | 否 | 否 | 实际绘制内容相对于组件自身的x轴偏移。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) **说明：** 仅在loadingStatus返回1时有效。 |
| contentOffsetY | number | 否 | 否 | 实际绘制内容相对于组件自身的y轴偏移。 单位：[px](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) **说明：** 仅在loadingStatus返回1时有效。 |

## 示例

### 示例1（设置对齐方式）

从API version 10开始，该示例通过[verticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#verticalalign)、[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#objectfit)属性展示了ImageSpan组件的对齐方式以及缩放效果。

```typescript
@Entry
@Component
struct SpanExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text() {
        Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)
          .decoration({ type: TextDecorationType.None, color: Color.Pink })
      }.width('100%').textAlign(TextAlign.Center)

      Text() {

        ImageSpan($r('app.media.app_icon'))
          .width('200px')
          .height('200px')
          .objectFit(ImageFit.Fill)
          .verticalAlign(ImageSpanAlignment.CENTER)
        Span('I am LineThrough-span')
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('50px')
          .height('50px')
          .verticalAlign(ImageSpanAlignment.TOP)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .size({ width: '100px', height: '100px' })
          .verticalAlign(ImageSpanAlignment.BASELINE)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
        ImageSpan($r('app.media.app_icon'))
          .width('70px')
          .height('70px')
          .verticalAlign(ImageSpanAlignment.BOTTOM)
        Span('I am Underline-span')
          .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)
      }
      .width('100%')
      .textIndent(50)
    }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/XENysvNyTYyBsilbpnXzog/zh-cn_image_0000002531795772.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=211E7990C7BC4A3D2BF9B8372C050E6F8CF643F8F02152B27F8CE10C07E050E6)

### 示例2（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```typescript
@Component
@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Text() {

          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
            .borderRadius(20)
            .textBackgroundStyle({ color: '#7F007DFF', radius: "5vp" })
        }
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/4meGnTgsQgyReO6UKO_x9g/zh-cn_image_0000002562555737.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=58F1CBB784E8926152B42C925F55BFBDDAD9CF1ACDA07B7CAF87CAF2249ECDC0)

### 示例3（为图片添加事件）

从API version 12开始，该示例通过[onComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#oncomplete12)、[onError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#onerror12)为图片添加加载成功和加载异常的事件。

```typescript
@Entry
@Component
struct Index {

  @State src: ResourceStr = $r('app.media.app_icon');

  build() {
    Column() {
      Text() {
        ImageSpan(this.src)
          .width(100).height(100)
          .onError((err) => {
            console.info("onError: " + err.message);
          })
          .onComplete((event) => {
            console.info("onComplete: " + event.loadingStatus);
          })
      }
    }.width('100%').height('100%')
  }
}
```

### 示例4（设置颜色滤镜）

从API version 14开始，该示例通过[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#colorfilter14)属性展示了给ImageSpan图像设置颜色滤镜的效果。

```typescript
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct SpanExample {
  private ColorFilterMatrix: number[] = [0.239, 0, 0, 0, 0, 0, 0.616, 0, 0, 0, 0, 0, 0.706, 0, 0, 0, 0, 0, 1, 0];
  @State DrawingColorFilterFirst: ColorFilter | undefined = new ColorFilter(this.ColorFilterMatrix);

  build() {
    Row() {
      Column({ space: 10 }) {

        Text() {

          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(this.DrawingColorFilterFirst)
        }

        Text() {

          ImageSpan($r('app.media.sky'))
            .width('60vp')
            .height('60vp')
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter({
              alpha: 255,
              red: 112,
              green: 112,
              blue: 112
            }, drawing.BlendMode.SRC))
        }
      }.width('100%')
    }.height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5XxP8jwMS2ybckNEo5rpww/zh-cn_image_0000002562715709.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=19ED093F9A3312FF5A92EA172832DAB900398CE0A628CC543A200C531A87977A)

### 示例5（设置加载占位图）

从API version 12开始，该示例[alt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#alt12)属性展示了ImageSpan设置加载网络图片时占位图的效果。

```typescript
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SpanExample {
  @State imageAlt: PixelMap | undefined = undefined;

  httpRequest() {

    http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
      } else {
        console.info(`http request success.`);
        let imageData: ArrayBuffer = data.result as ArrayBuffer;
        let imageSource: image.ImageSource = image.createImageSource(imageData);

        class tmp {
          height: number = 100;
          width: number = 100;
        }

        let option: Record<string, number | boolean | tmp> = {
          'alphaType': 0,
          'editable': false,
          'pixelFormat': 3,
          'scaleMode': 1,
          'size': { height: 100, width: 100 }
        };

        imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {
          this.imageAlt = pixelMap;
        })
      }
    })
  }

  build() {
    Column() {
      Button("获取网络图片")
        .onClick(() => {
          this.httpRequest();
        })

      Text() {

        ImageSpan('https://www.example.com/xxx.png')
          .alt(this.imageAlt)
          .width(300)
          .height(300)
      }

    }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iFnFgj8gTY2Grm0qxILUxw/zh-cn_image_0000002531635838.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=7F9F96DE89939843243F59343E59AD8DB2520AC163D604ACA2944732BD1F08F8)

### 示例6（使用supportSvg2属性时，SVG图片的显示效果）

从API version 22开始，该示例通过设置[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan#supportsvg222)属性，使[SVG标签解析能力增强功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg易用性提升)的SVG易用性提升能力生效。

```typescript
import { drawing } from '@kit.ArkGraphics2D';
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('属性字符串不支持svg2')

        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
        Text('属性字符串支持svg2')

        Text() {
          ImageSpan($r("app.media.ice"))
            .width(50)
            .height(50)
            .supportSvg2(true)
            .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
              drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/pr2rUBO7SymlMIbZXwY0ww/zh-cn_image_0000002531795774.png?HW-CC-KV=V1&HW-CC-Date=20260324T022748Z&HW-CC-Expire=86400&HW-CC-Sign=92ED79E976BE4DD5A249199AFCBB1845CDFD3759ECF811C48615D27987C51675)
