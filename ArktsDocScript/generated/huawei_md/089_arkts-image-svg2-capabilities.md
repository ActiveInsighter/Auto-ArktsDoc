# SVG标签解析能力增强-图片与视频-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/h_KWyUzhTnmb5QxEOYEfAw/zh-cn_image_0000002531795808.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=4521AF7F25BF97D9BF0F4ADCD5A005CAE9CB88503EDA98175715E2CA63188A3E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/sr3piskYS--eOkbo_r7QVA/zh-cn_image_0000002562555773.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=D128935AD0A2AD1A8363CC4D8EE205BD8BF8FF7E4F616CB94F2208F9AF43F10E) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/fj8REkhjRQK6BAzRURU64w/zh-cn_image_0000002562715745.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=6E07E5739796017E1DBEC32C6147A6245A8F2AFE36C9E2DCB699E531F29E2589) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/bLR1Jp2STwS9ohGJs544ng/zh-cn_image_0000002531635874.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=C74479BEA8E1234F51ED85F8B8DD0C7CBF4F37B62C80D74B07D7B79FDDC1F128) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/8MCKQNegThyTjLozioqMcA/zh-cn_image_0000002531795810.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=93723CD3C1901964BFE19641C3F039D2C0FE3292AC3CD5D5DC1633202E3111AB) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/OZFYtsGXQcyJNcu-LcGQ9w/zh-cn_image_0000002562555775.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1DC528BF4EDF7DE09FCD74E736719DBE40D0495F10B0EC6BAC3EB97D04D82BC5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/TCyOBjQdTv6R9HY5oYE3SA/zh-cn_image_0000002562715747.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=42E6D71D556514D55A01B2DF46BDB0FCA1EC7E0E8028CF268D02DAF03F2DE454) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/-KdWvsP2ThKkXrNLFuzxUw/zh-cn_image_0000002531635876.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=20B683ABBCE67839244E84967A6DF89833F5ABB5C0D5E62EA5CD4E790503AD5D) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Nz_iZQAtTYyzgOaTUD-MSA/zh-cn_image_0000002531795812.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=5645FAC2105170D04E18F72D042903258FE1D544E13AB4991E8D251D1BB181D3) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/tQTPXddXTcSDkEmdBJgtYw/zh-cn_image_0000002562555777.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=6B16BCBBAED7C4D74899D76043372E58297B324B6EFAAE5D28032C64BDECB2F7) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/x7GJ2kLKTMK-rfIocaDn3Q/zh-cn_image_0000002562715749.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=55C8FB845420EA409AECDFB99FD181D07689D0DDD218FEB1F7E1BEE6D511E351) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/MyNGwgWcSNmuTt20RIQ1UA/zh-cn_image_0000002531635878.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=F56BD347EB5649C88A0D1C4F8CD69DEECC0D43744748F2E8944E450E0C4B6AE7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/vr5OdXj1TNqSNXsjpAJBgw/zh-cn_image_0000002531795814.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=4B4B8994FBED6B3C965A4262CE561B508C3CE3EDE88E23CF58810FD6511FEF1B) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/VAGMe2mQSHiKX8Qjv-C0CA/zh-cn_image_0000002562555779.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=25B0E799A968D9AB41CA7CA4A45EBCB61BFD9A76FD7C6C430ECAF411CA7B104B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/HhXT3Wd4RPyzoyHNrGpr9Q/zh-cn_image_0000002562715751.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B047CAC5B18311F0E2DAE73B497ABCAC6DF0279D7AE44468A3D38D8EC81FEDCD) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/BLds0yK7S3aJ0dO4eTsHXw/zh-cn_image_0000002531635880.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1E4E24B080EDDE3036ADF970202F9B9A5CB9B812D6F3E6BCBE61FAEAB42DD15C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/zbQnA2PhQ_W5J_9deBQe9w/zh-cn_image_0000002531795816.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=D14F2594B32ECC921CDA65C1CDFE61BCA3E5F8B17BC907E6D0ABC96BDFB8A8FF) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/tGdbHktDTxq8y1amlOqBOw/zh-cn_image_0000002562555781.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=CE97726703A4DAA27AF8C7EE9A2E442A15B1669AF9327C8981B4BE6AF4710B4E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/LVp8R93uQKieuPUVLpBflA/zh-cn_image_0000002562715753.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B3D96DDBE0064BAD7DE9684ACF0870D869F4AD01A634979803F680621FCB29B0) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Agi2oYy2RNeG0EHyaM_ijg/zh-cn_image_0000002531635882.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=88865B27375469AAFD692CF52887E50B74686D8B70B6ABA7F70DB6E52A24FC06) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/kxb3_QZaSyGIEiUld5-sNQ/zh-cn_image_0000002531795818.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B4AC460BA412CACACD62B9668BDA707399A74ABFA066BC36B119619F41FCC2CA) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/OUednSETRTaEPRKbOr9q5w/zh-cn_image_0000002562555783.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=FAAD73470F1BCAF489D7BADB8B29395B7D04A2985B2D065C69E8D54416805A47) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/bs00mvIyRtGD6B4ZWGPOEQ/zh-cn_image_0000002562715755.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=20104FF8746F30D344F31224A4A10FAC9FA1375F9FF1E91D2977444EE753BB28) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/b-1Q5SZNSiOQ21ILmI14mA/zh-cn_image_0000002531635884.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=62FE8DA14360F0F6343E2A024E9D3327430B3162BAD9B28CD7874D050FD31E64) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/C0Vr6-hPQyqAU6_SXG-gGA/zh-cn_image_0000002531795820.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=8DB64AD21A09BDDF8E70790A93CBF8A5D57BAD1298875D5D2B22ADEFADBB2D4B) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Wrad9yf7QpO6WVXO_F5Kmw/zh-cn_image_0000002562555785.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=FC46ED9641E907C7F4AA6611F7C571D084E687A82A8251B5ED528468FBA6BCB1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/3LkeQUzbSW6NxVh6b2meAw/zh-cn_image_0000002562715757.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B90D0280DA8205B26E902D4C186FD57FBA272FFC10A366747F3F21267C8F6651) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/T6DL117bRsqxqOhhonFvtQ/zh-cn_image_0000002531635886.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=5CDA02DB990AF93AF3E7FB54ED212E1C3A16697B8C5C6DF3963C15E01FDF49C5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/-rF82AQ3SV2E2zdO1Oqdmw/zh-cn_image_0000002531795822.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=137706D2C10C424466FF11AAEF86A314D6F4F07F1FB7D45E95DD25C9BBE7EC18) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/3EzOfmxtRjKhQu5xuqLhDg/zh-cn_image_0000002562555787.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=3FAA79F021C1322219876F26DDA54C651C7FDAE294F2DAC7E525C26CF05ACCC5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/tF7eSHppSZascIRvCmou0Q/zh-cn_image_0000002562715759.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=D974643487AE44D31DF570865A3128DA78D406E147C70C9EE8620622DFC3B6E1) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/JGwQBI28R9m6lOcxW7qtQQ/zh-cn_image_0000002531635888.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=4A504B740491FE185CDD65FA949C966F785BC432F57FF968D1BECE0B9E35A882) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/SnXxSf3ORNS2JRMp36DFxw/zh-cn_image_0000002531795824.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1BFDE016EA35A1DC88659EE5AA0B6985ED795AA997C44C4939F5EB9A4B6C5444) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/iWZLeVmsSqunKsCrhc652A/zh-cn_image_0000002562555789.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1D67B69F3FBE27C58EE3176D7D4BB6019AC03EE1E58E3216D3B435A774C99F94) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wJt-BB-5Siyctn0vbgGJmw/zh-cn_image_0000002562715761.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=0C68C8CA4E67988F0EC9A8D76A3B99E2FF71F6F848F913580B33D836F8C64ACB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jSos4G4uQv-R8lwdfIp0NA/zh-cn_image_0000002531635890.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1EC6D2CAE68DBE7FC400D6C8ABD36EC7D4CAB53D22BA95FA48B9E30F20CCF86F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/e4YAfEzDQ1GEGOV4T8jSNg/zh-cn_image_0000002531795826.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=E105382E7A577953FA120F9A0FC13F7A6BBBAD441D9F4449A769CCE8BF8129F9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/SQYpxlVUSkecHLdeFQhXyw/zh-cn_image_0000002562555791.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=02B8685996B6AF1A470C94331C30B933C4810B87F1FA71DB9326605BDD0A9E43) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/IEWEeteHRDKPg3vLspYqDQ/zh-cn_image_0000002562715763.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=2D06137B65934FE6A1CD4DBFE946BCABC7028F85B76FCAEDADEBD5DCB3E4D8B7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/6Ew1N48KRdmRM6zV9aAsNQ/zh-cn_image_0000002531635892.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=736C017D1BD1964B4C4A9844C4A01F4A5C936AC299D67A7C79F8D39C329880EC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pRGL8iBeT7ChiCCwZCrGCg/zh-cn_image_0000002531795828.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=75CF26663C8CDB038D5DA279AF09D8693F4BE1C3BF275D006A729E9AB3BF4880) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/6fEgOpZ1TC-5GEMvy1nJ_A/zh-cn_image_0000002562555793.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=18134B23D92942FB641527A515081385171A371BB6EFCA25075E93DBC5E979DE) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Kl8W208BTVSJZHxqSvBRIQ/zh-cn_image_0000002562715765.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=7D4F33121C5F3F91A33B0AFF3A31FD90E758F468AFE5A1FF6B2F4FE5FB381695) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/7NIQ_yrDSiSoYySYJLB0-w/zh-cn_image_0000002531635894.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=AF3F197CC81D99BA35CC28B09671D0AF5FE6D2EEF1E6E637B95247B37BDE9305) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/XCUqO6jQTIGBvZ3HOwgJTw/zh-cn_image_0000002531795830.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=AEE9C37FEE706B2302DA4C2D2E3779D7912115BE3DF4050735EF19D6CCDCFA66) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Jo18IF8SQTOOQdxfkL-nGw/zh-cn_image_0000002562555795.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=C66D0E937696408BBBE571F904EB8B3FC6E1F8D209371F69C6B90D0280C540E4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/yjtsCiV3QPOU_H1U4p30XA/zh-cn_image_0000002562715767.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=FBD639C3778E7344848BCC4B7425E920766D4720551DF34F0FDF6A19740D113C) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/jvXuBvc3QlGugCmguo1i0Q/zh-cn_image_0000002531635896.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=58A1401FCCFAB5610D9835F47618BD4E9C67455A7022C584E5AE2CCD94E92959) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xbsjPaW-TFaRArLlxgvc5w/zh-cn_image_0000002531795832.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=5E8B808AAF3BDB7C0C6A6D7C0C99A1CC82BE6A9AB4305E0E19C000FF8BF35F0F) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/DCIZ34IVTy-9WUbgyFhOnA/zh-cn_image_0000002562555797.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=782ADC4476C0381A6C62F6EE40DEC4A94806D546882400A35BD182236F71A534) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ux8mmLzhSp6a-8dSqWWaoQ/zh-cn_image_0000002562715769.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=77C6C8F0DE676162F8055B92618F3C536EADC1D100AC7F00E34A55C47A6D09EA) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ad6OCbJ-SxegEE1U9yUnFA/zh-cn_image_0000002531635898.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=D88BCBBCB58E5AC5825814E7D20B2E0D18B6618DD5302B1309E1CEA5A7A474F0) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ru3X0fm7RS6rmUXp5dJcag/zh-cn_image_0000002531795834.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=0DEED39F259DDD8D9C483D8C6BCCAB85D4730AF7FFAA60C2019ADD5A626A3535) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/_PNRMflISuWsbENsKRMomw/zh-cn_image_0000002562555799.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1E5F3F02CA60A23031B3CDC856FA75751CA7ADAC1FF920E3DAFD33FC81EA6C21) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FAgPSnplQmW7HGHF2dPLjA/zh-cn_image_0000002562715771.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=44A205F4490802A266AF3195DBADB6F2703411CA856D670276489F7BD6553925) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CBtCMkVzRNalZZnkXCNNVQ/zh-cn_image_0000002531635900.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=8490C364203877EE25B0983927B3F0C1211ED85C62884D07E21467FE3EFD695B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Pt1hzSRTUSzFjaBPUstOA/zh-cn_image_0000002531795836.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=D98CA1DDAA8F189D99BF63639E411FCEBF09609731C3AA010BF0B10E7DFD713F) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QTDZ8AHuRdmF7v-SiN3Fpg/zh-cn_image_0000002562555801.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=9ECEDCEAB7950F60CB155D36E2FDB82037E32F3EE86BEA8C8688F0EEF4BC4713) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/mJN30AnSTaKbpLmqaeleMg/zh-cn_image_0000002562715773.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=E63BD92E2870555F85B78F9FFFE09260E8CC7DB08E8FDC3F4D1AD9F06955C1C1) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/2hf3WTKgSDWqHAtkdmXg-g/zh-cn_image_0000002531635902.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=9C5F08E68E2576ACC1DA2B4C3E801AD992D4D5472E80D289AAF17D41B596FFA1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/-Fh6F8cDTciGHPVWZRbQPA/zh-cn_image_0000002531795838.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=ED6E901CE9A0AD32B50E4256CAB59A6388CA22B8E47A109FBFA9AB8791D6EBF6) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/WTaTwFEEQUuGEowfaBkm4g/zh-cn_image_0000002562555803.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B79735BC82F553396BFD7AE3EA76622E29000BCB9D0DEE6F9A026E9C3960090F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Gv_wcxZoROm5twYWFcwz3g/zh-cn_image_0000002562715775.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=DD41902A3F55F519983DCFD94E625D95A021B56E066009B2D9777056629A5FF6) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/9fZ8hFmmTRy9ZgYfSKomrw/zh-cn_image_0000002531635904.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=AE907963A0CC681E3D3C34DC30D18E25B6B80E7C43241F656A073CF8E375781F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BYWIY6coQGqiei3A-mG8KQ/zh-cn_image_0000002531795840.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1553843F1C2FEE9D53FDA211F188796F0CA487B3F54CC70B918AC8354E4DFCF5) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/541A6utwRaSdHoHxBvbP7Q/zh-cn_image_0000002562555803.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1F9624ED621D2E614B621B3A57863493B7A458279A9FEABCC9C9032242511B11) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/NrL3D6mpS5C1PG0m0yTypQ/zh-cn_image_0000002562555805.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=AB8C4EF3153875D90851CD0895EC1AA5360DB57E889406692051FD6A23EC09FC) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/lE9FQo90RICMjYugNBF9Cg/zh-cn_image_0000002562715777.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=49C4602047F59A1A3620AEF1A8F41090054348CAA374695A83E62FAF8744196E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/bXALUmCKRlCZeBtV_ctubQ/zh-cn_image_0000002531635906.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=31D9DFA2CA6952DFC696A2E1B37DB6D57D666C97F26B78120F585A151EF904FF) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Z_taS6GLQxGdaSJecscqGQ/zh-cn_image_0000002531795842.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=E4F30CC1BB7A4A7510A70E1DC3210CFE83C3DA005951DF6FAEE47A79A91E1FBB) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/EY3JOH4HQYuFaLSdM53pXg/zh-cn_image_0000002562555807.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=DB26AF8C3FD2146043A387E12CFB4A134ADDF4B76C8F58522DCA29F777E3AFFF) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/4_6lkEnSRpmDMc6dsIqSHw/zh-cn_image_0000002562715779.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=68DDBA28A4B8BBF89ACBC1D0466B8FFA1F5BD420A0680E598E70CBD63CBD5704) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/vxui98mgRJ-qeEOs3SreWA/zh-cn_image_0000002531635908.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=030A7535DACCC59EBF107AB81F34A4D016F668C066D099E8288C5CB451FDA6D7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/j4TPmjrmTnC8F2ZPLcNlQA/zh-cn_image_0000002531795844.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=1E7B2CB3AFC52BD153EF5DF39691E19605C7A440DB9FE4F3F9B00E5B3098039E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0BzKjOTeRJuN9wMK4TeLEQ/zh-cn_image_0000002562555809.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=CAC6C0E7E0ACC418CAC26E7F5CD95D06C4669BCB3E4E75B2F1080CA553BF191B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Yos5SI-jR9K4B5NwenY_Pg/zh-cn_image_0000002562715781.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=0AF731F9ACF56780B354D4B510B0BD6FCD18CCEC08443F4A049D0B50294F0268) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/Xjg8-EaRQB6IfGoU75A6JA/zh-cn_image_0000002531635910.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=BAC7419D0A3D0D0E939FCB61DE697A7E5F9834EDB0BDEA05CD57D7D1CD8801A0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/rQSOVecsSOC9V-1zEwrjyA/zh-cn_image_0000002531795846.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=027A85CE9F1EF87F9499D18C5C0A28749736348E5EB1E76667B4E94103BEB1E1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Q0SwW_qtRdiZV8PIZIUAbw/zh-cn_image_0000002562555811.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=ACD152F24BBC6901EABF93AAF6C1F98900E9DA7C7FD0BA61E58C3DD0C602A04A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QhCuS-tjQ_yucXXTCVUE2Q/zh-cn_image_0000002562715783.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=E1285D9E20F88DCC0E8888FFD674046DE3F6BF436EDB017211EBAAA0CB9D5F00) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/vjakAnb-RGa3LG4JwZMGbw/zh-cn_image_0000002531635912.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=410DCE6ACA19E59529EE3DD757BF8819BDB909FFDBB23A7FAEB075EB71BF700F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/0e2krEYmRdSTreAQJgAzUg/zh-cn_image_0000002531795848.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=B81C5A8A4F2FF49A7E9F5A1FF485837B6B2FDB236FCC479E309FD7856ABC7233) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Ybgq1GGyTWS3rWwSIUeRmg/zh-cn_image_0000002562555813.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=3A1D9ECE1A58A8F88E380B9959CDD41528FE7CE05B4BCACDE0F5EC6448757391) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/agFmyU9jSlq8xGbLfIop3w/zh-cn_image_0000002562715785.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=8D18BA01914527650D2BEC0C947944EF0621989A53DB2965159DC40A3046B6E8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/cqKGkYrsQHS6IIqVtWgmKQ/zh-cn_image_0000002531635914.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=41BFC4FBD0B0AF911B7ABD52983D4A7D5BF3B651312663D2EFAEB76DC77FC26B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/la1Rl5cwTY-Am1uCPpjb7w/zh-cn_image_0000002531795850.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=8B964FFAF9A9D33A3287736ACE5E7AF98E7B19BF048C204F213ED510515643D4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/FwGz8KzdRXiCW77lmueFzQ/zh-cn_image_0000002562555815.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=4F8F4E14980DC9945BAB7131A56C7130584A4CEBDF6CA05F5FC3500D5EEE170D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/uniyeURnQj6fbFOTZiah4g/zh-cn_image_0000002562715787.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=31D0DC03125FF4157AB4D098B7B5BB086B2B91A0ECFECA8449EC86A3F7336C6F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/7XJZ7wNnSF-GpkWhQW8xJQ/zh-cn_image_0000002531635916.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=3F01F32EAF782BCCC1C414A88748CCBAA3F7F45A2430BA1CF10715EC9E49B3BB) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/0ZJOxWspSQC4xVruVB7e9w/zh-cn_image_0000002531795852.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=C308A5F412669C58533B475E29305B307B52A0D67367DE2AA35EB00669CBB220) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/uGBKBrxdR8GQKRVAb5Amaw/zh-cn_image_0000002562555817.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=A1BADE5C72D50ED57EBF3AD2C5090B767630F2E08584D22D124D94F36F81848C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/JVFI-W_gSfK8zt__z_hxZw/zh-cn_image_0000002562715789.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=57887802C35D28EDA455387BCF50601F79BDF374D094A4E0E21C8A84C0D6A6AE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2bv1AI3kSt2KNbe_xjdWRw/zh-cn_image_0000002531635918.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=81B0928049E2E6DA89FE085AD366AAD31765CECEDA493E78B9F843C6E5198A0F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/TyXde3TeQXayTvFk2L6Iaw/zh-cn_image_0000002531795854.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=FF8211570072AB4BE46461DBB49EC2CAA5CE71C8543A4B1627D838A6EBA5CEAD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/oJOCuFj0RCS3DRHu51kBsQ/zh-cn_image_0000002562555819.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=F614A9BFCE95298BDFDA5906BF5B298414D77A166BBFA6F9A64BC17C1FCE39F4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ZEahGsjjQXa2Kpz4MTTa-A/zh-cn_image_0000002562715791.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=DC1EBAD7B78D3D14E8A390E82F0A791A9CF6C26F6EE635D612105C9A7EC71692) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/laP3vlIbTLWRJg4aBnsbOg/zh-cn_image_0000002531635920.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=611EFC16D58FDD2705D91240BBAF95701403AE23BEE9DBA7DF7051F82C63A4FB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Z5QzckrXQ6uWGW_5K3BSxg/zh-cn_image_0000002531795856.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=6626086AF97FC0AEB4627C0F8CFE9A652BFE6B77CFE0F120497336149C417E72) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/kMGwC0X6SM6O2eUQBurixQ/zh-cn_image_0000002562555821.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=45BD3A1F7CBB4A2D66464AABAE3B9987335AC41DF73BCD268A26917B431CF585) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/pA1TKvqXQaKPea3PcdD8Pg/zh-cn_image_0000002562715793.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=C17DE846531BDD2020B98A7B2E15EE246AF2FB1BECF580EB8846991069227425) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/XME4nQNkTdiOfsdV4EJeVg/zh-cn_image_0000002531635922.png?HW-CC-KV=V1&HW-CC-Date=20260325T023330Z&HW-CC-Expire=86400&HW-CC-Sign=EE512AD841F2EF10397209D22393A36F01A7D76EE9BD1FF10406B1EAAD467D92) |
