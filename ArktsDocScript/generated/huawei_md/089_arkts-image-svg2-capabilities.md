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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/h_KWyUzhTnmb5QxEOYEfAw/zh-cn_image_0000002531795808.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=F16F56BE4E8D0325C355167F55A1539E1FEDF121BC3D0C52FC9AE145FA0FF538) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/sr3piskYS--eOkbo_r7QVA/zh-cn_image_0000002562555773.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=9E344090F5B053BE47E8D7F2CC909DBBD6C6A0DF371A350CAD43BA641F4255B3) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/fj8REkhjRQK6BAzRURU64w/zh-cn_image_0000002562715745.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=9760E88A46347A180EE49580688F61A62363D8D3063C2789C5DB1D01962E46BC) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/bLR1Jp2STwS9ohGJs544ng/zh-cn_image_0000002531635874.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=DA0DB923C1A151CA71600EAF82BF373023E7E0F09C95DE0EA0D3D319398FEB49) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/8MCKQNegThyTjLozioqMcA/zh-cn_image_0000002531795810.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=22A86397788EC871770F4FD693F60B96C8904B5D1F3151EAAD47C1AD108EEFE2) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/OZFYtsGXQcyJNcu-LcGQ9w/zh-cn_image_0000002562555775.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=A6B2D219AF723D284C4C2D95C1ADAA3AA69ED86E3D75779E80AD961831BA5AB2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/TCyOBjQdTv6R9HY5oYE3SA/zh-cn_image_0000002562715747.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=ACD136BB0E9384B863AC0816BDE221C59E773C252AE6A272FF5CE72721DA96EB) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/-KdWvsP2ThKkXrNLFuzxUw/zh-cn_image_0000002531635876.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=EA2DDDA9F892E20C5330728232992328DA5F1BF4C9E1DD6216333F6064E384F2) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Nz_iZQAtTYyzgOaTUD-MSA/zh-cn_image_0000002531795812.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=84961949065E34D312606822902B29947DEDE0906A44E143DFB740310D3DF0C7) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/tQTPXddXTcSDkEmdBJgtYw/zh-cn_image_0000002562555777.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=50F511C3B447099EA90CA7661D2CE907670459D2808FC9D2D07182DA91944F89) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/x7GJ2kLKTMK-rfIocaDn3Q/zh-cn_image_0000002562715749.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=F0AC4ADDF3A91BE9FA9E5A6C5AAF822630EEAEC58E3672C335152D884654E411) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/MyNGwgWcSNmuTt20RIQ1UA/zh-cn_image_0000002531635878.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3620795D850E7BD7C76BC7ADC425DB8980187E61058CE46EB0A150A6CD951DC8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/vr5OdXj1TNqSNXsjpAJBgw/zh-cn_image_0000002531795814.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2FDEF19138145544D0E948D3AAB71745B407212450C2CBC84D34E4D846326735) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/VAGMe2mQSHiKX8Qjv-C0CA/zh-cn_image_0000002562555779.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=121AAFFC94B5E2C147BC07C70129447403D1629CB7717FEDA36E0EC2306D0DCA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/HhXT3Wd4RPyzoyHNrGpr9Q/zh-cn_image_0000002562715751.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=12FE43BE47B304B2C6B7FBBB3ABFE7445D0CC778B66160BFEA638F900A01D232) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/BLds0yK7S3aJ0dO4eTsHXw/zh-cn_image_0000002531635880.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=093BC35A4E8166F5912FA7E92E642BA41000483FC85FE86215C04F86B3819575) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/zbQnA2PhQ_W5J_9deBQe9w/zh-cn_image_0000002531795816.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=4DBC550FD75120571933C67ACB280C802EC2D4EF058BE5D638EA77BCA53A7305) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/tGdbHktDTxq8y1amlOqBOw/zh-cn_image_0000002562555781.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=B7F19A022773FB5E2B4BDA37DCAC7CFD7F4767C7D1AB38AF07533B67DA59B42A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/LVp8R93uQKieuPUVLpBflA/zh-cn_image_0000002562715753.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=765B144546AC7FA1904C3B73689597575121897D2476D65F013148321A01EE04) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Agi2oYy2RNeG0EHyaM_ijg/zh-cn_image_0000002531635882.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=1A62F57320A18C6ACC95714797F96BAE87CDAC0568C32629A120E3293C3F2585) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/kxb3_QZaSyGIEiUld5-sNQ/zh-cn_image_0000002531795818.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=72D96E74B92AA194F5CCEED7CD3618C3B5266658376AE0491440A2E5BFAF2E31) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/OUednSETRTaEPRKbOr9q5w/zh-cn_image_0000002562555783.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=9C133C58966BEBAD3E11EC4D7A87AFDD33B9944E5A1AB73FCDEE9CA9079CA78D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/bs00mvIyRtGD6B4ZWGPOEQ/zh-cn_image_0000002562715755.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=C7B5EDD86F9B6DF6762A3E29A93DC9FEC168FD7E7D0B22A45C82BAEE49E316DE) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/b-1Q5SZNSiOQ21ILmI14mA/zh-cn_image_0000002531635884.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=7C14C6AAD85B4C376669BA523EEDBE25CAF8A206F5E48A5A26CE123CF1D8B592) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/C0Vr6-hPQyqAU6_SXG-gGA/zh-cn_image_0000002531795820.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=18AD25EB45AFC3B254D0FC8EEB6F2F4EA13FD134661CA3E2A17E05AB70C8CFDF) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Wrad9yf7QpO6WVXO_F5Kmw/zh-cn_image_0000002562555785.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=A08DCED8BD1B9C37FF16E864F1771CC986054167A794A7731C189739A6E3A24B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/3LkeQUzbSW6NxVh6b2meAw/zh-cn_image_0000002562715757.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=FA1AA7449C16DFBDD665CED90F493EEDED72FD101B29D09022DACE2DA08705F4) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/T6DL117bRsqxqOhhonFvtQ/zh-cn_image_0000002531635886.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=58F4626EA0C866D81B49027A7BED67EA650182D802F7A01480DC9D744794C52F) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/-rF82AQ3SV2E2zdO1Oqdmw/zh-cn_image_0000002531795822.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=C7FE82AF66BA0910C9D1C1EB7AC4D2B8C4A9D980385B2AF27730B58D376F8BFD) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/3EzOfmxtRjKhQu5xuqLhDg/zh-cn_image_0000002562555787.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=FFDA153B90A71895BD1313226C5A77D19211C3814E9F795F14A9787B28887F22) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/tF7eSHppSZascIRvCmou0Q/zh-cn_image_0000002562715759.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=86BD0CC839E12559B29EC4253C8879491372A472AF2FBBFC407873FC532FEB01) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/JGwQBI28R9m6lOcxW7qtQQ/zh-cn_image_0000002531635888.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=4BEFC5ED5AFBB7E47B8DEBAB4FA05A089037858D2304B268857A3EB9205BEA96) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/SnXxSf3ORNS2JRMp36DFxw/zh-cn_image_0000002531795824.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=5DF8A7638D8C7CDFA6A5B301316355795DE85390F198C4894D6BB109A923796A) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/iWZLeVmsSqunKsCrhc652A/zh-cn_image_0000002562555789.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=32CC5F094889302A767B73544B3A68A2F709434B1422043B09A433261FF78A9D) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wJt-BB-5Siyctn0vbgGJmw/zh-cn_image_0000002562715761.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=F38FDB8DA84724223615FDE5D892FFC2694F8580AE18009BABE4818A4D66BA0F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/jSos4G4uQv-R8lwdfIp0NA/zh-cn_image_0000002531635890.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=7CD0B5737F6BDDF207DEC6DE1A94D042EF8640EBB100938546C80B7D60E522CB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/e4YAfEzDQ1GEGOV4T8jSNg/zh-cn_image_0000002531795826.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=F039FE549F92FB60CAA09C14371FE41E388A293FE8119BCB3A8FB49110573BB2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/SQYpxlVUSkecHLdeFQhXyw/zh-cn_image_0000002562555791.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=BCD4B509A2DCC0F1A078631EA53EB46589A368E4126669438518CA836F11393D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/IEWEeteHRDKPg3vLspYqDQ/zh-cn_image_0000002562715763.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=DE6AFDCD6AA0F9A0FEB9C37C562900495D0CECF433303D12294A109BDB291EA6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/6Ew1N48KRdmRM6zV9aAsNQ/zh-cn_image_0000002531635892.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=9BC0E81114B6555D50BDA67876C53CACE61D3F95875DD3F644A1A6DB8D5F08BE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pRGL8iBeT7ChiCCwZCrGCg/zh-cn_image_0000002531795828.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=D74B7AA78BA5ED3D24976D9334CAC88279C75BE53B7D91E065A85440102D37FB) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/6fEgOpZ1TC-5GEMvy1nJ_A/zh-cn_image_0000002562555793.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=08B77B7C11CE39A68A32EB138215C7D67FAE7828B0C9F75D860510DF27958A48) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Kl8W208BTVSJZHxqSvBRIQ/zh-cn_image_0000002562715765.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=8C35CDE085CB6F06D12A717F7B1622C8CF48B92D857114DD1E858EC019420AB2) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/7NIQ_yrDSiSoYySYJLB0-w/zh-cn_image_0000002531635894.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=97033F09533C98C41E60B0F6428718E633B8B10471D6D09C2882BEDAD1B3691D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/XCUqO6jQTIGBvZ3HOwgJTw/zh-cn_image_0000002531795830.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=94373EE92C3FA9A641BAFB1ACDF8A4FA1FA3E646C979B3F7A8630DE7BCF5A689) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Jo18IF8SQTOOQdxfkL-nGw/zh-cn_image_0000002562555795.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2C3EC6B2720296476057298701D2E487A0262917440AFE531CD752E0E38EA311) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/yjtsCiV3QPOU_H1U4p30XA/zh-cn_image_0000002562715767.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=8B8B3624144DD6815BC1FED0B11540411076983888167A7634780057D18D3AD8) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/jvXuBvc3QlGugCmguo1i0Q/zh-cn_image_0000002531635896.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=9E2FB220EF89CC36EA235E2AB961DFEF60F6E1BB54DDB17D447C87A7389EFD6F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xbsjPaW-TFaRArLlxgvc5w/zh-cn_image_0000002531795832.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2CF82262DD875A24FDFD5E7542B19FC36179D45974F4EF6C1942ECC8490ED9C5) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/DCIZ34IVTy-9WUbgyFhOnA/zh-cn_image_0000002562555797.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=0ACAFFF8FC67BBA30A2212409A70985762690673E09AAFCFF72940A28F930416) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ux8mmLzhSp6a-8dSqWWaoQ/zh-cn_image_0000002562715769.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=FEA99C75557EDABAC2EECB2B5AA4DDDFDEB816E178EFDF09BF1CC378F18F8E73) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ad6OCbJ-SxegEE1U9yUnFA/zh-cn_image_0000002531635898.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=A3B88F276508D8B86EDF0B9AC3A0B07D67400D7C05D92C94DEC626A53EDC4C2E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ru3X0fm7RS6rmUXp5dJcag/zh-cn_image_0000002531795834.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2EDBD5D2AFE336D3DE14A7C116E8EFFDD8C888D75EE743E5A3B2F383E1BF40ED) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/_PNRMflISuWsbENsKRMomw/zh-cn_image_0000002562555799.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=327DDCBB7E22B90843A6E6E931C6176AE7D39043CAD4BB29DC0B9E5506C6AFE1) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FAgPSnplQmW7HGHF2dPLjA/zh-cn_image_0000002562715771.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=19D45F958D18F6F928C463174961FD77FB087BD1FB7282204781845470D1CFA9) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CBtCMkVzRNalZZnkXCNNVQ/zh-cn_image_0000002531635900.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=512E8EC4C00F18C4CBA78246B1B0D9D961D8B2A96F72B50CCFCC0AFD0A7EF6B0) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Pt1hzSRTUSzFjaBPUstOA/zh-cn_image_0000002531795836.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=D70205A17268C61ACC815BFD8530990838D008B177D72DA1F92AB1232203C98B) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QTDZ8AHuRdmF7v-SiN3Fpg/zh-cn_image_0000002562555801.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=60EB01E739BD7AD3AE1F399005B0084A915FE829E31953D107CFCA51CEF14AD4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/mJN30AnSTaKbpLmqaeleMg/zh-cn_image_0000002562715773.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=D7509B79A1F3F73C1A552888006A22E416377CCB924E9CCEFA51689E51970477) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/2hf3WTKgSDWqHAtkdmXg-g/zh-cn_image_0000002531635902.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3BEEBB10BB31C43BB476F7C3E299EF64F991EEDB01FD4CF23D68F225FE9AF7B0) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/-Fh6F8cDTciGHPVWZRbQPA/zh-cn_image_0000002531795838.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=1A2E93C21244F54791DA7C39433944641508FF5B3558872CCD24F40DA207C8B8) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/WTaTwFEEQUuGEowfaBkm4g/zh-cn_image_0000002562555803.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=B63C62CCBFC707ADBD55CB72995FF73486B4190AF2964E320918FA67E1DEACBE) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Gv_wcxZoROm5twYWFcwz3g/zh-cn_image_0000002562715775.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=43D258C0F1806A89523234792B6EBE9F585B08D48565373A6603748219B6AE15) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/9fZ8hFmmTRy9ZgYfSKomrw/zh-cn_image_0000002531635904.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=90B068D84F53CEA1CDDE2D91708F1FDFD07A802F6AD1FFB54443396555F967F6) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BYWIY6coQGqiei3A-mG8KQ/zh-cn_image_0000002531795840.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=0659FD8E15C6F4F5ECFCEEB61B57809558E9741A1A9B454DC27AC4491B7249D8) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/541A6utwRaSdHoHxBvbP7Q/zh-cn_image_0000002562555803.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=302EE16970FB6BE7DE51E3F993A0A78696CA64F3CFEEE0A1223A25FE0A9BE33F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/NrL3D6mpS5C1PG0m0yTypQ/zh-cn_image_0000002562555805.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3970A163665967903DA4C3F671C3441787D733D78E6D6D1318B166F2F6C2A924) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/lE9FQo90RICMjYugNBF9Cg/zh-cn_image_0000002562715777.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=D7D3840063C8745DCDF90322FA6A0CA300788FBE6014A1BED76738AAF8FCD83B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/bXALUmCKRlCZeBtV_ctubQ/zh-cn_image_0000002531635906.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=EE882E43B122F5F32C709416972AAF011743E7CD4C8DE32036EDACC9E193F031) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Z_taS6GLQxGdaSJecscqGQ/zh-cn_image_0000002531795842.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=E406B1AA966A7CD59922C81CA15568A516C3E7EF0F90BFFAE4E8697E89C2FFE2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/EY3JOH4HQYuFaLSdM53pXg/zh-cn_image_0000002562555807.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=EB595E51F2A94C233DF46AF1B9B2CB61AABCC25125B7D661E22C42E2656A5876) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/4_6lkEnSRpmDMc6dsIqSHw/zh-cn_image_0000002562715779.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=278042EF3A6FFB05B2D599B60AAFBC34737A2AE71A5615ADF6360E7209CCF03E) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/vxui98mgRJ-qeEOs3SreWA/zh-cn_image_0000002531635908.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=06CD7C8F78C0F49CFF095F215FE3145B931493531E072B94C91E56E6BF44F5E7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/j4TPmjrmTnC8F2ZPLcNlQA/zh-cn_image_0000002531795844.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=77B07AF616F39465FCC912DEE82D6054B7E6BF68F2978A12C4F7CA89B3752BEA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0BzKjOTeRJuN9wMK4TeLEQ/zh-cn_image_0000002562555809.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3B60BE09B1DA18ADB04C81D7DB33AED086FD89939E453F2B9B6B18F0701E8B0A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Yos5SI-jR9K4B5NwenY_Pg/zh-cn_image_0000002562715781.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=86DF2FCF8937A6EC155E4C299DEE0E99E4C58F6AC3AE885A38B6CD87820243AF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/Xjg8-EaRQB6IfGoU75A6JA/zh-cn_image_0000002531635910.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=6E3F6D573537DA2498452F54B4AC0BDD6C4DF77E64A6B0F00D1BCA724E5314D7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/rQSOVecsSOC9V-1zEwrjyA/zh-cn_image_0000002531795846.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=7F2DABFE9189B8D80829D4876806EFC6C56FEB60FA77CD4F2A4BA4D22FC7485E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Q0SwW_qtRdiZV8PIZIUAbw/zh-cn_image_0000002562555811.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3A60F2B1948FF24361D41514DDE9568307E50918E8156C88675D6301B50CD0B5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QhCuS-tjQ_yucXXTCVUE2Q/zh-cn_image_0000002562715783.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=3479923D1BEF3F3D95241D30CE17D087EF1E8DFB32317157702F48334600ED46) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/vjakAnb-RGa3LG4JwZMGbw/zh-cn_image_0000002531635912.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2062D91B99551AF02DB1E3A1BC4B7D8A8EC6E5D38B01C47E60DA443D33062312) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/0e2krEYmRdSTreAQJgAzUg/zh-cn_image_0000002531795848.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=BB16986EDBF43E718CB84B42B4021DF3D838F672F023B2439F540C4D9FD70FE0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Ybgq1GGyTWS3rWwSIUeRmg/zh-cn_image_0000002562555813.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=99CC173A15E8DBD1BBCED681B23B9FB729FB16ACB552B1344F5020C712469C9C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/agFmyU9jSlq8xGbLfIop3w/zh-cn_image_0000002562715785.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=22E16FF4F009162A0DF323890044A5327FB7604F94CE05405E69E766D4E3E0AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/cqKGkYrsQHS6IIqVtWgmKQ/zh-cn_image_0000002531635914.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=648ECF8DA27BE44B48E5D20B672563B41FD301B8570084D6875F2EDA272E5067) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/la1Rl5cwTY-Am1uCPpjb7w/zh-cn_image_0000002531795850.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=5B840881A25B0494A67DCDC8179C8FFDD476D1360F16620005B4CA02C22864AF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/FwGz8KzdRXiCW77lmueFzQ/zh-cn_image_0000002562555815.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=A4DE0A122F9958906BA5767C76F3CDB348B4ED1E7F82A188E397954E95C40A98) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/uniyeURnQj6fbFOTZiah4g/zh-cn_image_0000002562715787.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=00DAC3B8E08C3A26D49C294B7FFD1C18BB013948A1D2E67C0010D0A72FCFD276) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/7XJZ7wNnSF-GpkWhQW8xJQ/zh-cn_image_0000002531635916.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=703840CA539046EA27144E90DF82777CFED47847D63A2222AD5C35865C4399C2) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/0ZJOxWspSQC4xVruVB7e9w/zh-cn_image_0000002531795852.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=B32E57FD6F1706AEADD795EBF3677D8201E95402C9115E4ED15890C2BB00A774) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/uGBKBrxdR8GQKRVAb5Amaw/zh-cn_image_0000002562555817.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=F9ADC9F3F8595D8DFFCCC7638A1055F9EC701A4A8A19B88B0D1162D005916C8F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/JVFI-W_gSfK8zt__z_hxZw/zh-cn_image_0000002562715789.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=D9FD6483E7F2D6B9917EA641D3DFDB24B4925F814FF2B09B59928372574CD836) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2bv1AI3kSt2KNbe_xjdWRw/zh-cn_image_0000002531635918.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=C0325A8B5964EA374760BF12E1B6ECBB15366A36D63C38F3814041108E3F3D32) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/TyXde3TeQXayTvFk2L6Iaw/zh-cn_image_0000002531795854.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=183BDF123868B16135FA07ABD1446ACD597D40EAD9B58F9BE0B04766EDA30FA7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/oJOCuFj0RCS3DRHu51kBsQ/zh-cn_image_0000002562555819.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=43567370E58E65408168B938ADC603474211C77835FFA1D913326F3815A3204E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ZEahGsjjQXa2Kpz4MTTa-A/zh-cn_image_0000002562715791.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=0CB31901A8136C1A28401D6D92EE5F5AC115D8A9C32A1C7343BB57CA7C445FBC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/laP3vlIbTLWRJg4aBnsbOg/zh-cn_image_0000002531635920.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=2AE08A22952CA1FF8D34417B58C26E312F227239159F5D1B2087B23B33C8E5AF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Z5QzckrXQ6uWGW_5K3BSxg/zh-cn_image_0000002531795856.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=E3963528A24E2F1D313E3B9AE6D24C44D9711005BC441544DEEEB72B2FA2D0AE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/kMGwC0X6SM6O2eUQBurixQ/zh-cn_image_0000002562555821.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=DAD44CFC595079131515A78C2207F191154795762E332A517789ABC5C923723E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/pA1TKvqXQaKPea3PcdD8Pg/zh-cn_image_0000002562715793.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=AC934A6670AABFED2A84A229CDEB9263C437452773F0BE844B59F23C74276477) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/XME4nQNkTdiOfsdV4EJeVg/zh-cn_image_0000002531635922.png?HW-CC-KV=V1&HW-CC-Date=20260324T022826Z&HW-CC-Expire=86400&HW-CC-Sign=0868DAEE535C0DEFAA6659816D96BFFD5DFA2AD0F606E24DEB1BECF11E4FB780) |
