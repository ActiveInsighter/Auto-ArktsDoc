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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nF53NYegQ42Y4g30GI05Vg/zh-cn_image_0000002563787021.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=2CAD259D1D17253A34820CB9C0168CD81EA077968C5503985AB4E3FB5AB0F317) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/uZbH8fBmQrOtIA_gy_2fYQ/zh-cn_image_0000002532907126.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=B589DFEE55DCE158926B848960AD6316253E622A196C17A7B87FD64D26172B62) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/xhY0Ya1_SxSAowqitPw_sQ/zh-cn_image_0000002533067074.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E771B576E88C6F8CB3C4431B21AFA74738316AF808119E2D9DDD0FFB0D0C71C3) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/tZtCr19sRkSQG1srqHoDig/zh-cn_image_0000002563866977.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A0083CF79042EDBCB45B60E6CD98DB943CD5069F46462A0CBB6CF452824AE512) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/DuK3jIg-QtC6F1MdD4f0tw/zh-cn_image_0000002563787023.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=5FF205FC13499817158AB0638277AF955B2E44F908BFA8FD86E70CEEA996BAF4) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-WpqmfKGQaK8jWaI8LDoZQ/zh-cn_image_0000002532907128.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=83E11F6B6831B23070E2117EF9719672D003E31BA65783F93012CEA39E115253) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6OCiTm9CS0WTBhbKF-TKMA/zh-cn_image_0000002533067076.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E4384B41FD6195DE5EA3711426FEDE53BA9FA5C3040DE9B4F81CD7B488B7699B) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/rMSbKLbwSmaZSlEbEXuWuQ/zh-cn_image_0000002563866979.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=874AA34472926832C2DFDE09013283DF0C2F1482874189E105754E8ED9659B62) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XIB5dkWNTCCxP-pB-bmDwQ/zh-cn_image_0000002563787025.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=90CC96B879A7B1A5FC640E36133AD360A3A110D63280A0C190AA4547383D8955) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9nj1LBG2S-Gu5qTOWRcRLg/zh-cn_image_0000002532907130.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=8EBCD8566D2151F9650D01EF2F76BB4E44413EFB7692C3AE058074EB35144399) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MSpIfr27QbSy7Lu7uvbaZQ/zh-cn_image_0000002533067078.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=0278F59238E96C9B92BD678AABAB73569995FF823309D7E73464C670EECB9FF3) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/NtcSKjagTCCxK0TgHwgPgg/zh-cn_image_0000002563866981.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C4A4399E87F41C881FEA550A40FB95D95581A59ED12A1BEB5C29D4799851B260) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dNVmhl_rRO-O_xIoiqVWRA/zh-cn_image_0000002563787027.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=166E36F95D35ED6960FAF286E1B7833297F7B7740DCEDA5565F5FD97679B86C7) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/1Y9RqQNiRu26x5HcbkVe3g/zh-cn_image_0000002532907132.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E997B49323E30505EABE4BEFB3308F095AE1D15FD1B2B7EA8F41F03BB990FA37) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/qughuPY3SnW8f3QyVKl-lw/zh-cn_image_0000002533067080.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=71A4F110D0CB5A5381D86D2BFF3C6501D8CFC0AAA1D74910BD9FFE19C942D05A) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/gZ1G0fkCTcuGYeVqDU7Aow/zh-cn_image_0000002563866983.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=975ECF2C9C34B182B91C2F3EB658B80C96ED117C7D830EF7358500CBAD0F431E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vJdgSTHUSAK025u2QQ7vfA/zh-cn_image_0000002563787029.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=8A34CE2CDB7F72E41D27894DB897888D7B7E84A200333A6997BA2BA6C448242A) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/RFvQknBZTpC_tnzo6ToPOA/zh-cn_image_0000002532907134.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=07BB2091CB9846B6A4D6F196F96D6446DB7816A3E79CF2EB315FC74F89A76B02) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/f7GUxTg1RTyrSmD_xXVblQ/zh-cn_image_0000002533067082.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=EE70D1CEA83EDA7BDA6067AF90A2A7D83076C34576D81C6F31F26A103C889BFB) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/r5Hhze9fTj6ZjOnIOI7RYA/zh-cn_image_0000002563866985.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=50C930AAF8905FAC2C8CF30D58BC5549D85F9B1C5B672512575F3DFEF4789162) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8YqIAj-zSxKMv_VhT8xpJA/zh-cn_image_0000002563787031.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9CD29582A511FC500E3172747B37EC65A91F4476A4D72CC94A3CA90761106E8C) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/VeuKSoDFSViKGMX5ghvdyA/zh-cn_image_0000002532907136.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=48ADA93A7E03DC6344056CE1B042AEF988DAA1F1CB3E61C0E18F34832906A901) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VOubMPnZR7WclUYSbF4g0Q/zh-cn_image_0000002533067084.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9A7F987128D532FC59AD7C8E34151AB6983B0E28158B363E1B449304588CB397) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/suk6tetJQ-eTb_wP65OFnA/zh-cn_image_0000002563866987.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A8FA0F491FD9CE2DDCB1B47E2A0DC3262412E26E140F7D4E192D018B3ACB9218) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VQTPtYMITZ67W1rOi7YFEA/zh-cn_image_0000002563787033.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=55B0653ECAC7E199795813C7E28F1C290FFAFD70794C07588AB40CFF5FE168EB) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ShI4i9bWQa6zEWWnzc-fFw/zh-cn_image_0000002532907138.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A5F66F49AD8703F49B9AF49B347801269C82789DAC98759E2A10FE2575DD8DBC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Vxw4b7XDRnaaIKXH91RceA/zh-cn_image_0000002533067086.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=01A8B67EDBD6F4DA9F219526E553A5ACAC78E489DAB9B97B496E602AAF0039AE) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Hms8eO4mQueMUVXv-ciuag/zh-cn_image_0000002563866989.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=68439C78244A760C89C8E34AF580946AF93F460B6F122F6D0ABA04FD570FE258) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yL5NC2uDTxOEmGjFGg_ujw/zh-cn_image_0000002563787035.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=CF7F682E15BE0CD3820F09D2806ACC8E87729BECCB7436E6253AAF71DCD5EE02) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/mJeE5CrnR6uZLX97PmdTwA/zh-cn_image_0000002532907140.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=19689156EC32D516AC8FE210CDDC7586AA65A24072ACBDD34594A3FF8077D4DE) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/wN439rM2QV-PtLCa6cIQ5g/zh-cn_image_0000002533067088.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=BD803E173FF16546ED1E581E16D45AD0FC2AE6EB51E1B8B05E0DC047EE08DB33) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NVicZqDASZW0d_-txGMZSQ/zh-cn_image_0000002563866991.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C6E8DB667B5EEBAB9FB1FD578012BD3F455DD8410FBBD70FE008EBD54DB8F2B8) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2qiaZoavRXG5c4opSQA30A/zh-cn_image_0000002563787037.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=3DA750063EB6A793271E7DA03D2E32E84A3A406884B58EA73A2CF65208082DB4) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lX225aVtSu-4nvAtUyIPMA/zh-cn_image_0000002532907142.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=ED52E8EE1934C7E3EB62363B8F5C0ED5CFE3C740700212B66ECA14EE5D78BFD9) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zUifEkaGQreX-P-W31DXfg/zh-cn_image_0000002533067090.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E578D4FBEA1FF7AF368D55F8684A20AB0EAD7C03948435F0DA2AEA614D886E19) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/X2zABTc6Q9WbYXK2ClShLA/zh-cn_image_0000002563866993.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=7FC7A61471343732084F249D6FF95D2536B890D7EE049FFB7B4BED43FF3EE202) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/v_j2wR1yT7edorhG7el2Vw/zh-cn_image_0000002563787039.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=696830C29FB83CE3B585FFA97D040DA79CA4C43041761643819922EEF0E6094D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/CW5bJd7iR6qzFrmkEfIfrA/zh-cn_image_0000002532907144.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=0C88D51CD76587B11BD4A7095F9D53CD0A03EBBFE063931A5420744CB4546808) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/nTuBuaANQki8toorvozBBQ/zh-cn_image_0000002533067092.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C18BB8EF467694BD8F8EFC2F649E867D4FBEFC07DD8717B5E6E7E06D2046BE4A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/uKuzD0l_SL6Ch_R9pAPaTQ/zh-cn_image_0000002563866995.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=656D1CE7EFAB47CA241C8ACB3B3FFB2877BF0D7A0B6DC971D4743F37B2FEC24F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ttv8C5SGSPS-IuWGizRPWw/zh-cn_image_0000002563787041.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=FF4B902CD1284505F677B77CE2E6D010827980B9FB918D04C2EDA8070D03F1C7) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Bwfe0_WrSW-txYWIG-f2jw/zh-cn_image_0000002532907146.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=33571CCB614EDF1F3DCF5989664DE092C28C6979974761FEB70F8424744D5E57) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ouyNukCiSX-HNT4CfdBqOw/zh-cn_image_0000002533067094.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=6883BBB365663FDE2707BD734B62E732B001B49F90959496DD3604887D4FD52D) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RqKmqxDmThCm1uxvggu7lw/zh-cn_image_0000002563866997.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=8F5EFDDF03B6AEFE6E1064DEDEAE05918D576A5DD2397F0CE868FAC2F390FBE0) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/N39nkasrR8i7MPz22lHw2Q/zh-cn_image_0000002563787043.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=F4027E23B9FFAD0846B28E2DF5F884C4B3B4B5A52B246D33DA320214E781371C) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ro5Zmt6wTPuJEncra2YSQA/zh-cn_image_0000002532907148.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=FB5F838DE0B1111DECEA792EEB326E45857C61FA6F9AFE7B95839E441DDBCE3A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9Z2fbEgITBqHpUI39CeITA/zh-cn_image_0000002533067096.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=75931DA04036C1554013C8F0CB19B604E3613A0C0350D781928B3B7CD915936A) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4pfSQmlaS1afzIsOsjJLdw/zh-cn_image_0000002563866999.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=3A5B8EFEDB49AC2B9855F7EDBE1BA83EE80F539590ADC5643AD8A97E0E339CB7) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/omfYG4BKQY6lpCn4NQasBw/zh-cn_image_0000002563787045.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=2F7A896BDA51A0A667CDA43EF9856932448B58974623F70C9E68591FB908AA55) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/gV3e13IRQe6p1gSYI9I-qA/zh-cn_image_0000002532907150.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9A0500D74A47B3CF49656DBE549E66CB189C5477E5A3131A7DD053643D07068F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/JNt6zIKuTISfGgn1gTqkEA/zh-cn_image_0000002533067098.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=B50B3DAEA9EB9324187F2011D6A536648176A2CB2F2A11C09FF3BF57D39B58AB) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/dMRrxWJWTKmTnypU4ZcXFA/zh-cn_image_0000002563867001.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=04052B4C2E2E8DD9D14CE5846F3093ACBC62B3085DE111EDE51C5EE6BA73CD17) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dcke9U_wRzubGXXNCwDiKg/zh-cn_image_0000002563787047.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=EDE29D91CE58F84D387792BB6D7405016B7314F003F0AF526E910179E8CE0E81) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/VpATvnXHR-yZtURdPUGjzg/zh-cn_image_0000002532907152.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9B589E159DADE40687455F2588666F31C8DBBAF4C245C41F6B4B360D5BBC6DAD) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/sUAUQwuHQBmFB12_RQbsNg/zh-cn_image_0000002533067100.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E87FBF36C04AEC5A32AAFDDCB6B5EBC49F43C6B355DD1BD522066896A8A01AAF) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Fu5Q5cI3RpOTLqBSnXFGxQ/zh-cn_image_0000002563867003.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C6E3D384EDA9A5C52DAA1E211A37120A6CFD42C559EE7593FC21C6617EDC9E7F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mliCiAXgQe21RNpF4VPrXw/zh-cn_image_0000002563787049.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=35DC369CA24FE1EAD5C12906B94807908EF45EC04E718761FDC1D05C93E16492) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/dftpkyeWRQeHjaSSjF10Ug/zh-cn_image_0000002532907154.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=5005D17C50498192A0FFA85BFDF0347F7D0702B48095B04B78475F70AD172D85) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f-fmtmNOQz-aNrID8OYASQ/zh-cn_image_0000002533067102.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9FE71F31A1B06FE0008C4EC5AC2F480ACA7E6A59B738F13BF05BD68D940F4475) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jedp2XI_S3yqHhUqiDrKpQ/zh-cn_image_0000002563867005.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=49D338B4698E18C06A263784359AAB4EE09DB292BB0E4DDBF378F7C250618C61) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/fYpE5uHFQHyXRC44X70FLQ/zh-cn_image_0000002563787051.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A0E9DFEAB0CAD82A960AB8EB7376A5179FFD571F354441ED2EB6D3C64C305F43) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Pi_wzNGGT9uQbpbqeL07yg/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=CAF44433958E236456A53533C39CD3BDD73E131D4CCBF685BD92B39436CE63B1) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/UaCiXAmnTcSXNUVDXPtYUQ/zh-cn_image_0000002533067104.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=22224B219BFA82A662D41FA15E813835E7F3732D1DCB59B35500D2EBBCE97C59) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/uymCv_ZNT9WysHsQ_RnCvQ/zh-cn_image_0000002563867007.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=6B62C91BA5511422D5303997B5FEAE62476233F17BAEF99305DDCCD93AFDD658) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/I5yqOxWQQfi3dRP7aP6cyQ/zh-cn_image_0000002563787053.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=DA2A9AE5D5C80F3F63A6E6C5F605F42EC6DC0E0539D38F7830C1DC189F744CED) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/PrEX7Ts1TdGeZCoLBJwc3g/zh-cn_image_0000002532907156.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=D7AC42BD281E71A283E1A906CFBA62A97DA9C7F56A9886A385C07A0983721192) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4z_Mrnn_SRO1h7BwYgt6sg/zh-cn_image_0000002532907158.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=34FCC0DABA4B5BFDB13407D4CC421611989541135A9A69420244F857F48FC42C) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jjjGtwhpSIqe6jgDZ5LWUA/zh-cn_image_0000002533067106.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C4C95995CB82D8482740A5805323FFD9513352F28DA3BE8BFD256F8D0CC24312) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/N60h60w6THCGOJhD2t5_DA/zh-cn_image_0000002563867009.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A4CFAF1DCC59D7FD11EE339379EBF41D8555CC3A2315D49F045BEB9BA80FBFC2) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/3Cba8q3XR7CjclUz19o7zA/zh-cn_image_0000002563787055.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=2B702332F1EE7175BE584DC55CEB8E19ACCFB65D4EBA997D20856664A5174A09) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ORJiok74Rz2CSoBesZ3uBQ/zh-cn_image_0000002532907160.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=67A2D171A932775D4E84586FFD1758FCAB12F07975853D20BAE25734C442922E) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kS8QxgOYTS-d5cNmYusvwA/zh-cn_image_0000002533067108.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=DEEFCFF67CDD0E3E83F100FEECFAE05AF12790291E96CD1DBB26031BCF99206C) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/FqhrYgCYSRyWv_GyzHVaWQ/zh-cn_image_0000002563867011.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=27CF5F375573F654872BAAC8E9F26A502B2F023C51581C16BA02E35EC1A5A2C6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/IHFglV6YSfagtD4oJXB03g/zh-cn_image_0000002563787057.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=A9D70E6525E6E27015F229AC3CE0FC829D00CE9BBC2E8C1CEE8F6ACC50A8FB56) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U5wSt5bZQ5CFuFWTImRpUA/zh-cn_image_0000002532907162.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=93642FC34E9153CCF58D955C53CF1DB92975BA3F5075A88049CE32A8D89B8B65) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Fgodj5KhTB6bW_8curtGFA/zh-cn_image_0000002533067110.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=62B096E430746CB26A25C35674F57CE14D68F29CE5672BD05EFBF0340980262F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXQVKOJ4R0e0mhNBj2heYg/zh-cn_image_0000002563867013.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=8CAAC401D3F8C45D60FBA5DF95C20E9A200C693154399BD8BE22D2B0B9D81FD0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/e841zjgoT7i1NajW3G0Fgw/zh-cn_image_0000002563787059.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=AC92C9D155DAE84CEB6F9EFDD1C006B8638B1BF9AC2860D324B7A8499B1D03F7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Scfu2NgeSoWMXu9Z7kHE3w/zh-cn_image_0000002532907164.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C2732E60401AC9EE745E776D1341BED3CF1D7FE663B9F7B0CFF9A9F01D036056) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/tx71_cdJSPG4PgutSa3eew/zh-cn_image_0000002533067112.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=F2BCCAF93F43B56736C5FD32639CE1BA14A150EEF2D5DF7C63E9B6F5CAD2BA62) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aKaVzFqiRhmWYYXcd6iCyQ/zh-cn_image_0000002563867015.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=629F453E371DF33B5FCDEBD6C16FA7AB90158C88F835B31B35AF3FF3A21651EE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UXmCbSgoRI2edZvC1oZOfg/zh-cn_image_0000002563787061.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=983D7B7FECFF0D76C1825FD95BB993039480DCF6721C3B5C19A7BC52BF9B24A1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bfHS5QrdToOl2uLPzaZpTQ/zh-cn_image_0000002532907166.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=55D4C14ED1569FAE597E0552B05096B010C7DB783590E75F999D599690A3E6A3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dY1ZmU5rQeOtPK1XrKkoxg/zh-cn_image_0000002533067114.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=645B18A39B87A34E41E466DCEFA68145EC2AEF940DD75EE3D4FAB651EAE702EB) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6KYcMF5aQOC30E3sUOyQEw/zh-cn_image_0000002563867017.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=1A4C5506C26A60434C2705714F58E35AB5181F780727E2AAF320F298D3D14F28) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/CsUqL_vKQBGwWRIu10UISQ/zh-cn_image_0000002563787063.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=16F82E5BA0678F8E85A3B9584E63B481B07552AE256B9222B8AE640AF4AB3A76) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HamQBKSPRIarddT88Qafuw/zh-cn_image_0000002532907168.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=324A25E9D086096B0C8F0C8765785852C633C62DE38435AB4FE42EE9AE2A1454) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/hdkBe5lXTu-Oj9dYP7-SRw/zh-cn_image_0000002533067116.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=24CEB041762F33142E0EE1928A56FC58C84A07202E92E0EAED2E66CC93F41D82) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bPcpQD2IQsq9Tb8wMCKipA/zh-cn_image_0000002563867019.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=B2FD032024FF570255B74B6F8EC5E3BDA3DEB0D3AE6D479B2F646DA446320DEE) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Lsf_5lwtTyW69H7ANU6wvQ/zh-cn_image_0000002563787065.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=94E595E81B9B63457B282155E7CEC587093D6ECF63A2AAB78B85BDCD8BB01E43) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nkN2EaSbR72_Jj4tqjogkA/zh-cn_image_0000002532907170.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=C70AA165AE8AA3A6DA16EC6F6619206DA83AEA33BBEED62FAB2C3B5A6CFE1BA8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/z3ypE5fBQyOSkEweS_ESug/zh-cn_image_0000002533067118.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=9549EDBAEA68495F9B324CADFC6CC7EA0585814A92B6A8DD97C87C4C52F1CF71) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2w_tvBaYS2uY4WHELvG1-w/zh-cn_image_0000002563867021.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=EA23295436A6A82AE2987CAE96073EB8C9B7519D32A554EB8ADF9CA2AD3E3819) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0oCV6JisTKiAQtZy7QPaoA/zh-cn_image_0000002563787067.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=47C82A66DFFD6EF181B4405B52FBBB42D97F3E61A6F954DEA605C5DE7A2FFA91) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/r4sK6GP1SvacWeoZSTjxNw/zh-cn_image_0000002532907172.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=E775AA77FC39064B3312E4A437C1F3172FA164D040529B7ADB5C0E7C1EF2D2DC) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zOfrPPrMQr2cYRYV2518Og/zh-cn_image_0000002533067120.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=2E218883AE40620CC54113619558E85351DDE1C95EC1095CEFA91F1FF576EE43) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFYmzGd2Q6WC9ZfzA0GN_w/zh-cn_image_0000002563867023.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=4BD57A5C01899DD791213D313F338217BB0EA3337CFAFD1C31E4BCFCF12A8879) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/sAwW5N2xQqqwlEARGHdNiQ/zh-cn_image_0000002563787069.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=F97409270E6CDEC519BF00FCB1A5DD7A37B456FD4D221BC2DBE76309F8BD3D89) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/S86IasA6SlqhjKkGYNmWBw/zh-cn_image_0000002532907174.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=4A0B1A995F5B83A6A36C670BE730E0078FC20C9AF69EA19DCFDFDF9B67529294) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/3UXtbFQ0RPanjHbDJHMT_A/zh-cn_image_0000002533067122.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=DEC500E7D4540E43B2552A592F4EE8E1C853E754B418037CBBADC6AD7F4FA19E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Cr4UTxyTLCzjfln5MYI-A/zh-cn_image_0000002563867025.png?HW-CC-KV=V1&HW-CC-Date=20260328T023219Z&HW-CC-Expire=86400&HW-CC-Sign=4DCE733B8568F2A7DBCE89CFC8686A0744E9AF57B066B0D67A4566184BC1A6C9) |
