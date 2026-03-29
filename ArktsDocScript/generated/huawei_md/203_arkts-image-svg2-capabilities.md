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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nF53NYegQ42Y4g30GI05Vg/zh-cn_image_0000002563787021.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=BCE2A9228A6F4233B38F98AE7CD65C11F83C850305DB57F0C57C74508BBFFC1E) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uZbH8fBmQrOtIA_gy_2fYQ/zh-cn_image_0000002532907126.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5881420709DA03B69DB99301677DC22B3A9A7F4426EB8FD3BE25043A82321092) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/xhY0Ya1_SxSAowqitPw_sQ/zh-cn_image_0000002533067074.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=37C644A2FB68EF9B4AE19853ECE5BFA9121C9E81906AF21483F3BF69DAB01632) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tZtCr19sRkSQG1srqHoDig/zh-cn_image_0000002563866977.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=E21D801E3D0288569AE7F579B513FAC210B6A424177119DCDDB9ACD9B8935F3A) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/DuK3jIg-QtC6F1MdD4f0tw/zh-cn_image_0000002563787023.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=78371261A537DBEB063DB22D81F9AFB8703DACE7E999A475A5C16F569241543C) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-WpqmfKGQaK8jWaI8LDoZQ/zh-cn_image_0000002532907128.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=A512A6917150C2114899B9A6A40085FA84344F117BA230C1E586392F62DDCFD5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6OCiTm9CS0WTBhbKF-TKMA/zh-cn_image_0000002533067076.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=C57E5464AD56641DC73261A18D033047CDE92DBB8BE561A91B2EB2F40552860B) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/rMSbKLbwSmaZSlEbEXuWuQ/zh-cn_image_0000002563866979.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=349E089BAD9123EE196323E6F553127F7031241EBB2E1AEB59E5687DA6EFA7A7) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XIB5dkWNTCCxP-pB-bmDwQ/zh-cn_image_0000002563787025.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=2150E864562EE9356FF63C21DD6FB04A14407A6190CF7F0EF37EEF85C463EDE2) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9nj1LBG2S-Gu5qTOWRcRLg/zh-cn_image_0000002532907130.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=EBF582DDB89A238679E3077DAB70A5C83B1B3759953077B2437AB593ECA7B908) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MSpIfr27QbSy7Lu7uvbaZQ/zh-cn_image_0000002533067078.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=574250046659DEC7855C2CAF6E50734FA99BC297465A4EF369BC8D5BBBC1AAB0) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/NtcSKjagTCCxK0TgHwgPgg/zh-cn_image_0000002563866981.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=736061919663A952C8613966726B26BC465743D4C05DFABAEB70055A2590A035) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dNVmhl_rRO-O_xIoiqVWRA/zh-cn_image_0000002563787027.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=C2973FCA7D5D6FCF5C5E82B660BFCD1C87096273E645495A148B6D5A9F6B5E96) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/1Y9RqQNiRu26x5HcbkVe3g/zh-cn_image_0000002532907132.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=C485B38676B25B59E470373595655B51546827229654A373A4B7925031436B75) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qughuPY3SnW8f3QyVKl-lw/zh-cn_image_0000002533067080.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=B82349D2030A4A3B5AE5095B579F9A921EE24244BF1F6F04707F8A68B7CEF869) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gZ1G0fkCTcuGYeVqDU7Aow/zh-cn_image_0000002563866983.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=D100805C7D71FBD8663890654677A21DB1AF32C2A9BD424A9EA8DB616C959D7D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vJdgSTHUSAK025u2QQ7vfA/zh-cn_image_0000002563787029.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=B5AD00F8B6E88517F9B4173A4F242B23F53BD34A99FB5DF8E37882AA2153A8A7) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RFvQknBZTpC_tnzo6ToPOA/zh-cn_image_0000002532907134.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5A03FB3E4030B4418829845AF78EB245328F1845472376806FDAFC4D543E0782) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/f7GUxTg1RTyrSmD_xXVblQ/zh-cn_image_0000002533067082.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=408985101BD633EA59A18A29A3A69762D843CD356C612F86FB454E363C66C925) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/r5Hhze9fTj6ZjOnIOI7RYA/zh-cn_image_0000002563866985.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5C5003C5A90A3FA8039212426F8BE11B9BC76AAAB774087242226CB999012E8B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8YqIAj-zSxKMv_VhT8xpJA/zh-cn_image_0000002563787031.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=75458B0D778E4B0E87E20E7AB9B4F603AA91AEF6C461300C3BCEA02671D0F79D) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VeuKSoDFSViKGMX5ghvdyA/zh-cn_image_0000002532907136.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=1513B4B512D9CFFD147AF4FCD7980E6C03129359C24F0DBC54646B77B492972E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VOubMPnZR7WclUYSbF4g0Q/zh-cn_image_0000002533067084.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=F2D95018C832A485D2257AB6488544A66AA55DF1D8EFB213EB0AC39E4ABCA661) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/suk6tetJQ-eTb_wP65OFnA/zh-cn_image_0000002563866987.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=30ACE1E469E726CCE54F3FBCE661F865562F46A4BAB5E49E5261F586130A3275) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VQTPtYMITZ67W1rOi7YFEA/zh-cn_image_0000002563787033.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=89E7EDB946DD3AE4922CC6F8A9DFEEF1259A76DF85EAC4E7146D6B57FD700F17) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ShI4i9bWQa6zEWWnzc-fFw/zh-cn_image_0000002532907138.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=EA3AB087DEF6766590F3169BCCBBA02120C9DE4E338CD0C1145DF8CD5E8DE69A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Vxw4b7XDRnaaIKXH91RceA/zh-cn_image_0000002533067086.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=F72234E4C2AFBD58285D44744F9FC7C29630F1C483AA51FE0F9C114AACFD82F2) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Hms8eO4mQueMUVXv-ciuag/zh-cn_image_0000002563866989.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=303029F0E413A6CE5F319D7ADD92CADCEA740BC7AAC857B1B26419506C3A882C) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yL5NC2uDTxOEmGjFGg_ujw/zh-cn_image_0000002563787035.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=504C4D99300EBD920E7EA0CFC8A13D13D41D8948F8507CE012C55A3425EAB64C) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/mJeE5CrnR6uZLX97PmdTwA/zh-cn_image_0000002532907140.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=BE7977A10923BE854E5CECA3B14437C71E1BA00C5BBFBB268E32D953A1929B06) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/wN439rM2QV-PtLCa6cIQ5g/zh-cn_image_0000002533067088.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=35B9650E47A645A33F852B5739CEC060716EAB5DB5288DF3564C3BFF5F3619F3) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NVicZqDASZW0d_-txGMZSQ/zh-cn_image_0000002563866991.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=3C5D368FEC65A35FCF6C268E8275C1072A2F0417179861935C55DDEA65B98872) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2qiaZoavRXG5c4opSQA30A/zh-cn_image_0000002563787037.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5E7A27B9CF65B6B25BCC1FF272672F5BC0DC8455AB078B827343908CF787395E) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lX225aVtSu-4nvAtUyIPMA/zh-cn_image_0000002532907142.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=E781CEF1DF58F62016694EDD682207A742B5370B32668DA7694CE098E6AE7E2D) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zUifEkaGQreX-P-W31DXfg/zh-cn_image_0000002533067090.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=372D23C261C8C25007CDA5B94E347F5DF013FE9E47262F6DCEF69E0BF372F54E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/X2zABTc6Q9WbYXK2ClShLA/zh-cn_image_0000002563866993.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=8B72D707F44EB5A26A45016C1BF4ABE5ADAD326E96D749AB027002F7F98575BD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/v_j2wR1yT7edorhG7el2Vw/zh-cn_image_0000002563787039.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=8227A566428B2ECF22FB75FB769F2B8D87F23EBDF01FDF011F5024C9BF88013E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CW5bJd7iR6qzFrmkEfIfrA/zh-cn_image_0000002532907144.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5AD769B4C73A8D3C06C195B1B17038434FE64BCB66A71D39C9F3E795B9651958) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nTuBuaANQki8toorvozBBQ/zh-cn_image_0000002533067092.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=F828DE36CC79560C28D525576C40F3CCE56E66C6B944338D39960D2408C0FF2C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uKuzD0l_SL6Ch_R9pAPaTQ/zh-cn_image_0000002563866995.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=F5A5708FD5FD25AA518BF5CC4FA03AB00A42B08EBAD75A8F8C499F1497B26553) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ttv8C5SGSPS-IuWGizRPWw/zh-cn_image_0000002563787041.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=3E20D618E9FB6C4E08B519EB7C65F1EBDB48537F0E865FED7A6850DCD77D2F1B) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Bwfe0_WrSW-txYWIG-f2jw/zh-cn_image_0000002532907146.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=D3657005A37CE6C00C1707DEC2C7D309026F4612164B189FD8A11C3B4CF2E043) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ouyNukCiSX-HNT4CfdBqOw/zh-cn_image_0000002533067094.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=16BD2D22E4CA262B85E2F8845C4ABC3F64C064F09B4C5313E07EDFF9D2DD5399) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RqKmqxDmThCm1uxvggu7lw/zh-cn_image_0000002563866997.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=73BF4817176CB04974311F844F187E2BF8AEF8446B0091FC966EDA9641942753) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/N39nkasrR8i7MPz22lHw2Q/zh-cn_image_0000002563787043.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=ACAF34BB9BA4E615838D9AB6025F4C0FB8456F117E39C34D94AC82D9FE3B10D4) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ro5Zmt6wTPuJEncra2YSQA/zh-cn_image_0000002532907148.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=4B802FE17CC1C0C83128870BC08BC88F973ACF7708AD2A1D6FC2A3EE6E30A7A8) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9Z2fbEgITBqHpUI39CeITA/zh-cn_image_0000002533067096.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=3F5BBB42FB53503331CA060C338F35F8181E95BAC12470D4C41FDBD35A080E38) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4pfSQmlaS1afzIsOsjJLdw/zh-cn_image_0000002563866999.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=CA8C5588B7C80A98F2F92FA6AB1AA5FE2C0C6BF65D3499200EF5E39E148CCD0C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/omfYG4BKQY6lpCn4NQasBw/zh-cn_image_0000002563787045.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=D4B78EE0B8EF985F4C905B05BA589BFB4AD182BEBA2E0A653191EBE750FAF386) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/gV3e13IRQe6p1gSYI9I-qA/zh-cn_image_0000002532907150.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=7660EED0698FEF191DF616A759BA3D544AAD292B7CF4C65F59529A4F33B0D406) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JNt6zIKuTISfGgn1gTqkEA/zh-cn_image_0000002533067098.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=776A80B65FF46CB40621A306F2010E4EEE8E23B1141F6FD7E5E3622D9CA56228) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/dMRrxWJWTKmTnypU4ZcXFA/zh-cn_image_0000002563867001.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=FCA00B2DFBB6839B6F975C6591A522FC6D1825E4CBCC266292B3BEF7B08C0D08) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dcke9U_wRzubGXXNCwDiKg/zh-cn_image_0000002563787047.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=AC4462C98AA67F1B14C90FFAEA0AD0A50CA42A84971A45363FF445928FA1BDF0) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VpATvnXHR-yZtURdPUGjzg/zh-cn_image_0000002532907152.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5CA8AC86F24BE4DA5B62941BD0F456825F00879F99CA85BBCB41CEF6751C75F9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sUAUQwuHQBmFB12_RQbsNg/zh-cn_image_0000002533067100.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=E4612487AB33D6474B2854D72AE79B882913B1EE398A2A45AF0A012CB8E7CB4F) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Fu5Q5cI3RpOTLqBSnXFGxQ/zh-cn_image_0000002563867003.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=242D6E9CC47A5D1D94E7B637B6C1612183505ABCF90706FB505B04BC7B40965B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mliCiAXgQe21RNpF4VPrXw/zh-cn_image_0000002563787049.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=EA784F3B982C4B32DD7BDF2EC07C47C695FD61885E45485CFC927095E74D3BC4) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dftpkyeWRQeHjaSSjF10Ug/zh-cn_image_0000002532907154.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=4D56414CA0ED4545CD66E67879F633F034BCD80B103DA6B32E5F91F8A4E334A2) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f-fmtmNOQz-aNrID8OYASQ/zh-cn_image_0000002533067102.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=123963176C393A9EB3572B70701C444DFDF41D71B5B515E04E6BD66B57BC1D5B) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jedp2XI_S3yqHhUqiDrKpQ/zh-cn_image_0000002563867005.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=1B4681D34F983F6F6146C361E29D198438F3352F949A2807EF50B2399C4D9D17) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fYpE5uHFQHyXRC44X70FLQ/zh-cn_image_0000002563787051.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=B1842318387E67E54B58C1F3DB1033AA24A35FE2CCB38B646DAE1531761B4C66) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Pi_wzNGGT9uQbpbqeL07yg/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=6A5BAF6E5E24E129E2EE205812FE578772BAD29AD02C6416816E70779B66F70D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/UaCiXAmnTcSXNUVDXPtYUQ/zh-cn_image_0000002533067104.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=EF518B0EACC976D94022C58BFC1DE4A2D61CEEDCEE6DC25BFE3C2B3058415CDF) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uymCv_ZNT9WysHsQ_RnCvQ/zh-cn_image_0000002563867007.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=623459B7112E6D6962F8514CC75D6B7CC9EC4BAAB35C57AA4A7BA27C5A7B38C4) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/I5yqOxWQQfi3dRP7aP6cyQ/zh-cn_image_0000002563787053.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=ACFA7187D164FECE33DE5D21769FE2A0574C6DDA7BB6151DFCD2BECD680752A1) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PrEX7Ts1TdGeZCoLBJwc3g/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=FB686BB49C621171BC54130D7ADE9D18FD6047DEAF403E792E86A3E320856974) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4z_Mrnn_SRO1h7BwYgt6sg/zh-cn_image_0000002532907158.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=344643EB6E3CDE9791C11A8D2BEF8CCADD4B331132B99E38195E1834DBFE9235) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jjjGtwhpSIqe6jgDZ5LWUA/zh-cn_image_0000002533067106.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=70C703E649C354F6CCCF0560B653D4FA5316F02C043512964AC1B2349F14215C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/N60h60w6THCGOJhD2t5_DA/zh-cn_image_0000002563867009.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=E9C116E73A80D009091A577BA755D97D3303CCBF0BA93F6F82812A7F28F78CB1) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3Cba8q3XR7CjclUz19o7zA/zh-cn_image_0000002563787055.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=D9CF16A25CA4E1E41D74ED71CBC8CB61A2077BF0D8FC18B0B52F354778FC3487) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ORJiok74Rz2CSoBesZ3uBQ/zh-cn_image_0000002532907160.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=A6DA32571991CBD538AEC07545994D22EFACDD3554E064AB1AD7A5B92287E04C) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kS8QxgOYTS-d5cNmYusvwA/zh-cn_image_0000002533067108.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=7968A30210D3F1095526653DB8572AE111FD28358DE8835BA7978E059502D8C3) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FqhrYgCYSRyWv_GyzHVaWQ/zh-cn_image_0000002563867011.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=00AFDCFACBE4FB3C195397CD9EDED2A8E6C245365F9ACFF8711222BF9EA59DA1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IHFglV6YSfagtD4oJXB03g/zh-cn_image_0000002563787057.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=39109EE6F852AFF231B1AF05874F5C6EC28B9D6053F7E4814032AC56EDB8DA2D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U5wSt5bZQ5CFuFWTImRpUA/zh-cn_image_0000002532907162.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=129936686E83AFEA68BC9417DA334F3A52DE8CAF292EA4FCBB6ACF1391D8A3A5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Fgodj5KhTB6bW_8curtGFA/zh-cn_image_0000002533067110.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=65E7A37C4597827055C1788CC0ECC61C0BFAD4539E82704A72CE273AA3D3607B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXQVKOJ4R0e0mhNBj2heYg/zh-cn_image_0000002563867013.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=3CF98EE2F8672F44CD78BE0C0A26123CC918188A7BB6CADFA585670DF759B8E8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/e841zjgoT7i1NajW3G0Fgw/zh-cn_image_0000002563787059.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=C9750939024AF5E5FB4C7FD11AE4BB720FBFFEBDDD073216104E1C5B87118715) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Scfu2NgeSoWMXu9Z7kHE3w/zh-cn_image_0000002532907164.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=10DA3BCB227851AD19BC82AD6FB3F5435E054F7CC4E4FD0B0F0855E6D3E89482) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tx71_cdJSPG4PgutSa3eew/zh-cn_image_0000002533067112.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=3019423E38F4F1322A8474AD5E02D8E783813C61310FD9B74CDB69898B35C0D3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aKaVzFqiRhmWYYXcd6iCyQ/zh-cn_image_0000002563867015.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=42BBF8C3ED4AB72212C08410DFBE5C54E37E5B34AEA854FB1A587219C47AB63C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UXmCbSgoRI2edZvC1oZOfg/zh-cn_image_0000002563787061.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=00C2B5CEE5F7B7FB1B2A2D868457D1BAE7950679428825F4973A86C0F89CDA83) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bfHS5QrdToOl2uLPzaZpTQ/zh-cn_image_0000002532907166.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=139B047D31DC611ECB622EA252289EF7CDA7139FE32EB084EE7F3DFF4A7FC8E0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dY1ZmU5rQeOtPK1XrKkoxg/zh-cn_image_0000002533067114.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=E29E781B7EE354F08D1506579CBBAE5B396E4185B1BEC35D4EAA1721802CD3FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6KYcMF5aQOC30E3sUOyQEw/zh-cn_image_0000002563867017.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=C8FDA2704AC8284BCF252B5A15609B6BABDD587A43C2894E3BEE27ABE21DECD4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/CsUqL_vKQBGwWRIu10UISQ/zh-cn_image_0000002563787063.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=049FD912D4B7D71D43C5D9A2487B0D073AAF290E26E09740DF9D4493C90A02D8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HamQBKSPRIarddT88Qafuw/zh-cn_image_0000002532907168.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=2F543D90AADF5DB189C414182FC7B5512B689A6B0F4650E5320F990AE25DC552) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/hdkBe5lXTu-Oj9dYP7-SRw/zh-cn_image_0000002533067116.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=B26393F2E4CC159BC4AF07E0D7C3195C73A63A00438F1803B17F36C573986FC7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bPcpQD2IQsq9Tb8wMCKipA/zh-cn_image_0000002563867019.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=5C074225CC577E57DCA2563D093D571D3AEC150B619B859AD93551AFD8D1793C) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Lsf_5lwtTyW69H7ANU6wvQ/zh-cn_image_0000002563787065.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=A4B587BAA1275D961128D6D823532D307574CC51D77798CA920FD7066776FE46) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nkN2EaSbR72_Jj4tqjogkA/zh-cn_image_0000002532907170.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=2094C5F26296C23E293ADE783D222D9F9F69F2E24FAFCC8C6B93E2A727FD6029) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/z3ypE5fBQyOSkEweS_ESug/zh-cn_image_0000002533067118.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=210D5115EA4955875174810B55B6F14847D6342B17AE51AF942325A209449903) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2w_tvBaYS2uY4WHELvG1-w/zh-cn_image_0000002563867021.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=0CA840B75FACE664E7F1D54E8A7495ED3FABF8B0E17B0CA289702D364B9CC6B5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0oCV6JisTKiAQtZy7QPaoA/zh-cn_image_0000002563787067.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=0FB3CD6FA64E7E8C483BF7526C0A85FB1CC597CABA659C6215C057C6A1E79967) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r4sK6GP1SvacWeoZSTjxNw/zh-cn_image_0000002532907172.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=CCEF4190697BA0B8DB5248A0A1CFD77710B324F85E4EF6A9AAC6537B887F06CA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zOfrPPrMQr2cYRYV2518Og/zh-cn_image_0000002533067120.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=2386612A6756673E228554118EB719A3B76EBBCC9EAFED7C6FAEB7AFBED8E0E3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFYmzGd2Q6WC9ZfzA0GN_w/zh-cn_image_0000002563867023.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=2424B1B1E1850A89C0917535C049EE4CB3E8ADA1B6C2C00649705C82FD2ACFB6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sAwW5N2xQqqwlEARGHdNiQ/zh-cn_image_0000002563787069.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=D7B6535240187D16222FAF14DEEA510A8DD0C6504B81666B78702DF99D8D95EB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/S86IasA6SlqhjKkGYNmWBw/zh-cn_image_0000002532907174.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=086F11F7804379036CE095C82A985436D3D47DFD564D0EAC453D39B55A2148C1) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3UXtbFQ0RPanjHbDJHMT_A/zh-cn_image_0000002533067122.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=B5944A6A32891F12FC45E22718BDF7A4D233046330715B3BBD0438566F7B3C60) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Cr4UTxyTLCzjfln5MYI-A/zh-cn_image_0000002563867025.png?HW-CC-KV=V1&HW-CC-Date=20260329T024811Z&HW-CC-Expire=86400&HW-CC-Sign=4E2979B724696124267FF8D038CDDC75BE4DCF44BF0128072A85951DCB054E58) |
