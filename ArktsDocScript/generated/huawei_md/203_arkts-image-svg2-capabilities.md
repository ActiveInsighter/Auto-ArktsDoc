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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nF53NYegQ42Y4g30GI05Vg/zh-cn_image_0000002563787021.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=7E348D48AE93FDF75A9622641CF338A86E6235E55DA311AA54F7385610AB9B77) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uZbH8fBmQrOtIA_gy_2fYQ/zh-cn_image_0000002532907126.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=475B42F97A31CDDC59FAB88A55843C70F777D77369F531054C2C9AB39072B593) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/xhY0Ya1_SxSAowqitPw_sQ/zh-cn_image_0000002533067074.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=CF420D8E5271DD6D21D9A459A8363251151BF6CAEED4AD6A6B0E066F60625011) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tZtCr19sRkSQG1srqHoDig/zh-cn_image_0000002563866977.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=D2AB3A8CCC2D4F01A89F576199F30949B1283866750DF561B2E9193DD9885955) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/DuK3jIg-QtC6F1MdD4f0tw/zh-cn_image_0000002563787023.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=F210CD3C80B246B42B37F69EAF029F845A4A461456F4329677B7C8B1FDEA4DF2) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-WpqmfKGQaK8jWaI8LDoZQ/zh-cn_image_0000002532907128.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=CD19D73682419BC3E68BC8A621D4E79FE65C50A331CA074416D47BF340EE94E5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6OCiTm9CS0WTBhbKF-TKMA/zh-cn_image_0000002533067076.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A4E38469EB3D29B30C8B95B615DB008DD201232B0FF99FA76DDDE5EF549702B0) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/rMSbKLbwSmaZSlEbEXuWuQ/zh-cn_image_0000002563866979.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A720C3A913EE969D3FB5A372DB04A91E455AF428BED3A3092D3DC5B5E2019DEE) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XIB5dkWNTCCxP-pB-bmDwQ/zh-cn_image_0000002563787025.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=350F97BFBEB0C1B09E6F9AC680B9D271545ABFFD4C8F3892BE5AD3891CF9C04B) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9nj1LBG2S-Gu5qTOWRcRLg/zh-cn_image_0000002532907130.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=1D1727B63BF7F23F35A457FD2473A8D6379CE8B7AA986A8CE20A0089589FFC16) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MSpIfr27QbSy7Lu7uvbaZQ/zh-cn_image_0000002533067078.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=E2654655E8ADD5D49DFED59D6194F88E5682AC464E00BE33B97857BAC3434D4E) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/NtcSKjagTCCxK0TgHwgPgg/zh-cn_image_0000002563866981.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=C7AD532AAF42B205738C9AA3DDC0FC0C0CEF518F6513A8A81AEBC9D34C43C7C0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dNVmhl_rRO-O_xIoiqVWRA/zh-cn_image_0000002563787027.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=789DDD8275B7A7293F11932C6F37171E039EB4A4E77B3E03F271FEAD9349E675) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/1Y9RqQNiRu26x5HcbkVe3g/zh-cn_image_0000002532907132.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=7EF9250D297BF28E9F8B513DB8DD77E8D4E3275F70F21DC0EDAEC6C2ECEF4916) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qughuPY3SnW8f3QyVKl-lw/zh-cn_image_0000002533067080.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=D4E6774C66BD890759D74C0C109109017F7A7D7C183815C74761A8B70A5B77C6) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gZ1G0fkCTcuGYeVqDU7Aow/zh-cn_image_0000002563866983.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=41F03C011790E74278EF772AFB5A13A203C10DEDF1399BF8E0E1002961E9A5F6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vJdgSTHUSAK025u2QQ7vfA/zh-cn_image_0000002563787029.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=34343F89233663313397B34E81068AB14A11D6FAFEFBEEA4ABB83A0E17E118BB) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RFvQknBZTpC_tnzo6ToPOA/zh-cn_image_0000002532907134.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=B2C0A581BCCCA56F43CF48CECCCB5D3DB977CD7DB922C25B0D32AB9E534F2C41) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/f7GUxTg1RTyrSmD_xXVblQ/zh-cn_image_0000002533067082.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=274F01B28B048A1C31C89B87058E2ADB40147A1C18E54F90F2A2B32316A770D2) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/r5Hhze9fTj6ZjOnIOI7RYA/zh-cn_image_0000002563866985.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=B29F50ACBB01DBE33A640CAC47DD7B8A02268BD11C17910F2A56241B3017503E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8YqIAj-zSxKMv_VhT8xpJA/zh-cn_image_0000002563787031.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=254A5040537270107F2B304C165D6CA26F67DFE03AEBF9BA347CCEB90DEA9C51) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VeuKSoDFSViKGMX5ghvdyA/zh-cn_image_0000002532907136.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A11EA88EB6692A71E635300E5E5BBF55E308BB9244F94BFE11A016C5F241CE8B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VOubMPnZR7WclUYSbF4g0Q/zh-cn_image_0000002533067084.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=37FF4A243580B75B3195294FC4A493F09994748052BA39AE3DC7BCB6BED557DC) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/suk6tetJQ-eTb_wP65OFnA/zh-cn_image_0000002563866987.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=D11A1C9A351D09E482C91CA10A857F7F010AAB129E1758022AEF1662BFEC6BA4) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VQTPtYMITZ67W1rOi7YFEA/zh-cn_image_0000002563787033.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=F4A6148001A367BB6E060D020893E8719CDB032AD93831541658E94FCBFD9376) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ShI4i9bWQa6zEWWnzc-fFw/zh-cn_image_0000002532907138.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=B9ED2334DD3CD02FD8059CF4C56CBFFBB75776DC3502375A6D6C648136A4A7F7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Vxw4b7XDRnaaIKXH91RceA/zh-cn_image_0000002533067086.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=808D45005A00EBA2A4AC9869E96FDF3EFE2CB33C93BF44891F5A0B5D92AC2305) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Hms8eO4mQueMUVXv-ciuag/zh-cn_image_0000002563866989.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A479A1276B794AD937C188BF6D647811540FDA0F15AA37733C58DC564002F85A) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yL5NC2uDTxOEmGjFGg_ujw/zh-cn_image_0000002563787035.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=08B677EA6098C3FA38171708958023EFE7877DF18E54F071E291466D9EAD87F0) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/mJeE5CrnR6uZLX97PmdTwA/zh-cn_image_0000002532907140.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=5EACA5531610CC5362FF957721502E3E38B5E1711AC33B0DF862A44FF922D5F4) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/wN439rM2QV-PtLCa6cIQ5g/zh-cn_image_0000002533067088.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=5037B9740DAC11ACF9374F5F32187F93EE19C473D2187BFED4A7DBF33E7B3D1A) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NVicZqDASZW0d_-txGMZSQ/zh-cn_image_0000002563866991.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=AA0ED07BC143225E412800B2FA9B0D1341C02B3ECA0BC4297ECB163FC23F426B) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2qiaZoavRXG5c4opSQA30A/zh-cn_image_0000002563787037.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=C092ACC80EFC6844BD9D4203D3DF27FDB20B459DE610D9F0411323E1244052C6) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lX225aVtSu-4nvAtUyIPMA/zh-cn_image_0000002532907142.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=9DD27E5BAB8918FCB90DE172DC2533E0A90691340DEC4A044E8129420D2D59E7) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zUifEkaGQreX-P-W31DXfg/zh-cn_image_0000002533067090.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=1677A893BA39CCBA3C55BFC3508B14CC20ECC4C0CB97B57EA927EACD2B1FE2DA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/X2zABTc6Q9WbYXK2ClShLA/zh-cn_image_0000002563866993.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=6CA01DCBBE23705AC2B03F75E4B3304316B5597DA5C5BB5CC75F5C2DB1C0536B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/v_j2wR1yT7edorhG7el2Vw/zh-cn_image_0000002563787039.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=630B307DD05611540C184594695A28F17801E73C3A070F44C5F8A507D176BBB4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CW5bJd7iR6qzFrmkEfIfrA/zh-cn_image_0000002532907144.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=9C4E42E6E1E63109209E8B0FB431825058CF3662AFE77BDA7D9C1D4A2CD9C451) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nTuBuaANQki8toorvozBBQ/zh-cn_image_0000002533067092.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=67A3DFB6492B311EEE598D53C2DACBF5342CC3A17E8A32CD4D24FEF57D855DD7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uKuzD0l_SL6Ch_R9pAPaTQ/zh-cn_image_0000002563866995.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=2DA92C607E84F57AD50570A20ED0037B0A23456A7A7DAFAE5C7D934559E07290) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ttv8C5SGSPS-IuWGizRPWw/zh-cn_image_0000002563787041.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=26DFEFB677E227F26C9F66E3F1AAFF98BFA9E5B23A0BEB56B9A0697FCFDC7990) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Bwfe0_WrSW-txYWIG-f2jw/zh-cn_image_0000002532907146.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=E126BEB1A60C161F063D69ED80CD6CC9C1E0EEEB918720EEA5F40744C4F4BCF2) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ouyNukCiSX-HNT4CfdBqOw/zh-cn_image_0000002533067094.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=299DDFB4B53D2465906ECE0864783292596DA0884FC538C3464C81C861E4D730) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RqKmqxDmThCm1uxvggu7lw/zh-cn_image_0000002563866997.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=8FE45B33D5E85455C70C68AD6AA72877238423B8966FFD37BC498AF46ADF6BEA) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/N39nkasrR8i7MPz22lHw2Q/zh-cn_image_0000002563787043.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A64B4CE021B1D37E836887AE618C994FCCC3DE9F671A0BB2FD2298A946D07737) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ro5Zmt6wTPuJEncra2YSQA/zh-cn_image_0000002532907148.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=70801E9F236E861466891FBBB7133CCA97D48BF4981C0A1C8A103E37028EDCC8) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9Z2fbEgITBqHpUI39CeITA/zh-cn_image_0000002533067096.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=FA14DE04FE8EF3DF82D2EF28B718C6EB86EDFA2B8852AACFA7CBD0A728658616) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4pfSQmlaS1afzIsOsjJLdw/zh-cn_image_0000002563866999.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=BFC43476A2F407242C0DC4D32E3EB70B95D3BBA342D45AADAC171EC881F7C303) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/omfYG4BKQY6lpCn4NQasBw/zh-cn_image_0000002563787045.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=94F1D7A023B65BC604981254360ACB03B094BCD66BC25993FB959EA69AB8004B) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/gV3e13IRQe6p1gSYI9I-qA/zh-cn_image_0000002532907150.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=427031321B3D177EE32F1A6B58E36B0BB30B4BB67397BA4BCB1869B87FBD5B6A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JNt6zIKuTISfGgn1gTqkEA/zh-cn_image_0000002533067098.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=7AFEACBB9BDBD41C76F806143D1841F2214BD412E38F9D37D9949426915AD8BE) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/dMRrxWJWTKmTnypU4ZcXFA/zh-cn_image_0000002563867001.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=B021EB374AC1C29CA0AF4068DE00BB7C7F7F7B28C8B0559651AE00F089DE39B6) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dcke9U_wRzubGXXNCwDiKg/zh-cn_image_0000002563787047.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=6998A70572C9D513986F657027BB328FB89E7B842A89B1EC6792A200931166F3) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VpATvnXHR-yZtURdPUGjzg/zh-cn_image_0000002532907152.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=985E8B21AECEA5904966D1406FE1F78C60AAB3D3D0E3F76C5CBFD499AC6095C8) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sUAUQwuHQBmFB12_RQbsNg/zh-cn_image_0000002533067100.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=110B3D9C424B558C9EC8CEC87358A013967CF404D2115CF866D1E363B2964722) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Fu5Q5cI3RpOTLqBSnXFGxQ/zh-cn_image_0000002563867003.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=278766E8B41E7A37BA0B3755F31F069FAD529A471D48A05EE944F18BBFAA199F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mliCiAXgQe21RNpF4VPrXw/zh-cn_image_0000002563787049.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=F895929EBBCCF9F50E50223AD064BBBCA9A6ADF2F52CBBDAAB697350FB98C500) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dftpkyeWRQeHjaSSjF10Ug/zh-cn_image_0000002532907154.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=24ECDAB768E40F4BD505F4702C3080A445384F2846E3327896CB43805AE0D259) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f-fmtmNOQz-aNrID8OYASQ/zh-cn_image_0000002533067102.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=871F3BD76FE26834DD8351F37539531D053A6E30C25DF76A99F256CD89917F27) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jedp2XI_S3yqHhUqiDrKpQ/zh-cn_image_0000002563867005.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=569C3B74CF75F847F321B6C3070DDEE42A6A0E70DB638B99AC13AA12949E1EE3) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fYpE5uHFQHyXRC44X70FLQ/zh-cn_image_0000002563787051.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=213079CCDB81A707AC6EC2705E8ABD6CF8FBAD2DB607FE59CACD397C98657AEC) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Pi_wzNGGT9uQbpbqeL07yg/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=DEA705A6D00292EC17658CA9E02A3923CF8CEE05826E67453F00021580A46045) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/UaCiXAmnTcSXNUVDXPtYUQ/zh-cn_image_0000002533067104.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=FD72BCD18BBA7120D341FBCAAF5B5B37C6F1C51742EF06B78C7A7082E48D3AF6) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uymCv_ZNT9WysHsQ_RnCvQ/zh-cn_image_0000002563867007.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=2483667E4D1D0C0AE639E18B74C943C97082BAED89A030DB0F4224694D21458F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/I5yqOxWQQfi3dRP7aP6cyQ/zh-cn_image_0000002563787053.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=C462779CC9ACC9A3D2976FEDCE6B645FC9F5C97A93F251072D592B5781CB2E59) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PrEX7Ts1TdGeZCoLBJwc3g/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=5F280F0DB4CEB407A45826EBAD734024111A1DB07D4779A04BA9A5545F5EDF09) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4z_Mrnn_SRO1h7BwYgt6sg/zh-cn_image_0000002532907158.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=6CC2584BCD57BEE9E1C6ADA3D4F4ECCED2AB19C9B0AEF99F3CA660354EA9FBEE) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jjjGtwhpSIqe6jgDZ5LWUA/zh-cn_image_0000002533067106.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=BAF4791E5CC22C00B73FB1E7FAF1CEE31AD8C311D4435D803065A028734A5DAF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/N60h60w6THCGOJhD2t5_DA/zh-cn_image_0000002563867009.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=C727DF652AC2FDD74E87E1D193361198A6FBD20A6B17D4CE89F62A981C792BE2) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3Cba8q3XR7CjclUz19o7zA/zh-cn_image_0000002563787055.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=BB3C0CBD6EB44F58D1BC5C93995C4724155861EDED59A238B48567DF3724D8B9) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ORJiok74Rz2CSoBesZ3uBQ/zh-cn_image_0000002532907160.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=F0E5037226322D8817B2D35451D48503A1DE34535B8B8E45F813C47237D54B9C) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kS8QxgOYTS-d5cNmYusvwA/zh-cn_image_0000002533067108.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=27F5DFBDC97FA15B73A3D902B1031D5F7B61E3758063285F9FC1E1E8F78BD9CA) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FqhrYgCYSRyWv_GyzHVaWQ/zh-cn_image_0000002563867011.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=25B62544EF30323CBE90C3EEB4DDCD2962BD25DBD0433698F13F2CA1FE0B9805) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IHFglV6YSfagtD4oJXB03g/zh-cn_image_0000002563787057.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=A2C4680EBB0169C507CA88DEAFAAD1693C3E4E5E56E8FD881F3C55CCB6E6369B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U5wSt5bZQ5CFuFWTImRpUA/zh-cn_image_0000002532907162.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=12C166571A4B0F134E4FC57B123280DB8248DB5A1521A7C03DAA9F799FD241D6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Fgodj5KhTB6bW_8curtGFA/zh-cn_image_0000002533067110.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=721757F8FAB266CC7A04548B4599C98A2CCE18B79E242EB8F6055D96F1833DFA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXQVKOJ4R0e0mhNBj2heYg/zh-cn_image_0000002563867013.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=350EFC1B60653A7A410C503C5322154E10F1A42EB48DDA21EA428DE83DAC6B62) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/e841zjgoT7i1NajW3G0Fgw/zh-cn_image_0000002563787059.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=770F530E89BE56F9172F4DEC1CF2C40FFBACA9A119676F709D5D88858682BC13) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Scfu2NgeSoWMXu9Z7kHE3w/zh-cn_image_0000002532907164.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=161564B62124A6B95B12C19BBB028C198E2E5274737BCCA09EFE6D8EDA44BCB5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tx71_cdJSPG4PgutSa3eew/zh-cn_image_0000002533067112.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=593F2D3D8FAE9081147A7CF394293B8D7211618556D25AECB64C58FD61851914) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aKaVzFqiRhmWYYXcd6iCyQ/zh-cn_image_0000002563867015.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=E5C4C8AD3E00649BD7B82DD51BD00CD4639D72E7A7AA02952F6FA284C1F19776) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UXmCbSgoRI2edZvC1oZOfg/zh-cn_image_0000002563787061.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=190054867E802E28D404FCD7C13A4496D848E2B5B58FE815828BE0CF754350C9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bfHS5QrdToOl2uLPzaZpTQ/zh-cn_image_0000002532907166.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=CA524F75B5899885FF58B631ACD8513D16DBB216D650193C9290B4F65F448C74) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dY1ZmU5rQeOtPK1XrKkoxg/zh-cn_image_0000002533067114.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=6BECE572439BEAA1A97DF84F4D594FE5E7D83B8233051084271B4EC66DC50FF4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6KYcMF5aQOC30E3sUOyQEw/zh-cn_image_0000002563867017.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=888324CA01586ACF8248FF4790A8094B9A812CA8A6909328168ACA84EA7FAF48) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/CsUqL_vKQBGwWRIu10UISQ/zh-cn_image_0000002563787063.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=8930660A62F1877874AC2A73EFA7AB8CD8A8FCD81EA20B89496C6888F1F6030A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HamQBKSPRIarddT88Qafuw/zh-cn_image_0000002532907168.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=9C33A2E3B0977A9E86C66EEF3C1C21A56A91D4FF2893AADB2D5CF8FF8D7C2C06) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/hdkBe5lXTu-Oj9dYP7-SRw/zh-cn_image_0000002533067116.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=E96A86B2FE0C976155BDCB1AC736275E550B3E8530C5E3F1D8D57A864A9D61FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bPcpQD2IQsq9Tb8wMCKipA/zh-cn_image_0000002563867019.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=E2E51BB1F59C1D92E075641184C8815470B218BA4807C257061B864B3F4370DA) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Lsf_5lwtTyW69H7ANU6wvQ/zh-cn_image_0000002563787065.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=6CA89AD176143F91CB0D9E4CA7D8DF5FBD28448330BF8CA9DFE0B19131295B57) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nkN2EaSbR72_Jj4tqjogkA/zh-cn_image_0000002532907170.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=9920B60C484C282485F469B74C843DEB780E0A27A0DF8FE64C3517883622AB72) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/z3ypE5fBQyOSkEweS_ESug/zh-cn_image_0000002533067118.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=B41AEFEE185C2021C5F14FE62B8FBBE057A4F46D8A90E778682727AA32542517) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2w_tvBaYS2uY4WHELvG1-w/zh-cn_image_0000002563867021.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=1867ECED559AF3830ADDBF4D0D960B3CC992EB56D668ACB0502DF80B51D71835) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0oCV6JisTKiAQtZy7QPaoA/zh-cn_image_0000002563787067.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=C56325E4F9A0C06DFBF574ACAF4BD89E7895ED7642B2C4A1BCAF732217AAF945) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r4sK6GP1SvacWeoZSTjxNw/zh-cn_image_0000002532907172.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=42112A8BBE882AD068BDEF5E982E1CF17ECA9A441A64AB606E067EC030322E17) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zOfrPPrMQr2cYRYV2518Og/zh-cn_image_0000002533067120.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=41123AE01807D4586F8CAE3EA9515413DB4D2B18D05282EA80DB40AB8C9AD29C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFYmzGd2Q6WC9ZfzA0GN_w/zh-cn_image_0000002563867023.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=2B310116C61B3C837662F32A8C31CEADB112755ACB7EFE3014F547791ED3E0EC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sAwW5N2xQqqwlEARGHdNiQ/zh-cn_image_0000002563787069.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=9EF13CCA84D05CF77518C0534BE050B1FC7DAA7540ADA462505AD31EF2A629BA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/S86IasA6SlqhjKkGYNmWBw/zh-cn_image_0000002532907174.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=FA7491CC4CAEE5C9E60A36B69360B3999313ACD07B9E8967A886E55A7D7FAC0A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3UXtbFQ0RPanjHbDJHMT_A/zh-cn_image_0000002533067122.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=D5D3B715B5298BA8BEDC8E73B888C617B511C91D73D0AC901DB1C2316F402B60) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Cr4UTxyTLCzjfln5MYI-A/zh-cn_image_0000002563867025.png?HW-CC-KV=V1&HW-CC-Date=20260328T143630Z&HW-CC-Expire=86400&HW-CC-Sign=8328937886C2B569130A0B5BC35C81DB22A8DDD73F056C1F64416C25487C9C97) |
