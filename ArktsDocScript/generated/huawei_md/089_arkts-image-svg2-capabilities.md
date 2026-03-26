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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/y4wPPJCORHm8A16naweh1Q/zh-cn_image_0000002563207235.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=01D35A781740F8BE408E1D0193B9089F0D8585094541430B119201B7E7778BF0) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Hkc6RqtTSPOI3Xb6Bh_9hQ/zh-cn_image_0000002532087336.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=5926C39D8BE00A132D96BB0F0B5CBE87DA7A83178B93EF7B3FBFB4D16C9640BC) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/PNvcHP4IRTGxBq529RCvuA/zh-cn_image_0000002532247272.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3971DDA796FA2F038EA4040E9B443FDA279791C5575BC37ED051ACDA7FCDC6E6) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/onc1S3D8TjSFd_x7ZG_STw/zh-cn_image_0000002563127215.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=802324397B15F61E0490AE479C82C28A4E37831D72043DCD4004E16A7717BB2E) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/C89Foh72SFiKdiQ9pTeijA/zh-cn_image_0000002563207237.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=D47DB1A0A65477AC9E0F382340F7AA579E306745B71B23C6521E8DBB041C2332) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/RJDHAOJgQOu3Wpo9r8uwfQ/zh-cn_image_0000002532087338.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=BC148CC2D28B2D8417112A342750DF178F3D9303EAD0A75D978A7FDA20D9D44F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zq-GQCTISTK26HuSZekR9A/zh-cn_image_0000002532247274.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=325CCE64E49648362D566E30BB7FD1F1EA03E75022F5E34B8FD96410F9BF51FE) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/g1HprhrLSqC3PobkDXWeQw/zh-cn_image_0000002563127217.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A7531C0DB1AAEACDA23AF3AFF2D0B369DCE8AC2FB82497F5BF766D759B2C9E7B) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/z-26vOSmT3OwSK0-DfnblA/zh-cn_image_0000002563207239.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=10E2937E144E2D03A3553D65AAF86D6A9E6A887B50746EFF1F9DFB6C9F9AE84A) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/eks6uZI2SiG4p3CC30KnNQ/zh-cn_image_0000002532087340.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E8754C3076394E0E7F9F5A0155B37E7DBA15AF1297741BAFE10A187885C79980) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/bksbzyd5SEOhueFkLnkZfA/zh-cn_image_0000002532247276.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A816743E723D19290A8794AFB3214879CEB18510DA894F5E10875DBF9C6406BA) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/MMqEYYiPTryL99ax3CHOFg/zh-cn_image_0000002563127219.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3BCD106DF6074B06AF7357572D8998F6D853877620A231CC75EDD1AA48FEE52D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/LjCwF6TOQpiVnTE0nYUkmA/zh-cn_image_0000002563207241.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=CCFBB739267B3C0934E065ED67BD4620103F5206E3363E1796C84874F19972BC) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/s_y8eoNoR8yxwSCGrQOdCQ/zh-cn_image_0000002532087342.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=979218B2752739FF94F9601BA842F33454E664255CCF31C217E6F7A95CE1B53A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/j9GsA0Y0SKuLxiJxmmiuzQ/zh-cn_image_0000002532247278.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=1BC20A0DF0A467C298AF466AF6CF1809A0BE1835C26BEDFC1BD4417FC111C17D) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/0AFM7GzoTFiQpIkQHUTt4A/zh-cn_image_0000002563127221.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9D177DBE6D7A8D75C1FB2440341B5862EF347058B6AF15AE15D6C432FF7CF294) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fbHYXKgURdyG3kiXvB0NnA/zh-cn_image_0000002563207243.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=AE0EDC4C95673E0030FA234CE0979735928054D0EE34A3C557E47E2350848A7C) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/6--uQXLvTXCaMZ4eqM9tXA/zh-cn_image_0000002532087344.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=65BEC86AA433EB89D09304B3242118D8F81F70063EB5A5E787DBFEE216EA5A4E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/UOq616tbSDWJpZ-r2zjiVQ/zh-cn_image_0000002532247280.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=C7541767959A2DD1209151A9F0950088E4DFFD122370C3EB295964DCF29634D6) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/cN-LBo3NSF-BKsQ6ikKAbg/zh-cn_image_0000002563127223.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=2133E75B9996292BD491EC08DBCD3D6782E666BAD71A467F7938E08403CAAF17) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/zeoSP7NHR_Kb5pZa2CYhVA/zh-cn_image_0000002563207245.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=734FBFF8C8280505BDD37ADA90A12D20B3DAD22E706745FF9703DEC6C521BDAA) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Fyyo54wOTp-nndghZ1uVBQ/zh-cn_image_0000002532087346.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=BD9046F602A07436BAFD18BE016FF5AAB7AA624CC25FEEE89BAD0FC6CF330B65) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/XYZqerplQW-MTeVef50CRA/zh-cn_image_0000002532247282.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=DAAB9153D206379EDB5F092CEB1113D0FAAE265E1393393E2732C24A5D1149CA) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/xOTB2JyrTwuqPcUFcY-9kg/zh-cn_image_0000002563127225.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=07D550A0BA076FE407499B0EE5B735AD63F7640796000757A0C9A4DC57519F37) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/vYRFxq42SEepYFBYth3vKA/zh-cn_image_0000002563207247.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9FAC37AF1790771BD0F105F659F2B6EE20CCC6DBAE2D0A079E48B657DF468965) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/poE6oonQTSa9tgZT3Ohw9Q/zh-cn_image_0000002532087348.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3838B9FDA1D3E60668F44FF55AE0F3C69A558FBC7436CF22D7FDEF1BC85E9BF9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/uWy8eFh0RYKpU6uJgimiZw/zh-cn_image_0000002532247284.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=1C7D4FF2126D78BD0AF69ED622BF03B4705FE8D058674F141D8F72037C1ED297) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/8_aH9xCjTjGNOnEmQjQpEQ/zh-cn_image_0000002563127227.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=C10912AAFE9AC8AB2ACB1AB09F6F5E5AB4AF2984027AC611A734C86F4C9BDC58) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/78xT1BpXQleGjejo9AZRYg/zh-cn_image_0000002563207249.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=97CDC6B7316D0BA908EE79EACF52CE8FF1239397BA8D1945E8F39C6245AC4EA4) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/UYoMJc9jTsiarmPeKOelwA/zh-cn_image_0000002532087350.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=CC63C5A0CD3D9622F96C216B670EF29EF0FDFD499DA1A4B392ACCDA4955D6070) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/_9Ej4_JxT4SxAw7Dkj1RDg/zh-cn_image_0000002532247286.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9E4BC2194ACC1FE4E8B4BFE32324CDF55EF0CE38B8ABAD73F5C18EF64C9FCEFB) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/5POFzj8fR86T5BQHx93jOA/zh-cn_image_0000002563127229.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=985DDA83DA66C407249A5C9F8B8BEC6934649D1FC88FFFBB86CE6DCC321902F8) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CmadBoeSRACfvgJYhc8Z_A/zh-cn_image_0000002563207251.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=C42FE56B2738F3C2445B1C59455E8AC1CFACEB40B479F7B2C89123585DC9C02C) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/t5avZseIQUOjVWr5FWjZiA/zh-cn_image_0000002532087352.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=DA7602690A33C638A1B20DF84E7E9C77C7AD637B9F19886F67A5BFD7DBEA60F0) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/BSDyxnCkRnyOrntG0E9kRg/zh-cn_image_0000002532247288.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=704E8EE7FA842BEA5C34EBA7A37308A9561B4E694553B5A2263EC2D1E6504659) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/qlingLbhQLK0a_qAXf_gGQ/zh-cn_image_0000002563127231.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B2FAD1F881B626B6E4212CD741740F0CB4D9E2ECF3F9E096A1E6BBA55D7608E7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/KQOtQeB-SgyO6jpIKiTS4g/zh-cn_image_0000002563207253.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=EA250FEAE5B8E34A588320621554F59CD51D4178EB8675AA7CEA6CF7DC4BC026) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/lrutBd95TZ27cTEjQnHi7w/zh-cn_image_0000002532087354.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=5ADE0A7D94AC22D4BB141F644ABA46C3B009A4E236E016F4489242DC08083BA0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/nAanyb8eTqOY8s-kCvXv3Q/zh-cn_image_0000002532247290.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B1312306FD10A3047BC007C99FBD641AB20E16D950B56B364F9DD63E35E88530) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/8QwNXixkT8iZzRGQSJI-Kw/zh-cn_image_0000002563127233.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=1B5E310ED648D9EEC68A2EEB1C466EF8990AF99927F4A44B038A9EA9EAED1A31) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/vzQ3ZQ99R1afOHQJsTbHoQ/zh-cn_image_0000002563207255.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=CEDCFB7028F63E9FED5EA76399BA8C53631DB483E2ADD0D74182669681B73B43) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/k8yxUazeTqmL3E82pjHdDg/zh-cn_image_0000002532087356.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=00F1FA02D7D4E09064C1E9B4CE14CDF42141ECFBEA9212885A7B533439FED9A8) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ST7f5bJySLisZOm7k2y5pw/zh-cn_image_0000002532247292.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=4A97CF36EB27AC32EA016D76268FEB90EB5B8CB614FEF4940A8BCF01403DA689) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/mzDLkpe_Se2fvf9Y4p8ifw/zh-cn_image_0000002563127235.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=06FE012938114E4BC498F9DAE521A581760680C3431D7E3CED268389146432E8) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5LIF5bvRRKmOzwbeGwhF3g/zh-cn_image_0000002563207257.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=BB76C98C2AB87D7C79CB303AC7808FA75730350D780D9B7E84A3B584B908FFE0) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/_aFl6IXZQ2ed05uSbg7wFA/zh-cn_image_0000002532087358.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=FEF9B7457390C49430DC27EBCE70F8D6BBD292E68430DC6151FD888E0BBDA582) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_ZuFcKt8RpmpXXmSZ57sCg/zh-cn_image_0000002532247294.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=11B37AAC00157A2D6C038EE33BD6B80141712FFA94AE0ED6813B9199726E2A77) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/acTv2QH6QE-mhuNZ2zj8ew/zh-cn_image_0000002563127237.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=F7ACA6A83798518A6023B2C011DC1686AA46E7E6583C335EA475A181569236CB) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/-GXYuwOsRt6zDVcHDhdnmQ/zh-cn_image_0000002563207259.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=8F15D15562D85C6494BF4FA1BB325F66888410F518C67150894E5DF5800A2DF1) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/mQmSYWaHRY6RR-XPCSUhEg/zh-cn_image_0000002532087360.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=5817EAB9432E123EADCD0E20032F87CBA746B780EC0F4C1F1F093F57E083CF0D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/WKsU6X2aQxqJQxPXQIe8hQ/zh-cn_image_0000002532247296.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B15B9774DD4BEA1B5B838E21D391171053BA25FD0A920ECCEAD85D9AA250908E) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WDl_fA95SkScoFLj0r0WAA/zh-cn_image_0000002563127239.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=27F51EF2B608A456B8C2FDA4E17A536F118BEB0EE6D14151189559BF7303CE98) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/qWNJzpZjQoSgdNvGZ4-_mg/zh-cn_image_0000002563207261.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=320D142133508784854C651DAA422B6856233FE4C4D72275F525064ABD4385F6) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/W5LVkMFPQYyTHmhEkyzPNQ/zh-cn_image_0000002532087362.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=8BE55C105C9AD4FF6736561F8E6F3FE52DAD6CE0B9B017D170A0676D9D308514) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/QRSSBklUTDiU2KU-aN4SBg/zh-cn_image_0000002532247298.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A7424428A35383E030AE7097DEF9631AE016852BF0E734F814DFB7FFFAD8A22B) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/-jY3NjDLTeOv15KXAWIraQ/zh-cn_image_0000002563127241.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E5CEA104E77E15304A429BC322CF9D21D4512DD16899997C12951C151476147D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/58OYeRDHQUGXGXGdohog0w/zh-cn_image_0000002563207263.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E96B3B5388DD3789514A3F7B21A52C7493C7EE6A5B1F83FA4F9EFDF641EA2D1A) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/CBc1PpcjR-OXe-Yy9znVrg/zh-cn_image_0000002532087364.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=44BE0397F5D751A137B94A5D04AD801CDFBDCF2EC9F394197CE097E11068423A) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/SxpUjah2RQCI85n2tjT9qg/zh-cn_image_0000002532247300.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=2D42FC986BDA9BE385702750C5B9DC125C1CA6484224E8189D4C8EC19B7A3B5D) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/MjTo6YqsQ9GresoZij6tCA/zh-cn_image_0000002563127243.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=D6C496F255BE9E80917FF51F9C657498A4A3F8CC34D6A4CE23DCC19869BBF7CA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/XmqPZvV1Rq2qWbsxrecLng/zh-cn_image_0000002563207265.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=750C2FC42AC0BD8D1CDDBD675848053E4FC60C172212DFB5278268128C9E20C4) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LKJo-9jVTe6TD8ECrJ5gxQ/zh-cn_image_0000002532087366.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=657D0E4A979BEA4577F2C98064B7B39DEE53BEAFDBC1274C2AFFDA4947E9FD91) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/WrSzW_rZRWmexDTeqRaJCQ/zh-cn_image_0000002532247302.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=5F0B25928217DAD893C14FE52BDB68698DAC50F5A310D7719854C9DFB33A5F8E) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/30Ej_ZazQ4aLUIFVV7bD7A/zh-cn_image_0000002563127245.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=34601AF27537AE955F3F9C298DECD11A0E7858F8B7A4DDF4111CFF05DFDB89B2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/-5B17T53RVCNGC38XNhtIA/zh-cn_image_0000002563207267.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E1F810BD2E3A060D3574258FF7486AB78E0A825880E79291336066F2D42F1CA3) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/SGJVa3MGSXiGKdwhgkNOdg/zh-cn_image_0000002532087366.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=48B2117FF17D990E17B1FF95A597B874EB0EB476B3CCF6F3DF3E68D1954EB64A) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/FylssQw0TRGeSBuDdNwk4w/zh-cn_image_0000002532087368.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=EE11D1B5172B5122020240F162500719034D650E1B3FA317B1605349794044EC) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/fRu_jC3_QaOQnTpnQMDYQA/zh-cn_image_0000002532247304.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B2EA2C718C3D93AEC5DF98A7F1266B61D8C94514440C2A3B8FAA4EB78F883DAC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/nbTIcWEFR2a-Y_hahpZ5Zw/zh-cn_image_0000002563127247.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=FF9B2625DD96EDC4E7320B09170676CD2F9C47BF1D7220BE0AA07BE774636223) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FMVOCZA7SEaFxgr0VbgwFg/zh-cn_image_0000002563207269.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=1D764C45F5A7D98B92D19237EDD4A73EAA6EC9AE95A7B622044894743EA77528) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ZzU0RjjtT7GGsrSMpOKDrA/zh-cn_image_0000002532087370.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=6E192C413A8C0D55919FF8C1566899E8A6FD080251F6A7569EF0345D52C111B0) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/k6yllvjqSwKYYaSQkWAKtQ/zh-cn_image_0000002532247306.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B2F9596D5ED85E3FC6023F62B0D4A6B117E511B2F9AEE478A5596F97AB5E40DD) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nQKcj4YzQIGB8OWYuRQkIg/zh-cn_image_0000002563127249.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=BAFBEA8E58F48FDD2BF9870ED9CE4B606AC90CE134CE4DD60B03AB2272C35F1D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/G1lENDSGReO8bmBXtR1EUw/zh-cn_image_0000002563207271.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9CBC12276D1E1B890C21E25788E8B3B4DD79CB579C61031C8FFA397F69920ADF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/NW7Aryl5QfanzcEr4bN1VA/zh-cn_image_0000002532087372.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=1C2F89B94C9B7A0A52F027FBCB392E30AC15F37D02B93A31A9C00776E7DFEB08) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/N59ZnC31TmOlR19YIXVEbw/zh-cn_image_0000002532247308.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=84B1D658CB81FD5B79387068B04957710B2D664499E1E0F5358FDD68C35DD22F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/-60MjgEQTSCwpb6wo80hTA/zh-cn_image_0000002563127251.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A9A3BD457C3B7EE1FFEE82D949BAAF1C6BC0AD9C5562ABA099A06BDC24940D60) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/bIvDjpndTeKc0XmkkczNow/zh-cn_image_0000002563207273.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9F458878446C6AD7B900AF41A4962E708781A0A12E505C0B616B4D6067C85D93) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/e3Oq7t_RQF-69QgUi1_S-g/zh-cn_image_0000002532087374.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3780F4DEED7276CD48121DA10F03EF4F6F1CF7FEE631B0261E2B163F653830CA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/FcSG0ekwQHW78hekTaye2w/zh-cn_image_0000002532247310.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=FE82B05C6732D926BE0452CA3B479C11CD325095BA693731D2C668D9475F722F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pfEYONVLSC2t73fhCrpm8w/zh-cn_image_0000002563127253.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=CD7EA1B8C71CB6881DABF9F34C816D57E57CB07FCC7E8AB7140BEA8A1A1B651B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/3jagMBDbT-yDNaMKBWG7qg/zh-cn_image_0000002563207275.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=D11ECC4840D57CA4CAE5F540FD7FD64C7D09725DBFB9CCCB082CAE11CD0CDD53) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2kxJwyhrQpqihzf_3iDCNw/zh-cn_image_0000002532087376.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=2651C5078981A3A815AC924DABC4F53B1A6D0511CAD991791DD37E3BE4193F5B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7kUXxC1ATr-NyvTO-z4sKQ/zh-cn_image_0000002532247312.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B8E13606FD33DB215FF5E2F02178E6E27CAE5DAEFBBB26B038DB20E500370AE4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/x-ejdw4UQbSY9hP-Uu6rng/zh-cn_image_0000002563127255.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=082CE2B38E614B094A1B1268AC3236E7A2C7C482DD26029B723F839225926995) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/sVDW_7jwRaG6npRC1MkyYQ/zh-cn_image_0000002563207277.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=5D6C3A99494D24810C975986B5389CDC3CB300CDDB3B18E62F7088343FAA90AA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/esxf4e9YT0GXLGmrXvCIJg/zh-cn_image_0000002532087378.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=9FC9649D1B8C72DB32418EC9024F94B349953B97739FF4E5A624A3846535CD9C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/cnWVySS9RlC3QyaCaXes6w/zh-cn_image_0000002532247314.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3E8C9E6998EABDBFFF97F17F051340FDBC94FF5EBD5EBBC4ED77CB225CB6AFB7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/YbjrmUMLTg26TeWMt9VSsA/zh-cn_image_0000002563127257.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=7BD11F2468A3C5CFECF6E8BE920C1DC56EDE3EE67463452062CDADB334C2E721) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/xCZmMN37TvWUeR_akiWj7g/zh-cn_image_0000002563207279.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=CDF5566F804A344BD659041C306E490D7935D80ACCF25C8AF40721BE11E7C3E8) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/MySNoP-YRrykc6WbhCmNdQ/zh-cn_image_0000002532087380.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A9C8C1F5CAFCFB92CC319E60F5032CFF2F21FBFFEC6A3C6EFC0B7D950FC93948) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/J9HgglNfQeemrcfcf8yLUA/zh-cn_image_0000002532247316.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=515EF1D7FCFA7910AD309F3047327A77C3E75999997D8A094F7BA2CB49EDBB0D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/QM0vYgbhQxu-tsKtAkrPZw/zh-cn_image_0000002563127259.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E8BD29FBDA7CE30881AE3F747B6A32E16636ACC406DBF3C148874353C6B11A6A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/YKr2Qn04SFiYrDLv04Kz9A/zh-cn_image_0000002563207281.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=845A9F0B380F51977617053B713F934DC58B281D11E9ACAC05890158F2223B4F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/e_0xPIYyRrqhRZiAq4g50A/zh-cn_image_0000002532087382.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=E2960C7F219CE2EC9D4043E07225A7FF6B218E3A2F4D18B6C3C220F5DB93E6E9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/xbclXILGR7SkhrAJcfRDFg/zh-cn_image_0000002532247318.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=123C598FD7B3BF476C57873DA25E79AF72F1BCBC2679D0627018BD9E56F2EE88) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/HLPc9BnkQR-qQtV3w4AxGg/zh-cn_image_0000002563127261.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=8CBE82946251A8AD0A964671ACC6E682025D81115DD5FF1E3AA056B4AABA92B2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/MaiCKcQ_RiaXmfbZPZPKcg/zh-cn_image_0000002563207283.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=A547F017EFDC29A6D24C7EDC21B632B9C5FABD30E4B8F7B0AFC766897371D3BB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/UvqKlJNqQ4SHr1mHnfsORQ/zh-cn_image_0000002532087384.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=BCE5C8698CF753F60B67ADA1921854E84B96CC5157C6CC56C1FFEA7D9A0131E4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/K5HDcaOUTGOzKTbPYDhXGg/zh-cn_image_0000002532247320.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=3E7BC0B8899DAC68DFDF0453281D942130999D55B1663FD816BB880EF7425543) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Tnt2xPhYQsC8XQdwbIVfvw/zh-cn_image_0000002563127263.png?HW-CC-KV=V1&HW-CC-Date=20260326T024029Z&HW-CC-Expire=86400&HW-CC-Sign=B7C8E7D42DC1852F84E276CAAFCAF0F50FB7CC89A6D51E52AAB63560857606AE) |
