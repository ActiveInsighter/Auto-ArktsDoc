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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ii-kyNGOSPOMwAq-foHpaA/zh-cn_image_0000002534411520.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=96E776C75798AFC73C20B0692B9DB4171DAEAF7D74549676123972AFCB8FEAED) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IZ_5ZBQvT7W89wQIMjwv8Q/zh-cn_image_0000002565291421.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A407B36FC4CCBD75C3BCB84952FE909D5A3E39D1DDE6914263AAB2BCFF576EAF) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LVE_4LLeRTSfpd8S0seZug/zh-cn_image_0000002565211399.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=1154A6207A6A5232608F1A5FB57735A2B2338EA4F2498A987E16899DEE9E4699) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A72sbB7TTHuWW869yWGdjQ/zh-cn_image_0000002534251576.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=4356F4EA519DA791DBEF6EA017A87B32088C25F3B897661A8DE1CB2BDAE8EA57) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LW4xwmBtTGKE2WoB7sXEkw/zh-cn_image_0000002534411522.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=AB4A4B1F6C58BE24980F216D601A4DA17BA17C62F6222271F414C1EFF1175462) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qstJRj2MSVKsZ3winwkx-w/zh-cn_image_0000002565291423.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=2B33A2D0034448BA6ED8DDBFF291A5D46285D36AA63DB38860129769E533130A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eiDytSAYTZKZZCWPOB2mgQ/zh-cn_image_0000002565211401.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=16DEFFC763D82562740EF3938496A1AF44BDE4BAA15805413721E6CF6267346D) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/sElyaqdiSq2VMjUYeI-srQ/zh-cn_image_0000002534251578.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D630F01AD44DB68B1A81A16C0DA873223FB3C875A7D90A39CBECF14DDBC7974C) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/EK38ItASRAKWIwpbCKuVog/zh-cn_image_0000002534411524.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=42E55170AB31D7842DA832E6EC51B37291DC62FF7F7D3089182DE4915BCE9829) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4NMB4IbpRZ-FcVDUkbanhQ/zh-cn_image_0000002565291425.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=7FFD79E2BCEBC6FE080DDD8AC2E34D8899352D883432305D9A3DA9554CCF5B55) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/F306G7dOSZmMC4OegqcQ9A/zh-cn_image_0000002565211403.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A464DCEB4D4909736E0704EF75B560B1C6402A179E84A37CDAC3315D499DFA21) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Bke1AR0jSU6s6rnSNgpTCw/zh-cn_image_0000002534251580.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=AEDD7DD732E6B71D724DBDF9EF78809220D1A5F61B1538D5728021B0DF117AE3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hcAO4iYDTWWoPHiOExwgYg/zh-cn_image_0000002534411526.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=B7304FB835A96BFE0C43556743BCEAE04A4BEC2022F845C9BC6DB1AAB089089C) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/2KdZFk0qQ7uH_JSD4jhpAA/zh-cn_image_0000002565291427.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=771CAF11A206CA6CCD1818BFC0F7F0379EB9549C8F91F9171B84C00B5AAD2F99) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sh_HjmXhSyimKMaTQI8q2Q/zh-cn_image_0000002565211405.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=3D6959CB65387ECD1F6707970EEC75564A252C928B76CEE3411C3885700CED25) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/JigmDfrpR667kD6GTUcOQg/zh-cn_image_0000002534251582.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=E08F08B10B0B42AFEF8BB992E966567C772D2C0B61081A97CB4BAD7536B34EA9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DhhYJ8V_RwaLzOrG2pef6g/zh-cn_image_0000002534411528.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=99CC29BDB4B469CB63660FDC3C17EF6A4429B63ADD605D92B7E223046EB68894) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bs1Nyw1oSEalRz2mMKNKzw/zh-cn_image_0000002565291429.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=18306424CF1100E7E7B713DECDEEBE35369BD4C705E55B09401178E8334854D8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3920RCa6TnuauqZ4QqYICA/zh-cn_image_0000002565211407.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=4DEDF960C27AE1314D7FB9C5A3CB2E62E5BC899E09250373402656A93ACE3E48) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/n1KsuxQWRsOgqduN_DWAng/zh-cn_image_0000002534251584.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=C0001D586CDA6EE04D63FD64FC526F7AF44E029287C0EBC6E69039A0C56572BE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NrmtU54qTtOHiS3q8GoOpw/zh-cn_image_0000002534411530.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=592CB09394EE0E0D63F0DEF42D6E1DC273DFD37CD4CB4FD2D81CCB22389F1F19) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GoRJcqUFSUGeWbODwYYa_A/zh-cn_image_0000002565291431.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=EEE63A8ADC8EB0D7404BA6B3BB8468A1E014DD5D76FA36FB8B5FA439F8159925) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8VSXJ2EPQ7Oxnl4eUjSbpg/zh-cn_image_0000002565211409.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=DE91C87E49DF2D4915067B67ACA50479465C687A7927746680558BF3065479A7) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yfoy_YdMSFW26uaZgaQ3cQ/zh-cn_image_0000002534251586.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=43E34CCBA8A595DEA77E553DEFC00AE84039ADFE9D9A0F1A45F6D46D0A742A0F) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/8QHr7RRvQZafaqyK0PHgvw/zh-cn_image_0000002534411532.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=5C6DBCD5B4AFF9983EB0F269560E7A8D408F44337CDF0DADD176812C9BB41B77) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/76Buxi4tRIK__Pir7TgdBw/zh-cn_image_0000002565291433.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=3E53D5D103A5C05A6F6879949CA03DC141777AE0A96C5E9A1B3E4B3C5CC066BF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Ez_4Qre-TgWCbOJrvJT4Bw/zh-cn_image_0000002565211411.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D89070B73A2AED154B213D564F81874F889D243559B69DF6FF632B367CD99FAA) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/crwaIsXDT96N-IeYAbW0aw/zh-cn_image_0000002534251588.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=C04F23E92943972CFE6E28C41AA762E56BA15057DB0CC67E4F363F69A42FCD0D) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DJQkoOb8SSi6fJJxBpVH8Q/zh-cn_image_0000002534411534.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=178C70F2B7D007A712849E91C2CB650D3DB77C3893F21E7B5ACB4713C0324924) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vmNZSo24SfitNb1mdYo7Yg/zh-cn_image_0000002565291435.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=661FCDFF1440FE2B072E3960F4D3E481AF463C42CB1BD9210889F59836A1A43E) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WSgFDG7BQRy_Whm0iPxGUg/zh-cn_image_0000002565211413.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=554BAA8CF91235D114BC04E9C3803AD1493BF1EEF1F7DFE0C8075CB863DBB1C0) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DEynjX8dQOagdzDlHqYe6A/zh-cn_image_0000002534251590.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=FB191F8B3841B7A414D0D34E49297AA8F8151BB0466B668CC1BA7DB2D0DA71A0) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nSC56eGaSyiz8GITFKiZtQ/zh-cn_image_0000002534411536.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F494799B8E2AF8A2578CDC54E8948138B0031CB9E336815ECD0968B82ACE31DB) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vQWoAnqxQ2S_09Air_PyeA/zh-cn_image_0000002565291437.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=B70A92A6DBF0EA8E31B501FC155DA79A7E4BAE0F3C13F2A659591389EB2CFA42) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aRzPA3D6Sru1r0qqT_lbiA/zh-cn_image_0000002565211415.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F2E7FE61F4CD1544C98F4ACB5AED995AE5953D948411DB618551F277B698F866) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AK6F763hSYSDjwLqQruZhg/zh-cn_image_0000002534251592.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=182A6E5D2F57DBBC2E4A089099F107896FE17385A69A62373F04FBC2709B1DF4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AumZMu5QSn6qmq2YAkgImA/zh-cn_image_0000002534411538.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=01E5602226E92DDD5085C469F359E2812CDDA53F26041EBE2841F4526D2602EE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eGt-LIpyTsabAc4MQXW64Q/zh-cn_image_0000002565291439.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=2054D33961D24C6CCCA16B819EFD8E34C356AFF6836C1EC401C249B9C3F54B46) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_-yf95JTTQyZDoalZ667Cw/zh-cn_image_0000002565211417.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=2C049DB893E4CB540CB149B3AF1BD0CF8F87D379EDD533757BC282834801CCF6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/oZC-V7nGRhaw-Zz-3oun2g/zh-cn_image_0000002534251594.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=B5C6AA4CFC75FB508DCF03E9C3389CABC3B997ECC051085385657F6D153115B0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GgPzWsdrRgS0Swq-ZDDDqg/zh-cn_image_0000002534411540.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=C62B99FA0D5312BB71492A5878EBEE8854C734D51216DCE7A760F526EB129A78) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/veKhEp8PS9yCxuMXzz89-g/zh-cn_image_0000002565291441.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=25677CA808A30B45761B6B0651BCE6AFE8567808B70CC6A7D3E2172EBF01819F) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Xlm6fTeBTdyzCFbzalofag/zh-cn_image_0000002565211419.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=0837FFECC96A33CA55C789D88802DBFFADDA21077E8FE0387ADA7A72AB849010) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NunMMI4TQQOBcu80y8JvVg/zh-cn_image_0000002534251596.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=3C59295E0C8F524E8137D4CCEF6F5E2E2FFDE22065D8EB7784617F848D0159CE) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9dizZSWlTRG3adRzGSjOOA/zh-cn_image_0000002534411542.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=18DAFB9EE108171B99E40B5F35CC416483BA63227B2764398560C209A5FD3E6D) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EQKx3iiqTzmD6YjGLOYXFA/zh-cn_image_0000002565291443.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A39E1147BECF7609EE90A4EE750E747D7D289E1456D1283E124848C30EB7F51C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1WsXuK5aQnWjJi6xetnWrA/zh-cn_image_0000002565211421.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=CD0273F9B07337D5EBF276B483B1E0E1D046399FE50DA53EBFBF1CFA949F5D93) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uYUS40C6ReaYGs7HPMLS4A/zh-cn_image_0000002534251598.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=1E7F56E42DDBD046CA24BE830BFDF3420158CA456E6AE4BCF5AB995CE129A74A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cHSMm1g8QV-Me6LBPUV40Q/zh-cn_image_0000002534411544.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=0FA7ABDA3D3B8FD97BA534D1B99AE92B116BCA130D69F65696F15F41A8242BDF) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_nRJJHFsQKS_FcoMgJ9-Nw/zh-cn_image_0000002565291445.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F0091EB6181030F7C069AF58C58A904EC0A75EEC377F1F797AA51E6DBC5318EA) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qIKsUZLxQ5eCHEfo_muz0g/zh-cn_image_0000002565211423.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9E939A6EE2F5F3F4A7C1CC224F012A1FC7F76450A6E66B4B46988FAF0B2518E4) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/5ZPdsFE7TEKAEpQiijvQLw/zh-cn_image_0000002534251600.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=C8168B9B86A590EB548BA859A3410A633C24DDAD32388DAFE381EFBAA8AD99A6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vYljLAQvQ9OZsXQpKsgM4A/zh-cn_image_0000002534411546.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=8BB37C58B70576BFFA80532C42F06B4A73251DE5B8DF9F92875DCFE597A6F23A) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/52HZkPiCR1SL_e7NYaf-ug/zh-cn_image_0000002565291447.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A96E887A7140CC109ECAD36F63A2D2914F3032116DECFCA63094FB8A1B7545B5) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FC8C-rupS9qRw9ymJcR-RQ/zh-cn_image_0000002565211425.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=783F1A3D492BAD447488EDE76AAA1B02482AD51DD55167CB06AF482942363E41) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G14KchPeRRuW3rHCaVAp0Q/zh-cn_image_0000002534251602.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9D42318682F7BE1EF4F6982EFCB32531EECC2672780F26D139FD3130A8E0B396) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gBxz3uJbSTmQF7OESWFZcg/zh-cn_image_0000002534411548.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A813EA1426025760B113C1A4D3199F83DD4774E680D921750760C08560E19F6A) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QEr0qsK_TU6E6zWy0wiFfQ/zh-cn_image_0000002565291449.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=36BB6424252C469A98BBDC581CA7339A1DFBD72443D9C75F43424ED49EE6CD36) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_HCxlBGaRdadDF1OOOoptg/zh-cn_image_0000002565211427.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D27B34271E398ECBF8F84F7D4886B541F1BDBB3CFEEADBCBDA17C70239043982) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/oO6TyryNTuiU1ImCdgdRQw/zh-cn_image_0000002534251604.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=B12C46115B772DD20536CB05BF389D890A87A93827891621A42AA0392A1EA9F7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WyNCM8-2Q76PjHhF6DDFaw/zh-cn_image_0000002534411550.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=526FD2D5B7BF596F8CA8D8CC2D35527D46CA466AA438DB996DC43307CEC95660) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ItI9jH7hQyK-e2jr4f-U8g/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F6E0832D9B0DC97002D7F574D9B8F5E37CD5D72D9DFFDA1EB31BBF2C77EE8278) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1z6iQdJfSZiGfwxO0-X6Dg/zh-cn_image_0000002565211429.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=ECA35D399E448801B7DD61B06B3143D8EB9C05F901216B82CFBC646CF9415C71) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4yMyaYbpTyuR9cBmW5L91w/zh-cn_image_0000002534251606.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=126CA8F218A8F680567C60EFBBDDEFD74A64A4FBF7A633331644AAF38840FB8B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/59ZiPuz4QXe1rzLmFktNGA/zh-cn_image_0000002534411552.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9FA3B77F3C5C246B83AF2D2FE1D3711E5D1D65BE9639B535E88A4A6F61F3F37D) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MpfXLUq9SbS5Jvu6n06cWw/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=622D1C2723AAC51D5158B78AE783779A02FA2114A5C50BC05ECC09C08CD11A37) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/tiGGbyfxRtOYYvpk9Hro1A/zh-cn_image_0000002565291453.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F4130BBD7FE4356EBD10C8781DBA18C760BDEBD80903F2F22943E995FC653AB5) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yBCtH7JLSsuV5cR4z-raMQ/zh-cn_image_0000002565211431.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=2CD979F9EFC5771411803169495E36F877DAFAB8FAFF56F902FD6C1098677B24) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/k1yWcafmSEmEMXe9Lr4W9Q/zh-cn_image_0000002534251608.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=8B29050B21582DE39AC897791A834A5E21D6812A37B9ED426041A4C5223B6C7A) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7NwI1coDQXqISDHeiNpJOA/zh-cn_image_0000002534411554.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D79A6B2979304AC29F6D2A2E10D276EEAC78BC477EEA4BB66146225C9595FC41) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ST5XGG9eQZmb3g48GkY17w/zh-cn_image_0000002565291455.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=E870F9DCE8334C61BB02E59B907ED18BAA3100BC29E3899E5315362C6CD90A7E) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5LYlOjNmTZ-FucsQU70VIQ/zh-cn_image_0000002565211433.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=2D077FE94CFE25D2F416E1F74E92304CB23D969A9215F5BBC24DCD73E1926E82) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuhAU9IlSDWFuGr0FU53bw/zh-cn_image_0000002534251610.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=1A729459836006C10C8CEB5BCCE5ED6F3CCB8EF674CCE50AF46F032DCE01085B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gf4tXK1KSD2XtIVjOP-9Dw/zh-cn_image_0000002534411556.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=7DA5E49D17EBBC2555C5F83CCE85F16FF5DBC420E72E92F20630472F451E06C0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/V4FSyf_SSwKGTr9yCRUg9g/zh-cn_image_0000002565291457.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D0DD4D45F75E7CE85158A61DEE79995901445B660C1133162BD66032CAA22334) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/kdMZMjmRTj6nGHYBVUXwYw/zh-cn_image_0000002565211435.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=355A545A93FC93EABF40161443182AA800B3C5594B444C74DDF094EA8702FA0D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xb-R39t4QAC0OsF5lWyHDg/zh-cn_image_0000002534251612.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=1A32B69F4969F6520B4F0823D9C5E8534D479C4FF776CE1065361C0FAA2BEAC4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HnoQfmW2Ri6e5K1ffwWzaw/zh-cn_image_0000002534411558.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=D5A36901464381033EC54E4F7092BC8B41E78134BCC5DFA63F0126535424B596) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wlZk-6epTIekWZYIeCO-3A/zh-cn_image_0000002565291459.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=08C20643580EE4515FE37BBD317EB459CAD795CE73CD3D2D9DAF14D8C4409418) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2uZs4Q6pTJ2qFE87i-cJzA/zh-cn_image_0000002565211437.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=F3EA7335D13278574BB80F4C7DEC11A9CFB3BF193D375A565746716D650D1B97) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O5OWYVKpTEiIo047460RsQ/zh-cn_image_0000002534251614.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=CF8E9A2F3FD34E7676FAFC5E74DEAA06BE88801C88E23C3627C680856A746823) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Md_YXiTOSE-xtLVUZ_CYhg/zh-cn_image_0000002534411560.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9ECF74BB3FF5A11BEA6A035BB46862D74D357BB1420A268A7D8E077F5D2BA7E3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kFb6hRscTIiHIVztiqZMjg/zh-cn_image_0000002565291461.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=5DEDD740E91310E67DF6914D1653FE2EE3E98F151DFAAA952C1CED70A198875E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/pTh56Ja-SJ6FQHgb6lzWSA/zh-cn_image_0000002565211439.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=6889B912BE417C1BCAF3AA4E7B438A2B013152F79447FAA8FC7EF91005EC0D9A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vMGeYhcRSZCB-qVDJDKCpg/zh-cn_image_0000002534251616.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=B6CA2A3C2F969891B6CFBFF7347E24BB3600BE53D03EBC786B358879602371D4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nqUcPMrKQSCVCtwTZg92Gg/zh-cn_image_0000002534411562.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=26335ACAFCC822947B3AE285C1E1094A61266A10CA2E2AC4F05BBBDA3B34A48C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O8vSOm-hQFGFkpq1e5u1ZQ/zh-cn_image_0000002565291463.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=DFB77B6C0CCE959CFD91F6357259DAAC5744FB24CD6B46B34958973BB7FCBC0D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6uplnqqAQTmApsGDeqBpxg/zh-cn_image_0000002565211441.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=4DCAFD7071C6031EDE60EAB44BF0189A8A7DC03445B2D9AC9A6F86D255FEF841) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/I_rnRsxzSpGxBEwjN1XU8g/zh-cn_image_0000002534251618.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=331D8FC92A6955F29CFEB4DD61DB50E7172B66BF753DD626EB87D6DC8236DAD3) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lXHCjT4eSV6w8LQaMbopvw/zh-cn_image_0000002534411564.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=ABCEAA1F255A21554FFEC47D82005E6DA2159C9FE26FD7D3A6B8CF361812A123) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SJhv0EWETuWxFXXqwPiRkg/zh-cn_image_0000002565291465.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=0BBE70DD46E34C3F734F43CDA1D918368364990BB3AE95D616DD2002FD251C32) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Up-SzE_rT5KMvJAw-WuYeg/zh-cn_image_0000002565211443.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=96269A788D88720D86B0790CCBC04EA0F93983CC00A70ECA8A8F60FF9403AF8F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qT0NlbsyQE27uHHYdWm95w/zh-cn_image_0000002534251620.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9FCE192BE8E83AA50DBAA873ADE1ECCED3D8CDD91FB6732AD86F2534369A1A1A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qqxSsYC5TcuLwNBiEKfLjw/zh-cn_image_0000002534411566.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A51C62022F2457BC2CF89E7B877D4E9888D01A769036DC4910E6391D28617FC4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WdYtIMmgQlaRxBupL9XHqA/zh-cn_image_0000002565291467.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=3E63692C1370650EC5091E70A0AA8FC278291D58C404A315A745E7A72A248210) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/irXQlR3cR06IaYiez7cBeQ/zh-cn_image_0000002565211445.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9F2CAE8B8B68B82E9ECD15094F6D03EFD056C3F633A05FC825DCF81F5E2FB0F3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sOb8_9WAT1-72HPN0cUjZg/zh-cn_image_0000002534251622.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=E78887069BF7A0CD36EB837C988886FD3226843950FF528CC7979BD191AD09A8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KoQk2RgdSxOqe-vSgKkqHQ/zh-cn_image_0000002534411568.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=5E336824235D7FB46C31AB190FD551FE657E8CABBC1763CAD93955C749081AEE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/eCMDDMQaQJy8yAdkcnwR7g/zh-cn_image_0000002565291469.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=A1CD2DD20148E7E0FEF2EEB9E91B946D1D90E87C8469DFA84C2A6E5C2B1FCF6B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V2fKSuNPQUmceefgjrkahw/zh-cn_image_0000002565211447.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=9D29A925FB4A77E93F3F881F00FA1243EB26B69E6496E7DCECBFDC6901BAFDC2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/1qAyH0vDQ3Caif_VOm6mSg/zh-cn_image_0000002534251624.png?HW-CC-KV=V1&HW-CC-Date=20260402T023955Z&HW-CC-Expire=86400&HW-CC-Sign=AC6A004B602CBF0A92EB97420E13B656434C3295AE396280236102BDE0D0AAA8) |
