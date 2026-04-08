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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/U7rdcJ9lTzm68awuktHtfg/zh-cn_image_0000002566869369.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=EFBF5A202641A8EE0593F6B95DB733C40A45DF8B3025494807E2C12A5DC1789C) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Chv8qEXQHe1rB4XeVdraQ/zh-cn_image_0000002566709387.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=5A8B737CFED4A3D121FED510D8633D1738600E2D38F127E8101D427235A81DFC) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/YO1-A2xcRuyklvV_JOhjKQ/zh-cn_image_0000002535789592.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=5C3034511B6F38CDF269E29DF47986B1717CA6D3FB0ACF314191FE19F70E996F) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/icj2yO_MROKol4D8_t5nYA/zh-cn_image_0000002535949538.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=D5110221B98172CAF2C683343BA14EB3C5C82004BE40300C1C9CCE77445F100B) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NXM2Ut2wQEam3LHCIBp7Qw/zh-cn_image_0000002566869371.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=89E6AE541EFAF071BA5BA4FD447BFBBF2F4A600803FC18EAC77960A6514A2EAB) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0pMboDzTT3eaWJib2Mq5Ww/zh-cn_image_0000002566709389.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B593B591FDA333C40CD7AC15C68900ADC23D8A1B8EBF3C1C8F4BB8E159282758) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_XzI4LNsRTyrw1Je5Lf5nQ/zh-cn_image_0000002535789594.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=272D61BFC93DE675BD7A9B65DEE0430C301FF9332EC885C3CEBDDC92AAD85FEE) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SrH2BHLLQrS91FqXrOzktQ/zh-cn_image_0000002535949540.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=622876A75A794AAE5B970E3D17B335C311C555314F346273A6C975A82456731D) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aC9PrmH9Tzev4O-2-Z3RiA/zh-cn_image_0000002566869373.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=93EB9D17AA6E4D291C0DB9CA65A365408B06ED9A457660766B28E96A9F7A6343) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sLpBbvpnRAysuEMqySw9eg/zh-cn_image_0000002566709391.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=D35FB761AD391DFBD3B09C309DBCBC3C52D7B1EDDE51676BD97872404E29C239) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/IuujT5iTTk-rOynEyl_WyQ/zh-cn_image_0000002535789596.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=9D321A28B978974A2B48B695EDD9913FA3AB6C36F65E5F967F618BD91FCCB612) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/aC8JK6VsSZea7QwA2VfaOw/zh-cn_image_0000002535949542.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B23CD4402B92D19ABF5C21E265F8B79ED22DA24C4CA525DE7AE106D280F4F0E7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vqR5ddigQ9ywC1-CCaaYxg/zh-cn_image_0000002566869375.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=F3BE7644BE69B2162C83FA0B2722C51183B78E02532FA66D94BC8E1AAA763E9F) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UVr2aZoFRG6RKZYWyA9KgQ/zh-cn_image_0000002566709393.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=D9C74401FCEDBD899918829A2B9E35F10465A70AA4097A6855BC4DCE0D4751BA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dJCNjPOfSF-njYTsv3XG0Q/zh-cn_image_0000002535789598.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=25096022E8675EAEB29DEF5D47835A75448186D4A504A6C011B263A373598869) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/SFRTzRgiQN2euBnwvn7IhQ/zh-cn_image_0000002535949544.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=8B596579992005850D0A6D2EE245C91527B1336353DF571F886291A62658EE56) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5NTEzPD7QkyUuvqZO3oEsQ/zh-cn_image_0000002566869377.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=0104439B09CB65872947A35CE42A39B9C57D3F5E71CBA911155B7165FA9016A3) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M3F8wzf8RY6UZou75gGF2A/zh-cn_image_0000002566709395.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=789AF7F1B19A507F6234E8CFF441E984BDB7253980D0AB88F4FCAB38430CFA03) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YTYpWPzlQouj7C_sliIgCg/zh-cn_image_0000002535789600.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=02CEF16EB53D7D6D2E378F2AB646F4B1AC73030EAC123452D69E0DDDE4BF6E00) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aKZHl6rFT9G7A8y_97-bgQ/zh-cn_image_0000002535949546.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=FC96C7EA6D9CA2D30B2F6F1C7B34ECEEC0B6025F3BE02E92CC296B10E83B2A60) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5Fk2t3ozQgm_lnODTyBZkw/zh-cn_image_0000002566869379.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=8DD09FC9E74DC2197A4016BF88A227FD754030DA8DE90064454E03718EC49A3F) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2zHQsYs7TwCDioiVXxo8Kg/zh-cn_image_0000002566709397.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=9549C9DE16B790F8CFCC0095241DB9BC746DE1A4BF4AF646585D54FB9C60C3A0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qe1Nys7URrqMBhWcjS56NQ/zh-cn_image_0000002535789602.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=68626F018B73C13003CBDAF3A5B966AD83806604499E1EA59F75C9C55BC3F80A) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GN_uCkuVTU-cLupiYbF8pA/zh-cn_image_0000002535949548.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=2F4932EFDF8BCBF015F884583349AA6CD84EE4A36253929870FEECD9681EAAF2) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/froqUDQCRk6qdwY6NtLA_g/zh-cn_image_0000002566869381.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=76FDA21A1E25A357DDE72CBE77AB67F16B0F44AC83097F9E7B5BAE22920ED995) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/o8FG5N-9TLublhc6LBgn2Q/zh-cn_image_0000002566709399.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=58C0DA3EF983F569451BDDD251A6D03DA762DECC9B2B262E3D63B6A274F97604) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w0xAT_SZSwGtKKcIP43-Rg/zh-cn_image_0000002535789604.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=BAFC438E3403DE22FCE63661BE967BE0C501D1C914C0C4C1B5EC00236A4C24F7) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Nw1IL7FySiqsm83mmJvgrg/zh-cn_image_0000002535949550.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=026A112CA5620AFCBF68439367141EEFB8DC209F0AF0A7105D6738A01171893D) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SH2Vi2bwQHy4iHinx93EIg/zh-cn_image_0000002566869383.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=6793AB9330240128EFDC3D84D4C60E01DC027DDB568A819792261C5374B7AAE1) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eO5JgJI-T9-SUDEJRJ54Ag/zh-cn_image_0000002566709401.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=1EFEBCD21EBF3979AD924B95D911A3F8147FB320CBD3ADD3BB1C662DC192CDA8) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/97Dhdj-xSaK-Z-2lunsg2w/zh-cn_image_0000002535789606.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=5D11794BC75C20CDB65366B978848F0B0BC451965070F59128CD52761A6C1754) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7szxUCnCS1OLRnqMCPBeCg/zh-cn_image_0000002535949552.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=C9D7B57970377EEDA363B1D8545318746F9A93F63341E9F38725AF834DBC7EC5) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mGJhBKvgSjmdCGcfdi3F0w/zh-cn_image_0000002566869385.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A53CCE7CFA66FE92134C15CF2FDBFB244E7A07D771EAAC17541BCEC4CC0CE998) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OdN34v3KROaT37VOXwtjlg/zh-cn_image_0000002566709403.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=44AA32A78F861235CF93196F6AB49151DCDC92C6F08EE4EEB59A03152BFC709A) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/19zg-bVLRoWH3VHfcTNViw/zh-cn_image_0000002535789608.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=36699AF5FFD6B9FCB60BB6877D85BC4E57244870342A229DECBB09896D401DC2) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xIuMxN-9RyegGRL5dHaEJA/zh-cn_image_0000002535949554.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B3E58C02C55C66A0275B4E49DC749E64B9E3CB7BEF732AD8838EE7B5023C63A4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/VfEoizikRBeXtMe698hxSg/zh-cn_image_0000002566869387.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=D1B7C2E261AF6F1D94797DF291A4F5F8BE8722EA71F504BE2580695121235211) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wwhjfe1PRH-W78dl5NoIoA/zh-cn_image_0000002566709405.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=204A0EF2118F9D591CD7C28145FE6B4F10D58334B42F92F039C34883F02EF47A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1LNPgbj3Rt6wCFJKKRHe-w/zh-cn_image_0000002535789610.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=BA38C5E5C2D66A8AEB958EA3140CEB6B81A1A449D36FB7DFFFD5438059CDD6D6) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-eh7Cr7VRFeJdcig6Hrpyg/zh-cn_image_0000002535949556.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=66ED69237BD06ED6E84A2CEC8B270CC4BA5C0E638E3E7DC4CADC3EEB621AF01A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Azb7Wy7HR9OdIRqK1DMvuw/zh-cn_image_0000002566869389.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=3B9D24A86A24A969E732C44C4D479742F43511701FFB05384B933411FC421849) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CiQCW9mAQfS0hhJwMmvZJA/zh-cn_image_0000002566709407.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=388FD54FB7C85099E5123787BCCA1EDDF4DC1C226686F28961C8865DDD0C1EE4) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/D8l8UXDfTSme0sV7RUpO3A/zh-cn_image_0000002535789612.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=422077EC56978D9F275D2FE83AF8984C2BBCB97BAB3FBA0B413F48807F10E973) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_SOZVNmkSlijpq0jDaVKoA/zh-cn_image_0000002535949558.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=DEDA7CDFFF91EEE23D3E1BE3338897559F93E6FD57005DCB29E43E43899897C4) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YYqFyBoGTA2vZXSDPZCjOA/zh-cn_image_0000002566869391.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=6C6B8F2A1342ADC1A8FE294AB94FA1559ED6ABF2C8EB627C1BC962340EDC14F9) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gO5RYHc0RkuRbo8tl5cpUw/zh-cn_image_0000002566709409.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=7C95EF0AB8ED43BFB95A9FAFC523FAB5A02E61EFCF4FFFE709AE451A47090769) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/u3J0eTcETKCFoPO2FGUlrQ/zh-cn_image_0000002535789614.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A253583AD40A43C70951C6AB260E4070BC5EC9140ADE2307EC5905A903FBB0CD) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/f9TxVgxLTDiVA9kr2x1xQA/zh-cn_image_0000002535949560.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A7605098222ED0C84BDD8E84E10588C2373D29DA17D1002AB892FA449C0BC81F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uxLUOaLnS92fwrXjhBgHsA/zh-cn_image_0000002566869393.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=DA7C0502762CBCDF81CE1CF94FA519BAE2032588145BE12DEABBFC20385A88D6) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wmjwYIcKRwCSIDy87TlFcA/zh-cn_image_0000002566709411.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=FEC4829F86F3E00B036DE7C81202F45E0F1B5793333A7B8D2F5393CA3555510E) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ta_HAbEJQYyYXC2lDfDogg/zh-cn_image_0000002535789616.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=909DAFA757F03F26AEED50A621631E00530B9A27167454206E4465A390B133C8) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OrZn2KpkTiODEIzPWvuL5Q/zh-cn_image_0000002535949562.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=35C5F061E42C68C52A9F12E41D7D897CFD4F75FCF5BCFC681F4BBEDF59BE325C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Yd6hiKb5RrqmUCZ7hJqrsw/zh-cn_image_0000002566869395.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=C4520242A3917B3D887F03DAA216A1DB872EDB4D5A688468764347E722ABE6E8) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/W7n6-EhBTuCWfiAxUu68Gw/zh-cn_image_0000002566709413.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=25892A2E7826FC2CC1553A96F5A30AA4D16B9714EEA0A6B479D9B64127CF46C2) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UvPE1EaFR-aHXXZgrpvt7g/zh-cn_image_0000002535789618.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=004996FF96D260E9C9846931623846ECDF72CB941091139A48C3463D511847D2) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/adwBfBfYQSSnRidIkB5IrQ/zh-cn_image_0000002535949564.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=49A3014B6903747750F07F37ADD0B2EA0BB3FAAE48FC8151101B25F9B1492BF7) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/usfrYNLGQgushAeNs0NqTw/zh-cn_image_0000002566869397.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=BB34D3206A67A6EB3EF5B039930B1421E4203280623F06D217037ACD425D4FBB) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YsZTJb2AQres1u2YP1q0Xg/zh-cn_image_0000002566709415.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=C32447699D91ED408009FEDB202853C2800FF98D6FC07A1E31D00C9E1341F196) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ay-KcBR2RWObY9boujQlbA/zh-cn_image_0000002535789620.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B066CED5CE67D1C27347E24438671B8656A8CBA1FAECEA1E25D71A3DF2406907) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pdJ0N-IBTwG1Fjo8F3ZcAw/zh-cn_image_0000002535949566.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=DDA13835CFFAE4505ABFAB171C82DA185E38A3EB414DDDF153462F2631DD9B1D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dAqyaaSPQpuWimDA0trtQA/zh-cn_image_0000002566869399.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=FE290B53A0DAD7C4C0E66961964CF3CE2D968801CB65642134BD03B0C2C27620) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jz5EjXpbTy6Y7S23nNZ12Q/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=87D19743A25CC6F59B42435F9F7203C35FE40A5AA92B695DFF0896CA604D099A) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D2m7NEm4TIGfjWasxLeddQ/zh-cn_image_0000002535789622.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=0D89BC5650E6EAA416983ABB54F88843F55A22B9702612A42B7B816621CD4777) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f9Le-Z_JRPq2leN2NrqPhw/zh-cn_image_0000002535949568.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=60B737A45286B030FE90BD3BA9023FBF770EAC19570DC1992B71624F230EB236) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XwNU10qRRQeSCmkd5xcF3A/zh-cn_image_0000002566869401.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A80E775D8B0B07B8404DA3F47AE924F31D01CE6BF58A8C2EC98B0B599F43A09A) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TMWufEkPRC6JEZpbkwBibQ/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=6ED87AC352A4ACDF33E5E69F83E4EE498439574B4DAC30D72EAA804B7F94CC95) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/har11OZAS7K2y-7K4Fs8Ow/zh-cn_image_0000002566709419.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=2934C29B1056D62410E2B845C4B9AADD93435DB631F833ECE5DCE9EE28944444) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/MqFJOAc6Q9uAP14cHwhNYA/zh-cn_image_0000002535789624.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=7A6DB0C1C0E24461FE8AA4B0BF9F4CEAA8838E6814786C01B2D1B7FABCC43C86) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/FJbQ5BzBSd-8SVEoTOvi_g/zh-cn_image_0000002535949570.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B8A86FF637D1CF20A2999B17DB895B84D5DA36E215D1799E2AA872DC67DC11FA) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/p_cZt0amTZ-zEkmhX1uWpQ/zh-cn_image_0000002566869403.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=41AE439E348DD9DC9554D8D13447EC49FB1792C10B93AB7245F83556EB7CA99B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hIBpgsKuQOKj7xsM3xyZ1A/zh-cn_image_0000002566709421.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=861DA025F07F34C7A59D50586A6B6C5F1798A0096F50AC1CAC847012F9D3EF4A) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_EqLXtnEQxSa5ahDTGuidw/zh-cn_image_0000002535789626.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=56BBAEE42CCD7AD25FAE8F92D40DDD373DB1E0FF291C2F941BCCA5D04514B1A6) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zgPVm-4YS92H2vCY7LkpwQ/zh-cn_image_0000002535949572.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=9D88BB3AD0007685BC64E42B987B589F75B28942B77EAAEB1CBDC692D739E011) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3c9ltMn2R7WokEmt03mzQg/zh-cn_image_0000002566869405.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=2221B9C239A63B349E8089E730CF466305BD1418BBA0B2B5B5308BC0DAF0917B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/64B1Gu0oSpuS8cDQNY2QxQ/zh-cn_image_0000002566709423.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=AB4A32D40C46486848BEF4C62D60971E027396C9E60C151F4A52DD15EABB224B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_-UVeHd_TDyEuVsL1BGigw/zh-cn_image_0000002535789628.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=AC18CF0FB480DA61E43718220937D7EE8E6A5E62115AD8480BF552BA9977D82C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qObFmpDdRHagpRUC6OAHmg/zh-cn_image_0000002535949574.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=1926FDDF0133A629550F4B54F7CD58FC1DB0661B8DDF5A2FF3E938693C50E6BE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/jCCjt3UZTse5bSw-QoVeuw/zh-cn_image_0000002566869407.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A92C6130724B259EC463DC68EE5732801CABA08DE2DD07197E1FF5ED9F081A48) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uai-LJEARh6vKW1mUWSuxQ/zh-cn_image_0000002566709425.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=F645C2F7755320BE0CE3F4761CCC49D709E634C82A0AEB642E9E73BC3F607235) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WizO8OTLS0SYRoZhqBTBgQ/zh-cn_image_0000002535789630.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=5F8BF7519E7EE223FA0F98490697953BD6E11B13B9B1A9E8D9A9A0917D9CBF6F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eIT7t2u3QZ-ORNFF2AooKw/zh-cn_image_0000002535949576.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=876E4E80BEFA43E254291BD55D627BFE8F770A7155559F0FEF12B3E595846678) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vwcORGOyRPirEYDv0xQdpA/zh-cn_image_0000002566869409.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B718855C1A455D5A2923BCB315C7608F39E7710A24A8702C78863CBED67715BA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fhdKY60CTa6L4NVmc1ipRA/zh-cn_image_0000002566709427.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=7E702B9060A58851C34CD60A3E7886F15774FAD35D243C1763CD96215CE553BB) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VlwP3bMtSTGtCS2uOIx--Q/zh-cn_image_0000002535789632.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=32EAED2D0FF3310C58BC3FFCEE232887CEB05E37F1BB3CB9B496897926204012) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gh1LEYD8TI2B61ybr9CWOw/zh-cn_image_0000002535949578.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=FA8E1E6C25AF603EE5AFB17CC4641D7936378E77BBA236490D4D9E12A30411DD) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XIyPi4CTVGBDuU72cuEHQ/zh-cn_image_0000002566869411.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=DD9AEAD505C7D2238B1CFB87FA17C89B057CC612ABBBF33D8BDD8845B0BF17E5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UjnILisFQhSZB2S5GeqRuA/zh-cn_image_0000002566709429.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=7563DE34A9888C420A71209EFF459F1FB1008EBBF574545DFBF0AA2901F458DA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_0eFQ-ZBRGmQ4B2o5tXZEg/zh-cn_image_0000002535789634.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=EA5BF1B4341602B285729DEBC697A195E88550DFD7C96695CCFACA6E35A8010C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LjFFjQaFSC6oeyDX0jsIKQ/zh-cn_image_0000002535949580.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=960D6EC70711849B04BEBEF12FF58E9201F01609AED8A1D2128922158E396BFE) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UqjTnxADSGaluQ_YwkxHXw/zh-cn_image_0000002566869413.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=CC46010F29F3DF39F7186819BAB635692134F06EF161CEA22EAAA08CA1AB2894) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GWSRIFUnS6S4BA0XbPfP-Q/zh-cn_image_0000002566709431.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=8D4FF8E4E21A1B91CD875D37191A2EFE7119A878D4AFF1EF97E8D811DB7FF30D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G6Ed34xnSJ6RqRmwZ1ZApw/zh-cn_image_0000002535789636.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=1FD007233D8AE6598501CD81AF44DCB0DFD3879D8A9D073FBCC40CF23EA1FF65) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHcsleUcTFqqY7gkyrDheQ/zh-cn_image_0000002535949582.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=3BE0089CB1A9133AF2D3F5D44B2174665DEB0AE63B46961F363BFA6647477730) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cuVXGXHPRO6-kQVrVZOoeA/zh-cn_image_0000002566869415.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=EC0C851712CB4F4D5C440BD90F3E071576652DE0E8A10C816DC193D6B891D73C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ff_IWYiQTUKuhXMeikrZ-g/zh-cn_image_0000002566709433.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=B3C3B282AE33DDDC1FDC0640323AF486A367FF283E4E3840305FB1EF34DFD14B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gExoH-_yQpSgwehc_hIdqg/zh-cn_image_0000002535789638.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=24142B007CB28D317129C2CF50CFE184F341EABAA95EEF31C8E87507796D312C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Istmm1W3Tceg8u105X6HiQ/zh-cn_image_0000002535949584.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=D1AF5C2906EEEB402BA05A2CE5E8DE87D4DF6D2DC58DFB7B17D76E73E87B4D46) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/feSI7ILTR1uwt7mU871adw/zh-cn_image_0000002566869417.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=EDF0824932A3B97A4C3B2BE7D8215086E1303F30F64B18384BE606AF4142C002) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WKmlZlnFT2C6YZGMCTk6mQ/zh-cn_image_0000002566709435.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A00DFF4B3F6C7B5AD816E4E542ADE21B259BD3261E3DF450103C9D06630E181C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/os9tJOTOQZabXC4lnt9Arw/zh-cn_image_0000002535789640.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=CD0202D33F917F525580CF063C57A536849A1F6F390EF5A3A775EF6DD3A51EEE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T18jLZ72Q6So-DK-ocwfOg/zh-cn_image_0000002535949586.png?HW-CC-KV=V1&HW-CC-Date=20260408T024548Z&HW-CC-Expire=86400&HW-CC-Sign=A5410650EDC2484E276DCF32EF88CB543ACF93A036D1D98CA4E24279A2E124DB) |
