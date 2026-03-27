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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/y4wPPJCORHm8A16naweh1Q/zh-cn_image_0000002563207235.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=C1A68C742588BC43DFA16C59A10C119435755AA5F8F84AB47B032FCC0C2A30E5) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Hkc6RqtTSPOI3Xb6Bh_9hQ/zh-cn_image_0000002532087336.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=0B8122E7D50E763E7D091C215A512DF38045B6D39E495DF7925088F9BFDA6460) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/PNvcHP4IRTGxBq529RCvuA/zh-cn_image_0000002532247272.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4E2E112C028C2FC078FAEB9D57F1DFF22209F4BA773863E859FBE8F42BA23422) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/onc1S3D8TjSFd_x7ZG_STw/zh-cn_image_0000002563127215.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=1B430C3B1E6F6A99A3E3EDEE10EE9F7FB6DFD9151ED8F7D12EA395C21B284ACE) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/C89Foh72SFiKdiQ9pTeijA/zh-cn_image_0000002563207237.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=13A256AF42E21FF4B1EC75ADAAF5AE0649268C8C2B08876517CEAF592A40349A) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/RJDHAOJgQOu3Wpo9r8uwfQ/zh-cn_image_0000002532087338.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=C159DBF55A18FF235A0ACCA3AAE8BD239AE56BA3BACF60D4011F4E1FEE5F9658) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zq-GQCTISTK26HuSZekR9A/zh-cn_image_0000002532247274.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=6CD5DBCCDD29D617D1AC533326FA354921D72993262AEEC9228AD2D25353E902) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/g1HprhrLSqC3PobkDXWeQw/zh-cn_image_0000002563127217.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=754CD2E784E48644707FFA1E0AEE800EAF46B9E9880D8F5208145BAAF0E8E492) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/z-26vOSmT3OwSK0-DfnblA/zh-cn_image_0000002563207239.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=142C12EC2A20F78246C45F8F1B385F7C94C4202991E3DAB31C5D22A4E211AC46) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/eks6uZI2SiG4p3CC30KnNQ/zh-cn_image_0000002532087340.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=B8886585B6119E69373C1FBB0A281B697F08F57429A0920D2EF04C224847A01A) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/bksbzyd5SEOhueFkLnkZfA/zh-cn_image_0000002532247276.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=90F0123E12109FCD883B133E7CEE089E7219ABB05D898A5316E8F598CCAADC6A) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/MMqEYYiPTryL99ax3CHOFg/zh-cn_image_0000002563127219.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=7F1F904E7CCE8EAAE6B2E8EBDD21B241B9F7CFEE6B30BB4152B19C2375F40116) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/LjCwF6TOQpiVnTE0nYUkmA/zh-cn_image_0000002563207241.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4DB976BCB166012FAD2E791A8D788F9BC1EFD4C0023D7AC9934D01C4B8518AD5) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/s_y8eoNoR8yxwSCGrQOdCQ/zh-cn_image_0000002532087342.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=36E6363134D72EA9E744819E761D266DE8AB0D1C5DFA2DC7AA2080A5781CDB61) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/j9GsA0Y0SKuLxiJxmmiuzQ/zh-cn_image_0000002532247278.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=122DC680414C3A9D4A84F12020DB48EABB136E9EF5D87F7F774FEAB38D42D689) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/0AFM7GzoTFiQpIkQHUTt4A/zh-cn_image_0000002563127221.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=22E809198741E8C3F702F55BE8A4C389A1AB620DB04817E8FF59D6FE83FC4A42) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fbHYXKgURdyG3kiXvB0NnA/zh-cn_image_0000002563207243.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=CF288EF1748FEF768E530A646A91C9AD0406DF9C6E594F83E55663B87F064E6B) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/6--uQXLvTXCaMZ4eqM9tXA/zh-cn_image_0000002532087344.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=875BFA0A6FAC4A98D20A5B124AD0B486E59BA4D759A58DB49BD3EEE019A32E24) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/UOq616tbSDWJpZ-r2zjiVQ/zh-cn_image_0000002532247280.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=AD35A80054D8048EC79DB51BDE640B60AA719706478746648D02C76423337DD5) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/cN-LBo3NSF-BKsQ6ikKAbg/zh-cn_image_0000002563127223.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=CED8AD15631C8524F73DAA8FC7367316D1ED98F07B6FF9FB79EA33457B892B34) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/zeoSP7NHR_Kb5pZa2CYhVA/zh-cn_image_0000002563207245.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=D9CED5BA942E775669115747DBE9EEFC56CF4AFD221ECDCFE2DAE253B0CE7425) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Fyyo54wOTp-nndghZ1uVBQ/zh-cn_image_0000002532087346.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=2783134F01BB012EDEECCDCC46951DF825CB0DC4CC16F70A33C2E71AB99B7A7F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/XYZqerplQW-MTeVef50CRA/zh-cn_image_0000002532247282.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=5D6E73D3779D470201D065860A657DB2573CA024BFB388F4060ABEF3FA4898EC) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/xOTB2JyrTwuqPcUFcY-9kg/zh-cn_image_0000002563127225.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=24C37BA1ECA7D8EFFB6C56988FA87693D276443B4040BBB83306CB2AC9D64AFB) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/vYRFxq42SEepYFBYth3vKA/zh-cn_image_0000002563207247.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=27DC4A9EE6C192ACAF652627EE972AD043D934317BE8155F3361E0A05F5FD3D2) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/poE6oonQTSa9tgZT3Ohw9Q/zh-cn_image_0000002532087348.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=24E67F67BD02A6697431470241281B4189832759EE8C2EFDACCDBEE5EE78E36E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/uWy8eFh0RYKpU6uJgimiZw/zh-cn_image_0000002532247284.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=91526BD93802A8E5887E83C7BEB2533BA2F21D23D8B0B78332A37AE7F1DE2DA4) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/8_aH9xCjTjGNOnEmQjQpEQ/zh-cn_image_0000002563127227.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4F617F7BBF6F50A71E363DC60EC0AA3FB0121FFC113F97C75B5F5B30B8C66828) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/78xT1BpXQleGjejo9AZRYg/zh-cn_image_0000002563207249.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=3EBB0520D911E96CDA12A52451ABC7BB96562C9288E1378E23ABC109BDF1C5DD) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/UYoMJc9jTsiarmPeKOelwA/zh-cn_image_0000002532087350.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=7014EF5C13A33D8BEA8003EFD1B1336C220932C34B294AE14BCFABEB334C50B3) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/_9Ej4_JxT4SxAw7Dkj1RDg/zh-cn_image_0000002532247286.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=BD738FA0AB2592033B96474EA8CFD073E1CD8482736C718821B11D074CF1902E) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/5POFzj8fR86T5BQHx93jOA/zh-cn_image_0000002563127229.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=50734045A585CDE19DD4F3F2E6243AC6D596C8CFFB4A7EDCCC33A46916C9CC38) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CmadBoeSRACfvgJYhc8Z_A/zh-cn_image_0000002563207251.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=E4EAFA6938ADA9B72CFF798B19ACFE08B6FE4834C623853DAB17A509FCD6277D) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/t5avZseIQUOjVWr5FWjZiA/zh-cn_image_0000002532087352.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=9DBD2D5B08B57511F1ED72C3D56719C2453C0A9B7A8CAF1278B9BB138A9CCEB3) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/BSDyxnCkRnyOrntG0E9kRg/zh-cn_image_0000002532247288.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=743689928665493B6E90C58B8A4C6C1286B57E2CD0CD3F91E5EE684CEFCC4F65) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/qlingLbhQLK0a_qAXf_gGQ/zh-cn_image_0000002563127231.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=EF776719B73291D19B7DE409B5DE7F1ACACE25DE681A377DD42973DB64D3D728) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/KQOtQeB-SgyO6jpIKiTS4g/zh-cn_image_0000002563207253.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=B765988F92A5FC8C566692CB91A1F7D4B6701D13B8C741EAA674E1168823FC01) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/lrutBd95TZ27cTEjQnHi7w/zh-cn_image_0000002532087354.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=5C07A489F27D77962B6B2B89AF1ED066A8044405CF3C7B430694D80CB2E80CC4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/nAanyb8eTqOY8s-kCvXv3Q/zh-cn_image_0000002532247290.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=7EBF00FABD8878B3CE75DC1D9F87724B7B2F0CFE2D996460C024D34B20F2EE91) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/8QwNXixkT8iZzRGQSJI-Kw/zh-cn_image_0000002563127233.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=9DC8D94E3C007054EDE443B91891B4AC45793D2FB3AB36A6441259A2BA96B9FD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/vzQ3ZQ99R1afOHQJsTbHoQ/zh-cn_image_0000002563207255.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=D9EB472E9B8CD389636E7EB4938559D7130CDA1F906A9986A71AABDFCDA12C22) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/k8yxUazeTqmL3E82pjHdDg/zh-cn_image_0000002532087356.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=39F2A4767C2248310B550B156175D6016D89EB96010D8CA3F98056C1CBD0D6ED) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ST7f5bJySLisZOm7k2y5pw/zh-cn_image_0000002532247292.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=DAF8397B321ADF368D09D2E488FBCD612E2629D5B8AC78DF4DB80B4AB470553A) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/mzDLkpe_Se2fvf9Y4p8ifw/zh-cn_image_0000002563127235.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=BEC4B187F68E65F3C2ED57B3FF3BE730D7E390A53C532DE65E165B6911406AD1) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5LIF5bvRRKmOzwbeGwhF3g/zh-cn_image_0000002563207257.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=A618D4313363C47E655ECF320220A908B3EBCB3DE4C48A5E6D9815BAEE46431D) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/_aFl6IXZQ2ed05uSbg7wFA/zh-cn_image_0000002532087358.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=A61590FAC791F39436C79827F677F19CAC6AB63CAADAEE56ED61FD72E63E2E92) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_ZuFcKt8RpmpXXmSZ57sCg/zh-cn_image_0000002532247294.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=E7CAC97F1B606FAE90B10B7510A454A83CFADC06FDCF8773AD5014C232566721) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/acTv2QH6QE-mhuNZ2zj8ew/zh-cn_image_0000002563127237.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=0C93E50D75CACD9BC7B65F6CE9410A4FD4AFF41CA3F1F899478E8D9920FB8938) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/-GXYuwOsRt6zDVcHDhdnmQ/zh-cn_image_0000002563207259.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=C6D63A654BC800D42C6AE371CC59FF569DED1C9CB6CC43F6FA71D9D4A15BA050) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/mQmSYWaHRY6RR-XPCSUhEg/zh-cn_image_0000002532087360.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=794DA659A796EEC59DB514BA8AD2AFDC15641634E813D9E7AB6513A3B863DBCC) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/WKsU6X2aQxqJQxPXQIe8hQ/zh-cn_image_0000002532247296.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=740DD8EC0287F8B72A57B30A64B474DA348DF6CC8301F5F8693FC8F67E4B7F76) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WDl_fA95SkScoFLj0r0WAA/zh-cn_image_0000002563127239.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=6676550B54B8779BE266BB1F73AB6290DE448BF36AB2CAB93E1FDB21EB0B6314) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/qWNJzpZjQoSgdNvGZ4-_mg/zh-cn_image_0000002563207261.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=7E6902A51834DD690420B836F06A82443D9A4F65CA1031D617988AED9A095581) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/W5LVkMFPQYyTHmhEkyzPNQ/zh-cn_image_0000002532087362.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=5B3DCE7B1D2524B6ACFEED70926A1493A257F2B033089BE71871240DE053A6E0) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/QRSSBklUTDiU2KU-aN4SBg/zh-cn_image_0000002532247298.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=426AC3AB02BA715AE085D2EE57D37D470807FDFBDE9039D898636A4A3AF92C57) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/-jY3NjDLTeOv15KXAWIraQ/zh-cn_image_0000002563127241.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=AE91C1AE2673B2DC9605409E1DDD8FD47EE71AAE23F5C54000FFEB441735C3F9) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/58OYeRDHQUGXGXGdohog0w/zh-cn_image_0000002563207263.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=E4011648F9A6129C7A12F7794B24B19C9939CAD49DF7CE3B861DD5E098268272) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/CBc1PpcjR-OXe-Yy9znVrg/zh-cn_image_0000002532087364.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=A2F6E13646CCDBE5AEA6814D0BD43703CE2CC7D7AB05D298E12B4CE8F4F452B4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/SxpUjah2RQCI85n2tjT9qg/zh-cn_image_0000002532247300.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=05F9569F5F853D2361277ACF4BA6ADDFA8E6B2AE9C3C8A9048A9007F001F0FF4) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/MjTo6YqsQ9GresoZij6tCA/zh-cn_image_0000002563127243.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=2E292D77A6868DB4B1E12CDAFC9FC3B8C8EF08379CD1D9E4B243DA4EBBE523CC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/XmqPZvV1Rq2qWbsxrecLng/zh-cn_image_0000002563207265.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=0C093ED7A3334308668F718CBC4ABCEDB16B56D96E3DCFA7CA19F11940343F24) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LKJo-9jVTe6TD8ECrJ5gxQ/zh-cn_image_0000002532087366.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4EF3503A0BAE27D67D508395EEF714E376E0E45B7731E361A9A662FD600D593F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/WrSzW_rZRWmexDTeqRaJCQ/zh-cn_image_0000002532247302.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=0811CC64292397FBBD73E685522208955848A4FFEB41603F56B5F7DFBE9F47A0) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/30Ej_ZazQ4aLUIFVV7bD7A/zh-cn_image_0000002563127245.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=53BDE35A07C7FA40F4A4E6B018A8446FA4342C6E6AA34F76753B6377BD4A9504) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/-5B17T53RVCNGC38XNhtIA/zh-cn_image_0000002563207267.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4B8ADA300B4C66390A71E952CA1D99A1BC69AACFF31A287629219029818C8D24) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/SGJVa3MGSXiGKdwhgkNOdg/zh-cn_image_0000002532087366.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=0C234E158F6AF7F7CD4B714DC7F48976530359372AC0CA54600207441061D109) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/FylssQw0TRGeSBuDdNwk4w/zh-cn_image_0000002532087368.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=462FCDD6570C05DFBFF35F11D801DDE4215697AE999E323E6E7D41830641FE61) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/fRu_jC3_QaOQnTpnQMDYQA/zh-cn_image_0000002532247304.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=11B74E0E1C2FE1E6CAD04F3C94D9FF06D9DE364A97F09812FB16D254F88374E5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/nbTIcWEFR2a-Y_hahpZ5Zw/zh-cn_image_0000002563127247.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=BCE1CCEA617373DAD29373E9F00CE55021E49C4AEC6F24CAA691FADC67EBC6C6) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FMVOCZA7SEaFxgr0VbgwFg/zh-cn_image_0000002563207269.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=1CBD743E4DD47818A52DF173BB1B92EF89F8789611152F809587B2E15ADA96AF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ZzU0RjjtT7GGsrSMpOKDrA/zh-cn_image_0000002532087370.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=BEB19BD29313613B734536407ADE10C4F04A04DE703AAD70C71D2A1146830008) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/k6yllvjqSwKYYaSQkWAKtQ/zh-cn_image_0000002532247306.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=26866F8CD37EA7971DCBF07CB2BF75B8A08E3CCA7E4AB50EEBE30B162BD2B91B) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nQKcj4YzQIGB8OWYuRQkIg/zh-cn_image_0000002563127249.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=F00C9A78C5042D53DD9073789FEF1172B602CB32BF2857DD5446C6C6418A0B22) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/G1lENDSGReO8bmBXtR1EUw/zh-cn_image_0000002563207271.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=9EB22FF69109FFC9568E9B33D6A1D03B24D2715564C2CED0687063EC3AD372E7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/NW7Aryl5QfanzcEr4bN1VA/zh-cn_image_0000002532087372.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=415024C9B835C94D5A78B15FE85AC45E3AFE3298A8F5C8F0D2047E251732130C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/N59ZnC31TmOlR19YIXVEbw/zh-cn_image_0000002532247308.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=7C57FD362E645A6B43A29011D9F7825C2529A0745E750B71146CECC7096B5AA4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/-60MjgEQTSCwpb6wo80hTA/zh-cn_image_0000002563127251.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=A46A64E89B2C33EEF07D4CDA095DD910DA1D3BCFF3C8D57CECA1D56D1BFD13DF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/bIvDjpndTeKc0XmkkczNow/zh-cn_image_0000002563207273.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=F0A4B0D94A7ABFCBCCC02E3E5E9E7535B3F3D0C5068F0515AA296751FEF99744) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/e3Oq7t_RQF-69QgUi1_S-g/zh-cn_image_0000002532087374.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=D6FF7FAC478581425CD75F72E7CEDF070F0457EEA0862C468D9E8D2D8E74AD1E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/FcSG0ekwQHW78hekTaye2w/zh-cn_image_0000002532247310.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=F5882924F3069BAB09CFDB4DBF110756C4C3A5A1D7E1E8E4D4BA658FD8AFFA2A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pfEYONVLSC2t73fhCrpm8w/zh-cn_image_0000002563127253.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=4398AE4FF54CE94C27FC07FE9FD9FFA64C255783D41E80D4A6DF57E244505B10) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/3jagMBDbT-yDNaMKBWG7qg/zh-cn_image_0000002563207275.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=A2E433BAAE6D9D27EA5475622DEDDBB6D549A9C3A97E2A37F913146CB0129F52) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2kxJwyhrQpqihzf_3iDCNw/zh-cn_image_0000002532087376.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=6C45EEA1A81081D391363431C3F923900E771C7F5F0D0FB78D36C1932ED9FE61) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7kUXxC1ATr-NyvTO-z4sKQ/zh-cn_image_0000002532247312.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=59894E716932684B962F75DB37F53B79517E71DA0E9F17BAEF9DC9DE1457C78F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/x-ejdw4UQbSY9hP-Uu6rng/zh-cn_image_0000002563127255.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=B4837C93C3D9D1258D851BA8075E305CF1AA02E3BFCF286F27A5C9DF141E2AC6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/sVDW_7jwRaG6npRC1MkyYQ/zh-cn_image_0000002563207277.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=04BBAC4F2C2639DE964BA3CECFB68A226A5BDFD8175F6DF942C2585F0D0F2906) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/esxf4e9YT0GXLGmrXvCIJg/zh-cn_image_0000002532087378.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=6B7EBCD0E31BDD4AC0A42E49DAC842AAF537C73AB78EB309C78363FAE40CDC93) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/cnWVySS9RlC3QyaCaXes6w/zh-cn_image_0000002532247314.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=223AD7371582F80DB8BFAAEBA5B040D9BF24A139B7312A3579C315780476A2D1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/YbjrmUMLTg26TeWMt9VSsA/zh-cn_image_0000002563127257.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=F57496D285BF4B4EE586969CF183F83B0B13CE57DE7D4D96978E1F8FFEAD9D6F) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/xCZmMN37TvWUeR_akiWj7g/zh-cn_image_0000002563207279.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=32812B31689307BDE27F375C926A315FF905BA2052FDE729F511B02B1E4DA2A6) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/MySNoP-YRrykc6WbhCmNdQ/zh-cn_image_0000002532087380.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=DC7F25610389658821957F2AD996805DCE8DACB73A8AB0BB673C0766E06A2073) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/J9HgglNfQeemrcfcf8yLUA/zh-cn_image_0000002532247316.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=579CA7F2327C1349CAEBE42C5A9F35E0E624DEE2AC7CA419165CF6884B683326) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/QM0vYgbhQxu-tsKtAkrPZw/zh-cn_image_0000002563127259.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=8A24823143EA8EDC5AB1A94024B3493D810901EF34BD577E83C17A2CA56CC529) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/YKr2Qn04SFiYrDLv04Kz9A/zh-cn_image_0000002563207281.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=96D5D121D26C8D09F91D22216BFC9DA96208F89E0603F821A8A8264BAA2D31FA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/e_0xPIYyRrqhRZiAq4g50A/zh-cn_image_0000002532087382.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=697A04A9E720F4972E297A05923957DD414A2F4EFCC656377DA41C29AB0EFECB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/xbclXILGR7SkhrAJcfRDFg/zh-cn_image_0000002532247318.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=5114DD4058D065106D20DA8DA2F429322962E924426B6B0C7D8892817B2210A7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/HLPc9BnkQR-qQtV3w4AxGg/zh-cn_image_0000002563127261.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=AE09D5CEECEFE84CAB78D53906CE978DF5D8BAFD767DDBD71C75D5E1DE113195) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/MaiCKcQ_RiaXmfbZPZPKcg/zh-cn_image_0000002563207283.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=73C16C06EC133D8A12FEAF1F79945D11577E7F8750A92FEDE5F80551B49444B1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/UvqKlJNqQ4SHr1mHnfsORQ/zh-cn_image_0000002532087384.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=C48121CD89A66F05BA13AF176C3B436D932E0FE627D814D8D267852FF73FF39A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/K5HDcaOUTGOzKTbPYDhXGg/zh-cn_image_0000002532247320.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=D797D3CFC8A4725A5980129786F4590FEDEAADC7F8A0AD5EC41CF0765C49DCDD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Tnt2xPhYQsC8XQdwbIVfvw/zh-cn_image_0000002563127263.png?HW-CC-KV=V1&HW-CC-Date=20260327T024220Z&HW-CC-Expire=86400&HW-CC-Sign=2B4DC272E988E01825B24C3146549E31FC07E20845F69899E7C7D8B2EF30E120) |
