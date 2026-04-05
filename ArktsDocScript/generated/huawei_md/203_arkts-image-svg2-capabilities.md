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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/U7rdcJ9lTzm68awuktHtfg/zh-cn_image_0000002566869369.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=72655870831FC9B89F471DC666CC3F6A80660E5DE71FFEE5EAD7053A7E6B093D) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Chv8qEXQHe1rB4XeVdraQ/zh-cn_image_0000002566709387.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=21FEA2F450325805C91D3EC20B162F3673E66CDDC052FB831C8241CEA4AD3398) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/YO1-A2xcRuyklvV_JOhjKQ/zh-cn_image_0000002535789592.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=D59C505F984DA832B3C36FB23295C5088777B8FEABD6CBEB9C0BB802EF726C3F) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/icj2yO_MROKol4D8_t5nYA/zh-cn_image_0000002535949538.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=80E476837774487EF21B3C146FCCA03DD0E3F81AECF75BD524ABA904A89958B6) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NXM2Ut2wQEam3LHCIBp7Qw/zh-cn_image_0000002566869371.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=1048F3B02FEDDA4D9D982BE3BC45406C23BCA09057101A4A5DB2340E1C22ED45) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0pMboDzTT3eaWJib2Mq5Ww/zh-cn_image_0000002566709389.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=B30D932BF2F6AD610495422B09474BE106E5B2EAF352F39DC43A0A07E63C04A2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_XzI4LNsRTyrw1Je5Lf5nQ/zh-cn_image_0000002535789594.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=CBA2A03861C990656538BEC141B62B1E387EFEDA4335778F7BE32BDEDA51B10E) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SrH2BHLLQrS91FqXrOzktQ/zh-cn_image_0000002535949540.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=7BB5BEB69EDB31A74BF5C4E9BC983A7A556AE0C2CF7D7A16E485E16AA9392D57) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aC9PrmH9Tzev4O-2-Z3RiA/zh-cn_image_0000002566869373.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=BE84D73CF5DDA1D7CA93BDEAEF1108E2F4097E163D3380E8610B83C76C88B1B7) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sLpBbvpnRAysuEMqySw9eg/zh-cn_image_0000002566709391.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=C0BE0E1570C9FDAE6C9243435A494DA62898FE17B8BD43701303747F0A8414B9) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/IuujT5iTTk-rOynEyl_WyQ/zh-cn_image_0000002535789596.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=7482AAF2D79C2DF909B25B16F70626D89FAE7AA9C4F42D1369E0908E9515B37D) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/aC8JK6VsSZea7QwA2VfaOw/zh-cn_image_0000002535949542.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=67187BB0B000BA2E0435045E537609E812CB4FB71A524EBE3C8D7F94996A743B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vqR5ddigQ9ywC1-CCaaYxg/zh-cn_image_0000002566869375.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=E592A76FF5F4B97D9F268DA0E4433AC67694DCF285885B4EE32B953463E3D4B2) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UVr2aZoFRG6RKZYWyA9KgQ/zh-cn_image_0000002566709393.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=166EDD2F5F4A9BDF6CCC7638FDD15AB58BFF37EEAD11AE495224E69D0E800EED) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dJCNjPOfSF-njYTsv3XG0Q/zh-cn_image_0000002535789598.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=C6B8ED0163F7FE5E7CF1B472290FDFC2AD87A925D017F7625F8689CB2F34DB30) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/SFRTzRgiQN2euBnwvn7IhQ/zh-cn_image_0000002535949544.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F11AFCE68C3B715DA15B5D2B9E4B3C7E5BDB415651036E09D6A960165E27E4B8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5NTEzPD7QkyUuvqZO3oEsQ/zh-cn_image_0000002566869377.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=EE4CB9FCD7F3E87C8160E0DF78A27DC0E40A1207301CA16D91389CC349C0F71D) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M3F8wzf8RY6UZou75gGF2A/zh-cn_image_0000002566709395.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=8F22C8B5F72058553147EC2AF94DF4F3A88FF3998B692021A23DBFFEA5E5A5AB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YTYpWPzlQouj7C_sliIgCg/zh-cn_image_0000002535789600.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=AC6EA69A76D68827482CA70A2EB500EBDA5174E28CA40D8CAE2D006EBB4FCB26) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aKZHl6rFT9G7A8y_97-bgQ/zh-cn_image_0000002535949546.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=5DD969EB764D9A2AF745E8DDB258DDB06F74932D482DC22B5A59B65487A2976F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5Fk2t3ozQgm_lnODTyBZkw/zh-cn_image_0000002566869379.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=D122BD5551E09B662ADE9577DB188A064042BA05ADB288C9D888AE531C57772A) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2zHQsYs7TwCDioiVXxo8Kg/zh-cn_image_0000002566709397.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=FD7522E3C47DEEE16586B581D219FCB4948F7FAB481CA1279BDA9E63B26CF7C1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qe1Nys7URrqMBhWcjS56NQ/zh-cn_image_0000002535789602.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=1564DCBC3E22E339605C2EE9AB27866E4A2D670AEB55CA96A197C8E2AB5ADF05) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GN_uCkuVTU-cLupiYbF8pA/zh-cn_image_0000002535949548.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=D403452B49AD0DAB6901847B153BCD9B635C40A7694DE2FD388371B2BC363D7C) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/froqUDQCRk6qdwY6NtLA_g/zh-cn_image_0000002566869381.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=A4D35C0DC5DB645A0096397EDF33174E20BA128166A0EB24617D9FE08B95207B) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/o8FG5N-9TLublhc6LBgn2Q/zh-cn_image_0000002566709399.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=90AEDDA5B47E27D080EE5F342CEAD33F0C8F31C7C7B8589277C4E843942EA19C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w0xAT_SZSwGtKKcIP43-Rg/zh-cn_image_0000002535789604.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=782C742E2FAE8C7B591AAF6CCF4ABA788783564835BFD753760065D41F6691D2) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Nw1IL7FySiqsm83mmJvgrg/zh-cn_image_0000002535949550.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=AF966D8AE1FB9E23E939C8E78B6F0A9E9178CF3FE8E8EF78D134D6978AE9905C) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SH2Vi2bwQHy4iHinx93EIg/zh-cn_image_0000002566869383.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=CD6C3B6633FE427BD197539405BD59650E9ACB0F824A6C1218A606EB978EE8AE) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eO5JgJI-T9-SUDEJRJ54Ag/zh-cn_image_0000002566709401.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F3A8ADA569FD77D6D5BD0047D5DA378F1D3C2926B258468E8E58C4C9E9EBAB88) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/97Dhdj-xSaK-Z-2lunsg2w/zh-cn_image_0000002535789606.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=78F8CC9F5F29022DA72574087DA7DAC9DD7FD5A74D4938504F9BD100C22764B6) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7szxUCnCS1OLRnqMCPBeCg/zh-cn_image_0000002535949552.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=19B8C04431E742DAA6690E74C7BA3490200B986F5AFB90A8ABFC6B188A82FB09) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mGJhBKvgSjmdCGcfdi3F0w/zh-cn_image_0000002566869385.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F5C5756F6455516CCA2B83C4B66327F7E3554F61BD9AD5B36EC00D2050525A05) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OdN34v3KROaT37VOXwtjlg/zh-cn_image_0000002566709403.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=76CC242783A8A69D3CB47F71BF14CC6CCE0F53AC4BBB206F4BA6F491811245E3) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/19zg-bVLRoWH3VHfcTNViw/zh-cn_image_0000002535789608.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=34BE130E43431760CDA28C180BCA210D1E5D91F004318804CAF8878A61428D11) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xIuMxN-9RyegGRL5dHaEJA/zh-cn_image_0000002535949554.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F1B7EAEF126C7A3D1FF1771026001A692CB2286E2B08CC3CE1B35AB707F6D402) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/VfEoizikRBeXtMe698hxSg/zh-cn_image_0000002566869387.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=0B1415697BB9C4CA8D97BA7A89ACE99E6A712BF246B74123C8F5A62B4E12E6E2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wwhjfe1PRH-W78dl5NoIoA/zh-cn_image_0000002566709405.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F0FA64A38912B82E7128B15D0A105082FBE85C18DB237B1AB99972D070449D51) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1LNPgbj3Rt6wCFJKKRHe-w/zh-cn_image_0000002535789610.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=2184C174B6589FA1E52E84D7CCB596F6FDFC73826D58DFC7EE81F5299554A3EC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-eh7Cr7VRFeJdcig6Hrpyg/zh-cn_image_0000002535949556.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=DAF0BC7C3E26B732642A89923D77820513DF9D693DB72349E36BE213888631FB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Azb7Wy7HR9OdIRqK1DMvuw/zh-cn_image_0000002566869389.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=12392BB2AFCC878137E7EC57BDC629AFBEA6CAA5BCC0DD447CD104E0099424C8) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CiQCW9mAQfS0hhJwMmvZJA/zh-cn_image_0000002566709407.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=5D1C0F01AF415B26C5CF713A4F0EFC12C501F56268C0A45FB9B855FC484B8B1E) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/D8l8UXDfTSme0sV7RUpO3A/zh-cn_image_0000002535789612.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=54AF94F1014CF27880FD91FCA878A337EC1E557E5CAC0843312CC111DE4424E0) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_SOZVNmkSlijpq0jDaVKoA/zh-cn_image_0000002535949558.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=43571DCE0832708B661ABFD4D41AB72E7F7B03402004AC5CC3A4ACD66E9CDE4A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YYqFyBoGTA2vZXSDPZCjOA/zh-cn_image_0000002566869391.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=B63F4E6BB2868D6A3DFA48E1C7BC680952E66FF9FFCA15028D40F43B804504AD) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gO5RYHc0RkuRbo8tl5cpUw/zh-cn_image_0000002566709409.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=BE6C6D9284A4CA5F7B087B8ADC3C6F4322D589CB9617D5DF2BC09AC4AE341393) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/u3J0eTcETKCFoPO2FGUlrQ/zh-cn_image_0000002535789614.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=5C591606AB9FD4886CFEB9BB4AC581371EFF7F0869E80E491927982D585AD1E6) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/f9TxVgxLTDiVA9kr2x1xQA/zh-cn_image_0000002535949560.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=DBC46259E373DEFFB8612E5F574BA4E8E062E78AFF2B0FB9D3BC14CB4DDF3FD9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uxLUOaLnS92fwrXjhBgHsA/zh-cn_image_0000002566869393.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=9FD212BB700D2256C1C286EBE9609316BDC47136C0581B87023641BD94F9FFD4) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wmjwYIcKRwCSIDy87TlFcA/zh-cn_image_0000002566709411.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=E20B073994F8BC8FBA7F2FBA615A12548A7D7122C711AACD4937358464B03E92) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ta_HAbEJQYyYXC2lDfDogg/zh-cn_image_0000002535789616.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=94D999E767DD370EC61346AC4D459878CBD95DA10246E164094AE20F3986BDAA) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OrZn2KpkTiODEIzPWvuL5Q/zh-cn_image_0000002535949562.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=CC612C97895251245A79D9FC9183055D1E79D5C33BD37B57D95187E09EE697E8) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Yd6hiKb5RrqmUCZ7hJqrsw/zh-cn_image_0000002566869395.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=9BC74CDF77BCD87E909A6504A1BBAD3B7430F445D68C8873B3A1D6F15E2BF826) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/W7n6-EhBTuCWfiAxUu68Gw/zh-cn_image_0000002566709413.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=2139F5E10A8DB55EF5995088533A8BD0ABB375989E0F3E448E0DF880F3AA4F1B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UvPE1EaFR-aHXXZgrpvt7g/zh-cn_image_0000002535789618.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=4969E3358F2CBCD68E9DAF37E4D7044D8F0FA902A288802144BE61AE90BD5A0C) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/adwBfBfYQSSnRidIkB5IrQ/zh-cn_image_0000002535949564.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=4A8C30F6137DC3231E7C066A994F3A0C38533B9EF943E33DFF39E130DE4B5E45) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/usfrYNLGQgushAeNs0NqTw/zh-cn_image_0000002566869397.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=D6813C7EC624B2AFAE5CFDCF639383AAC6B93503536913A8EA33A40BA4B83991) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YsZTJb2AQres1u2YP1q0Xg/zh-cn_image_0000002566709415.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=CAD941A53E1D90D3C2F4DDCB8229941261D6AB6311588EFD35D3C2340A633AF5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ay-KcBR2RWObY9boujQlbA/zh-cn_image_0000002535789620.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=8D4F1B6AE52F197E6E34433713F78379D9E8FA4211A77C601C991E110A9C3F13) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pdJ0N-IBTwG1Fjo8F3ZcAw/zh-cn_image_0000002535949566.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=FBEA71F1BC1C32E99EBC7F2E5F7DCF0E6B851C3AADAA5F67D42871825B9E2281) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dAqyaaSPQpuWimDA0trtQA/zh-cn_image_0000002566869399.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=0DB856654165BC9B05DC2242C619F8C0C43CC35CCED08EC6A4AD12DB0A3C8961) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jz5EjXpbTy6Y7S23nNZ12Q/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=A70628C15B35115FBE859004AEE7C40A233BDF93864019B26348768C68082FBF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D2m7NEm4TIGfjWasxLeddQ/zh-cn_image_0000002535789622.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=B0FBEC38BE6A3EE1EF282AAA303FB58C79EF6C77A62B4AB5E430C4728BEA3811) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f9Le-Z_JRPq2leN2NrqPhw/zh-cn_image_0000002535949568.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=2B3850A65A89713C1D823645F4C234C4DC2E48ADB6A9E799A3C4CFA68FB55AB5) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XwNU10qRRQeSCmkd5xcF3A/zh-cn_image_0000002566869401.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=01F992E3A781DBFF8CB1D1E63484E41B22F3F8F922C41281C275B26EB925C78C) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TMWufEkPRC6JEZpbkwBibQ/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=A67945F9B849C63F6AE5968FBA8B6C17FDB671A0856C6782AAF2180FC0480ABC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/har11OZAS7K2y-7K4Fs8Ow/zh-cn_image_0000002566709419.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=FACDFE55AB9B96A079327E4C1F05C0471C00C2A2D9E95A7A278C733D082AB5C3) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/MqFJOAc6Q9uAP14cHwhNYA/zh-cn_image_0000002535789624.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=6A1E653F19722D1C9F92DC3A47F5DB8F41F1B9C3E1DDDC3C521F255B2DD95A06) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/FJbQ5BzBSd-8SVEoTOvi_g/zh-cn_image_0000002535949570.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=CA60AE1EADA00B89A43294A16E24E7623BABD5614FAF007D47BAB781D54204F7) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/p_cZt0amTZ-zEkmhX1uWpQ/zh-cn_image_0000002566869403.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=C7B95FED7C64988C3CFD2E824841E981AF0E58B91FFF7D9241AF88798437EA4E) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hIBpgsKuQOKj7xsM3xyZ1A/zh-cn_image_0000002566709421.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=8A84F8CCBA442B0F3F597C97B99E1531671282A2587C86D6195DDCCC4082AE0C) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_EqLXtnEQxSa5ahDTGuidw/zh-cn_image_0000002535789626.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=C198527DDB89770CEF8B9917C4EA96C96B25EB132156125B92A74C76604033F1) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zgPVm-4YS92H2vCY7LkpwQ/zh-cn_image_0000002535949572.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=F9435CF87ECE7022850AD7F4852B01D15BABACF9814F0EBD920A0C45A2E2864D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3c9ltMn2R7WokEmt03mzQg/zh-cn_image_0000002566869405.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=AE8C144C6EF7447090AD47A0B6F4002D2AB3066B3978349D3430B43141A7B004) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/64B1Gu0oSpuS8cDQNY2QxQ/zh-cn_image_0000002566709423.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=EB62DF856D32A7A5371B6A49156CD432C595EBF66EF586FC5574D73B9E2B87E9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_-UVeHd_TDyEuVsL1BGigw/zh-cn_image_0000002535789628.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=900D89763B54B8BEB155A7497E558D8984E4D0FA940E592F793806E7A1489150) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qObFmpDdRHagpRUC6OAHmg/zh-cn_image_0000002535949574.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=7231ECE2DEED22541AB5D2EBA033764C2728ADEA8A00261900826C2CB645D277) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/jCCjt3UZTse5bSw-QoVeuw/zh-cn_image_0000002566869407.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=B8212F27326AA96097CDF5BB1436B92E8A7F2AA94E7BD1EA6B7D45FAE9118C04) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uai-LJEARh6vKW1mUWSuxQ/zh-cn_image_0000002566709425.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=D980CBD29D432DE094BE3F560AE846B1B96C1F44FFDDE50AFE82094D79E6872C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WizO8OTLS0SYRoZhqBTBgQ/zh-cn_image_0000002535789630.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=1FF89F845A23A1A1B1DF82E4E3C6D9D6A8A70ECEF7641620865D2D4F3B3D1364) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eIT7t2u3QZ-ORNFF2AooKw/zh-cn_image_0000002535949576.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=BE408FB360FF3BAF1021B8CF02D8949D90D6660BFB96F1BBD74CD3A5E04094EF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vwcORGOyRPirEYDv0xQdpA/zh-cn_image_0000002566869409.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=2DF09F50B480249E3B382E495417E9FDDC914EE8A133555B586C0337EDC12D89) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fhdKY60CTa6L4NVmc1ipRA/zh-cn_image_0000002566709427.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=FA27FE8B7803B3F4012927E060FAA2039181AF73EFC93E3E1F998D341D3207FA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VlwP3bMtSTGtCS2uOIx--Q/zh-cn_image_0000002535789632.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=51440437B87BB87B95331ABD292A6FA404E5138ED10D929FCA08A5EEC6226283) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gh1LEYD8TI2B61ybr9CWOw/zh-cn_image_0000002535949578.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=14D9700888CB4AC57442EE9A1D4830D15CBE8CC29163329E581AE4C392351E31) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XIyPi4CTVGBDuU72cuEHQ/zh-cn_image_0000002566869411.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=501578261A6A584353896866DE90E8131AE35876E105B7403CD98A0AFC81D8DA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UjnILisFQhSZB2S5GeqRuA/zh-cn_image_0000002566709429.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=C8698394E2654C0A153BE4ADB64CBBA4BE3F8BC30F2E886E8E00ADDE093EC91E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_0eFQ-ZBRGmQ4B2o5tXZEg/zh-cn_image_0000002535789634.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=62F26770E9E221BDC5F1BE6B6989BA2A8268993E067353AD94123D1B11D7A7B9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LjFFjQaFSC6oeyDX0jsIKQ/zh-cn_image_0000002535949580.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=488ACB999AE57427BD64C31DA61D4D4A21526F0B4118F142B0DC1EBBAC4FA87B) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UqjTnxADSGaluQ_YwkxHXw/zh-cn_image_0000002566869413.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=380F0FECDD1E39283F52C44479C2484FA081680430D135C142579257A6B5F960) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GWSRIFUnS6S4BA0XbPfP-Q/zh-cn_image_0000002566709431.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=53D2266B4A98B9FB686018EC9216BE163432AB9188C8D9EEE38C03C2AA417653) |

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
    <image id="image0_0_37" width="120" height="120" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAYAAAA5ZDbSAAAACXBIWXMAACE4AAAhOAFFljFgAAABZWlDQ1BEaXNwbGF5IFAzAAB4nHWQvUvDUBTFT6tS0DqIDh0cMolD1NIKdnFoKxRFMFQFq1OafgltfCQpUnETVyn4H1jBWXCwiFRwcXAQRAcR3Zw6KbhoeN6XVNoi3sfl/Ticc7lcwBtQGSv2AijplpFMxKS11Lrke4OHnlOqZrKooiwK/v276/PR9d5PiFlNu3YQ2U9cl84ul3aeAlN//V3Vn8maGv3f1EGNGRbgkYmVbYsJ3iUeMWgp4qrgvMvHgtMunzuelWSc+JZY0gpqhrhJLKc79HwHl4plrbWD2N6f1VeXxRzqUcxhEyYYilBRgQQF4X/8044/ji1yV2BQLo8CLMpESRETssTz0KFhEjJxCEHqkLhz634PrfvJbW3vFZhtcM4v2tpCAzidoZPV29p4BBgaAG7qTDVUR+qh9uZywPsJMJgChu8os2HmwiF3e38M6Hvh/GMM8B0CdpXzryPO7RqFn4Er/QfBIQM2AAAHoklEQVR4Ae2dT2wUVRjAv5kFW5RkV1uFxNhuYmIbTbrQgx7AlR7kYihcPGhsXALcbMQEgocm0AQPhoMkcqvETXowkQu2t3oobOGgB2B7oiZqiyER0pLdBKRN2B3fN8uQZXb+bLfzZt/7+v0S2jLbbZv9zfvee99731sDAkjN5lKPE5CzADIGQBos8a9GGph2sGh/NOzPt4STIlTgyupQftHvCYbXxc7ZXNpKwI9C6D5glMcyIG9WYNxLtOm+0DGX+7Jqwk2Wqw+GJaKscNZRyB13P/ac4M653GmownnRrFPA6EZKNMrvXkCHdTwL0dhyUS4w+mPAV2vZ/Pnal1DrczEsc8slQ8mowm7sk+0QXU3AaZZLipQ9SBYY9ojZhL+BIce2KrxsQoJHy1TBHIZpWbALGJKIbjdjio8ZYEgiMpBpsy79yFDDQsEMaVBwGhiqcAumDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmzhYgRG9nN2S2vwE9Hd2Q2vKifW1pbRmWVpehUFqAzYj2glHkF69/CCM79tqCg5j89xpM3r+2qWQbHVexeFBPxnoPCrn7n7XWZimUbsOxPy7aLZs6WgrGlnrp7VEY2N4DG+Hs0mXx7xegjHYhGuXODJwKDcfNMNZ7yP7sJxl/D0aH4sM7MP3gBkwt3wTdSGw5vOsMaEKUch2yqX77c6Hc2C8vra7AiZ6PxMCtBz5+9T27ny8/+Q/mH/0DuqDVNGnirSORynXAlpxN9jdcL5Rv2/21A/7uib6j8LPoHmT8HTLQRjC2Hqe1yWCi74jnda/wPdw9GHkkkYU2gnHELBOUNbJjT8N1bMUlEZa9vh8HeqqjheBm5rhR/R4vpldueF7HUbzsG2+jaCF4uGs3xAF2ARmPqReOov1oZR4eJ1oIfl9i3+smm+xruDZX9s98OZk0VVFeML6AcbaQgZcaW7BXH1yPX2hXAeUFD4jFgzhJbm28mcJSmjg+UDVM83Khi1SiNVGqTplYcEQkuQUz7YAFE4cFE4cFE4cFE0d5weUnj4FpHeUFh2WRomb+UWPeuZk5bjnmv7NZlBeMWaQ4JXtlrXo7uwKfg39f0IJEO9GiD56r21Uhm6LHdhyv/HQ9uGasKloIvhrTC1jbIN/4uz5IBq9mTS/fAFXRQvD0Sjy7GQs+kSJse26hrO5Gei0E+7WsqJm8f73hGm4ACBpkYbWEyhvotZkHT967DjLxu4m89mnVc/aO2hvntRGM+6JkjqaxysGLA12Dvs9RvfUi2ghGud9IKjNBSV4RIpvq8w3P+BzVWy+iVary+7szMC9hvunXesd6Dnlex5tt//y3WhSvaZeLPrpwMdJQbZeUerRebLl+G+0xkuhSmaidYEwlnvzzJ4gClHTyL++fhWUyXuANgZFEF7RcTZq8d23DZZ8oF8OsVzQIKpOZeqBuUsMLbZcLsd/cyNwYW6533rlb+WqF9aD1evCFFkMlLgxM+aQXL4VUDg6/4j9tUhGtBRdbrNP1G4njokLY7siRnXthVOFKBjdaC251s7nX5nYEB3B9v5+EYwvB53ece/NTabXKUaO14JHX9kArYLF30M2Bg7gw0diSF949Z9cJY0JEVbQ6wqEeDKcT/UehFTrNrbBjazJ0lQpb9IW7v9pHOeCig9dNUasr3mvfNLUzuVZAJbQ7Zcep5ouibNOZKjWbtECROMIOCs12ClOM8GUvjjSLNoKjFOtmvQek6SRaecEyxbrBefXZO5ebFo3JkLGeg4Fnh7RbtLKC4xTrhpJo5QS3U6yb9UpBwbhBIKggPG7RyghWSayb9Upx0p1hoqPIqYfRdsH4YmBm6DPxYqh8mAmyXtHDXYMiKfJJ6J4uPBhVFm0T3MxdrirrEd3M8YsyD0WNXTCeuTEqwrCOYt00KzpMMi5Z9ovMmYw9Z7EJxnQeboHJxngkUlw0IxozbzOZU77d0LGFH6QMvKTnop27d2bga5JyEeeQUsxN+22zraU9ZwJ/hgykCsa79rfBcbJi3Tii/bb7YF477mpJaYLtwzrfGVV+ZCwDXGnC0bMblHsh5v1c0gSH5WqpgwPJjEdVol92rPhITvmpFMHOEtpmZ2Rnc8cTY2p0WtLbBUh5z4ZscnP0uWFg2csJjy2+OOJ2ui58e4ApieWnUgSHVcRvFvy6KBxsxQWfskMcFkwcKYLjnuupigqvgxTB8w/1eV8hmahwdocUwTgVoP6WcWGoUj8sdbEBR5EHunZvumzW0tqK3XpVCNFav/soEw6PoonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgomDgheBocoit2DimGBwCyaLcGsaFiwBQxMLiqZlwC1gSGJU4Za5VoE8MFS5YsJQviRi9RVgSGEYkF8dytdG0UYFDlsAJWBIYLuswDh+bQtG04lq7QKjP6LvHUen+PWzefDjofx5gyVrjyUcrgmXzv8N9zdsm80dr5hwWjyQAkYbMCwbLrmI4fXNnbO5dNWEM+LBz4FRHgMHyWIc5YTl5x4LeiKKFp/2WSbsEj8kY1mQfvpQGph2sIgfjFr2cdGqQHEbQL6EMyEf/ge9rhOytvtnwQAAAABJRU5ErkJggg=="/>
  </defs>
</svg>
```

| 扩展前 | 扩展后 |
| --- | --- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G6Ed34xnSJ6RqRmwZ1ZApw/zh-cn_image_0000002535789636.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=36F9E305C4440CDFB0B983077CF1A7C8078E634B9C9C26F9F6D525F063BA171F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHcsleUcTFqqY7gkyrDheQ/zh-cn_image_0000002535949582.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=407BFD651447A256F7CB6DBF19E737C39114A0E9E1945C1656243E31B4668733) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cuVXGXHPRO6-kQVrVZOoeA/zh-cn_image_0000002566869415.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=AA5E43E99DA55D7AE559C860DAAE1ECC4EE580E305D622F69FEA4059F1B35446) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ff_IWYiQTUKuhXMeikrZ-g/zh-cn_image_0000002566709433.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=4E85BD1BADB00ECF898F5AC5166D5243C187A315B0FF7AA9782B1D6E9912E8E0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gExoH-_yQpSgwehc_hIdqg/zh-cn_image_0000002535789638.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=32056B21B8640777C3FC6344B3CA60A0B42887EDF75FDBAD9AB5E9368BB05FC7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Istmm1W3Tceg8u105X6HiQ/zh-cn_image_0000002535949584.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=09C434D2BDC7EB120B79165D8BBBEBAFB646EBA6FDB930FFACC8DAE3A15205D2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/feSI7ILTR1uwt7mU871adw/zh-cn_image_0000002566869417.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=384CC7D92BFBC96B725FF3E407E460B438F72A9E81B335BE3D3142F2F802157C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WKmlZlnFT2C6YZGMCTk6mQ/zh-cn_image_0000002566709435.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=318E5AC09A7258709FFC33CFC259B8C7EAA5A1C0020F3A78AEDB621654012DBE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/os9tJOTOQZabXC4lnt9Arw/zh-cn_image_0000002535789640.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=BF60D99A2F3E0D346DA80E1CF802BAC11FE8D626BBFE41C8EC8C0304F18D1837) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T18jLZ72Q6So-DK-ocwfOg/zh-cn_image_0000002535949586.png?HW-CC-KV=V1&HW-CC-Date=20260405T025032Z&HW-CC-Expire=86400&HW-CC-Sign=22314E0380B63FCC30DE44E0C9A63780BC8F0170AF9BBEE3FB40B48BEA1847D0) |
