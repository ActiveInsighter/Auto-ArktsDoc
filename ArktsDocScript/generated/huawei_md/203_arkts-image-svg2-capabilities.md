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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ii-kyNGOSPOMwAq-foHpaA/zh-cn_image_0000002534411520.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=FE887378B7C390AA18BF43E2E37507E579C9A03767E19C9968FB74A743CB69CA) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IZ_5ZBQvT7W89wQIMjwv8Q/zh-cn_image_0000002565291421.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=C7720EDF8B6252B1E7193317D02042CBACE55586AA1C72FE75FAABD191913BA7) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/LVE_4LLeRTSfpd8S0seZug/zh-cn_image_0000002565211399.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=4009DB09B854ECA5AC36BF0E2658C611EAF3EBFB0756486D992DD582EC589266) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A72sbB7TTHuWW869yWGdjQ/zh-cn_image_0000002534251576.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=0C74EFDAD2D5D68510942D2B11901D5F5D351E3F759641658521AC8057378F9E) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LW4xwmBtTGKE2WoB7sXEkw/zh-cn_image_0000002534411522.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=597036A350E8B67D39523DF3042AD875CBDB6C5E75C1BD0B124C2CFB825D5A81) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qstJRj2MSVKsZ3winwkx-w/zh-cn_image_0000002565291423.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=237D527873E9C6ECBF3B9CBFDDD5C0F534DF7BA9A18FA3E113E7C368996BB0A3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eiDytSAYTZKZZCWPOB2mgQ/zh-cn_image_0000002565211401.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=CF1FBDCF6FE355A62747F8EE32C4C57898E953AB10CCBD78AC4EEF2D816D8C02) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/sElyaqdiSq2VMjUYeI-srQ/zh-cn_image_0000002534251578.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=1F49BED2AACA6368AC9AC0E82498524B8DB2B05F2950F8EE53A846775CDE1165) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/EK38ItASRAKWIwpbCKuVog/zh-cn_image_0000002534411524.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=78426AA345C21B4B2075225E4E5795267BA2307C30928B0BB314166B0EA3AB5B) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4NMB4IbpRZ-FcVDUkbanhQ/zh-cn_image_0000002565291425.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=F93E7DC2BC450F0400717F3371A9C4960A71C5590EBEED98446D9D4C085095AA) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/F306G7dOSZmMC4OegqcQ9A/zh-cn_image_0000002565211403.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=2C19D04C06A0EE1578D39B12EA14F664BB58F47554569821633DD83635204639) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Bke1AR0jSU6s6rnSNgpTCw/zh-cn_image_0000002534251580.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=5D01A2C0CE13BA871F74198B0B8392AC7161F7D579C54A2E210208E5F811BF8A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hcAO4iYDTWWoPHiOExwgYg/zh-cn_image_0000002534411526.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=C4BCC07D78F57FA889109297CDBD1D7F06F9451553952D22172A6BF426842D43) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/2KdZFk0qQ7uH_JSD4jhpAA/zh-cn_image_0000002565291427.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=1B739E57C93D78C74FE8348AA3BC911FEE6DE74E360C3A1AF2206145F91E75AE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sh_HjmXhSyimKMaTQI8q2Q/zh-cn_image_0000002565211405.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D6A53BAD6AFD59813B3A04AF51A3F210E760063BF7682E2E6C5C628C2B835EEB) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/JigmDfrpR667kD6GTUcOQg/zh-cn_image_0000002534251582.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=98222D84F72E7FB98B098612E9612227411C66191AEB243D67834F506CD9A4F8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DhhYJ8V_RwaLzOrG2pef6g/zh-cn_image_0000002534411528.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=6C70413D59459B9424383D8BE4173190CD1DEE480340EAE314FA775634536F2F) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bs1Nyw1oSEalRz2mMKNKzw/zh-cn_image_0000002565291429.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=197EB2411B8220DFF18476EFEC1F9E3E8F0056102997FEC56E1537E5C2676579) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3920RCa6TnuauqZ4QqYICA/zh-cn_image_0000002565211407.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=06199017FF825C195FE4B777A78AFCE514FF1CD11AC55194F584473B1AE9729C) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/n1KsuxQWRsOgqduN_DWAng/zh-cn_image_0000002534251584.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=69CBE74BA6318A2914BB142FCF5B90940A0366477F2A84A7A5C5DBC5563AC3DE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/NrmtU54qTtOHiS3q8GoOpw/zh-cn_image_0000002534411530.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=18388E5D5ED24E9E525CF9D3999B9A24455D256DA877E517C8812D1D9AE7DA32) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GoRJcqUFSUGeWbODwYYa_A/zh-cn_image_0000002565291431.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=00D33657730027C3AD0EF64754384BA98A1D99D63A2115F8BD57B54A43E71DDD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8VSXJ2EPQ7Oxnl4eUjSbpg/zh-cn_image_0000002565211409.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=211A967A21A65E2E950EE32F5FFB545FA8ACE4A3AED5067FDE09186207BCB614) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yfoy_YdMSFW26uaZgaQ3cQ/zh-cn_image_0000002534251586.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=978360CFAA23C3C6398737E7562042ADD481EAF4B6CF5937A5A1F14BDD6B378E) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/8QHr7RRvQZafaqyK0PHgvw/zh-cn_image_0000002534411532.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=49F1631FF9ED26F2EDC9C05E6CA61643EF5764A3AB1C474190BE31943AEF8229) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/76Buxi4tRIK__Pir7TgdBw/zh-cn_image_0000002565291433.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=F8D5D10A377DFEF1498AA3323D99818AC8B616A437D7284D99D8154DCF147E2A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Ez_4Qre-TgWCbOJrvJT4Bw/zh-cn_image_0000002565211411.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=CD2964D769BA181E7C1CE23C0B915772A8D4D630F624D2656A4DF499E7A9C029) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/crwaIsXDT96N-IeYAbW0aw/zh-cn_image_0000002534251588.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=5F50801AA0168F8FB6163CF1CB5F2E5DD51058D05E021F75ADE040DFFC906928) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DJQkoOb8SSi6fJJxBpVH8Q/zh-cn_image_0000002534411534.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=5738F7873045F7E9DBD069A6D87C3CDDFE781EF29B1A96DB803FF450094BAB25) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vmNZSo24SfitNb1mdYo7Yg/zh-cn_image_0000002565291435.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=C6AAE4EDF5015B89FF1BC5EB88FE2FAE7E7F74543A3A0C553B4FBADA3E9ED475) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WSgFDG7BQRy_Whm0iPxGUg/zh-cn_image_0000002565211413.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=6CA735AE8E0D40F867F38D8D626516747E1B37FA1C14A0E684F606EE54916A58) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DEynjX8dQOagdzDlHqYe6A/zh-cn_image_0000002534251590.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=1DEFF8FBE11544686B30E74851BF7581F24736C36CB9ECA62E5F573C9CAF8AA1) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nSC56eGaSyiz8GITFKiZtQ/zh-cn_image_0000002534411536.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=9FB765BBBB39504BB4A679B5F2512226237A6389E7AD16A59E4B7BCB43C8DB15) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vQWoAnqxQ2S_09Air_PyeA/zh-cn_image_0000002565291437.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=48D05DCB0A3E03EA47CBCF2B3919DAB49C42457EA744DC5CD4DDD328922DA91A) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aRzPA3D6Sru1r0qqT_lbiA/zh-cn_image_0000002565211415.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=9DCC69A2C03AECDE9AAB039F91F749F9D7839072F98D1CB68AE25D4DD2B1B6A2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/AK6F763hSYSDjwLqQruZhg/zh-cn_image_0000002534251592.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=4567D7E2DD3D8F2E462A502127BEEDEAB2EF1BC480097BE65267DD68E4EB44EC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/AumZMu5QSn6qmq2YAkgImA/zh-cn_image_0000002534411538.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=1A8119AAF3AAD9A31C22E5CE0EF96114341756A2DF82F07554EBF5A09CA2DB62) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eGt-LIpyTsabAc4MQXW64Q/zh-cn_image_0000002565291439.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=BC8AEC20D8EDEF3404E56C254EAD49C62C28FE98B7EDEB7E8B3C044F585D5131) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_-yf95JTTQyZDoalZ667Cw/zh-cn_image_0000002565211417.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=FF81926D57554390E70C06D57D3D961A42FD5C88111EFC2C34FE063F8B0A98D9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/oZC-V7nGRhaw-Zz-3oun2g/zh-cn_image_0000002534251594.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=DBBAC23EF88BCDAB480A1BEC3CE234D421CEA64B89D5BE0E9A986E44C17EC4B9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GgPzWsdrRgS0Swq-ZDDDqg/zh-cn_image_0000002534411540.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=998BE61F8BF34A5040C806E9CA6153B3FAA19555A5B233831FB4100100564CC6) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/veKhEp8PS9yCxuMXzz89-g/zh-cn_image_0000002565291441.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=96B3827E825D491700E1D3FB7E0CA2815E4F729BEDBA83D47D6BD0724AA223A1) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Xlm6fTeBTdyzCFbzalofag/zh-cn_image_0000002565211419.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=2B380EC9292D5D4E2798C42A8B26ACD0C112208EFE343250EE5493794C6F61EB) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NunMMI4TQQOBcu80y8JvVg/zh-cn_image_0000002534251596.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=B5DD6568E2D18A5ED5DC194B3DEBF569CB08BD66A98A260868D5B5DF5E77BA11) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9dizZSWlTRG3adRzGSjOOA/zh-cn_image_0000002534411542.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=3EC6936237A3F1F69D70638041D9C31D66D41F038F1CE994C31546FB6AD1654A) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EQKx3iiqTzmD6YjGLOYXFA/zh-cn_image_0000002565291443.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=4BD50188BC1F00001DBBFE63BDC140A90FAD0077E00B466B12051647D82DC406) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1WsXuK5aQnWjJi6xetnWrA/zh-cn_image_0000002565211421.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D207AFD820DF5120B722A703A101982737C2A2BBD64F01E850D2062E232A266C) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uYUS40C6ReaYGs7HPMLS4A/zh-cn_image_0000002534251598.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D96A2AEE83DB322C20B592CFC1D1A605FF645F8AA0408E790E2FA548C0D1E4D9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/cHSMm1g8QV-Me6LBPUV40Q/zh-cn_image_0000002534411544.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=0769B40FEAE56471CB735BC12ECD8065631064470EB63271020D8B5C982AC719) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_nRJJHFsQKS_FcoMgJ9-Nw/zh-cn_image_0000002565291445.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=12EE7E69B7D3CD9E4655A4B6B7A9A5B90E421640323FD8DF6E6865A1A36AD2F7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qIKsUZLxQ5eCHEfo_muz0g/zh-cn_image_0000002565211423.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D8754B61E5C39D75A4E99F161C089174A858DA1032991DB8FE32B70EA1CD25C2) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/5ZPdsFE7TEKAEpQiijvQLw/zh-cn_image_0000002534251600.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=88C93D23169401004C70ACE7C5487ED694EDB626A64DA52C43BFFECA7EA9E145) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vYljLAQvQ9OZsXQpKsgM4A/zh-cn_image_0000002534411546.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=9DCE4003ADFBFD446FFB3C7B439E2C1E9FDC0BE3170314789C94653E0A97A5A7) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/52HZkPiCR1SL_e7NYaf-ug/zh-cn_image_0000002565291447.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=56A1C0510086F08C218FF360568384324418F97E0C4DCAC9DF31736ED737B9C9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FC8C-rupS9qRw9ymJcR-RQ/zh-cn_image_0000002565211425.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=8A9A0FE146DD3048249350CD0897A1BC43C77FF042C0D0C955393DE946831E1C) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/G14KchPeRRuW3rHCaVAp0Q/zh-cn_image_0000002534251602.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=678D82BD33B00FB36F63CC67FE9624E314543071384D19B09AFE7FABF77AF0C3) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/gBxz3uJbSTmQF7OESWFZcg/zh-cn_image_0000002534411548.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=BEDC28AA55804AE3D8EBAB4E29837FF977F600E97B06624CB3F8BA91701673BB) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QEr0qsK_TU6E6zWy0wiFfQ/zh-cn_image_0000002565291449.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=57C58380C9DF30A9490F7A8F1344DD310C6A3F7C50A0662474736C963CCEB638) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_HCxlBGaRdadDF1OOOoptg/zh-cn_image_0000002565211427.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=519BBAB95F6AB9CEEC028FE3FD9684E9FF7592D865DA834A7636979F3F339B65) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/oO6TyryNTuiU1ImCdgdRQw/zh-cn_image_0000002534251604.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=8AE896070A8A334C2B780007E403F09ED26568070A9757DA4FFD4706DAF6C65C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WyNCM8-2Q76PjHhF6DDFaw/zh-cn_image_0000002534411550.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=A33FD0931B1AEC8105DA912DA22B922CFFF092B2B5DB4187D838568DC99432DE) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ItI9jH7hQyK-e2jr4f-U8g/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=E158CA1AB693205E4EC7FDEE624F0B0B7980E04C074CD40A190C399AEA6450D9) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1z6iQdJfSZiGfwxO0-X6Dg/zh-cn_image_0000002565211429.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=5F351687D1C00D57D8AC86576335D409B2F8A88081D3E3A8373BF80568DE4AE1) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4yMyaYbpTyuR9cBmW5L91w/zh-cn_image_0000002534251606.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D4FD1EF5ACA1D6324FDFD2A81CFBA24EDD638001F526135050251F3B49D92747) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/59ZiPuz4QXe1rzLmFktNGA/zh-cn_image_0000002534411552.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=03DBC61A5889AF8625C67DD6850A35C695A7F53B0F0FE6A3293701D4046CA5B4) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MpfXLUq9SbS5Jvu6n06cWw/zh-cn_image_0000002565291451.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=1621844974F7021903F201B2225B9D839C2597C61752A82A5E846CD888EA50C4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/tiGGbyfxRtOYYvpk9Hro1A/zh-cn_image_0000002565291453.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=71ADFA5E83473DB75E8EBDC426FAB4959C26C51B1D25998702600C656DC56E60) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yBCtH7JLSsuV5cR4z-raMQ/zh-cn_image_0000002565211431.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=69A2452272678F524569CF806DFEA66B232F6B0D75B47D815B9595C835683BCA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/k1yWcafmSEmEMXe9Lr4W9Q/zh-cn_image_0000002534251608.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=8C6129828DB78A61DDCB7811F2975017EF4B40D511A8B8E51FE45AF392015181) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7NwI1coDQXqISDHeiNpJOA/zh-cn_image_0000002534411554.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=5A5184BDB7FBE551958555DA80021808393A148F694E135522CAC4832BFEA7AF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ST5XGG9eQZmb3g48GkY17w/zh-cn_image_0000002565291455.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=0259425DA778699CD170F118396E6DB87ECFB9289FA5FD6C7BA40F8AB6F3F33A) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5LYlOjNmTZ-FucsQU70VIQ/zh-cn_image_0000002565211433.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D0C5E316DCA228EB297A600584391C64EA34C3870BF91B7FEB2D2F19914056CD) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fuhAU9IlSDWFuGr0FU53bw/zh-cn_image_0000002534251610.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=FF494F6986A54EDEF54B1A5C8A3857DB91BDBA9B53ABD947660749160CBF754F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/gf4tXK1KSD2XtIVjOP-9Dw/zh-cn_image_0000002534411556.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=0C1EA9D232CF916014E611FB413C009FDDAFD3E41F3288E4F04B1501D58C0B20) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/V4FSyf_SSwKGTr9yCRUg9g/zh-cn_image_0000002565291457.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=C9E372BE2C1DD28C3803B9D932C894A2CFA6607DE25C6C29FBB26885F3F7BDB1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/kdMZMjmRTj6nGHYBVUXwYw/zh-cn_image_0000002565211435.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=C450628EC06E530D693A22B743B58C78484E9FE38C0D2684A7D6F742953A17C3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xb-R39t4QAC0OsF5lWyHDg/zh-cn_image_0000002534251612.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=DFBF6B404DC9612C827378CECF8E5ED96A7745A4EA50BE7867BAFC92BBABB3C6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HnoQfmW2Ri6e5K1ffwWzaw/zh-cn_image_0000002534411558.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=6C9E70BC0B4C53A963049E7DABD5273C3BCE3D48E0E70BBE95B7931109B4265C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wlZk-6epTIekWZYIeCO-3A/zh-cn_image_0000002565291459.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=CDC0A7FD235203E03AF2D9E7EE54E6938C505721D9BE0E0B456BF55C0079DBC8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2uZs4Q6pTJ2qFE87i-cJzA/zh-cn_image_0000002565211437.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=B167C0E3A211AAD7CD8A4D5A4A5FAD235449D7DB6C5A95549ADAA340148ED13B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O5OWYVKpTEiIo047460RsQ/zh-cn_image_0000002534251614.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=ADDDDD976512D0D5AE82F30528849A2541768DE5437A17B131498B57097A2444) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Md_YXiTOSE-xtLVUZ_CYhg/zh-cn_image_0000002534411560.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=EBE53E675DB4FF644F0D95BFA0BDDDC506A5136F5D93A5882A3A682E1606EE0C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kFb6hRscTIiHIVztiqZMjg/zh-cn_image_0000002565291461.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=609BD87465A0F667F533EE17EE735C0B127F189AB367B6F12CDC777A501C5BD5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/pTh56Ja-SJ6FQHgb6lzWSA/zh-cn_image_0000002565211439.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=D320C2D2F4A2332D39000BE3C0021AC593996845A8A18416244173C3F7BCD6B6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vMGeYhcRSZCB-qVDJDKCpg/zh-cn_image_0000002534251616.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=6232CB8B3506E4CF2BED04F9E828ECCA0638760FFFD9A801109B34B284F68D66) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nqUcPMrKQSCVCtwTZg92Gg/zh-cn_image_0000002534411562.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=ACA19C4CE4B973542B3D2C1CF829ED0D566765EA4B5E886DE713E8550A577AB2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/O8vSOm-hQFGFkpq1e5u1ZQ/zh-cn_image_0000002565291463.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=52A95BEB5B1ACE4F3836D207EEB2B0469EC23F819E548D89B6D5494B536C3C38) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6uplnqqAQTmApsGDeqBpxg/zh-cn_image_0000002565211441.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=DAE79CAC91134C784AFF3A0632485C974AFD12084AD2C5175964DD1E28EF330A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/I_rnRsxzSpGxBEwjN1XU8g/zh-cn_image_0000002534251618.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=55A7D4C6B3327288F55870D345D332BE0D541A3461CC6822FA81B6869412475D) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lXHCjT4eSV6w8LQaMbopvw/zh-cn_image_0000002534411564.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=7AD641ACCC2ECDC84EBE2BB9D4BF3A506FD890AF34CAF8588461A29AA31DD580) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SJhv0EWETuWxFXXqwPiRkg/zh-cn_image_0000002565291465.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=FF916AE7818A71EF04D86DEFADE07405B1348AFE9B6972F2B1FCF58B05D94077) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Up-SzE_rT5KMvJAw-WuYeg/zh-cn_image_0000002565211443.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=9A2A54A587E0439F73B27266949C29A26B1372815A3A1836136D0885BD3F9E04) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/qT0NlbsyQE27uHHYdWm95w/zh-cn_image_0000002534251620.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=2559C53C048C0DE2AEFF978D1A6B8ECCBB37571397F5B9CC0503A92F98D306F2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qqxSsYC5TcuLwNBiEKfLjw/zh-cn_image_0000002534411566.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=562FBF015F0CFFC8D6FC03E7F785F63FA35AB8B63233BC27E7E7DBBD2EFE029B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WdYtIMmgQlaRxBupL9XHqA/zh-cn_image_0000002565291467.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=19C38DD09977F14A3F32F9E25AC27D952CD385C2F1B658446D88EE6B33EA1AC1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/irXQlR3cR06IaYiez7cBeQ/zh-cn_image_0000002565211445.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=F390619F5A0E82B5FEC76DA747717498C9322D2CCDD9B003C330557BD754FCCB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sOb8_9WAT1-72HPN0cUjZg/zh-cn_image_0000002534251622.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=E1AF9C21BF8C68E49FAFDE3FD53ED4940EECE46520B1924E2B16DAF16CAF6242) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KoQk2RgdSxOqe-vSgKkqHQ/zh-cn_image_0000002534411568.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=BE58D42D8D9BEA2D96AD7A8F87D7ACE23C79B274FE228CDC8C9F22C053890CDA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/eCMDDMQaQJy8yAdkcnwR7g/zh-cn_image_0000002565291469.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=AEAD687712FCC8C3AD99C6C44079D199DB56AB01FADC49B1E6425B7EBEBEDEF2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/V2fKSuNPQUmceefgjrkahw/zh-cn_image_0000002565211447.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=F8560404056E1EB69927DCC3137321C73F7D6A466C5CD3A0A09DD16F6EB8E8BA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/1qAyH0vDQ3Caif_VOm6mSg/zh-cn_image_0000002534251624.png?HW-CC-KV=V1&HW-CC-Date=20260330T095452Z&HW-CC-Expire=86400&HW-CC-Sign=2D3C874B4CC0AD6B799B076D163DC89623B5EEF8AEC352DD7A5685A7F1FCF55A) |
