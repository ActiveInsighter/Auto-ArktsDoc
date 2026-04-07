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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/U7rdcJ9lTzm68awuktHtfg/zh-cn_image_0000002566869369.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=3957D9AC714CE4355CCE4316E412D7935A4F3E2A0E67C9505E7FBE7408C79A7E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Chv8qEXQHe1rB4XeVdraQ/zh-cn_image_0000002566709387.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=2C218F00FEC420DB78B3878182D46A78578948CB1B6852442C3D28463EFDAA72) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/YO1-A2xcRuyklvV_JOhjKQ/zh-cn_image_0000002535789592.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=877822D052150B84580393F0935A93D5021249D4300B8402199A53C8A7202C2A) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/icj2yO_MROKol4D8_t5nYA/zh-cn_image_0000002535949538.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=73F5A9DA0EFDB3CD10121B33383C95543BA549A4F287B2C606EA9A8F38A0C66D) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NXM2Ut2wQEam3LHCIBp7Qw/zh-cn_image_0000002566869371.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=08E8BCF9FD9E42B7EF5D3F1792F1EA8C49970E942EAD33356498BDE83344264C) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0pMboDzTT3eaWJib2Mq5Ww/zh-cn_image_0000002566709389.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=C438EFF034C0D33DFA0A86F3E14816F7125B0A7A705ABCDB9D0C93F96769F8C0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_XzI4LNsRTyrw1Je5Lf5nQ/zh-cn_image_0000002535789594.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=F54286FC822837F7A611E1EDBEF4B6C4FCABDF2082B1038C90F49C45E3C6FA4B) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SrH2BHLLQrS91FqXrOzktQ/zh-cn_image_0000002535949540.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D213603EBF6DFFAC353DF339C7824A0DDF76E85638FCF5AAA5125F3473EF8357) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aC9PrmH9Tzev4O-2-Z3RiA/zh-cn_image_0000002566869373.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=A6D0E31BF0E7EB487C5B7B20FA3F49CD64218FC77C5F19829C49F475E51420A4) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sLpBbvpnRAysuEMqySw9eg/zh-cn_image_0000002566709391.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=70561BD4EF61BEC0A9DC0CDBF147BEC3065C3F40C48BF194F9DFE4F2C253B772) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/IuujT5iTTk-rOynEyl_WyQ/zh-cn_image_0000002535789596.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=8C4AE856F9DFAD1EEE7B1A895998E555CBA0E3B82A3817BCCB67B5965CB13B71) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/aC8JK6VsSZea7QwA2VfaOw/zh-cn_image_0000002535949542.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=645D3E535748B59A85141B68437E12FF0C2235928E7DE3B0E80A8C7240077A79) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vqR5ddigQ9ywC1-CCaaYxg/zh-cn_image_0000002566869375.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=DB413F8BEB2AD4974AED6A66404883176A62B034572E5F1C002BB10C440A6586) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UVr2aZoFRG6RKZYWyA9KgQ/zh-cn_image_0000002566709393.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=FB82F1B9207AE10717ADCC9B34DEF13ED586BB841A8A6E4C6AB5664E37D9587D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dJCNjPOfSF-njYTsv3XG0Q/zh-cn_image_0000002535789598.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=8CAA1B3FC069A0831C6629E58485B806FF26992A972A7F01FA50AF8E80CD8335) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/SFRTzRgiQN2euBnwvn7IhQ/zh-cn_image_0000002535949544.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=82891FAF177BAABDDAC04E9D70D658AE7069E1E113B9DF8568710FE415BF6563) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5NTEzPD7QkyUuvqZO3oEsQ/zh-cn_image_0000002566869377.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=B013172B1778B49DC10A7C644390FA19CCB33E198F6C14DBA00CF6CB7C755BB2) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M3F8wzf8RY6UZou75gGF2A/zh-cn_image_0000002566709395.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=2CA4B4BD56BC3D77EEAE13CFCBC84F7971B190AEB2D780A9A3066279091B28A1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YTYpWPzlQouj7C_sliIgCg/zh-cn_image_0000002535789600.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=637EF7984497FED9BE70DB2250E7FFB9DBC4CD64D2324EE5CC9BF652A9123F57) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aKZHl6rFT9G7A8y_97-bgQ/zh-cn_image_0000002535949546.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=C5CE39B1A0284FEF8281FD2314F54ABF8EAD3187583ED63114B989CD4973605C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5Fk2t3ozQgm_lnODTyBZkw/zh-cn_image_0000002566869379.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=AAC4BD9D9FCC32CE867F12650C464144B5367CC4529B8B409B8BE77505FAF8CB) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2zHQsYs7TwCDioiVXxo8Kg/zh-cn_image_0000002566709397.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=397C4ADF83AC44A053283D8C0D301332281DBC3B5FACFA777D2390C3A7719589) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qe1Nys7URrqMBhWcjS56NQ/zh-cn_image_0000002535789602.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=33E3428491972B13C44161A9D65B5A61586189988EDEC8CB5A320CCD82D345AE) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GN_uCkuVTU-cLupiYbF8pA/zh-cn_image_0000002535949548.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=A9B223D85AEEB323A6D87A1C0924534A2DD6C2104E649E24D5A102BD8A0C9E09) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/froqUDQCRk6qdwY6NtLA_g/zh-cn_image_0000002566869381.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=E031BFC8AFCB59D991C5C0A81397B8C9A9B9199A5178C21903AE03B4256A2A55) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/o8FG5N-9TLublhc6LBgn2Q/zh-cn_image_0000002566709399.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=F4C2B0FB28650E8D92C5AAAB1EE5360764610D0B7F5E76F40AFF9DD3C21CDAA3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w0xAT_SZSwGtKKcIP43-Rg/zh-cn_image_0000002535789604.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=EAF94EC7820395DC29E50F9EAA6977DD28164066F5F009E24D4191D190AA4FC1) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Nw1IL7FySiqsm83mmJvgrg/zh-cn_image_0000002535949550.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=B28A942E40D9FD677607C0AAC53E3E3CA713AD5341B1365E9E9FCD7C5355833C) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SH2Vi2bwQHy4iHinx93EIg/zh-cn_image_0000002566869383.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=33030CCEA819E6568A651CEB0779E404BB3F3334215253DD55124B27058B0A04) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eO5JgJI-T9-SUDEJRJ54Ag/zh-cn_image_0000002566709401.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D4101FF62C80B8D37D2801B6378A1CC508C1A311DF110647C012755F51F862DD) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/97Dhdj-xSaK-Z-2lunsg2w/zh-cn_image_0000002535789606.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=9284199254849D35932564FE0F1DB1DEC2132E335E01DBF3F4535BDF68D09820) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7szxUCnCS1OLRnqMCPBeCg/zh-cn_image_0000002535949552.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=B16AF777923927151899A268D1E68A37DA1D526AD21C1473262A63AB6794C968) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mGJhBKvgSjmdCGcfdi3F0w/zh-cn_image_0000002566869385.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=27A069247F63A6CEB16C213F5146C5041009E9BE428BA4A1F4E325EDFFFE8A9F) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OdN34v3KROaT37VOXwtjlg/zh-cn_image_0000002566709403.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=099FFDE772B62B49188A28ECC1502C5AD3A233FFD1F6E8CB3565082C3A829C64) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/19zg-bVLRoWH3VHfcTNViw/zh-cn_image_0000002535789608.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=9AD0C4B3D1261768D1696CB97B7A5BC5B4842C5BB1B1743C78B981AD383ADE4C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xIuMxN-9RyegGRL5dHaEJA/zh-cn_image_0000002535949554.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=E80C8401DAC1DD99756F607317E05FC7FD4B084FDAB050FCCEAF7B5DE07EFBEC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/VfEoizikRBeXtMe698hxSg/zh-cn_image_0000002566869387.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=A02AC538E2C89C7138F96C403C420AD11D753AD19B5221E6E0B0579D059D0F00) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wwhjfe1PRH-W78dl5NoIoA/zh-cn_image_0000002566709405.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=CBD82D59B1B5FAB65AC7D49F079BF91BB5C9ACDE40EB57421AED684807BBDF1F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1LNPgbj3Rt6wCFJKKRHe-w/zh-cn_image_0000002535789610.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=1D1999FA965114CB3D9810ED43D50D15E43BAB8A3835219D0C2D9AD0E627FE6B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-eh7Cr7VRFeJdcig6Hrpyg/zh-cn_image_0000002535949556.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=CF2E7EC2C3D1137A8736491E3D96463C51A3A802A13471D88914EEA2E2E7CB3F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Azb7Wy7HR9OdIRqK1DMvuw/zh-cn_image_0000002566869389.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=547352DCABE8F782DCD5ECC451A8F7F76A6802AF52A6428D1F19E70480859326) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CiQCW9mAQfS0hhJwMmvZJA/zh-cn_image_0000002566709407.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=2FBBA9E2FF15DA4E42A68535430A34651E5BA5B50B46157C239887324AE3618F) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/D8l8UXDfTSme0sV7RUpO3A/zh-cn_image_0000002535789612.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D8B0E527E9EBF74DCD0A2DC1A58013DF45A64F34D1899FA06A2416BE0DCFDA04) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_SOZVNmkSlijpq0jDaVKoA/zh-cn_image_0000002535949558.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=BF3682FFFD5BF59ED8B759C88AF6CED9F568B302785CB2BFEC12ABC96528BCC7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YYqFyBoGTA2vZXSDPZCjOA/zh-cn_image_0000002566869391.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=C47D1EF63DE43B9FBAEC9E1C50DB8058888C7F205F7AFB481175D3A9A5EE32A5) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gO5RYHc0RkuRbo8tl5cpUw/zh-cn_image_0000002566709409.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=ABA8EBCB86B4D58ED8D7A5023FD5A3ABA6664999539FC570DD03239EB54E6A73) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/u3J0eTcETKCFoPO2FGUlrQ/zh-cn_image_0000002535789614.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=4507ACE13E9B335E46A421A92C8442436C58E85807E73C0CFB851C33359B6D25) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/f9TxVgxLTDiVA9kr2x1xQA/zh-cn_image_0000002535949560.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=20432A95E34A9DB40B6E4DE0F5341BB943DF79D6518516E9BD3A9EFA76C9A142) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uxLUOaLnS92fwrXjhBgHsA/zh-cn_image_0000002566869393.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=E0C5BE153A5213FA5FA49F47BFE9D8AE41114359E123BC10EC962361B465CE4A) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wmjwYIcKRwCSIDy87TlFcA/zh-cn_image_0000002566709411.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=879B98F57756DC4E323672DDE884451E29F63053869CED11F2A0E1E7DB08974A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ta_HAbEJQYyYXC2lDfDogg/zh-cn_image_0000002535789616.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=AF8D11605E195CA1162232EF7BDBE79C84AFB7700EAE3439C396C5188B335CBC) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OrZn2KpkTiODEIzPWvuL5Q/zh-cn_image_0000002535949562.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=CA7A082AFD8D3BBCAF607B2FB28CC367B82E6E7148ACF794A86C7D7079844FAA) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Yd6hiKb5RrqmUCZ7hJqrsw/zh-cn_image_0000002566869395.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=86D7416249A05BF7216EAEA25D07BB214630D1C83CB4D604431B95C017BE5371) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/W7n6-EhBTuCWfiAxUu68Gw/zh-cn_image_0000002566709413.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=149240AA6E542F7E625E317BD7A2699CF32D1341EE550FF426C02B38C5BEE18E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UvPE1EaFR-aHXXZgrpvt7g/zh-cn_image_0000002535789618.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=FF9F060CCC5D0DF381FB55A143E435190EF1418CB259AA9D3E7504D1C83B6C7E) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/adwBfBfYQSSnRidIkB5IrQ/zh-cn_image_0000002535949564.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=06B0556524C27E8A21AA3CA761693D6F51C38B7153E53DBBF14F2271D137EAD5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/usfrYNLGQgushAeNs0NqTw/zh-cn_image_0000002566869397.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=9A199D87859DB82749F2BC865B566A257D1C707D918162542BCD069F0C5772B3) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YsZTJb2AQres1u2YP1q0Xg/zh-cn_image_0000002566709415.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=6805CC82FC67ED1E393D1ED08256480F9B4FB12F528EAF9D3BC0E13B12C9D444) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ay-KcBR2RWObY9boujQlbA/zh-cn_image_0000002535789620.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=1B3595F6BAA445337D9D2A04EFEBF3FD8A7585B40A71D65D43C1EDB6DF9C6A65) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pdJ0N-IBTwG1Fjo8F3ZcAw/zh-cn_image_0000002535949566.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=3261D3811F0DBD8087912F359253B4C391E2C375BFE6EBF779BD7BAE31F7C711) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dAqyaaSPQpuWimDA0trtQA/zh-cn_image_0000002566869399.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=E1F2E9C6E8DC6EC5CEDAA4DC0363B1F752E5469A9B6BD741DBFD02064ABA2DA9) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jz5EjXpbTy6Y7S23nNZ12Q/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=80B52F765FC64A430A48EF126B8DA66B8144D2F991C00D0F6671FF2B39D6C7ED) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D2m7NEm4TIGfjWasxLeddQ/zh-cn_image_0000002535789622.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=B65E170197060B0612164320168A8246E16E62665FBBB1C0638F4375A9592BCB) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f9Le-Z_JRPq2leN2NrqPhw/zh-cn_image_0000002535949568.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=3246FA0D8B08FABC5EE47324A09DB559A33105F3B38A4AE0693322C463327E25) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XwNU10qRRQeSCmkd5xcF3A/zh-cn_image_0000002566869401.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=71D9AA9C4771A51F9FEEDAD0F635DD6B29BA0F5F4A29F8734F89026BBDCC33E5) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TMWufEkPRC6JEZpbkwBibQ/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=6A2F81199DC87EBE60B412EF386576D544DE1DAF7551B5020E3346A34D8E4374) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/har11OZAS7K2y-7K4Fs8Ow/zh-cn_image_0000002566709419.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=6F5CA7DEB27B721D683A3E6F157A4CE934366A7B95885618886F10DEE46D2725) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/MqFJOAc6Q9uAP14cHwhNYA/zh-cn_image_0000002535789624.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=AB998E14C721121B432E4F67028CC346C6FAD61A1F4C3FE0EFD0102FF4BCA98C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/FJbQ5BzBSd-8SVEoTOvi_g/zh-cn_image_0000002535949570.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=8670189B53CF790512BADD1B402BEC4C732A6FDD9BF2DF015D70402469400C10) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/p_cZt0amTZ-zEkmhX1uWpQ/zh-cn_image_0000002566869403.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=69523D2B4AEA226D8750DEB5399BA6AC41D18E382784D38E1D39BE9EB5628E9F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hIBpgsKuQOKj7xsM3xyZ1A/zh-cn_image_0000002566709421.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D55C25C3CFB5454D713EA1A99AF40697B499DF14FC22987A13DD7A90B126B643) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_EqLXtnEQxSa5ahDTGuidw/zh-cn_image_0000002535789626.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D045743DC08BD8FA4BEA1518FB59220DA083A3A07D1652CA3F6C9ADD6105F71D) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zgPVm-4YS92H2vCY7LkpwQ/zh-cn_image_0000002535949572.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=5840849623C90CA699CE030C89B73C8F55BBC55E9E3F5F5790F002E2B556F370) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3c9ltMn2R7WokEmt03mzQg/zh-cn_image_0000002566869405.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=393BDE23C1DAEF4E7979A963F403EC1F7CE99F698E318C8B3303FFF501DE1991) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/64B1Gu0oSpuS8cDQNY2QxQ/zh-cn_image_0000002566709423.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=5E34AB02F3AB3DE95C969A6B749E228A0799B7238E3664CFB86AEB1B8E2442B9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_-UVeHd_TDyEuVsL1BGigw/zh-cn_image_0000002535789628.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=699D6354BCF70E5DBD18EBDA43BDAF7D6C4AEE2F3BF5D5FF43E6BD5779269566) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qObFmpDdRHagpRUC6OAHmg/zh-cn_image_0000002535949574.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=4033461BDAD696C5A210302D01C69F45A2989722585AE11D4467E6B4BFDC8689) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/jCCjt3UZTse5bSw-QoVeuw/zh-cn_image_0000002566869407.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=978EDCFBC1FA5B19DE9B45A570CF6AA2509C2A5D20D60CA175A3B852C3E035EA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uai-LJEARh6vKW1mUWSuxQ/zh-cn_image_0000002566709425.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=3B4358CC20603BDC97D2E3B573E3E6B9A236DEBBF55195769B32907935B21CFF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WizO8OTLS0SYRoZhqBTBgQ/zh-cn_image_0000002535789630.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=C6B0C9D8BF97C0731606E640438149204D8CFEA9E117F8AF4DBB3919A4450481) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eIT7t2u3QZ-ORNFF2AooKw/zh-cn_image_0000002535949576.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=C5096ECE74D957B36A5AC5CA06DE4BC095C994F833DA432DE1ACD0228D577A6B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vwcORGOyRPirEYDv0xQdpA/zh-cn_image_0000002566869409.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=1FAEB1A4CF622903513299C95CAF76736D170251A0393EC2EC0474A6D34DF950) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fhdKY60CTa6L4NVmc1ipRA/zh-cn_image_0000002566709427.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=49DFFC6D234C658766BF14C3C26483B86A73C80C9F97132DC23D8392C526A57D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VlwP3bMtSTGtCS2uOIx--Q/zh-cn_image_0000002535789632.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=01030B1DB9B6BE69D30E948312460212E3F1CDD218CF4E061BD7E50722944220) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gh1LEYD8TI2B61ybr9CWOw/zh-cn_image_0000002535949578.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=52F418FBC73B041268BD07A07F2A4014A6BB6BDD71C97245C9DE7C3099883712) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XIyPi4CTVGBDuU72cuEHQ/zh-cn_image_0000002566869411.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=30497EED489E066A099336D37DEBEF94E76F67908D298DCFA4B95641141B85AE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UjnILisFQhSZB2S5GeqRuA/zh-cn_image_0000002566709429.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=5109EE8E3B90119335685DCCE3C84AAD7792D5AB4ACD908D8E7D78DA222DEBFB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_0eFQ-ZBRGmQ4B2o5tXZEg/zh-cn_image_0000002535789634.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=2802CCB8F66663AA393210ADB0F3269CE831A0AAAD72AA75D20025B418A79383) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LjFFjQaFSC6oeyDX0jsIKQ/zh-cn_image_0000002535949580.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D8152B489E9BEC96A172C6CDF556A0481AB1DCC72F15633E7445F1E9FCFB9685) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UqjTnxADSGaluQ_YwkxHXw/zh-cn_image_0000002566869413.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=1D463CACDE1727902AFD08B5D16483732C4DCC1D57810AEA8722E48210A17B4A) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GWSRIFUnS6S4BA0XbPfP-Q/zh-cn_image_0000002566709431.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=F49F9788941E592E3FB15C04F4E15D8DD53E7C0FFC8BB9B545118241CB9644AB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G6Ed34xnSJ6RqRmwZ1ZApw/zh-cn_image_0000002535789636.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=0F56596A1BA7726B271060443A697737E3CBA9A4814979B012048F4C1745F6DF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHcsleUcTFqqY7gkyrDheQ/zh-cn_image_0000002535949582.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=A5EEF7EFABB922F8B29F1B0F9D4C809410B7EE7FE5C9EF48885345A525E5B48D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cuVXGXHPRO6-kQVrVZOoeA/zh-cn_image_0000002566869415.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=F82A99367D510A9F47482F44EB7C0108908A8FA01BAF9342BB061A77D8CCBC8B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ff_IWYiQTUKuhXMeikrZ-g/zh-cn_image_0000002566709433.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=3F1C92C38EE0388ACD77D0A7DFE879CCD21E71AC1257E5563205900D83DD8EFA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gExoH-_yQpSgwehc_hIdqg/zh-cn_image_0000002535789638.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=2911A32E8468E347434174EA63EE289328ED6BD5FC9FE2B8B06B32C79D23E49C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Istmm1W3Tceg8u105X6HiQ/zh-cn_image_0000002535949584.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=B2423FB4D2E4211BAAEBE13F34284802BDD0978422CDD6D89AAAB30DD877001E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/feSI7ILTR1uwt7mU871adw/zh-cn_image_0000002566869417.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=D5592653FD244FEF9185BB5997DAF96968750A0C616FB6D14FC48A95904835B7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WKmlZlnFT2C6YZGMCTk6mQ/zh-cn_image_0000002566709435.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=853EB2AE5B9732C84A800A5BB1EA4ACBE6320F187BB43566AB253C5DECEF7689) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/os9tJOTOQZabXC4lnt9Arw/zh-cn_image_0000002535789640.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=18B6EBBE06AD4DB3E57727B6ABC89E98DC96AF6AFE768324E39CCC3388B74DD7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T18jLZ72Q6So-DK-ocwfOg/zh-cn_image_0000002535949586.png?HW-CC-KV=V1&HW-CC-Date=20260407T024513Z&HW-CC-Expire=86400&HW-CC-Sign=8B4432472E7551FE425110DEBF8F47EF09A6B004E3AFC62DBEF11A917C1ABCB7) |
