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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/U7rdcJ9lTzm68awuktHtfg/zh-cn_image_0000002566869369.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=33660B4D1EDE72C0BF789ACE7B52BE9B5B5FA9627F8D3AE18C8E9CBC7D2BCDF3) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9Chv8qEXQHe1rB4XeVdraQ/zh-cn_image_0000002566709387.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=086BFB17857F0B030F1EBA3C1F57FBB11099F446CA7E1BC3DC6D013EC414F49C) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/YO1-A2xcRuyklvV_JOhjKQ/zh-cn_image_0000002535789592.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=44B484C798D72E96BD02ADC836C9B0DCA88A0DD52E9C920F1BE90AC9DB937121) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/icj2yO_MROKol4D8_t5nYA/zh-cn_image_0000002535949538.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=3CF0C4412BCF1768BCAA8C463EB868DF689BBFD8517593A6FAA869EDAB56D6C7) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/NXM2Ut2wQEam3LHCIBp7Qw/zh-cn_image_0000002566869371.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=180337B73C6A51C1EE14DB803DFD4FA99FF6DD17BE274451775129BC346927B5) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0pMboDzTT3eaWJib2Mq5Ww/zh-cn_image_0000002566709389.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=34670B1955099314C8BA9777567C9D75A7909217D2EB53FAD94B850B5981BD7E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/_XzI4LNsRTyrw1Je5Lf5nQ/zh-cn_image_0000002535789594.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=CD7F0DBAF4224148AA6294C848C01828004FE2ECB08781915E64A77ADAAE03B3) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/SrH2BHLLQrS91FqXrOzktQ/zh-cn_image_0000002535949540.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=33333C158298EE9997802CC93BC557B14E3FFB3C9EF92CCA5E79B66DB9929E34) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aC9PrmH9Tzev4O-2-Z3RiA/zh-cn_image_0000002566869373.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=DBF4C104A3B6F4B1121B0450D2AF4D7A8C14FD2F3DFE22E1EDA5382FC0B67B94) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sLpBbvpnRAysuEMqySw9eg/zh-cn_image_0000002566709391.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=9586CD2DF21B391DB3B349AADEE9E8043EB6EA10E43F2B15550B49890A5DD3FE) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/IuujT5iTTk-rOynEyl_WyQ/zh-cn_image_0000002535789596.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=983CCB2965CF8C35CB4DBC419E0E2614646187EF398680ECFFA859584AA96DB9) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/aC8JK6VsSZea7QwA2VfaOw/zh-cn_image_0000002535949542.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=780B9267AFC547E665D47BF433B2F960123874021B53D6F9B6848AD0C0D4AE34) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vqR5ddigQ9ywC1-CCaaYxg/zh-cn_image_0000002566869375.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=77BE494C731B4D23B09BA8A71A076D3E46D36DE8DD336E0463794CB89A7CF580) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UVr2aZoFRG6RKZYWyA9KgQ/zh-cn_image_0000002566709393.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=6600AE73400C0B410A2457DD770AE6EC4073C2A2663F617B8326B78483A804E5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dJCNjPOfSF-njYTsv3XG0Q/zh-cn_image_0000002535789598.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=3F39BD693D23E4AFF7403C4AE8DDDC7BB413691F4EE37883EC6AB1BAB29406F5) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/SFRTzRgiQN2euBnwvn7IhQ/zh-cn_image_0000002535949544.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7C51B6F75C9639592F087240407448504B2628FBDE0C5C59FCD34013C872356E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5NTEzPD7QkyUuvqZO3oEsQ/zh-cn_image_0000002566869377.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=1986B47E41A70B9523B6C54CE3E371CF9E5C86EC1B7D2EC7A4B8567B04F607B2) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M3F8wzf8RY6UZou75gGF2A/zh-cn_image_0000002566709395.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=75ACC987B6EC4CAEDB3F55839B5655CDC46206D5E0D901D477B8556CF496B972) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YTYpWPzlQouj7C_sliIgCg/zh-cn_image_0000002535789600.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=FA28830CD4429C5540FD4FB8D1EF5EEE1B1076AD61480D97CBB85D38EFA59158) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aKZHl6rFT9G7A8y_97-bgQ/zh-cn_image_0000002535949546.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=F405B2BECB112315A5EF57E629B189985EBAB342BA8D41CD51F4B513CFD6FA05) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5Fk2t3ozQgm_lnODTyBZkw/zh-cn_image_0000002566869379.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=842C048DC3F00858071690A14EE5091B367424372D208A213E4F685C757768C2) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2zHQsYs7TwCDioiVXxo8Kg/zh-cn_image_0000002566709397.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=616D4750B2313AF0FA86AED74521CF1896C2C32FEF7B61A7808984B29EE20A69) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Qe1Nys7URrqMBhWcjS56NQ/zh-cn_image_0000002535789602.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7FAA46AFA625F16BAB1AFB2E275CC6C4F388832A8E7BCE25258B64F98EAFE15D) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/GN_uCkuVTU-cLupiYbF8pA/zh-cn_image_0000002535949548.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A669074962737C2581BE502B83A7FD31B44039652D3E98FF596DE5885BFA2946) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/froqUDQCRk6qdwY6NtLA_g/zh-cn_image_0000002566869381.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=3BE829530F258AEB3F93DA5E189B511883894FC31169833C143A7C200417BEC5) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/o8FG5N-9TLublhc6LBgn2Q/zh-cn_image_0000002566709399.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=9CA06CC6F0F0200571743A85AFE3226D47B8AD3CF5C2ED635E7D638679A5948A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/w0xAT_SZSwGtKKcIP43-Rg/zh-cn_image_0000002535789604.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=261462D08EFB3DD3F6A51B70AD8FBAB914F85C51C91CF93F568A174707858275) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Nw1IL7FySiqsm83mmJvgrg/zh-cn_image_0000002535949550.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=462A627EDB67B9A3620FF28F2FCB6CC86D5A7E1A65FE437F30F33C9103079BBF) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/SH2Vi2bwQHy4iHinx93EIg/zh-cn_image_0000002566869383.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=B683B6A460E4B6614DD002C867B79F9FF483FB85B8B75406195C9DBA45021775) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/eO5JgJI-T9-SUDEJRJ54Ag/zh-cn_image_0000002566709401.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=3DAA2ECAD9289D40111CF4F50753B1AE2914588F59212D401471F2026A6E25FC) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/97Dhdj-xSaK-Z-2lunsg2w/zh-cn_image_0000002535789606.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=3FEA0331FC24BA634FDF66D72FA24B9DA197E2A275AC2F488E69D50CB8C3771F) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7szxUCnCS1OLRnqMCPBeCg/zh-cn_image_0000002535949552.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=0CB86E969F368128A9A4665743C6F48799E6196C631879825FB4ABD4CB535813) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/mGJhBKvgSjmdCGcfdi3F0w/zh-cn_image_0000002566869385.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=E98A0A0C53DADB8E733F357B273E32AE2B3B44B6D5A6566B89AEA15B0CBC29F5) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OdN34v3KROaT37VOXwtjlg/zh-cn_image_0000002566709403.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=C1DB527599D76D1389BEDE32596E541C676F4CDDA2DB9BC60904C76BFBB63363) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/19zg-bVLRoWH3VHfcTNViw/zh-cn_image_0000002535789608.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=2CED7144CD5B4AD0ACAF81E8AC1451BF9405C549C354F0427555ACDBEBFC710C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/xIuMxN-9RyegGRL5dHaEJA/zh-cn_image_0000002535949554.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=DB81EAA43AAD9954AD46C987EA642D78490892B5D6191F01F6B614D49A464448) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/VfEoizikRBeXtMe698hxSg/zh-cn_image_0000002566869387.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=D08D1A75A7FEAD9A41F79585C912361719476D9FC1E1B5C86724428C0DFA084D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/wwhjfe1PRH-W78dl5NoIoA/zh-cn_image_0000002566709405.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=FF35983B533E3DE2D1D5894D7D2BD947B5EECA99684E0A4E9468E954AF96F786) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1LNPgbj3Rt6wCFJKKRHe-w/zh-cn_image_0000002535789610.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=04E54FEB5E68765B26DD0C3F2C35DF191133DA709BB356ED8F60B23DFEA846FF) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/-eh7Cr7VRFeJdcig6Hrpyg/zh-cn_image_0000002535949556.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7738C476CCDCF2967501ABF04F5D3B60984E195F76E17AD3A66A4C1C556C54FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Azb7Wy7HR9OdIRqK1DMvuw/zh-cn_image_0000002566869389.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=EF657BA5E5A7BF45943FA8E3B1FCB128BD855133E69870243A695A969883700B) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CiQCW9mAQfS0hhJwMmvZJA/zh-cn_image_0000002566709407.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=46FA2DD7E73DC8311A79BC55CF0213BFB6397B5506E491060830603C354B7DCA) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/D8l8UXDfTSme0sV7RUpO3A/zh-cn_image_0000002535789612.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7D70EFC6A9207DACDF217C31AB4A404EDF51501DC38AFCFA9F8EE7411364F0C4) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_SOZVNmkSlijpq0jDaVKoA/zh-cn_image_0000002535949558.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7A8257CDEB60199DF9FABB93842DB25F0B8B99F1A93C8A84A761495022EE3EBE) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YYqFyBoGTA2vZXSDPZCjOA/zh-cn_image_0000002566869391.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A343F5E332459F0B7E240295FC6F79C892A035E9AF587F919BFC1F762CFA129A) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gO5RYHc0RkuRbo8tl5cpUw/zh-cn_image_0000002566709409.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=BBD80CBB2B18728F02A3E24CACC68C61B02DF02018EEEB761527AC118FB6CE3D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/u3J0eTcETKCFoPO2FGUlrQ/zh-cn_image_0000002535789614.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=CFFD88EC0F87CA4BA574DC47800466EA8931396F3D973C777A11663EBF25A0D3) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/f9TxVgxLTDiVA9kr2x1xQA/zh-cn_image_0000002535949560.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7C1C1CE10DB0F01419D959C9643B7F9EA8EE57F1DA70144CB36D4FCD81BAF5F1) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uxLUOaLnS92fwrXjhBgHsA/zh-cn_image_0000002566869393.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=16E6D5048494B105B510011894F77C5061E5331FF369932C4B43CC7C5B7C3711) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wmjwYIcKRwCSIDy87TlFcA/zh-cn_image_0000002566709411.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=F91A75FCBC541AE81A43FF2A66524F3F68A7B103F78BB5FFB94A7AE4F0AFDEDA) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ta_HAbEJQYyYXC2lDfDogg/zh-cn_image_0000002535789616.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=2C30F69313D2BAB3C6B0A82CA19F914ADEEA272E2488EB297F040757C5C3859F) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OrZn2KpkTiODEIzPWvuL5Q/zh-cn_image_0000002535949562.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=1BBAF445D17E105ABBF65D827FF2905A1EBDD50243C8922544E17BC4AF140086) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Yd6hiKb5RrqmUCZ7hJqrsw/zh-cn_image_0000002566869395.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=FD88A1EEACFA4B8B093358056B8B2BE6FC499FADAFDCC68A32E63CE548201614) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/W7n6-EhBTuCWfiAxUu68Gw/zh-cn_image_0000002566709413.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=E483DF9B2BC106AFB5A61998DE950D60390C35857EF351813E7B30191509A67B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UvPE1EaFR-aHXXZgrpvt7g/zh-cn_image_0000002535789618.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=D745F29301CF4C7C5A45A1983A1B4C7B570D884F89961790B3A730F836E69B6B) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/adwBfBfYQSSnRidIkB5IrQ/zh-cn_image_0000002535949564.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A20FB65F1ED24AEF9325E9F16E531FCFCB66CA657EA0AD15BE1B6A16A68507DE) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/usfrYNLGQgushAeNs0NqTw/zh-cn_image_0000002566869397.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7012BF4402D0F657C7EED91A0DCBB46525E041F82D7AC4813B2EF84A1DBDD0BC) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/YsZTJb2AQres1u2YP1q0Xg/zh-cn_image_0000002566709415.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=F7C2889AFBA438164537A67A7CAE033382CD5E64119A16EF8D8544BED71F7C12) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ay-KcBR2RWObY9boujQlbA/zh-cn_image_0000002535789620.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=1449120EF7AB30F24EB5383C35F4D83468A1C1FEF75D11E5CA6567344F931290) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pdJ0N-IBTwG1Fjo8F3ZcAw/zh-cn_image_0000002535949566.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=7B372243D0AA5CE6DE3EC3488AF5277A89CAACC027D885963E367620CA09CFE9) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dAqyaaSPQpuWimDA0trtQA/zh-cn_image_0000002566869399.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=AFBE47C9A968FCF59DE0A8E698254435117C769EE1E82BEFFEB8D47C92BD3DE9) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/jz5EjXpbTy6Y7S23nNZ12Q/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=04315C1867AC038AC093E7BB756A5EFD58C679D52C203395CEE0D83D7832828A) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D2m7NEm4TIGfjWasxLeddQ/zh-cn_image_0000002535789622.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=49B58CC487B1C8F5C4DFFE3CFF866F79C6678E292D76E255E7A9A4C3F0858A83) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f9Le-Z_JRPq2leN2NrqPhw/zh-cn_image_0000002535949568.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=AF26D883157EFB9469B656B974795DF71ED50C9B909416E9A6253ADF7F53587D) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XwNU10qRRQeSCmkd5xcF3A/zh-cn_image_0000002566869401.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=EAB5442079D1E0E267063A13EE09A98FA0D429567506ECA4570F4A3AA66F7B9B) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TMWufEkPRC6JEZpbkwBibQ/zh-cn_image_0000002566709417.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A137227D5D3F345D0CF1CDD6A046B75F059DB65DAC81A60FE2DFCDBA2D3B0A29) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/har11OZAS7K2y-7K4Fs8Ow/zh-cn_image_0000002566709419.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A66A51D20208E9B696F35F99C3415B949D377C024B484440EFF578F1B452C4ED) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/MqFJOAc6Q9uAP14cHwhNYA/zh-cn_image_0000002535789624.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A2E48BE2676BA06CFC9D4FB3E2AA44E1667793A82ED5A6ECF1AEB96C0C73DD01) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/FJbQ5BzBSd-8SVEoTOvi_g/zh-cn_image_0000002535949570.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=F5F7EDAF90A54150BDC8F6DFFB4B32F57D27DF961908754E8211CAA0E07F20F3) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/p_cZt0amTZ-zEkmhX1uWpQ/zh-cn_image_0000002566869403.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=41100D414D3268D394B525E821861A493C07DF376CEEDE18C4397BBB20FF7D42) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hIBpgsKuQOKj7xsM3xyZ1A/zh-cn_image_0000002566709421.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=007D83F779A670C2E641647BB24823D2DAF115638BCCC4C41CBEBA5FF639FD7C) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_EqLXtnEQxSa5ahDTGuidw/zh-cn_image_0000002535789626.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=53A92909E96DB656561990A6DBAA7A0C3A689AF43268C05892ED538B1ED46066) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zgPVm-4YS92H2vCY7LkpwQ/zh-cn_image_0000002535949572.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=06BE211E206F3CC5B54B3B57C3AB53433129A109EE95BDAB5ED4A74F1D190F3D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3c9ltMn2R7WokEmt03mzQg/zh-cn_image_0000002566869405.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=005118DDC4E5186FF11DB0153745BE0C71D9E3303B329876CD6F42865E05FF15) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/64B1Gu0oSpuS8cDQNY2QxQ/zh-cn_image_0000002566709423.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=135C052D9ECB5F5BB647A8406F83886D5E00C4917D06EB33120091107E56282D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_-UVeHd_TDyEuVsL1BGigw/zh-cn_image_0000002535789628.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=C8DD91EEDCEA9AAC9036077C287DF94014C60347B4325CD977DD5C364F33C888) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qObFmpDdRHagpRUC6OAHmg/zh-cn_image_0000002535949574.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=465E6475CAB41AD61C6C9FA39A7789482B5339657335353FDB2D84527F2D7F3E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/jCCjt3UZTse5bSw-QoVeuw/zh-cn_image_0000002566869407.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=FFB3E31DA45424BEB4F5AE553C04E81588D6A88132EC86CA4DFAB1CFB257BB3D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uai-LJEARh6vKW1mUWSuxQ/zh-cn_image_0000002566709425.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=DB84A9AB1BCF761C8842009BA8B3EABF1F443F4E20A4F8797EBD79124CAE1EB4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/WizO8OTLS0SYRoZhqBTBgQ/zh-cn_image_0000002535789630.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=FB1A2436BEB6C00D85BE748AB9F4BE00C82709B8D5B16A3521CE11235E3E647D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/eIT7t2u3QZ-ORNFF2AooKw/zh-cn_image_0000002535949576.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=E150C19803C8B9A445DC7EF7D06132853D795ADC0B685672B1A105B9750A0B47) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/vwcORGOyRPirEYDv0xQdpA/zh-cn_image_0000002566869409.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=D8D221B587A0F75C2499BE61D7A950091A6E100A93B5A655CA7A9E7C24F4CC85) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/fhdKY60CTa6L4NVmc1ipRA/zh-cn_image_0000002566709427.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=D9B9E0EDAE68532FE5C5C7BE36E65D83CB06DAD89CC0DAC6DBB4327910663E12) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VlwP3bMtSTGtCS2uOIx--Q/zh-cn_image_0000002535789632.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=41CB9FD8A1928335F4A91F4B78D6B48B9815CA15A801D479E2B6BD558F79F594) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gh1LEYD8TI2B61ybr9CWOw/zh-cn_image_0000002535949578.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=512A9714EF04D62FA14F63E6FAD53DA5451633F38D0282C760F7948218AB028F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XIyPi4CTVGBDuU72cuEHQ/zh-cn_image_0000002566869411.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=4CA5C0C99DFD5B6F46CF35FD4BF9621318605039A5F48E5370C99187AE7BEFD0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UjnILisFQhSZB2S5GeqRuA/zh-cn_image_0000002566709429.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=510084FE9669A5D7B9E5DC260BA4E50ACFF6B45E9D69B4B39F5652659E1C55E3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/_0eFQ-ZBRGmQ4B2o5tXZEg/zh-cn_image_0000002535789634.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=4432101387BB7B7F69D833FBA4883207D601A22742042BC3B8604441A625809F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LjFFjQaFSC6oeyDX0jsIKQ/zh-cn_image_0000002535949580.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=AD2C4949A9057F94DC0989BC4A9FC132B421E6219C301DF9E6DC60E5C2B50BC0) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UqjTnxADSGaluQ_YwkxHXw/zh-cn_image_0000002566869413.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=24C1B2D55170CF2A6E8BFE106EDC275C63AFA5E2AA34C20057FFFA2DCD126450) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GWSRIFUnS6S4BA0XbPfP-Q/zh-cn_image_0000002566709431.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=714B8B9F4D69E7B9D2083828051AF6AFB395FDD4DA59F517A52BE4E6CB63092B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/G6Ed34xnSJ6RqRmwZ1ZApw/zh-cn_image_0000002535789636.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=48923648008676E622AEAD08608DC21F01187127C0EF84B544F84A700BA6C1E1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/uHcsleUcTFqqY7gkyrDheQ/zh-cn_image_0000002535949582.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=5B1776508B030BECE7723A6CE73B72BED091033A9F02CD9C00A7EDCE30648F61) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cuVXGXHPRO6-kQVrVZOoeA/zh-cn_image_0000002566869415.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=970CA191DCDD9D02F52FB21EEDB9BF802C49C6B507033A8A0133301EDF4B551D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ff_IWYiQTUKuhXMeikrZ-g/zh-cn_image_0000002566709433.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=E509F7A90CEC7881449AB4A6C949B9446E405D78ABBD29C081941BC6193D7007) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/gExoH-_yQpSgwehc_hIdqg/zh-cn_image_0000002535789638.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A401179977BA3730777F5A624C5E2B703877F326987D4688673F82CCCED746D6) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Istmm1W3Tceg8u105X6HiQ/zh-cn_image_0000002535949584.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=88B30B44BF1E0481B4D34E2C317EA9DA53BCAA758A603EDF17D00B59A5A1F5A7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/feSI7ILTR1uwt7mU871adw/zh-cn_image_0000002566869417.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=00160CE0293B010D1210CE41E552F91454BE5CB2F187B3777D2B4A47AF7D593D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WKmlZlnFT2C6YZGMCTk6mQ/zh-cn_image_0000002566709435.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=DE719DA4CBC9FE47C18AD79CC727D121F9FBD077AF14C2705AE3F66F2233FE62) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/os9tJOTOQZabXC4lnt9Arw/zh-cn_image_0000002535789640.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=C49DE5010ECF009556F149ED3BADDC64B8814A8A2FA5C5EC01D3E2AEE8FD3E42) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T18jLZ72Q6So-DK-ocwfOg/zh-cn_image_0000002535949586.png?HW-CC-KV=V1&HW-CC-Date=20260406T025154Z&HW-CC-Expire=86400&HW-CC-Sign=A2FCE2D8A6BBB203046410B43215E7AB2A063A8A5B5BBA152DA48A75177D8023) |
