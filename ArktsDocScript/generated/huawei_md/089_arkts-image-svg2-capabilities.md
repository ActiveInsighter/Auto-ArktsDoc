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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nF53NYegQ42Y4g30GI05Vg/zh-cn_image_0000002563787021.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C59BEF098A503F7AE862AA48619BA7C1CD16D834D2A3BD6591F6BBD14A45C97C) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uZbH8fBmQrOtIA_gy_2fYQ/zh-cn_image_0000002532907126.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=1CF0C1BA7AE398E893838F66CBD1BFF19544D1C4C2E27C816C9599263864CC06) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/xhY0Ya1_SxSAowqitPw_sQ/zh-cn_image_0000002533067074.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F11BBCB4845C3E9D1A99E275E1A3D009C50D3F03860A9F0EE5AF9F8AFD5B1538) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tZtCr19sRkSQG1srqHoDig/zh-cn_image_0000002563866977.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=8FCE7AE4AC7C607469E8E610227A98EFB778A5454C9D1E32B7AC59DEA8B07448) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/DuK3jIg-QtC6F1MdD4f0tw/zh-cn_image_0000002563787023.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C2B2CBCCAF84D6813977A39F468490AC0C64F08961C698D3C06CAD93CB3118E8) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-WpqmfKGQaK8jWaI8LDoZQ/zh-cn_image_0000002532907128.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=1AD1E2550487CDC55F7B6460A637820FBA8C7C12E5B64A5F634F6E73B850DE55) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6OCiTm9CS0WTBhbKF-TKMA/zh-cn_image_0000002533067076.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6837598A89944CEF10ED6260B7C988BE6C0295174E59E0128CA5E0DFCE9C0E16) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/rMSbKLbwSmaZSlEbEXuWuQ/zh-cn_image_0000002563866979.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B9EB9A39665ED5C5686E1BE5A1F759CEDA5FAFE7C50D9228B3740BEA298A1BF5) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XIB5dkWNTCCxP-pB-bmDwQ/zh-cn_image_0000002563787025.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=EE4DEC91CE69330A59D165BB21E82DF52796D19E731BA691F922C9D5D3C31273) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9nj1LBG2S-Gu5qTOWRcRLg/zh-cn_image_0000002532907130.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B248F7E3140E93BEA0F6880A1621E5DE8EBBCC0F3F5F964A6AC39E1C1EFD55DD) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MSpIfr27QbSy7Lu7uvbaZQ/zh-cn_image_0000002533067078.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=85D4046601476129FA8642A9B5546E9796998005AD3148DCF7E4D4503D07CA32) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/NtcSKjagTCCxK0TgHwgPgg/zh-cn_image_0000002563866981.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=0E8C90B4D71845DD876AF708D5543B23FF7597DE6F9748518E27B111A9DB4D9D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dNVmhl_rRO-O_xIoiqVWRA/zh-cn_image_0000002563787027.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=72BC83E13B580777F083D30F691E6825C578BB25D40FD2BAEAFAC47C940BBD6C) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/1Y9RqQNiRu26x5HcbkVe3g/zh-cn_image_0000002532907132.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F9CF5E1F24EB154E51E5A7A235C0D9538EE14DC7743FC05D83AF68BB613688BC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qughuPY3SnW8f3QyVKl-lw/zh-cn_image_0000002533067080.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=7F6304AA008BE49FA907F83521F35E7D0EB8FD9EBF511FA795D3C6AAF6A531A2) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gZ1G0fkCTcuGYeVqDU7Aow/zh-cn_image_0000002563866983.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=AC866446E2E2D801126D2B076916861437F3FCD3D3A3F56C09DA1F29F23D5A3A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vJdgSTHUSAK025u2QQ7vfA/zh-cn_image_0000002563787029.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F9A6E519B585548875D9DF8D943871D8B2AFB9253E68268101103551E16F9611) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RFvQknBZTpC_tnzo6ToPOA/zh-cn_image_0000002532907134.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=D40D21BE6439B3851A3FC6FC17C705185970FD3FE9FFDFBF22BA1E7D969072C8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/f7GUxTg1RTyrSmD_xXVblQ/zh-cn_image_0000002533067082.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=296B6416048148A8904C4FE2916FDC146824AF066647053C35FDFEA75342F88E) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/r5Hhze9fTj6ZjOnIOI7RYA/zh-cn_image_0000002563866985.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B4517D8A8B4B30AF583ED45C7DE691CFE752EEF33BD580B198393E119C117DEB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8YqIAj-zSxKMv_VhT8xpJA/zh-cn_image_0000002563787031.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=69626C9FCE90B0D51B33BC2C8E70F876DB5FE48AD97457BBC97D1B214D79AF90) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VeuKSoDFSViKGMX5ghvdyA/zh-cn_image_0000002532907136.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=DA9666128B648101918372F3BB409991A726E87415CD104444D04EE720DC76CC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VOubMPnZR7WclUYSbF4g0Q/zh-cn_image_0000002533067084.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=7525E4E42F901B0B41D0FE8ECFB308AA4FA001C02DCC4DF988CBD0090372B924) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/suk6tetJQ-eTb_wP65OFnA/zh-cn_image_0000002563866987.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=24937CA21015606A5E59EBD24E8F54F082DE2F4967115EAA616F13AB064CFACF) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VQTPtYMITZ67W1rOi7YFEA/zh-cn_image_0000002563787033.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B8C89D625C4B7A7D7005D04DCEA49D4E777AD50980CB9FA221961AF918469906) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ShI4i9bWQa6zEWWnzc-fFw/zh-cn_image_0000002532907138.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C4A57B425799CFE847A0E6C6196A985E864D192D0C662112CA4E97F6D62A9BC9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Vxw4b7XDRnaaIKXH91RceA/zh-cn_image_0000002533067086.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=239E524D1A2C05C20EA3750793B90302E02AF2F12B6FB9C4D4912B86A424D816) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Hms8eO4mQueMUVXv-ciuag/zh-cn_image_0000002563866989.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6FAB554FF0D629C0E07FBB59A9E414B9977E7A52F494875603CCA76E923BE5A7) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yL5NC2uDTxOEmGjFGg_ujw/zh-cn_image_0000002563787035.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=41C9BB5FD3674ECB7AF9D31E3D4977B235B99CD03A878E538C1B9B63A8CAF9E1) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/mJeE5CrnR6uZLX97PmdTwA/zh-cn_image_0000002532907140.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=3EFDC8740869B9538A59A5D8B05FF75B2891B15674F7A3376069920C96A86DCB) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/wN439rM2QV-PtLCa6cIQ5g/zh-cn_image_0000002533067088.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=5754642958F8F2DFE4AF4FF8F3B64CE1DCB4C21C2524522C485DDB2DB5AEAD64) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NVicZqDASZW0d_-txGMZSQ/zh-cn_image_0000002563866991.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=75F5417AE869C6A87A11E073272BD4A31CB2B5A3525C2D3943F7E92D864DD191) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2qiaZoavRXG5c4opSQA30A/zh-cn_image_0000002563787037.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=4A2089E58581AB978E666B6EA3DB4A046A63DC0EBC3FD7295212D57BDF09912C) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lX225aVtSu-4nvAtUyIPMA/zh-cn_image_0000002532907142.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=0077C629937D1512E27450E11269151CF1D3B973EC1383541BCA8A6E81842EBE) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zUifEkaGQreX-P-W31DXfg/zh-cn_image_0000002533067090.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=8B2CFC702522D813911962755D4AE0055F7806ED90C1277699346F80ED623AAC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/X2zABTc6Q9WbYXK2ClShLA/zh-cn_image_0000002563866993.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=5BD9F5AF38890C31D978189B3A53A049D9EE26742D093186990D2EF24E909698) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/v_j2wR1yT7edorhG7el2Vw/zh-cn_image_0000002563787039.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=9E37BE513375175ED7C3D82191461B36415E21741A67D0025DEDCC6AA59F3CE5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CW5bJd7iR6qzFrmkEfIfrA/zh-cn_image_0000002532907144.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=CF2457086C7CAD4831BC4C773E594DA79ECF299A897DB04078D5DE96AF7AC65E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nTuBuaANQki8toorvozBBQ/zh-cn_image_0000002533067092.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=AFDE9C7FDAA5507FA0D8051E5437D3F7DEBBA82AAFBF58616B57DA93C63B56A5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uKuzD0l_SL6Ch_R9pAPaTQ/zh-cn_image_0000002563866995.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=AD81C0630320AECD7E1527A9498BF3827DB9FF8503E143FA6DEC1C7C3751A650) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ttv8C5SGSPS-IuWGizRPWw/zh-cn_image_0000002563787041.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=36E0FDA0B7E0E5780B7B9652266D641DCEB2BC96A66BC0070784693F44E1C34A) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Bwfe0_WrSW-txYWIG-f2jw/zh-cn_image_0000002532907146.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=9B5E6719C8D898FB34F3F67B7AE8052DC57232063474C18A212350C67D2E937E) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ouyNukCiSX-HNT4CfdBqOw/zh-cn_image_0000002533067094.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C6D789B604BACC89B077B68319C2B9820282BD1922D7484D7DDD75CFABC5A672) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RqKmqxDmThCm1uxvggu7lw/zh-cn_image_0000002563866997.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6B6BFB1132162AE70436B355461645AC39987169A7151BDADD44C71D9F5E532A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/N39nkasrR8i7MPz22lHw2Q/zh-cn_image_0000002563787043.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=589C23DFFC16D64D11429E52ED9B3A9961C934D6D0942CD792CCBEDB7735A3AD) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ro5Zmt6wTPuJEncra2YSQA/zh-cn_image_0000002532907148.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=EC26DEA9A85D189253F6A0BE70909463958D04F1A423FB67AE67C2F3DE930ED0) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9Z2fbEgITBqHpUI39CeITA/zh-cn_image_0000002533067096.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C456DE9552829BD485AD2FD070C7D2057D10FDF449493BCF4387750EAA68D1E5) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4pfSQmlaS1afzIsOsjJLdw/zh-cn_image_0000002563866999.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F93AA63E29D283497C18865587027E567B28B4AC7EE2C329229EA50F92F7977B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/omfYG4BKQY6lpCn4NQasBw/zh-cn_image_0000002563787045.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=BB4B7CE4870528D072952CD73BF5E83A3CB9EE7CF5589ADD930D7C44116D8996) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/gV3e13IRQe6p1gSYI9I-qA/zh-cn_image_0000002532907150.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F9BBB0CB013BAA98E8FABBD80DC9A8F9474034240F39A75DE5A06E2A9BDE0133) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JNt6zIKuTISfGgn1gTqkEA/zh-cn_image_0000002533067098.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B614CC2E3466537BA4B9109F14C5ECBC39C39157FF8C611F2487DFA97F053F9D) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/dMRrxWJWTKmTnypU4ZcXFA/zh-cn_image_0000002563867001.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=1A48201C0E8AAD9ABBEBD27DB971F0F9CDB7AF5938D6AED94AF5384B031006C6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dcke9U_wRzubGXXNCwDiKg/zh-cn_image_0000002563787047.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F76D416C3227BDC95560D5877DFCB2BCEA5402473E1DAA2A4120F16B6C570B03) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VpATvnXHR-yZtURdPUGjzg/zh-cn_image_0000002532907152.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=3077DE74C8E8B5E27E01F4B92EE4801382AA76E6FF8985AE945336D5B07CF7E1) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sUAUQwuHQBmFB12_RQbsNg/zh-cn_image_0000002533067100.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B5758017F7A73BB22C6112888997D73AB2473A3C9C9A6FE969819289D9882B35) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Fu5Q5cI3RpOTLqBSnXFGxQ/zh-cn_image_0000002563867003.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=594C109220CDBEDCCB836E49D8A7140DE405F237B47AAD41E9F38B95F0A0833F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mliCiAXgQe21RNpF4VPrXw/zh-cn_image_0000002563787049.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=466C3C97E3F3B4F0E0AB13132999083380C1B3957378744AED4FAA883C71BE98) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dftpkyeWRQeHjaSSjF10Ug/zh-cn_image_0000002532907154.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=71EB84C4EB52BA954E7F905B8A6AE388BBDA1DD66262046C0793189A721EC557) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f-fmtmNOQz-aNrID8OYASQ/zh-cn_image_0000002533067102.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=612426F78AEFA551B5B3BDECEF5F4E110AD4C5278ABF97C2D99CF989C744EFF1) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jedp2XI_S3yqHhUqiDrKpQ/zh-cn_image_0000002563867005.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=B6FE14AEFE68E3B93ED581BAA29311DB91237688DF4E951263F393E698D01513) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fYpE5uHFQHyXRC44X70FLQ/zh-cn_image_0000002563787051.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=2517810427A07F92E18256265B2F91E643B1DBC7825BF3BFCD63DBF56230C155) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Pi_wzNGGT9uQbpbqeL07yg/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=0C0B4EA06330B006519DFE0C6CC88D2E7C156C2749D07492E55830B5CEFE2BD1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/UaCiXAmnTcSXNUVDXPtYUQ/zh-cn_image_0000002533067104.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=0317560B066D27AF70AE4F623905C39D5A0FFAF274E513F00D5597F61515DB9B) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uymCv_ZNT9WysHsQ_RnCvQ/zh-cn_image_0000002563867007.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=820BC8CD2F2FEB7501988F80B32BF284E17A5AB953BDFC7E99B29B7EE7898693) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/I5yqOxWQQfi3dRP7aP6cyQ/zh-cn_image_0000002563787053.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=9441F33888A816043201F47EC11E1A7D417F8F671214660D46EFA0E52E9A74B3) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PrEX7Ts1TdGeZCoLBJwc3g/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=73298C1BCB19EB08F22FEEE3F46ACCC1F6E60BAE83124FC682A11DC401176045) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4z_Mrnn_SRO1h7BwYgt6sg/zh-cn_image_0000002532907158.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=306C61CD963FA28C515C578D827596AE1E715110E0D4BD4A3758ACE0F98E27E0) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jjjGtwhpSIqe6jgDZ5LWUA/zh-cn_image_0000002533067106.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=E761E10360F9C8010E18A4837FCAD0B1183B1E05A340E910DD4DC5C6FAEAC5A2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/N60h60w6THCGOJhD2t5_DA/zh-cn_image_0000002563867009.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=855EAE43F39AC5233FAA757FCDF499B2683364550115C1042C3307293158FD96) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3Cba8q3XR7CjclUz19o7zA/zh-cn_image_0000002563787055.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=853759F0418922A06F02728EC6B51D4E4930D73F6FED5123FDF2012B3024293F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ORJiok74Rz2CSoBesZ3uBQ/zh-cn_image_0000002532907160.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=9D5C821D39FFD3915BF2F43378D8210F3D5B62D62C159F6F364BAF6AE3751034) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kS8QxgOYTS-d5cNmYusvwA/zh-cn_image_0000002533067108.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=97BF12705D47CA4E457CAC245F40F3FF5C2B57081464CBF5922EA378F73FB660) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FqhrYgCYSRyWv_GyzHVaWQ/zh-cn_image_0000002563867011.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=71DDEB577C3A4AC00B8B83966CF43925D7B89AF86A95711C9F2362F8211BB8DD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IHFglV6YSfagtD4oJXB03g/zh-cn_image_0000002563787057.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=EF11FCF55E9230457874CCC2D98900604A1EF7C2DF049712CC98B40CFB72BBE0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U5wSt5bZQ5CFuFWTImRpUA/zh-cn_image_0000002532907162.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=F86D4A36B570A656CE61F3B74C5C0396937307BD749C2B9DEAFBF45E4364DF33) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Fgodj5KhTB6bW_8curtGFA/zh-cn_image_0000002533067110.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C244C7BEDB99E9D1D11EB0455CC2CCC951FFCE5486083A7D1B1E0338AA664CCA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXQVKOJ4R0e0mhNBj2heYg/zh-cn_image_0000002563867013.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=E47F4AF3BC0AD5345F8D27E505239AFF8EFFC521D04F8CD597753C7253F94FA8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/e841zjgoT7i1NajW3G0Fgw/zh-cn_image_0000002563787059.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=E44BDCB8BACE44F79EF32EBAC197111BEC7E140EE1FED68F438D6853A2D6EA33) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Scfu2NgeSoWMXu9Z7kHE3w/zh-cn_image_0000002532907164.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=A37534212C0277C1141FB999A256D7E5C2E4388CDDB307DA887CEE45C877F486) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tx71_cdJSPG4PgutSa3eew/zh-cn_image_0000002533067112.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=06B61E37DC82F8EF526B86722BBA3BA12519777C516960D41205E1F758FD4303) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aKaVzFqiRhmWYYXcd6iCyQ/zh-cn_image_0000002563867015.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C3822EDD1FF4B79C72EEDBE09386D67C14CA605B5818B9FED71458E6E9F6CC1B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UXmCbSgoRI2edZvC1oZOfg/zh-cn_image_0000002563787061.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=DCF76F7DD09177F094B84469909FCCFD56AE7C3DE9A884E3E67DA97EC1D19BCF) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bfHS5QrdToOl2uLPzaZpTQ/zh-cn_image_0000002532907166.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6BBFB960204903FB9D0FDF35FDB6F23FB53FB7E86298B2837FBB113FB0DE410B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dY1ZmU5rQeOtPK1XrKkoxg/zh-cn_image_0000002533067114.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=8E88C4CFDC9B0BD4A6F93298C9FA8B55B56AD5AF8283EECC109884CE9E17E278) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6KYcMF5aQOC30E3sUOyQEw/zh-cn_image_0000002563867017.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=1F1EF7106E6D6EC254F7B435A3020CA1879B9FA83C566F75CD21B36936E84C9A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/CsUqL_vKQBGwWRIu10UISQ/zh-cn_image_0000002563787063.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=BDECF68A7BFABF3C745FE03BB3A21ACF0385AF2D08DA0BC718E3521089E20E73) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HamQBKSPRIarddT88Qafuw/zh-cn_image_0000002532907168.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6630ED692497C6DDC7DA30060EA4A132DFD87851E692D028C08EFA7DFADBC792) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/hdkBe5lXTu-Oj9dYP7-SRw/zh-cn_image_0000002533067116.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=A1EF4E763CE2A6883E3B41708E4A2A0738A96154FE3A3154D96349EA04BEA3EC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bPcpQD2IQsq9Tb8wMCKipA/zh-cn_image_0000002563867019.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=C49045A8D1A7B5B8D78E9157AE8A7FB3159F340AFA165DE16D2AEEB26592CB4F) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Lsf_5lwtTyW69H7ANU6wvQ/zh-cn_image_0000002563787065.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=E8091395461E0DF625FA4D9E7E112872745A2F9FFCCDDD45D27EAD726A82053D) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nkN2EaSbR72_Jj4tqjogkA/zh-cn_image_0000002532907170.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=54E590D12A3D22D93DB3E006F69451F5C6DE8E06FA9129C75FB834E5B139699E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/z3ypE5fBQyOSkEweS_ESug/zh-cn_image_0000002533067118.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=D15BD12C9569DC4581FEB67F186C6A1B2B9628792C60E4D30239F9A1D662C377) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2w_tvBaYS2uY4WHELvG1-w/zh-cn_image_0000002563867021.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=E7724C0ABD359A3F5C4C20C30EA9D9404480F6C2E9555D4F7F4029E39E1EEB0D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0oCV6JisTKiAQtZy7QPaoA/zh-cn_image_0000002563787067.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=A46AD25BE58138A93C2638162E8EFF8FE627E91B49E9B6147E603507686DF433) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r4sK6GP1SvacWeoZSTjxNw/zh-cn_image_0000002532907172.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=A017CC6C6C5062B95B18503A50EFC60F0AD3555C22B52637863DBDA4946CB91E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zOfrPPrMQr2cYRYV2518Og/zh-cn_image_0000002533067120.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=6C4BC3C53C41BC82B274B09B0A2FFF0F955541BBF7D748F850084BA305B22DB8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFYmzGd2Q6WC9ZfzA0GN_w/zh-cn_image_0000002563867023.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=5C782EA5F815BB7DFFEFE9A9658FD6E8541E7AA440583D94AD0ECAE71E92F18E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sAwW5N2xQqqwlEARGHdNiQ/zh-cn_image_0000002563787069.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=64CD2D6CC8FB1F39FEC2142C212527CF8759E175E52365BD5C12123BD8DD98B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/S86IasA6SlqhjKkGYNmWBw/zh-cn_image_0000002532907174.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=489DA1B6B049DF7C25865DBC4A43235D0A03412E7DE4BC90646B5E43579CDC0D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3UXtbFQ0RPanjHbDJHMT_A/zh-cn_image_0000002533067122.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=556AD3B18279571D57B67A126ECC083880DC66753FAA0EC93FE26ECBF9EAA5E1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Cr4UTxyTLCzjfln5MYI-A/zh-cn_image_0000002563867025.png?HW-CC-KV=V1&HW-CC-Date=20260328T075127Z&HW-CC-Expire=86400&HW-CC-Sign=66FA19776042FE6BA98B9D04AF9B55450A8822EBA5974D0A1AD6CBB0E110C9F6) |
