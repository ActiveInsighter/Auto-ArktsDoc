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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nF53NYegQ42Y4g30GI05Vg/zh-cn_image_0000002563787021.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=381E03D60105FAEBF3053D4A2C27C5D294BD8F66804A4412F650D9AE18FCF62E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uZbH8fBmQrOtIA_gy_2fYQ/zh-cn_image_0000002532907126.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=836204C7285EFEC08590C4362EF040F5B646502D1BDE83AB5AE3C8503B540A63) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/xhY0Ya1_SxSAowqitPw_sQ/zh-cn_image_0000002533067074.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=1BED2BE528D90242C0D1DCD845DE84DAC26A0FE633B6AC245BE6FD8C1D76D378) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tZtCr19sRkSQG1srqHoDig/zh-cn_image_0000002563866977.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=3D242B8EA036B3C47FD8C30168B5EE1A08E8D318A14B1FABE380BF2D728A0E94) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/DuK3jIg-QtC6F1MdD4f0tw/zh-cn_image_0000002563787023.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=3557C219E5889B3854403DDEDC3CE22E9DDC121B0DD25442E00DF28B4F34E869) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-WpqmfKGQaK8jWaI8LDoZQ/zh-cn_image_0000002532907128.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=791CB751243BA8092999733AC1A37DAC820CDAE343DEA75FBFFBA6550EB40782) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6OCiTm9CS0WTBhbKF-TKMA/zh-cn_image_0000002533067076.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=376B484D628F75F235138B98814F4A256A4E635895AC332B87AA488FE6AD7575) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/rMSbKLbwSmaZSlEbEXuWuQ/zh-cn_image_0000002563866979.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A6F753B2EB998D0BCE3140F33D6DDA859CA60AAB37C0C51FD09EFB94899F1818) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XIB5dkWNTCCxP-pB-bmDwQ/zh-cn_image_0000002563787025.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A3B530463FF3A65BAAF0A123C359B288582FA80241A2228BEA583E4809002246) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9nj1LBG2S-Gu5qTOWRcRLg/zh-cn_image_0000002532907130.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C1127C25CA2414A8DF58BB99D5A96C3D25336369FD635C5F04ED456F83DA0849) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MSpIfr27QbSy7Lu7uvbaZQ/zh-cn_image_0000002533067078.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=91B83E691128952DC2A215785D1FD6622B66F33BBA2813814DA7E3C0A6412CA9) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/NtcSKjagTCCxK0TgHwgPgg/zh-cn_image_0000002563866981.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D5087B69F3A52783EDE303CE06827528496B86B1313CF29072145A4A5ED0771B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dNVmhl_rRO-O_xIoiqVWRA/zh-cn_image_0000002563787027.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=CF1BFE2A4A11855C46DCE32F32FD301616B2FC50F25B04B2842C9DBB49A7E1E9) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/1Y9RqQNiRu26x5HcbkVe3g/zh-cn_image_0000002532907132.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D9873396069D6F50ACB17793FEA79C12B4FD24242D9CC9785B7FDE32E5D8936C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qughuPY3SnW8f3QyVKl-lw/zh-cn_image_0000002533067080.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=FF491AD3A108F770CF2275618A71F901EB0613F445304D150FA6C819FEC10690) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gZ1G0fkCTcuGYeVqDU7Aow/zh-cn_image_0000002563866983.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=1B96D40CD1BEA4F67726C0CCB864534B82CD4B3CBA24879E4B2A11837F9F1800) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vJdgSTHUSAK025u2QQ7vfA/zh-cn_image_0000002563787029.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=21EA04666E714FAA6CEF89D0A36A0D6392CEDE2B6D674A1FF49C2C68D3C4602C) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RFvQknBZTpC_tnzo6ToPOA/zh-cn_image_0000002532907134.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=4A7CD947A56E551446699613C005A8BA239FEF24ACFC27109D81EE7632AE2FF7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/f7GUxTg1RTyrSmD_xXVblQ/zh-cn_image_0000002533067082.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D2BF26B409B808B4E22FC38B8D764B528DF08B6566415BEFE7978D287DDDDA05) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/r5Hhze9fTj6ZjOnIOI7RYA/zh-cn_image_0000002563866985.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=F5AA3CA65C61E7C51BB057DC81B3E57ABBA165F0EA09BF3C0BAFB4C8361C59E1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8YqIAj-zSxKMv_VhT8xpJA/zh-cn_image_0000002563787031.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=8F1A81DEE7DEB2FCFB8283D0161F9E442280F5732BE0324F2343EEB6DF61BBF5) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VeuKSoDFSViKGMX5ghvdyA/zh-cn_image_0000002532907136.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A2D4C3F2FD5485A8B67BB188B9D67FA4F4B924975481AC83E2E7799FB064564F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VOubMPnZR7WclUYSbF4g0Q/zh-cn_image_0000002533067084.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=5B28F9EC858B52545026D5F866E71281FC284ED9822C0444BA9FAD0106092B8C) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/suk6tetJQ-eTb_wP65OFnA/zh-cn_image_0000002563866987.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D43F2B53061F34B806143190ED04B8EFF5B0213BA6FE3826352F31673852FE51) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VQTPtYMITZ67W1rOi7YFEA/zh-cn_image_0000002563787033.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=E93A60DAA75E74516B9B683EDA51C0B02C36CBD68E97710C9262AF7F03504A59) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ShI4i9bWQa6zEWWnzc-fFw/zh-cn_image_0000002532907138.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=EC9E2933C4CD75581AB0D5F2114C324A2197DC6F35A9E944499525271FB7AFEC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Vxw4b7XDRnaaIKXH91RceA/zh-cn_image_0000002533067086.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=48CB39A0ADD2993674EA43B2EC458FA9AD1EA9D963EFB26C0273D99CC0919277) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Hms8eO4mQueMUVXv-ciuag/zh-cn_image_0000002563866989.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C68D7BB5C32E37DF7229FDFE17F77ED1BF443C694775FA6CEDDE4D2090AB23E2) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yL5NC2uDTxOEmGjFGg_ujw/zh-cn_image_0000002563787035.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=EA8160B305B2DBB0281F1927D239D62A749ED22F3933215506811E5F999D0268) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/mJeE5CrnR6uZLX97PmdTwA/zh-cn_image_0000002532907140.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=B740E15567938EF588FB8E4199C21043B770A21EDFD14322EF8B633CD84A9FB5) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/wN439rM2QV-PtLCa6cIQ5g/zh-cn_image_0000002533067088.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=5C17DD09214E53E40CEC0AE963083C39CF17ADDDE9627D0F6F6E1CFD20134B8B) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NVicZqDASZW0d_-txGMZSQ/zh-cn_image_0000002563866991.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=FDE9FA315A6E8F82C50A9C368CE85EA4EF0C8AC438306109616539BB892D0A57) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2qiaZoavRXG5c4opSQA30A/zh-cn_image_0000002563787037.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D034E4C9BE8E62034592541A0F7350F6CCB05FD3CED232CE20D778DBCCCC4D73) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lX225aVtSu-4nvAtUyIPMA/zh-cn_image_0000002532907142.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=8744693D2D744B9BEBFB835E388C4FA69C96E0DBFDF49899417FF5B69C884252) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zUifEkaGQreX-P-W31DXfg/zh-cn_image_0000002533067090.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=E29D2F052F158D32602D748A89D7BFA7769B093BD694DBD0E07317D5DD5011EC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/X2zABTc6Q9WbYXK2ClShLA/zh-cn_image_0000002563866993.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=7827DA5F98E2F507EB4C0C61326B0EE26B4D418EFBB06AE7FECD84E627885308) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/v_j2wR1yT7edorhG7el2Vw/zh-cn_image_0000002563787039.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=2C1E23C7E4272894E85254EEEDE58D8507ACBDF438FA80B329649BBF45F425A8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CW5bJd7iR6qzFrmkEfIfrA/zh-cn_image_0000002532907144.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=BBE68B9DA72D83654C5B3EEBD5A87033B6E6C39577F54857828BF065A344455A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nTuBuaANQki8toorvozBBQ/zh-cn_image_0000002533067092.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C19031AC8C6D57CAA43449C94CF77DDA7A94AF5F585EAE6DAB70AF21A2D53D19) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uKuzD0l_SL6Ch_R9pAPaTQ/zh-cn_image_0000002563866995.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=9341BFA897EC0217EF841275EB8D2FBD12372D10F4BBFB4671F94219CF84CDA7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ttv8C5SGSPS-IuWGizRPWw/zh-cn_image_0000002563787041.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D968DB0043F8E0F3966AC288A98EE5EF311496599C8C66884AB0B74B0F864D21) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Bwfe0_WrSW-txYWIG-f2jw/zh-cn_image_0000002532907146.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C95949836F8B776D8ECB7B4C982FC1C2E0FCC05212032AFA747FC52964B198D9) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ouyNukCiSX-HNT4CfdBqOw/zh-cn_image_0000002533067094.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=589FF360C44843B4AF5C7CE9481E6AEF17B33A61DD8D549BFBBE601696B03AA7) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RqKmqxDmThCm1uxvggu7lw/zh-cn_image_0000002563866997.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=F81A51C54B20B64152540B6BCBF780B803AB72CF7594E817EB00CC7A956E3281) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/N39nkasrR8i7MPz22lHw2Q/zh-cn_image_0000002563787043.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=70A90AA33C91757ACDBA00D2CB02001BF9AA0644CF227AA170DE1882D2BF292C) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ro5Zmt6wTPuJEncra2YSQA/zh-cn_image_0000002532907148.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A5E611F9F8FB43E5690B1FD56E2B202CD19056061A849F33423C38F00E86004C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9Z2fbEgITBqHpUI39CeITA/zh-cn_image_0000002533067096.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=745F2B8C758DEC455C94C190335837A8E489AE2588F998597189F95472326CF8) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4pfSQmlaS1afzIsOsjJLdw/zh-cn_image_0000002563866999.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=9D3D6AF574EF2C9C91DA6F03A032A20941C9E48BC0EC71628FC01B7120FC3FCD) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/omfYG4BKQY6lpCn4NQasBw/zh-cn_image_0000002563787045.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=90B668FCD87D3AED9C0F4232B268F7C6934029BD06D1BD2641AE436012B1ADA3) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/gV3e13IRQe6p1gSYI9I-qA/zh-cn_image_0000002532907150.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=1A73B1982EF0E29131BA037D91FA894FB47FB2BF4E4CA7BD25E490BA6E125408) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JNt6zIKuTISfGgn1gTqkEA/zh-cn_image_0000002533067098.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=1DE1CA164CD9A0484522D846529D29AD0C3C0083C118D513C336DA525226E42A) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/dMRrxWJWTKmTnypU4ZcXFA/zh-cn_image_0000002563867001.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=803C51DA8F69A98760219F0E87008ABA5DDC962525978BDFDE04B016814928AF) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dcke9U_wRzubGXXNCwDiKg/zh-cn_image_0000002563787047.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=5380FF4322DAC9ADB02422F628BD9AA6F4254022E502E1B02E212EF44E61823E) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VpATvnXHR-yZtURdPUGjzg/zh-cn_image_0000002532907152.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=49F0AD06DBB5FAE44747D6D332FB325624CAE5FD4FB24AA3822D78CE128DE6C3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sUAUQwuHQBmFB12_RQbsNg/zh-cn_image_0000002533067100.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=3A5E27E20967F842D688C0C8A99EFD21049D58F407A2E48F041715BC73AF6A53) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Fu5Q5cI3RpOTLqBSnXFGxQ/zh-cn_image_0000002563867003.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=100FC54384238105366C58F3FB0E84190B523FD2D331AB609A4A714485F33B78) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mliCiAXgQe21RNpF4VPrXw/zh-cn_image_0000002563787049.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=035E77098EC02753175569C3E19FCB0F078B2EE0136C08545EFF78420CBF21A9) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dftpkyeWRQeHjaSSjF10Ug/zh-cn_image_0000002532907154.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=4679CA8868FB71377D6E54CA011956B3394B04E8D29FFDEFFF8540ECBD8EB3FA) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f-fmtmNOQz-aNrID8OYASQ/zh-cn_image_0000002533067102.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=ADA8518A5BD2FE8BB4B33DFEB6381EBB6A2962D83B7D0C3611B50BFC1F0AE1DA) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jedp2XI_S3yqHhUqiDrKpQ/zh-cn_image_0000002563867005.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=0A9FA1A2C79F9224EA3666D80B646CE32C27FEFB141E7194CE8D7AB804B4D4F7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fYpE5uHFQHyXRC44X70FLQ/zh-cn_image_0000002563787051.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=E062A7FA7F8321498495C9FA2936AE00F29C898E33494D54AB7EFB9ED7EF2F59) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Pi_wzNGGT9uQbpbqeL07yg/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=ED3EE421D7869FD613859DE497FA381889AFE7663603B5BF7768CD8A385D5615) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/UaCiXAmnTcSXNUVDXPtYUQ/zh-cn_image_0000002533067104.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=0BBDFA3B6CD7B2BA559C35D8A7D146638FF8FD1C6EB7E0B4363765FF4CCF2855) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uymCv_ZNT9WysHsQ_RnCvQ/zh-cn_image_0000002563867007.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=81FB7336E9BFEE2EB17618036DDC6472971C4E9925F1FD828F23B4EA830EED50) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/I5yqOxWQQfi3dRP7aP6cyQ/zh-cn_image_0000002563787053.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C1EBBAE52ED6FF64DC2703AF74CD4B1E30FBF30CD22ECA7CEEFE5042A70F8EBD) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PrEX7Ts1TdGeZCoLBJwc3g/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=46A86CB658307B8A838EB2F6E95E5F3D8811363D062E893F7028048E23ABF24C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4z_Mrnn_SRO1h7BwYgt6sg/zh-cn_image_0000002532907158.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=EE1A1D12676CEE67987793C2C5E8ACB0CF93097AAECB669F54F827B285B5CDF4) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jjjGtwhpSIqe6jgDZ5LWUA/zh-cn_image_0000002533067106.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=C2598EE862C6459732C472AF429E3601625C47303204B9FBA5D5B7F38C513BD4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/N60h60w6THCGOJhD2t5_DA/zh-cn_image_0000002563867009.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A34F98F3EC09A8ED5361CFD5AC38CCA0F5A03BE11FBC9D57128CAB5CE458C370) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3Cba8q3XR7CjclUz19o7zA/zh-cn_image_0000002563787055.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=87008BB1AA5D1E9707A48C50CCD12DE8FCFF8123397C9D8F15686EFE43EAD64F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ORJiok74Rz2CSoBesZ3uBQ/zh-cn_image_0000002532907160.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=DB2883518CD03795CB03B33D3BFB615D49D303A4A4B742C83E1489275D6A7872) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kS8QxgOYTS-d5cNmYusvwA/zh-cn_image_0000002533067108.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=E1241EEE4A099B3BDFE94E154FF62C4BF46F813D0216B342851E079F9B5DBBEC) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FqhrYgCYSRyWv_GyzHVaWQ/zh-cn_image_0000002563867011.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=501A626AF38B1DDFFC58BDF7180C536E5809ED3AF2C7414A522313A872AC8D99) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IHFglV6YSfagtD4oJXB03g/zh-cn_image_0000002563787057.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=01C2DD777EEF8DE6ACCE03428F508F8186ECD2E4006DAC21FD1592752B568ADD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U5wSt5bZQ5CFuFWTImRpUA/zh-cn_image_0000002532907162.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=FAF8FFF5C5CBD6B40CAC7DE344186839D85AC2AB9477CF3E980958184459F768) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Fgodj5KhTB6bW_8curtGFA/zh-cn_image_0000002533067110.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=2AEDE7BFCA5D5A19006ECFFEC9C39242C5CF7A55DAAF8A76367C84052505824A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXQVKOJ4R0e0mhNBj2heYg/zh-cn_image_0000002563867013.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=2E34507C05BE15EFC64B63B58B5B60DEF0B209855E2FB953C8BCC17A1A2935DC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/e841zjgoT7i1NajW3G0Fgw/zh-cn_image_0000002563787059.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=D0EA97DD57D766AC6BDBCDD528E5869D8FBBE446CB0299167093B008D3620AD3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Scfu2NgeSoWMXu9Z7kHE3w/zh-cn_image_0000002532907164.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=7C3ED7FC886AE8C3BBD5257732C4C211922BE8AA3581987F5A77F0EA8CBE3C6D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tx71_cdJSPG4PgutSa3eew/zh-cn_image_0000002533067112.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=472FA318A8AA276F2F2632D5A9F3C8DDC8832B000B41D1FDC35274249FF6EB73) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aKaVzFqiRhmWYYXcd6iCyQ/zh-cn_image_0000002563867015.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=B82B480BE20D503E3361B6E3A0637E44AE71E06770392B419F530C2392566D8D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UXmCbSgoRI2edZvC1oZOfg/zh-cn_image_0000002563787061.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=439EED38281B82CE4AC40859F1332ED387E6BFACB91B4A3C4F85D98E8B964D30) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bfHS5QrdToOl2uLPzaZpTQ/zh-cn_image_0000002532907166.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=721625527C3AAC398CB7D46A477C56E94E63C30129653421C28E83444939E330) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dY1ZmU5rQeOtPK1XrKkoxg/zh-cn_image_0000002533067114.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=26A758FC2483B07CB212D89757BE84023554D64126C3E673734C05283EBB05BD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6KYcMF5aQOC30E3sUOyQEw/zh-cn_image_0000002563867017.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=FE6102968E59DE94B1803A536E7D219D9D80EA53F89F767AA4ABADCEE1512A5D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/CsUqL_vKQBGwWRIu10UISQ/zh-cn_image_0000002563787063.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=6E38FAA5060347EEFA04B8820D5DBC2EAA8C2E321AA51C9F11C8192A8D28D5EB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HamQBKSPRIarddT88Qafuw/zh-cn_image_0000002532907168.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=E9A67FC4A6D40E4890860170148B9EA1CB0F242B2AE25B9BE5CAA6D3CD61B23D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/hdkBe5lXTu-Oj9dYP7-SRw/zh-cn_image_0000002533067116.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=98B444A9DDBCF935F16E1A882FA5493971B41E44589CC3ADE2DA65ECD382A425) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bPcpQD2IQsq9Tb8wMCKipA/zh-cn_image_0000002563867019.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=0DCA5A82FD106D50EF802B417E5A2DEC2DC38E021B6F4F6946EFFE1DDCFB82A5) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Lsf_5lwtTyW69H7ANU6wvQ/zh-cn_image_0000002563787065.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=7D3DE7251D6CF495CF8116F462B2174B723EDB7BED2F62B5D1AFAB4920D32FBB) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nkN2EaSbR72_Jj4tqjogkA/zh-cn_image_0000002532907170.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=33B0BC79D247325BD59D465CFB7F75F69DDEE0CF7A3CBEBF9BD9B9FB1C324ACB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/z3ypE5fBQyOSkEweS_ESug/zh-cn_image_0000002533067118.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A4647B2E07CF390F5FA7C28D3FA18F4BF0FC0B72E713108C3A563AFD10D5BC22) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2w_tvBaYS2uY4WHELvG1-w/zh-cn_image_0000002563867021.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=F6F08A212729B3A8DA5BDF8CAE2313CB2CAD8F0328D009C22E7A27181E6D18A5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0oCV6JisTKiAQtZy7QPaoA/zh-cn_image_0000002563787067.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=39B8DF99FCADF966D7D804EE0F27CF119383B82114D03B0485C1CDF869180743) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r4sK6GP1SvacWeoZSTjxNw/zh-cn_image_0000002532907172.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=62D7DB7B940F3475DB628111DED79210770BC1149FE07EF4FBDBF10F0351CD99) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zOfrPPrMQr2cYRYV2518Og/zh-cn_image_0000002533067120.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=26F52CE1EE5518B4AA97366323D4D492DD9DB5046EA52C3480B73F6FEDC1E2BD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFYmzGd2Q6WC9ZfzA0GN_w/zh-cn_image_0000002563867023.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=CAE49166E05C9E2B2F89937620CEED1A316811B486FDB795CF3B8242E1C3C56F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sAwW5N2xQqqwlEARGHdNiQ/zh-cn_image_0000002563787069.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=BAE69F76EAAF6679F8D3EF3C0BB7EEA1C94699E9729E82CE625A4410391BC567) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/S86IasA6SlqhjKkGYNmWBw/zh-cn_image_0000002532907174.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=BAF0567BA885D5481C666643788FCF14159463F71C2052B76F44E59163EECF4D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3UXtbFQ0RPanjHbDJHMT_A/zh-cn_image_0000002533067122.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=57BAF1E8948B46F0A0B9763CA6D2027E20394EA6F58FDD806A9668BA41F2C916) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Cr4UTxyTLCzjfln5MYI-A/zh-cn_image_0000002563867025.png?HW-CC-KV=V1&HW-CC-Date=20260328T073036Z&HW-CC-Expire=86400&HW-CC-Sign=A2FE53D22656840AD9510CD4DF7153B16330300DF278CC0CC655349CFD706C79) |
