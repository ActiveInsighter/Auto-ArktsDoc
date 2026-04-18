# SVG标签解析能力增强
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities

从API version 21开始，当Image组件的[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)属性设置为true时，将启用SVG标签解析能力增强功能，该增强功能主要包含SVG1.1规范中的以下功能。

- 易用性提升：SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用的URL类型进行严格校验；Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性对整个SVG图源生效；Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性不对SVG图源中fill = 'none'的元素填充颜色。
- 仿射变换能力扩展：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。
- 解析能力扩展：[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。
- 显示效果扩展：分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。

## SVG标签解析能力增强对SVG图源标签和属性的影响

启用增强的解析处理能力后，影响的SVG元素和属性说明如下：

| 元素 | 属性 | 说明 |
| --- | --- | --- |
| clipPath | clipPathUnits | clipPathUnits裁剪路径单元，指定裁剪路径的坐标系统基准。 clipPathUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| filter | filterUnits primitiveUnits x y width height | filterUnits滤镜单元，定义滤镜效果（如模糊、阴影）的坐标和尺寸基准。 primitiveUnits滤镜原语单元，定义滤镜内元素效果的坐标和尺寸基准。 filterUnits和primitiveUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 x：滤镜区域x轴偏移分量，默认值：-10% y：滤镜区域y轴偏移分量，默认值：-10% width：滤镜区域宽，默认值：120% height：滤镜区域高，默认值：120% |
| mask | maskUnits maskContentUnits x y width height | maskUnits遮罩单元，控制遮罩的坐标系统和内容渲染方式。 maskContentUnits遮罩内容单元，控制遮罩内元素的坐标系统和内容渲染方式。 maskUnits和maskContentUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 x：遮罩区域x轴偏移分量，默认值：-10% y：遮罩区域y轴偏移分量，默认值：-10% width：遮罩区域宽，默认值：120% height：遮罩区域高，默认值：120% |
| radialGradient | gradientUnits | gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。 gradientUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| linearGradient | gradientUnits | gradientUnits渐变单元，决定渐变（线性/径向）的坐标参考系。 gradientUnits属性可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| pattern | patternUnits patternContentUnits | patternUnits图案单元，控制图案整体（<pattern>）的坐标系和内容缩放。 patternContentUnits图案内容单元，控制图案内部元素的坐标系和内容缩放。 patternUnits和patternContentUnits两个属性均可取值： userSpaceOnUse(基于绝对坐标系)、objectBoundingBox(被应用元素的边框作为基准的坐标系)。 |
| g | opacity clip-path | opacity透明度：对整个分组下的多层子元素生效。 clip-path裁剪路径：对整个分组下的多层子元素生效。 |
| 通用 | transform | 用于对SVG元素进行2D变换（如平移、旋转、缩放、倾斜等）。 translate(x, y)‌：沿X/Y轴平移元素。 ‌ rotate(angle, [cx], [cy])‌：旋转元素（可选参数指定旋转中心）。 ‌scale(sx, [sy])‌：缩放元素（单参数时X/Y轴等比缩放）。 ‌skewX(angle)/skewY(angle)‌：沿X/Y轴倾斜元素。 ‌ matrix(a, b, c, d, e, f)‌：通过矩阵定义复杂变换。 |
| 通用 | transform-origin | 用于定义变换的基准点。需和[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性配合使用。 当配置transform-origin时，按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。 |

## SVG易用性提升

SVG图源颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA；引用国际化资源标识（IRI）类型严格校验；调整Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性生效范围；调整Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性生效范围。

### 颜色解析格式变更

当Image组件的SVG图源使用十六进制格式的颜色时，颜色默认解析格式从#ARGB变更为符合SVG标准规范的#RGBA，涉及的SVG属性包括fill、stroke、stopColor、stop-color。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview#objectfit)参数。

SVG图源属性设置8位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#ff000030" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/XOCON2-uQb2UOY3rdt0SkA/zh-cn_image_0000002572641041.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=756E021C147B4DC2A3199F98D1D2A42346F9FD6925A9A63B4B69770C3909A092) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/u4zF4uv7S2eFU_AvM0F-jQ/zh-cn_image_0000002542120734.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E59BB8449CE285C4DEFB02F956AAD373E286A7776E8690B692CFBD5CCADC005B) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/pQfI_8UJTxqjsj3-pJTfpg/zh-cn_image_0000002572681005.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=465B68014B7E6ED5EF668C1C764D1983ED093F37697DA9303C33549E69DF060C) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/xBEVM-LbSCWptZnmi4LgUg/zh-cn_image_0000002541961098.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=DF0E18D6619991C21C18238A471391800C99B39D4D635BEB6E990B59B02EB2A1) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/iXGuK1ofT-GFH2N02jcZSQ/zh-cn_image_0000002572641043.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=04F4F83DFE048D18F54591E63072028952615E95AB8390FB6572D407CA757797) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/NcbGzhW6SE2LHY5rbxfAsA/zh-cn_image_0000002542120736.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=767D9ECC8DB326CB25E645E0EE4D419E96B073D0172D737C68BF331C33F9D8C3) |

### 引用国际化资源标识（IRI）类型严格校验

严格校验filter滤镜/clip-path裁剪路径/mask遮罩引用的URL类型，避免引用类型不匹配。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| --- | --- |
| 滤镜/裁剪路径/遮罩引用的URL类型不匹配，导致错误的显示效果。 | 滤镜/裁剪路径/遮罩引用的URL类型不匹配时，不显示对应效果。 例如，mask、clippath、filter、pattern、渐变等标签都有各自的id，filter、clip-path和mask属性绑定其它类型的标签id时，对应效果不生效。只有mask属性绑定mask标签id、clip-path属性绑定clipPath标签id和filter属性绑定filter标签id时，对应效果才生效。 |

当URL类型不匹配时，遮罩效果不生效，示例图源如下：

```typescript
<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="myClipPath">
      <circle cx="50" cy="50" r="40"/>
    </clipPath>
    <mask id="myMask">
      <rect x="0" y="0" width="100" height="100" fill="red"/>
    </mask>
  </defs>

  <rect x="10" y="10" width="180" height="80" fill="blue" mask="url(#myClipPath)"/>
</svg>
```

### 调整colorFilter生效范围

Image组件的[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性从只对stroke边框生效调整为对整个SVG图源生效。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 原始图源 | 提升前 | 提升后 |
| --- | --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/nMxWjGLRSCKlc0odxq88XQ/zh-cn_image_0000002572681007.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=86FC11B0D9D5CC84CA448AA3F9C5EEBA59EBFD35678A288C8742E170E357FA72) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/WO4ZuDLrSR6cNcC_j-xJhQ/zh-cn_image_0000002541961100.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5B3AA36CCD1B389D05D5DBB2C21F89751E47ED43D65DA76E666281F101220AA4) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/afodBGdzTtqxgOB5hcu7xQ/zh-cn_image_0000002572641045.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C3EC2ADDDCDCECB01232AA3CAC50FCAC9E2F1BE088DE7C9515E784C7470BCCD3) |

示例图源和示例代码如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

    <rect x="10" y="10" width="180" height="80" stroke="gray" stroke-width='16' fill="orange"/>
</svg>
```

```typescript
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image111.svg'))
          .width(220)
          .height(220)
          .colorFilter(
            [ 0.6, 0,   0,   0, 0,
              0.2, 0.8, 0,   0, 0,
              0.2, 0.2, 1.2, 0, 0,
              0,   0,   0,   1, 0 ]
          )
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### 调整fillColor生效范围

当SVG图源中元素的fill属性为none时，Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor20)属性从填充颜色变更为不填充颜色。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| 提升前 | 提升后 |
| --- | --- |
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/SNGBIgq2SVyZN-otH12XYw/zh-cn_image_0000002542120738.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E11CD19E0B69B4B2B717FAFEF911439BC1D501575AC515B44758C9B259D21093) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/hyLsZo4nQfmIZmul_DxLiw/zh-cn_image_0000002572681009.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=3C21FBDCF25FDF5F2C015A2B63B50E29BBDEA33A3A71BC8413DFF5EBD56D5941) |

示例图源和示例代码如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

  <rect x="10" y="10" width="180" height="80" fill="none"/>
</svg>
```

```typescript
@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image11.svg'))
          .width(220)
          .height(220)
          .fillColor('blue')
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 仿射变换能力扩展

对于[transform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#transform)属性：支持变换全局中心点可配置；支持rotate旋转的局部中心点；支持矩阵(matrix)转换方式；支持非法值的校验；裁剪路径内支持仿射变换操作；组合场景支持仿射变换操作。

### 支持变换全局中心点配置

SVG支持解析[transform-origin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation)属性来配置全局中心点的能力，前后效果对比如下表格说明：

> **说明**
> SVG图片最终显示效果受Image组件的'[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形配置变换功能和transform-origin属性。 | 固定按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点进行仿射变换。 | 按照全局中心点（transform-origin）属性指定的坐标偏移(x,y)作为变换中心点进行仿射变换。 |
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/WZdoXbo9QNKbFiAY60HZHg/zh-cn_image_0000002541961102.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A3CCF13978E240E143FB42475F755539292E7AB5D80ED9805D1F8A6832F2BE43) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/740wvZYGTNaZhcpXyisj4A/zh-cn_image_0000002572641047.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=30A365A5F279B4DF9B10DBEA127DF191BFE29B5E52A70466FB19D429A79CA17F) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/T19Asi8gRWqPhAZCuVczXg/zh-cn_image_0000002542120740.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=3B9EFAE0D2DED2106D2D0B5E9C151BF4BA1FBC1FFB558FFC1FDA6CD4D7CE5E3D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/i2YCFYQCRGiDwlzdklYgiA/zh-cn_image_0000002572681011.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=DCB423BAEEE27196BD4551B08A9D35371E1E9875A3F10CA07C790EDCF25D0C22) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9pZqrLhGQPia9tK9J_-a_Q/zh-cn_image_0000002541961104.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A300D6FE2544175E7A3544A8BFDFD91D485B687704774C5B5992EE5F22AFEC6A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KQwgByDXTzSxPucUN_DlDA/zh-cn_image_0000002572641049.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=8051BBF555FEBB77C5A8A7702BD46CD18525AE44366C4B3284E3AB5745E519B3) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/CTKRNsnuQrq3aAoKKnpx7Q/zh-cn_image_0000002542120742.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=9F2EC63A4F89E3279879322C4A5A4D06F33467482DAE5FC6D079B7DD83CE8850) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sNbfO_GSReyU4qYd1ogSUw/zh-cn_image_0000002572681013.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=67CA66F64FB4D68225134F1A134138A9CF3A44E64E950701E6613B03767F6DAD) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/9gC-zVReSuWV5m6XRGUr7w/zh-cn_image_0000002541961106.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=ADD88105A5C0A73ACD1F53CF038B68AF0DD7550CCA775394A5251BE2AFB96292) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1GFV95UJSF6df5R2S5J9og/zh-cn_image_0000002572641051.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=AD55B96741AAF04229CCC2A2B340961924EFBB37A70F454AFF7A16FAC47C1363) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HYj_jhpoRhWSmapKFXltzg/zh-cn_image_0000002542120744.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=FD4D0B4CF48192DD5018D520FFCC9A0A90B05173F7AEA7C245D7A9FE86BB9859) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3j4mlAe7SUyGRaBhn9aOvg/zh-cn_image_0000002572681015.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=002BAE36CA5351B0935EB5E7F0CC97341BB351D98C85AC38AD46D562C112BDBD) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/gq49Yd05QqerVBJ4EeAeMw/zh-cn_image_0000002541961108.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A1A391B792EBCF2790A8B46EB5EDBA2BD834FE114AA642CB9C416CF6F2943EF8) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3EEFKcKTQ-SXF0tPz_noQw/zh-cn_image_0000002572641053.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E784318195E1686E44B44860E8A7CBFF746FFD0E06DD9129BFBA8769F11ABFC1) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ZNH8UKmUQEGfmY9HC2jejg/zh-cn_image_0000002542120746.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=7D3CE65F877A1E3F0EF28804E9D55278630D0CC813DD6BB148E130C978FBB6D1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7BKcU1zkQHu6aXKWsLIWSw/zh-cn_image_0000002572681017.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=AA8BFB4CF69C19E82A91B5BE420D2700CB71221A65E423FAFA383CB189F15926) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/MBOemEtMSfC9Uz25ooEmkQ/zh-cn_image_0000002541961110.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=297C456B0CBDC14185167C00BFC3CD9DC564D79049110651E73DD5EE53C80F58) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/vAVuyRBSSwm7uTmzV_f2cw/zh-cn_image_0000002572641055.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=DBA8D32402B2FC9E371154A4594551E76B86B7195D7632569BB81C7328D1466A) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/tQpCsIU_RbiySJWb9szdvw/zh-cn_image_0000002542120748.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=732AFCC48E2DE218F7B2C994BA797F4BF9B42ABE47D7EAB28068BD3E30AA4BE3) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/7T8VfcFrTQqoG0gl87vC7A/zh-cn_image_0000002572681019.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=65991F6D6BA0A0967D91D09FA806106509A7F49083DD6BA54F3C9DF24C9DF804) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/1Owr0fGUQbedmGvIlAlCNg/zh-cn_image_0000002541961112.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B0D4C1C4ACB6B0F652BE885515C5DBA98EE6D631086F214309754F9F0EC008A4) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/d6F7kjjfRa2YIkVVvBF9rw/zh-cn_image_0000002572641057.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=7CE8ADEBFA26061E9435E296511DE28FF7525EF76407152E88163F12E00B2F75) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sYXMkjZdSxyYM6K6bAJmIw/zh-cn_image_0000002542120750.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=07AA24B8BE9090D3A179DBEE1A2CDD3246CE54A117E583A703C6AD412B9CCEBE) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/-ujNBVM4R_ahO_NHBnK-Yg/zh-cn_image_0000002572681021.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4FC1200FD16D5D9ACC563EF3B3EFDE840160054264AB787F8C896CD9483AA4CE) |

### 裁剪路径内支持仿射变换操作

支持clip-path裁剪路径内的transform仿射变换操作。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="circleClip" clipPathUnits="objectBoundingBox">

      <circle cx="50" cy="50" r="40" transform="translate(50 50)" />
    </clipPath>
  </defs>

  <rect x="10" y="10" width="250" height="250" fill="blue"
        clip-path="url(#circleClip)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/HXyoO8pcR5q04qCrRG70tg/zh-cn_image_0000002541961114.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BF29E760B9147B034EFFC1D0888659259E96D1D36FAB98A99A1E438E8B7E1C0C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ivTqrWECSZuRkZMJCrnzlg/zh-cn_image_0000002572641059.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5D3C5C38A272901314C1E317FBFF7D29952CF8492351BAEF1F993C32B7480C58) |

### 组合场景支持仿射变换操作

支持多种元素组合场景的仿射变换操作。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

transform操作在use中，use对象也在相同的mask元素内。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
      <use xlink:href="#rect1" transform="translate(0.6, 0.000000) scale(0.5 0.5)" />
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5" fill="red"  />
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rWrF7831Q0u4Un0T-RvTGQ/zh-cn_image_0000002542120752.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=DA4067AABF4FF06E994A46AB210D06201BF350B79862FBED60163A30791561DB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dDu0I6H8QJSoin6P3VUVvA/zh-cn_image_0000002572681023.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=158C83DA3CA5CA0DFB45043D0F53C40D739E4D02862053F4E437135C64E0CFC9) |

transform操作在g标签中，且不包含scale操作。

```typescript
<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
        <g transform="translate(0.6, 0.000000)">
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5"  fill="red"  />
      </g>
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/znhupIyDRAygp6M9EIDIDg/zh-cn_image_0000002541961116.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B5B04272F5C8DEC34E5324FD1319EFB7BB496DBFDA96FA3DF69A1AFED5C11BDA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/RA0yrCxLSXCmaT0QTUazGA/zh-cn_image_0000002572641061.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B07E127B86194A5FBA9C5FE62970091F9F773AD1DB7668CCB2CC532CAD49970E) |

## SVG解析能力扩展

[viewBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#viewbox属性支持对齐和缩放规则可配置)属性支持对齐和缩放规则的自定义配置；支持裁剪路径单元的解析；支持渐变单元的解析；支持遮罩单元和遮罩内容单元的解析；支持图案单元和图案内容单元的解析；支持滤镜单元和原语单元解析。

### viewBox属性支持对齐和缩放规则可配置

viewBox主要用来控制在SVG动态拉伸效果，可以通过参数preserveAspectRatio来控制内容区显示的对齐和缩放规则。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

SVG包含“preserveAspectRatio”属性且值为“none”，示例图源和行为变更如下：

```typescript
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" />
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" />
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| --- | --- | --- |
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Gxv1i8YrS5KMjgVruMesuQ/zh-cn_image_0000002542120754.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E1F1E3A898D92215DCB38C7A2EF7EEFC70802F15CDE82EF45DEE11ACC4546432) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/w3TSrLDYQEKdXUfK6ve_RA/zh-cn_image_0000002572681025.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=29A73E33C056F2B321AC4E864A480E31A32F74AD352A0DBAED8BD3E97B9CD25C) |

SVG包含“preserveAspectRatio”属性且值为“<align> [<meetOrSlice>]”，示例图源和对齐方式、缩放比例变更如下：

```typescript
<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="xMinYMin meet" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" />
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" />
</svg>
```

| 参数值 | 扩展前 | 扩展后 |
| --- | --- | --- |
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4PvPGeHYQXGscIApv45pRA/zh-cn_image_0000002541961118.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=93E88E8771980155AA8FD5E1C2CBE4223BF10E802D504712A1A09AA43724B68B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/UrZuhER_Rm6sCDSEh5ZSOw/zh-cn_image_0000002572641063.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=FB000AA7EF3E2D9EEDA7CB41D1E327E8E2FC8E011F539F9893C4D46DA7D08137) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iOeo0dMkQYuAafASNNMkWg/zh-cn_image_0000002542120756.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=3077463F37D0EF3102196B87DF50FED453E0403FF4E552C53580189C1F61DD5A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/HDXl7Hr9TTidKkjHGHg9vA/zh-cn_image_0000002572681027.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A7D30511E09C1A482FDCF79739FEE09C28514075AA0BF5E34E564F6016B69F07) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/9FSmAJoTS_y9HJ-_yxxlMw/zh-cn_image_0000002541961120.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=47E9DB1D965471287BED146DD310EFB2B34CCEBAB649160CC6F1C0EFB91B2C1D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GmkVSkwkRUGZBXxT9MUHKQ/zh-cn_image_0000002572641065.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4AC583901AF19E6FFF283E6554D4E8E6AB470EA47253000DEE89C20A1D0546DF) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/J6hW8wMLT2-0rj6eQIIALg/zh-cn_image_0000002542120758.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BB8C3865D5C0296B67F38975A82BFA643F653A81B6D4B1C60161A335C39119C4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/9BDoHJ92SgiKrZ-z9n3yOA/zh-cn_image_0000002572681029.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=60CABF8890A2F726DA8181AF1F82DB26039F5FF47DA97972B32499CEB8169225) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/OW2e38RmQCGThA3k_4zozQ/zh-cn_image_0000002541961122.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=6C628E54C0274ADA53F17448FE47B6AAA66AB72CAC5BB746F2109A06A22F1555) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Jz-RV9KwQOeNOoAN8n7cJQ/zh-cn_image_0000002572641067.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B3DF28E4AACED33C99A1D0F1F6F3E320790FBE67FEC89E841106461F1E90FC3E) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7qp97mtQQyqNw_BEgXDBuA/zh-cn_image_0000002542120760.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4E81B3CCBA89C0AC9246B70AE88C0F15070712F8DB844B05A844E6450774B426) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/31s0cwBPQr-Vw3LWNi2T9w/zh-cn_image_0000002572681031.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1D7BA98496EB263A2B2ADBDA54492C3DB3999E8A17356E32EB2573716B7FC2AC) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/A2QFdWQWQimMQeHVwIKUrg/zh-cn_image_0000002541961124.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=3D05D3754B0DE8F56CC15C8093AE3BB03D0AE69E1CE133EDC994D5378FBC5DC2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/B0YBeVoBSviqKKmo5F65OA/zh-cn_image_0000002572641069.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=79D5F87CAFBB5FAD5EB2A27833AB0C6DEB7BF371C5871E6CBB10013F0AAF05C0) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/rcp8f3AWRj-x5LxXy75mwg/zh-cn_image_0000002542120762.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=F3003A3AF43FB3A02AD78D7A4E35A3850DDF86A04212030516C211DC25FE05C7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/BPaIwtR6T5SQg71JdjWCBQ/zh-cn_image_0000002572681033.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BF431711684DAE4564B9756782FF820C4C677F195D5449914BCAA20E614E6956) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/AKoKbUvUQ52qJWf6oEnFcw/zh-cn_image_0000002541961126.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=81748A32B0F97F8FE3C1317A98A013E6089B5267300B600458178C5896B00335) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aMMnx0BaS3mn1h1meRJylg/zh-cn_image_0000002572641071.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=86AF70EC6C4008DBA028897135AC23BEE7FEFB240F3BBCB1AD110BC09A107BE6) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/OQNdOJszSjq1SDnvYvdMeg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2578418643F3AEAF2CA50EE3B8BDCBEE7BA24183EEA56EE75F4D2AC491DD11BB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ycjmp067TX6LD0Mlhi_TAw/zh-cn_image_0000002572681035.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=987A8F78EEF1A0F112641065DF21556901BCCDCC0BC10BCCDE64B279E5B1AE30) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/d5j0vRGvSjG9JJvKZHL1cQ/zh-cn_image_0000002541961128.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E30BB304097EAB979C71FB403C2AA9CA9B8FA9347D0416587EDC247C25374B1B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/vbpBUr5CQ-K7sdL4cpSkQQ/zh-cn_image_0000002572641073.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B37D2F06E1DBCCE3F074B0357D8F54EF8DD39CC4C0C5EC82BF18A7334863F74E) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Rl-JGF89RW6h7nBxIj3kxg/zh-cn_image_0000002542120764.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E6F50E8771B11520C0391028BD7168E82FB7433FAC01E9830CF79574C7F9F6E6) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/l47uZ96LTRinBSrPGaFH0A/zh-cn_image_0000002542120766.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1CB61B70A4821B228F364ABFE0F6DF7EFEAA557E9080F13CD9CB042A3BC08F89) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/kpg--wMSSsq-hFdfOJlBpw/zh-cn_image_0000002572681037.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1F42E2C169D0DDEA2E59161C025C4D678DA9D3A05BD6B44914EC8E70319CAB84) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Tew9KmZDT9K-FBdB83enaA/zh-cn_image_0000002541961130.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2EC34586C106527B587041AA0C3E6E1431F2614A346B093A52322B5475A4C845) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qA6-Wr0wR6iRQ2AiSUDDvA/zh-cn_image_0000002572641075.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=45069BD4EEF88F58D3DFB5DBB8B029A676F2C7D5290EABC164B854521B918397) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/pobwkoNiRDu7Jle9WP8HkA/zh-cn_image_0000002542120768.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BBAEE3199645B37F34C364427EFB7F4FFAFC994066DC5D05FF875553EB6EAD55) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/dQ80W6hKQRy5WUvQgRRU8Q/zh-cn_image_0000002572681039.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=FBC3C010A724FB3EA0A657F3EE24A58273A4B31557FB8B69E834C73B6AC93736) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/scY4F_yIQziMRuqfpqVBaw/zh-cn_image_0000002541961132.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=13C3113E9381E445A1A47F3D803FCDC885C6122054F789AAA6BC5DA68753D3BC) |

### 支持裁剪路径单元的解析

支持裁剪路径单元值[clipPathUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加clipPathUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

下面图源示例当裁剪路径单元为"objectBoundingBox"时，长方形裁剪路径位于应用裁剪路径长方形图形左上角x,y乘以图形包围盒宽度和高度。尺寸为width乘以图形包围盒的宽度，height乘以图形包围盒的高度。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="clip1" clipPathUnits="objectBoundingBox">
      <rect x="0.2" y="0.2" width="0.7" height="0.6" />
    </clipPath>
  </defs>
  <rect x="10" y="10" width="100" height="100" fill="blue" clip-path="url(#clip1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/OYK9sjRET2uDBT_FwWY0JQ/zh-cn_image_0000002572641077.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B0172DA93395B43744125E5159B3424997C285CF7F97D7958AB6FA7B9ED8AA2F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/3nm68xvQQxmhi1ISnTNvnQ/zh-cn_image_0000002542120770.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=6148F7B0F7C9DC39BD3E4F6E557260666777110728854D7BBC1173D11450C725) |

### 支持渐变单元的解析

支持渐变单元值[gradientUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加gradientUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个线性渐变从绝对坐标(10，10) 到 (180，180)的长方形范围内。

```typescript
 <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="10" y1="10" x2="180" y2="180"  gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="180" height="180" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qDdvESYKTsiowrBqAuZlww/zh-cn_image_0000002572681041.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=3F42EB2202932D1CFE7A1CBC401FD4524CEBBB921AE6896328058A0557C15D10) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/dq2Zmz47QhuWNppxQgXXMw/zh-cn_image_0000002541961134.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=BB587E2AF48C26B3E2CA4EDD8029DEA368A4E4AC9DC2358D6B8D4DAB8FA08496) |

图源示例显示一个径向渐变从绝对坐标圆心 (100，90) 开始，半径为90的渐变效果。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
     <radialGradient id="grad2" cx="100" cy="100" r="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="90" fill="url(#grad2)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/VtKGxPsgQZ2Uwy-SkwVIgg/zh-cn_image_0000002572641079.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5271BE1EBE60D688C0631A62DA02FAF2C8F4E78BA04FB64827E45825CEEAE43B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WHDlCee1SMiJJQ_lFLOunw/zh-cn_image_0000002542120772.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=E5A1BD2C3877A37929403363B3ADF5BBC962C06748F9F569F0581C0DAB0DD887) |

### 支持遮罩单元和遮罩内容单元的解析

支持遮罩单元[maskUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和遮罩内容单元[maskContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加maskContentUnits和maskUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例显示一个五角星遮罩范围从绝对坐标 (10，10)到(200，200)，遮罩内容相对于应用矩形左上角，水平尺寸乘以图形包围盒宽度，垂直尺寸乘以图形包围盒高度。

```typescript
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" maskUnits="userSpaceOnUse" x="10" y="10" width="200" height="200" clip-rule="evenodd" maskContentUnits="objectBoundingBox">
        <path d="M 0.5,0.05 L 0.2,0.99 L 0.95,0.39 L 0.05,0.39 L 0.8,0.99 Z" fill="blue" fill-rule="nonzero"/>
    </mask>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="red" mask="url(#mask1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/P9UA_AQvRu6bsiORqYoJmg/zh-cn_image_0000002572681043.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4C7F3B8F7E21FFFC010A6EEFADE3162CA8852DAB569C42D645D3C680064D40C6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/bGQJl1HgQRmArKQhi93opQ/zh-cn_image_0000002541961136.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=8292746B7A204373DA21517AE2B7619116814DD61876B67E03F9620C8C642925) |

### 支持图案单元和图案内容单元的解析

支持图案单元[patternUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和图案内容单元[patternContentUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加patternUnits和patternContentUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源图案单元位置尺寸为绝对坐标，图案内容位置、尺寸相对于应用图案的图形，横轴乘以图形包围盒宽度，纵轴乘以图形高度。

```typescript
<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1" patternUnits="userSpaceOnUse" x="10" y="10" width="100" height="100" patternContentUnits="objectBoundingBox" >
      <rect x="0" y="0" width="0.25" height="0.25" fill="red" opacity="0.5" />
      <rect x="0.25" y="0.25" width="0.25" height="0.25" fill="blue" opacity="0.5" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200"  stroke="red" stroke-width="2" fill="url(#pattern1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/1uJueF5ZRqaYXSItwFendw/zh-cn_image_0000002572641081.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C74B175AB42455C167128EA4ED8D8AF9EC5081F73204EA441E077184E622EA0A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/P7NmOu2fRJelkTWkpXJ-Gw/zh-cn_image_0000002542120774.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=DE2C6F2CE38B91F593D6E4424E0710CA46178F18EEE604BE71C873F192ED4ECA) |

### 支持滤镜单元和原语单元解析

支持滤镜单元[filterUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)和原语单元[primitiveUnits](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)的解析，增加filterUnits和primitiveUnits为objectBoundingBox（被应用元素的边框作为基准的坐标系）场景的处理。目前支持到的原语有feFlood,feOffset,feGaussianBlur,feBlood,feColorMatrix,feComposite。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

图源示例：原语值为"objectBoundingBox"时，feGaussianBlur的模糊标准差X，Y轴的stdDeviation数值分别需要乘以应用滤镜图形包围盒的宽度和高度。滤镜原语子区间x，y坐标相对图形左上角分别乘以图形包围盒的宽度和高度，滤镜原语子区间尺寸的width，height参数分别乘以图形包围盒的宽度和高度。

```typescript
 <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
 <defs>
   <filter id="blend" primitiveUnits="objectBoundingBox">
     <feGaussianBlur in="SourceGraphic" stdDeviation="0.1, 0.1" x="25%" y="25%" width="50%" height="50%" />
   </filter>
 </defs>

 <g fill="none" stroke="blue" stroke-width="4">
    <rect width="200" height="200" fill="none"/>
    <line x2="200" y2="200"  stroke="blue" stroke-width="4" />
    <line x1="200" y2="200"  stroke="blue" stroke-width="4"/>
 </g>
 <circle fill="green" filter="url(#blend)" cx="100" cy="100" r="90"/>
 </svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/nb-9S4uzQ2uDqLEtz2TTSQ/zh-cn_image_0000002572681045.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1A7B7D7AB00B9A9A7E9963F3FA4EAEF530CE6B00E942ADA2C8C934D55AF44A8D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/TSvgASDoRAGZx395Y9UVhw/zh-cn_image_0000002541961138.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=051373005735708FE9BA2E7D2310DC308B67E103B69E6489E441ACAAC4393E23) |

## 显示效果扩展

分组标签g元素中透明度opacity对整个分组下的多层子元素生效；增强g标签内clip-path裁剪路径规则的处理；pattern增强平铺效果和偏移值处理；线性渐变和径向渐变增强平移和缩放效果；mask和filter的参数异常时默认效果变更。

### 分组标签中透明度

分组标签g元素中透明度opacity从对整个分组下的一层子元素生效到对整个分组下的多层子元素生效。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源有两层分组标签嵌套，被裁剪路径截取的半圆形的透明度为0.4。

```typescript
<svg  width="200" height="200" viewBox = "0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="myClip" clipPathUnits="userSpaceOnUse">
      <rect x="25" y="0" width="60" height="60" />
    </clipPath>
  </defs>
  <g opacity="0.4" clip-path="url(#myClip)"  fill="red"  >
    <g >
    <circle cx="25" cy="25" r="25"  />
    </g>
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/fvxy5GNJRS-0KJB4BNja8Q/zh-cn_image_0000002572641083.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=315D5C4D3AB555BA36E27D795970C254CAB1CCD77FBFC7A4C2C28B41110A132F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/xxHFB32XTjOerX_T5rs_mw/zh-cn_image_0000002542120776.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=A773F53A28E8668CF37BBCA69413E19B7EC3072E68D7BC145FB5541514BAE466) |

### 分组标签内引用裁剪路径规则

增强g标签内clip-path裁剪路径规则的处理。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源裁剪路径引用于g标签里，默认裁剪路径规则为"nonzero"，路径标签里的填充规则为"evenodd"，左图实际的填充规则为"evenodd"，右图的填充规则为裁剪路径的默认规则，也就是"nonzero"。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">

  <defs>
    <clipPath id="heartClipPath" >
   <path d="M 100,10 L 40,198 L 190,78 L 10,78 L 160,198 Z" fill-rule="evenodd" />
    </clipPath>
  </defs>

  <g opacity="0.4" clip-path="url(#heartClipPath)" >
  <rect x="0" y="0" width="200" height="200" fill="red"  />
  </g>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QKr1TBugSuaRhGz0o2iXmw/zh-cn_image_0000002572681047.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=9F094BDE6B4D1BF66B7F04D8A895E185F22AAAF5BE80DC7BED48F2A4AD8B2279) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Bxmv2nloTx-X6NQh7ZzAgQ/zh-cn_image_0000002541961140.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=2F750DC83D65AE91C443BE266DC08DAB7E76155BC72ED9FB8A8CCA7CE3A3A2CE) |

### pattern支持平铺效果

[pattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)图案支持重复平铺效果。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

示例图源如下：

```typescript
  <svg width="210" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1"  x="0" y="0" width="0.5" height="0.5"  >
      <rect x="0" y="0" width="50" height="50" fill="red" />
      <rect x="50" y="50" width="50" height="50" fill="blue" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="url(#pattern1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ue45WvtoSaewyE1SiPwKmA/zh-cn_image_0000002572641085.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=02A6E55DB465C43EBC538ECAB08FCD6824D402DA4ECD22A96B51FB2B521EC64E) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/bLMVRo5fS0Gbb2RCqF82kA/zh-cn_image_0000002542120778.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=B00FC88EB5F2747067F414A921436A316E0C002238E6B7A6A8EFA35FA458D81D) |

### pattern偏移值处理

支持pattern图案在x，y参数非0时，从只显示平移后的部分图形变更为显示完整图形。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="40" height="40" fill="url(#pattern0_0_37)"/>
  <defs>
    <pattern id="pattern0_0_37" patternContentUnits="objectBoundingBox" x="0.5" width="1" height="1">
      <use xlink:href="#image0_0_37" transform="scale(0.00833333)"/>
    </pattern>
    <image id="image0_0_37" width="120" height="120" xlink:href="data:image/png;base64,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"/>
  </defs>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/vV-EGMgVSJuITupvpxb6mA/zh-cn_image_0000002572681049.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=1AF4A3CA6653F93A3DA3FA8E88DF68ABB26BAD8F13B9FF2B4AA52C2BBD23F61F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kcHMnSapTWqg8EGGXsfOYw/zh-cn_image_0000002541961142.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=37788A657682F8CEC00D4D823511F970B99BD36C82FEB05AE6FC870E9008250E) |

### 线性渐变

[linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)线性渐变支持做平移和缩放。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <linearGradient id="grad1" x1="50%" y1="0%" x2="0%" y2="50%">
            <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="115" y="15" width="170" height="110" fill="url(#grad1)" />
    <line x1="200" y1="15" x2="115" y2="70" stroke="black" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/DlM-MBNTR26MZG3y8-GCeQ/zh-cn_image_0000002572641087.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=53F7FFBEBEF2DDB173F3921A2F98546975F2C81B2B89044B30B531516CB537BA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/wB6wF4R3TgG-eBvHWwLi9w/zh-cn_image_0000002542120780.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=4EEE79CDC4F4834479D64D4A5C686F1B02B5EB8FBE160712CDED706A0727F63D) |

### 径向渐变

[radialGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)径向渐变支持做平移和缩放。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <radialGradient id="grad1" cx = "50%" cy="50%" r= "50%" fx="40%" fy="40%"  >
            <stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />
            <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
        </radialGradient>
    </defs>
    <rect x="10" y="10" width="100" height="80" fill="url(#grad1)" />
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/WknhNiMLQfGKmvSrdAUh_w/zh-cn_image_0000002572681051.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=D002E4200064BECF0569AABC5C836B140A6B00BE0099D1C6B324BF5EEF18C639) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Qb326HaLRzWywKsu_se-6A/zh-cn_image_0000002541961144.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5F7BFFAD2A6072F15679A4691A971E2452D7C89F84B5BE32E1D2CA0D95C96AA9) |

### mask参数异常时默认效果变更

[mask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)遮罩的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" x="0%” y=“0%" width="100" height="100" maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse">
      <circle cx="50" cy="50" r="50" fill="red" />
    </mask>
  </defs>
  <rect x="0" y="0" width="200" height="200" fill="blue" mask="url(#mask1)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/qKivb77USP6TdFbNQSX2rQ/zh-cn_image_0000002572641089.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=F43D54D2148C5862053708B8673E1A60B4CA30AF93B623CB511AD053AAE767FB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/iNWSrIoHTK2oQQXPGAc8Rg/zh-cn_image_0000002542120782.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=55F99D17B19032B779A3257B316ECA20A750061B99EC50F2B65059F7CAD01DE5) |

### filter参数异常时默认效果变更

[filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities#svg标签解析能力增强对svg图源标签和属性的影响)滤镜的x、y、width、height等参数允许是数字、百分数、小数，当参数赋予错误类型时，从取0值变更为取默认值{-10%，-10%，120%，120%}。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

```typescript
<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" width="300" height="300">
  <defs>
    <filter id="blurMe" x="0%” y=“0%" width="100%" height="100%">
      <feColorMatrix in="SourceGraphic" type = "hueRotate" values="180"/>
    </filter>
  </defs>
  <circle cx="60" cy="60" r="50" fill="blue" filter="url(#blurMe)"/>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/T6IkU3fBSICZgN0pRwSVgQ/zh-cn_image_0000002572681053.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=5AAA05BCB9F159CCC413710353E6C8E5E82E684A4BFC635D90F566C37F5D732F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/D_37UJiBRQqo9_DVfNizFw/zh-cn_image_0000002541961146.png?HW-CC-KV=V1&HW-CC-Date=20260418T024435Z&HW-CC-Expire=86400&HW-CC-Sign=C897ECDB5D1EC3A00D1522C62F217EDDC981E607C4D6AC9439D5897EBA290984) |
