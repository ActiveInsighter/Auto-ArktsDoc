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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/U7rdcJ9lTzm68awuktHtfg/zh-cn_image_0000002566869369.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=CB027197D0F644F0B9CBD24D32A32B956782CE4572770D1CCB0D040E9BA126A8) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Chv8qEXQHe1rB4XeVdraQ/zh-cn_image_0000002566709387.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=45EA3DB2879B43A57F11A677BF8ED5C3ACEF662C6E7A2DD099E7A65A936C8E10) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/YO1-A2xcRuyklvV_JOhjKQ/zh-cn_image_0000002535789592.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=96B610A98EA99FDB53CFCFB904A58438026248BC822C45027CE4D23248FC91FF) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/icj2yO_MROKol4D8_t5nYA/zh-cn_image_0000002535949538.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=6125BCCDFED54AFCA057CDAD567E706EA28B0D263466ACF8F7443F8BBD0C0549) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NXM2Ut2wQEam3LHCIBp7Qw/zh-cn_image_0000002566869371.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=97217EF5C7326C7DD158DD4215A40721E7037401D7FF9570404E5348C6C638FA) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0pMboDzTT3eaWJib2Mq5Ww/zh-cn_image_0000002566709389.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=29D7A5573BA622BE6AB88E8F4AE72C76A4C0228D38A4F4E3F90E1D06F3413318) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_XzI4LNsRTyrw1Je5Lf5nQ/zh-cn_image_0000002535789594.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=CA76BB26703EA2714925478B27AF22E173C7C2CB697D0D03D64013F3C6291B22) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SrH2BHLLQrS91FqXrOzktQ/zh-cn_image_0000002535949540.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=758D94E837B370997731C8D324A22A7459DE3989A618E61845C821D019991D1F) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aC9PrmH9Tzev4O-2-Z3RiA/zh-cn_image_0000002566869373.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=1E987C3F4738FD9F76DBED7F9F056E4B2842B5465AB5E21DFD6C9F98E7924D4F) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sLpBbvpnRAysuEMqySw9eg/zh-cn_image_0000002566709391.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=16CC6326B5B3D0E7C8B7526552223E599315EAD7103426499A5FB205EC1177C5) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/IuujT5iTTk-rOynEyl_WyQ/zh-cn_image_0000002535789596.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=8562D3AA6BA5B70A346E663608EB68599AB79BE54A73E797CFFF5367F12AFF28) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/aC8JK6VsSZea7QwA2VfaOw/zh-cn_image_0000002535949542.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=88E220D2E75CED180BC8BA79C9A772C203296E4A2B9BCF364570983AA8950E64) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vqR5ddigQ9ywC1-CCaaYxg/zh-cn_image_0000002566869375.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=A9AA27D26AD55C1F78DD305480F8F25BC69E2462C93CB052711A819A86E879D3) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UVr2aZoFRG6RKZYWyA9KgQ/zh-cn_image_0000002566709393.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C15BB769FDD0177FFE12DB36C43FB196927F504D640739A4A8B2B40423A98A2B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dJCNjPOfSF-njYTsv3XG0Q/zh-cn_image_0000002535789598.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=EC4D204C96E1C560808A014E243469ED8B0A84D71994F291444852F0F94219D3) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/SFRTzRgiQN2euBnwvn7IhQ/zh-cn_image_0000002535949544.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=3F303DD75F0E050A2A2030949EC7A4EDEA88749ABA668AB026845BB83513FB94) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5NTEzPD7QkyUuvqZO3oEsQ/zh-cn_image_0000002566869377.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=2A62DB96F2A2219A1E5091F566689E781849915D87C0E8981DB56074F68E40E5) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M3F8wzf8RY6UZou75gGF2A/zh-cn_image_0000002566709395.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=183A2F4D818BA7209964307D798B139AD79D886278ACABBAB5E3292B02D4A094) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YTYpWPzlQouj7C_sliIgCg/zh-cn_image_0000002535789600.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=5C4A414436CE27EA6588293713AAA03BAE3E678FC4D67078FFF5FE363E98A102) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aKZHl6rFT9G7A8y_97-bgQ/zh-cn_image_0000002535949546.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=18DC341D2E2C39A81E9DB390A544A6D638860C598193A8FF788C4B1279D6CC3A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5Fk2t3ozQgm_lnODTyBZkw/zh-cn_image_0000002566869379.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=EEEE67203EC24BA7DD14DFEC068B25C27128D8E3ED135ACB5EE4AFF4134013D0) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2zHQsYs7TwCDioiVXxo8Kg/zh-cn_image_0000002566709397.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=36BA3B45426C8B7BD402A821D91017060B8626AD645AEF16BA08EA7AF89141DE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qe1Nys7URrqMBhWcjS56NQ/zh-cn_image_0000002535789602.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=8DD1F9ADF119AF2D17CD246A71FB586E2B25ACB5ABC9D90C88035757F4FB1516) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GN_uCkuVTU-cLupiYbF8pA/zh-cn_image_0000002535949548.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=B829406E544223F9831CB398AC4557F21526D91317B848EE3056B9686F3B00E2) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/froqUDQCRk6qdwY6NtLA_g/zh-cn_image_0000002566869381.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=501D9DD7FC1EBB9CD48519560E4E10C6BA11B210031DAFAAFA71ECF5143A2C40) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/o8FG5N-9TLublhc6LBgn2Q/zh-cn_image_0000002566709399.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=032DE99D29760A1F378F9B8C68AA3934DB90EEFD83469E1DE505A4B1735C94B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w0xAT_SZSwGtKKcIP43-Rg/zh-cn_image_0000002535789604.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=B65FF2123F65B70F3DD63429CEBC692896A8DCB8CFC2B0A03B0F65B193BFE2B2) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Nw1IL7FySiqsm83mmJvgrg/zh-cn_image_0000002535949550.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=3C3F4F1DFA3A572C2E27F4CE5A2C2E9DFB12AD186AA9B06C3DDA21B38FC8B9D5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SH2Vi2bwQHy4iHinx93EIg/zh-cn_image_0000002566869383.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=93569173B4E7BDA07F6AE988816AD3991591B322489C52BE26178D8E9DBE682F) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eO5JgJI-T9-SUDEJRJ54Ag/zh-cn_image_0000002566709401.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=F23B9EEB625E34DFDA03239439AFA392F3BCA40D2A49FA8D21A2892201E24C37) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/97Dhdj-xSaK-Z-2lunsg2w/zh-cn_image_0000002535789606.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E86B9205418B0E1F50E54E7F6CDCB1D2351F0F58E6B3DB6FC007B42E35F2E167) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7szxUCnCS1OLRnqMCPBeCg/zh-cn_image_0000002535949552.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=86CABC6D33961B0C0C0CA891D1939EAA1C3644DD442F1705420A0FC43FB56D08) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mGJhBKvgSjmdCGcfdi3F0w/zh-cn_image_0000002566869385.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=3BB4190FC4742A97D006C98E4217BDC1048C32B4BC2CBD509910B0E65B4D284F) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OdN34v3KROaT37VOXwtjlg/zh-cn_image_0000002566709403.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C4C88B213168B97130FA3A32EA91FF4EC5F237AECA48E95B56C2AD5352B56E00) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/19zg-bVLRoWH3VHfcTNViw/zh-cn_image_0000002535789608.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=81B83DA79A0489A4FA01F0ECEF79360C69D0A20FDF6ECB7A5CA6D46C1550B6BE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xIuMxN-9RyegGRL5dHaEJA/zh-cn_image_0000002535949554.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E1529159F3FCEB29F2B676D0A100219716B75C1A056F3DE8ABF71516E2D6689D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/VfEoizikRBeXtMe698hxSg/zh-cn_image_0000002566869387.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C54AF2B1A16EC875F9E107ECA34162B2CD56C10AB77DDAB762BEB402A827FDD8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wwhjfe1PRH-W78dl5NoIoA/zh-cn_image_0000002566709405.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=0EEAF0F610B82228F7297294BCB2FE422DBB50DA962C40E0EFFBE232CEC6E073) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1LNPgbj3Rt6wCFJKKRHe-w/zh-cn_image_0000002535789610.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=5AA7E1FF5BB0DA4253D45FB7D5AD5CF8C7ABAF539145D8DC4573736E527CD829) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-eh7Cr7VRFeJdcig6Hrpyg/zh-cn_image_0000002535949556.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=DA5FE9950A0C2D6307BEFC7C324BF07777773EBFDB51DC9808A045B857F99A6A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Azb7Wy7HR9OdIRqK1DMvuw/zh-cn_image_0000002566869389.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E6735D48036BEA6B66BC85292BE1DA3DAB29DA737EAC8675DF1D2FF7EFEAB44E) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CiQCW9mAQfS0hhJwMmvZJA/zh-cn_image_0000002566709407.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E9E57934F27EC5F359CA8E06C4D0D933D6402B276E91FB9579CF7AF165B18AAF) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/D8l8UXDfTSme0sV7RUpO3A/zh-cn_image_0000002535789612.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C969BCF6E5A257D860A8E8C72ED698E137748D6FDA7583BA9A53359BA47B76F8) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_SOZVNmkSlijpq0jDaVKoA/zh-cn_image_0000002535949558.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=1B3F0C94D6BA3B5DAAE5FB557B2BB347939D157BA2DB7EAB4D36AFA08386953B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YYqFyBoGTA2vZXSDPZCjOA/zh-cn_image_0000002566869391.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C87C4C593583F3FD1F67E3CA1DD091A4BAA44B45D4DFC027001A33B2CFB024E2) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gO5RYHc0RkuRbo8tl5cpUw/zh-cn_image_0000002566709409.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=8EE357EEE397AD7053982D1BB959EBB1ADF117A83D27C8A33D5BFE2E22D9B2CB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/u3J0eTcETKCFoPO2FGUlrQ/zh-cn_image_0000002535789614.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=30D0663FF0B72F10AB6A6695DA153EBD8D3632760A265AD2174A4FB018DC0BE8) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/f9TxVgxLTDiVA9kr2x1xQA/zh-cn_image_0000002535949560.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=A862F9FEF09382550047E0D5EFCAAFB6F68AF72BA8BCB5E1C9E713E68A48C8BE) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uxLUOaLnS92fwrXjhBgHsA/zh-cn_image_0000002566869393.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=50ACCB58DC0CB117AA80757519652E98863030407EE8EB273AC429E7C8436112) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wmjwYIcKRwCSIDy87TlFcA/zh-cn_image_0000002566709411.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=D62C96F15ACEF7CD3860C9629A0750D82FB0D0B0D3C9BA63A4B03DCA9AE0C623) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ta_HAbEJQYyYXC2lDfDogg/zh-cn_image_0000002535789616.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=DA371D9CB2FB09D9B72E00A18A42757DD69A3D21763A0578ABB757D9F16323F0) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OrZn2KpkTiODEIzPWvuL5Q/zh-cn_image_0000002535949562.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=FD6E4EE691C11B63E73AB699385A169A94C7CA38A3C4BDCCF7CA1CFE1878740A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Yd6hiKb5RrqmUCZ7hJqrsw/zh-cn_image_0000002566869395.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=9236CF971321E6FE688CA0CBBC9DB64BCE94AFB9ED3FC290BBA5352AFFC0E614) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/W7n6-EhBTuCWfiAxUu68Gw/zh-cn_image_0000002566709413.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=50E8A74D9B5D05A7D7CBC058F7E94B7777E760489AE1E2EE95ED99F48BAE4E6A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UvPE1EaFR-aHXXZgrpvt7g/zh-cn_image_0000002535789618.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=6C023345C46809D98CAE7E139FDDF0D7599E4661874B8FF2754A4949C6FF5334) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/adwBfBfYQSSnRidIkB5IrQ/zh-cn_image_0000002535949564.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=14361DA2D3C2DCFE4F832B22934FA3E736B79DAD886A46E6404BA41DFC10C32D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/usfrYNLGQgushAeNs0NqTw/zh-cn_image_0000002566869397.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=B37B0CD917DE70413F2B700198726D92A720CB98390D6BFE6846CE7C2A3CC6EF) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YsZTJb2AQres1u2YP1q0Xg/zh-cn_image_0000002566709415.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=8D3EC233CD1C4CD8F619513B31F02CFB67904180D0201B77E65CAEF888205B37) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ay-KcBR2RWObY9boujQlbA/zh-cn_image_0000002535789620.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=3CFA99F27879185C81893ACA72972E8E7B3A7354443FF22C2779084361FA23B3) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pdJ0N-IBTwG1Fjo8F3ZcAw/zh-cn_image_0000002535949566.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=27BEE9936C58C83CB80765114F22230702D8E39AD94368D7FFB3AB22E617D773) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dAqyaaSPQpuWimDA0trtQA/zh-cn_image_0000002566869399.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=041F93B660CDBB2B722C3272639A9B490D6A68AA71350647FC1B926201554F84) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jz5EjXpbTy6Y7S23nNZ12Q/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E61628BECE817044537A08D993DBA2C41CDC1F0751381E2D0FA50D3D866CF53C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D2m7NEm4TIGfjWasxLeddQ/zh-cn_image_0000002535789622.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=F4480D98EDFC30BEA0C7DACA77CC63E516AB7AB41A3AD2EBBE13A8DA1ED473A9) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f9Le-Z_JRPq2leN2NrqPhw/zh-cn_image_0000002535949568.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=DEC558985CB341720A2588EDDFC80013366E101D3CB1C887E4FBC5871BF81178) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XwNU10qRRQeSCmkd5xcF3A/zh-cn_image_0000002566869401.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=305189DB8853496DD54C5D42F0F20BF4538527CCBEBABBB7ECB3DF66D61B2B03) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TMWufEkPRC6JEZpbkwBibQ/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=68084008004FD9886FA9DBD260C203EC3D6F7298DE9A1BF3F69E6FA813FEA409) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/har11OZAS7K2y-7K4Fs8Ow/zh-cn_image_0000002566709419.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=B3CD2522A7B06C113B58DF25FE1ED75D8F2EC6FC662F00F4469DC16436F37D3B) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/MqFJOAc6Q9uAP14cHwhNYA/zh-cn_image_0000002535789624.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=799860A3B21F07CF9315C4F0B3CA4CC681E1A1C4391C4EC368507E5DFF2F0A02) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/FJbQ5BzBSd-8SVEoTOvi_g/zh-cn_image_0000002535949570.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=D25AA4067B7CD3873A92E0451C1AB76DC4FAAB86AA4FD5EAEFF14B915C5955DB) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/p_cZt0amTZ-zEkmhX1uWpQ/zh-cn_image_0000002566869403.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=6BF8B860A6CBBCA0241B46CD3A89D8BD83688BAFB824B85F6156248AD5C58E18) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hIBpgsKuQOKj7xsM3xyZ1A/zh-cn_image_0000002566709421.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=120031C1C5363C13F2FE3AF53526142EE80B3F7ECA7CA6255BF35456E73D3579) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_EqLXtnEQxSa5ahDTGuidw/zh-cn_image_0000002535789626.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C091B4AEA9A3FFDCF91E73CB5F0507A15521243254A34B34D61073D14C106B37) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zgPVm-4YS92H2vCY7LkpwQ/zh-cn_image_0000002535949572.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=84CFFC77CA2D0ED67F232A68EDB39D73516BF84F579F9B5510CBDE300D6EEFC5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3c9ltMn2R7WokEmt03mzQg/zh-cn_image_0000002566869405.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=EB4AF3E16D19C9C3874A9E6DFA8BDA2E113D85A13C48DA5BD8E14807238BEDC1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/64B1Gu0oSpuS8cDQNY2QxQ/zh-cn_image_0000002566709423.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=A2A43C8F7879B63267EA15E92D547FFF701F2795273EBAAC06CFFC59F0B72FE7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_-UVeHd_TDyEuVsL1BGigw/zh-cn_image_0000002535789628.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=AC158BB73312415D9B5AC3B6E958382A6EE2763268AFD76505769487AEE8BDDA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qObFmpDdRHagpRUC6OAHmg/zh-cn_image_0000002535949574.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=04CC7448F00A5B240D26CB893CA7095D86B71ACA49D89D5A03B1EE51FC178A11) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/jCCjt3UZTse5bSw-QoVeuw/zh-cn_image_0000002566869407.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=D0AB3C15DF1509CDEC5EF852585A3AF7B37EF853E4BF1658AB1A23AE3825998C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uai-LJEARh6vKW1mUWSuxQ/zh-cn_image_0000002566709425.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=A1C34B62C1604C7B7C06932CDAE5A0EDD5E30EEBC1D635F14CAFF97E9DF18985) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WizO8OTLS0SYRoZhqBTBgQ/zh-cn_image_0000002535789630.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=0BCCB3006785B880F06BA05654BC259DB41DF5F1D297337E31C786427AFDD665) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eIT7t2u3QZ-ORNFF2AooKw/zh-cn_image_0000002535949576.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=0E7014FD9B5913BD669B851A9CD5FE84635D58214649C01ADA0B3B4D1271D104) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vwcORGOyRPirEYDv0xQdpA/zh-cn_image_0000002566869409.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=C89847A01ED0B46AE675D677C67A759672EFF62CFB0A47C337AF255E492EAAB2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fhdKY60CTa6L4NVmc1ipRA/zh-cn_image_0000002566709427.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E4A306401D27E748364BD543787C0D87D33C39ED31FB34179F63A1A442131A7C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VlwP3bMtSTGtCS2uOIx--Q/zh-cn_image_0000002535789632.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=9A6296D2607217A9D802A15358FF08C2B22CC84DECBF9258345F0C5BE1FAE41E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gh1LEYD8TI2B61ybr9CWOw/zh-cn_image_0000002535949578.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=BD8100CD5C168A24EE10A00EFFEB777D34152B7AA11B0BD04B74932969DBD010) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XIyPi4CTVGBDuU72cuEHQ/zh-cn_image_0000002566869411.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=10FA89EC843B50B06EFE70B043001F1B852245131C6C1FEE65D81698B0F346EF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UjnILisFQhSZB2S5GeqRuA/zh-cn_image_0000002566709429.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=5A27487419E68392C013BFD928474391EDBC395F0807DED42398B78220E14BB2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_0eFQ-ZBRGmQ4B2o5tXZEg/zh-cn_image_0000002535789634.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=DB31E2DF909E1D8A107F2405DCA8D271E97EDCF1AE8C72A240624923FDBBA3F8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LjFFjQaFSC6oeyDX0jsIKQ/zh-cn_image_0000002535949580.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=DF6AE4A619B25C231AB404F94889D1A54D89B0465A9A67EFD6E50024339EBCD2) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UqjTnxADSGaluQ_YwkxHXw/zh-cn_image_0000002566869413.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=558CB1D2E8D370294022A8A0DE089D75D4821047317BA8CCEAD7313C1B15A641) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GWSRIFUnS6S4BA0XbPfP-Q/zh-cn_image_0000002566709431.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=81860D0662827DB60E5D28BE9632FF966FA59269BE4B0B4218D3221E8D4C0785) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G6Ed34xnSJ6RqRmwZ1ZApw/zh-cn_image_0000002535789636.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=D9273B264434463CDAFF60ED01F21737693B92842E342CF60EC6FE6B19CA614B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHcsleUcTFqqY7gkyrDheQ/zh-cn_image_0000002535949582.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=018B71843909E4CF43EF8BC758F9258BB287FE5FC39DBE37EB946938C566C9EB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cuVXGXHPRO6-kQVrVZOoeA/zh-cn_image_0000002566869415.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=E773E0A68819AE0F22E335CE833A92832D9BA6139D4BE5983FE029A9EC2D6205) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ff_IWYiQTUKuhXMeikrZ-g/zh-cn_image_0000002566709433.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=3F5E7BC94B1F39F93FBDC019429EA46618283B5786A54FDE553E33BC60DE6B0B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gExoH-_yQpSgwehc_hIdqg/zh-cn_image_0000002535789638.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=1E6D42210AB601D31C61CA6706B82A480DD8B011D4126E887E5B4E9E513DB5B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Istmm1W3Tceg8u105X6HiQ/zh-cn_image_0000002535949584.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=D6DCD208627950CBB08CD7F664DA583B801F7F5CEF72AD66F87709FD4008DD6C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/feSI7ILTR1uwt7mU871adw/zh-cn_image_0000002566869417.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=4921DB7B49D816183703EF485A3EB55224AF33909C14821F0F1DE0E045264C13) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WKmlZlnFT2C6YZGMCTk6mQ/zh-cn_image_0000002566709435.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=2B64A0234481EB2649BCACA72389BA48DC35218B7005D8A4826B7A9BF24DDDE4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/os9tJOTOQZabXC4lnt9Arw/zh-cn_image_0000002535789640.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=CA45289DD6D120076931D9A9E14F1FC8B819140120A45EB49BB916FBB47DB8A2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T18jLZ72Q6So-DK-ocwfOg/zh-cn_image_0000002535949586.png?HW-CC-KV=V1&HW-CC-Date=20260404T023255Z&HW-CC-Expire=86400&HW-CC-Sign=1A1F50C799038ADB00AC3ED1F97EE74BA54D0D21B3244E42111DF6BCC8CA826E) |
