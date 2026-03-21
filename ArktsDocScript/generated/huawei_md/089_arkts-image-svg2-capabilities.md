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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/MsGubtXLQAqnT-XqCdH1RA/zh-cn_image_0000002531226016.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=372368694E1D5D4FD2C5D9DD59B6B08B029EBF2929E58C73A3853861550D5CC3) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/hoY8r7ysQSSTZZULQD2SEQ/zh-cn_image_0000002562025999.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=D1963AA7C82E3FB0BC1A1CFEEB80D537ACBA13145DEAA24341411EED33C156B9) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mct86Xz-TCWGliRmSFUIIQ/zh-cn_image_0000002562145985.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=9A2D209838AA62DFACFB226DB5F5CC749E947805CCABD7C1A1A5DCE1BDB84E98) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zCulBZSMQYSG76AwACd6JA/zh-cn_image_0000002531106084.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=7B6A925C9E05AF4321FF519575877460ED15C3DF4E4994A4EEC07163B7282CE0) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/S5Bym8PZT6ulIQqqraZkeA/zh-cn_image_0000002531226018.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=84C06685A276F689DFD5886108D2521EF697D70CB40EC6CE0D5BE0A9AF646D44) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/IbEU8DcJQqyJc_jk4419SQ/zh-cn_image_0000002562026001.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=0E0ED62C16D0A89CB91762CBB3171BC910CC419E814769F47A0BC32C4E2C149D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eK8rWI09Teu6wCQr5nJPMw/zh-cn_image_0000002562145987.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=68F1FF7731028FC21CCF5CA6C10E64D2CEB79A6B62BA81EF58E0EFEE0496345A) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hDb7ycCaQae2i8EYs60ulw/zh-cn_image_0000002531106086.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=8984B53830E82D0C94894770D3DCECCEA35AD81FFFEDF5DB60CE57AC6E73C169) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/2y43ulkURVC0VEYhefESkA/zh-cn_image_0000002531226020.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=5FAB482FA35B25E2E3CE11B4AADD800F0DFE6EF8F84671A6FAF25BF8D8FDC97D) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/193mMcO-S0KUZk0DgvIpDw/zh-cn_image_0000002562026003.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=AE12460227C1DEF7AD4DDC7141D30626D69697DD1179AD575E36F0B7008626B7) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/JpwqOTFISlm2gQmpBRS3vw/zh-cn_image_0000002562145989.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=A01A1C22549CF80A5100715F8A89C759820D413E80C884A6F4C18A50639F089F) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Gc1O_NdLS2GUdifGCdLB7A/zh-cn_image_0000002531106088.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=EA20225434C575DFD03BDE339AE327CA17E39ADA9C768AE76F1AC89C5BFFEDA2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_At9qU-eRE-KRKfoWzpuQg/zh-cn_image_0000002531226022.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=739CD7AA136CE244009CDBBDDBAFDD73B181AFBD1422A6BE05A87008EDBADFB5) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XMSf5UlzSby6QPdQC5aipg/zh-cn_image_0000002562026005.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=2C28563D4AD5D812AC55EC7171CA5438E2D677F02D6CF86F7BEE81A09AD756C4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/-Y_PP3ulTaqz7w3GQ6cMQA/zh-cn_image_0000002562145991.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=08D9AC42FE1BE197128D9E0A01573AA4B07D792F55991DE964E73EA25B7ADEFE) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/g95t-8LaQoeEiFO4MZvcWA/zh-cn_image_0000002531106090.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=CC76C43F70CBF5F17023D1E1D334B0B45F40D8497A293FA2E9774C08523C2869) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/a1PNeI0sQdGbHPkFV_unMQ/zh-cn_image_0000002531226024.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4F95E1B7FAE8CF169925ABD9B353579EC8DA78F29CA10E0866403E7463999F8D) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/rjffx4ftQIC97m0ASoOxeA/zh-cn_image_0000002562026007.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=7FD45B65BDD3C5EE7A0E6A955BC5A3437A073E8DDB0BD990ADDEBF325B143B5D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/IPo1iBkvS6uLCEGV_LNB_Q/zh-cn_image_0000002562145993.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C7BEEC127CD3E3AE17B713297B9F15E58C60ADA26276B0527C3A46B427A6A1B0) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ooxHBqleQzWNGjKkF2FVDw/zh-cn_image_0000002531106092.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=04745B01F35BF5B07DC5773614A29A62BE81EA3665F98C8DD462C3359F82BDF7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KGhqJo_3QAS_Oh-wenTI5g/zh-cn_image_0000002531226026.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=3B1882D370AD5618D44673C6451F34F701D6A5545CECF1BDD7174E6857E4600E) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_XSzxZabSN-YmDmdi1hCrg/zh-cn_image_0000002562026009.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C67865DCD3687A300D43D1375F0F3CEC9B7D008771B7EFD446519E6F888104AD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WB-9znnzSlm64Gu2eFjkrA/zh-cn_image_0000002562145995.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=E4B90711010C5CBAA94BE1CF077919E93F86B9F183530FF888882EEE071C5B8C) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/WBMjY2ihQg-MEOrMMy6g6w/zh-cn_image_0000002531106094.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=6E1F6E85F037A0CEC19C391F8981726F0F1A209F2A5CB1B3C3EB317EC7BD3ED0) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/nsZIAqlGT96dM19SAzkqNw/zh-cn_image_0000002531226028.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=5DDC384A6111EC6340F86C63DF42B44A1F14CB7991E8B582A3DB5ED1332BF072) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nOqsIxreR9KnpLVLgnhKGQ/zh-cn_image_0000002562026011.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=E3DA742F3B2A219DF89CB029F0CE6CD494FD31B39E0ABCFE3D5E9DEF0AA9E736) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5FYNVTbHQrq6frtXlBf2Bg/zh-cn_image_0000002562145997.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=53A7526C1E66E9CEFD14013CBD735B588284D8D04938CEE4F5DC25221A1239F4) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/J28u8BgESKKUJy5IEn2l6w/zh-cn_image_0000002531106096.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=464A5CE4EB2CE23D92D20B28B81DA9519609467D41A48306ED0F2459299EC5CB) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/EcVtPbH9R0C3g1ThaKC8lg/zh-cn_image_0000002531226030.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=1D7F7CEDE7D5F822CF0863A0F99298F282732BB345602E226C56D9A0AAAD7C32) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/nEo1ZcJqQFaDTjBbLKjmOw/zh-cn_image_0000002562026013.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=208915C3A86A8C5A5CCBE49747AE9CA25A929BC1F9C8B232F2A5897B6F2F05B9) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KpNxHNSPRgaXImGaK65GdA/zh-cn_image_0000002562145999.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=E610E50C28C6FA0CF122938C82865D84CF19AC27CBC9431D1BF3A84BA8FE652C) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/GoTzTwV9RGWIhvkunMoHlg/zh-cn_image_0000002531106098.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=AE6DF2D161208068EBAE4FB346A02F378351F06203AD45B0A0379A705A0F056E) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/sHyhQyXzQAifR_TyrI4Vfw/zh-cn_image_0000002531226032.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C1F697CAB351B619D774E79D4762264FDA2C1B2CDAF5710ED2AE44B7750862E5) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MNhTmHqRT9KXatitgn76Zg/zh-cn_image_0000002562026015.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=B9F5AC874E44B2369A8535CA8635F8920F3DB4E704CAC654C0DFEE9E8F6294A5) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/DkcCpR9oRmu5BiVFeXFS0w/zh-cn_image_0000002562146001.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=52D7A8F83659843CF858174E28AC8766DE72BCB860ADB4AE644B40B926F66140) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/krxJcgkkRYiAphnKEQ_CZw/zh-cn_image_0000002531106100.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=798448A219BAC68A00D6190790E0D8A6E344C898FB3CCEA7C41167D0C90109CC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/FL8gcSEnSf-s_OviHqLR_g/zh-cn_image_0000002531226034.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=9A8E572F7EF49BE8F742A983C40E968F6A40B667D7845EDED5C62AF4DECDB88A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8XUI3hD0RpiYqEYyjF_Sxw/zh-cn_image_0000002562026017.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=DDB72BCAFF3791042CF74868F4A4382F3C94C96B830EE4F2BA3454D774E89BE7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/XgdWgq_mTbKbE_xSsSC4dg/zh-cn_image_0000002562146003.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=131F056F85A3F80457FAB43462CC5C5CC0882EBEF7D06945E9E1887D29A9D95C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/6sEhEPrbTKiGFAzHel5lcg/zh-cn_image_0000002531106102.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=3539729BE4EDC64E7EB8640A6D5AADC8B0F95841D6D47629C6D8513DEDA1C3F2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/frkhgIhMQaqv15-RjDFFZw/zh-cn_image_0000002531226036.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=33679AED45C74EECD677027DD435999FBD0B2332E120F806B02B8B6E1BC28B6D) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HikxhtJsQsGFat-LngwjKA/zh-cn_image_0000002562026019.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=B0FD247EB3BFCE3BB5745F78F382434FC741837E8FA252E26ECB7020D50D10FE) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zUvT6SjQRpiyjZ3IQqEiuA/zh-cn_image_0000002562146005.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4F3923A1EC123CB836F15EF65E65D3644128553C3D22829B4D8058CA949DF630) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CeUm7lnuQpSO-smMXisXBQ/zh-cn_image_0000002531106104.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4F29031D0A27B7736C72FAE3E0D90B5D06B222D8948891A0CA9E307917419CA3) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QeaoqrtwTI6igmpj9uyT0A/zh-cn_image_0000002531226038.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=2BC4D15896F2C4752F345D8E0BB3C0A02E623A57FBCB278181C85EC204693554) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kPpcvB9sRwabtVzlYpm5Mg/zh-cn_image_0000002562026021.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=04AA7509E9683C61DAD22F07940ADEC75711E30BA0F888BE22062A6FD00F2A14) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ivZ7iPxYQPWAxIWifJ1KFg/zh-cn_image_0000002562146007.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=AD732A70277B58C076A9474ED3F7924E6B4F5F676FF6573656AA2F93D36D4304) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wZQkntFcTiuiHjiFYCTTZw/zh-cn_image_0000002531106106.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=64F282A429D6553F6998C16C207F68DF2A32C4E2A55314300AF914CCAA1B635A) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/h6t6EC9pR5mQ5qTPslcfqg/zh-cn_image_0000002531226040.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=43AC175DA6B9D034DA55774B54ECB313EDD40A53E43FAA220290DAE1C4FEAB79) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MahNlqwbQHShWSkIueJLyg/zh-cn_image_0000002562026023.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=7F2B8A16E53DA7D0E1E3B9045A8197D72BB060F8EBC4B3E05ED4BEA7B311C2A9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VAJaGi20TV2padLk7E_GKw/zh-cn_image_0000002562146009.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=6607CA8F91983A11B3C5A86CFD016204CEB300B40F027B93171DE0086528032E) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/P15cbpUUQMaVkJNUumgzcA/zh-cn_image_0000002531106108.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=CEBEF4BB4313A438FB666F541550164874A6186E96AE9A88231F569DD276A8D9) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/stYmfh7MTCSotVPU3b0SKw/zh-cn_image_0000002531226042.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=68FF61FE5B704A3976AAB2842821DDF36760D8CE991C296DE8BFB7D40FB75930) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dgMA5i3JQauH20lYjohUJQ/zh-cn_image_0000002562026025.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=2613EA8F92CFA31883D5AF85D9D24ABAC3ECA22A76A3ECD754EBC305D98EC03F) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_pjHAW9-TgS-ZydTOuXv8A/zh-cn_image_0000002562146011.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C4C68A4F3A960B16724974D40A3BB32DAD8949169E5E3E07B25FB62C99A75AC4) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bfhAKlkWQM6laLnWgGTeuA/zh-cn_image_0000002531106110.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=B3AA84DDAA0B2B0927D3D48068BFDAC595E56D43B306945DE821FA66FEC59C68) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yag93OgrSHa9z7whde7fMw/zh-cn_image_0000002531226044.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=2F07B3B4CD666E4F7DAB4BA7ADE136DA7F9DAC4E9C6F41B4E9834A817D13E0EE) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/KohZoDqrS7OdvWpHQ07tpA/zh-cn_image_0000002562026027.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=46A54252E6F7592C7D8401C113D9F75B25212AED3082F9024E40E93D9837F3CF) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MDiYMd-7TFSeIUskarK0Mw/zh-cn_image_0000002562146013.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=666C45F24BC31531EB7F3BDD9BE7288A7E8A59E7AB0BEEAD2D36179F04E4DD1F) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/abZ7fuRHSDqfc4LbSqHkzg/zh-cn_image_0000002531106112.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=1DE3BDB2F47F1E414EA88F5EC9B3A0B7050488B8D9A1FFB87345EF01D6477770) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ptAOhSadQ7yoDs1gVRgfuA/zh-cn_image_0000002531226046.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=43671377F2B048F0D2A1316377B2CDF90ADA14E0AF81CC540AB1D15D180BDAD4) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JSfagPGsS6S_8zhTgVwsKQ/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=6BE0A55A700D89A35100EB3AAE477057D3669C49F4E121A9DB3010BE214A8A4F) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Y6CUxnEzQSK7kCZ-zklEmA/zh-cn_image_0000002562146015.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=60E3BC072B2CCD5E92AAB153BB0FD642C3FFB339258EA8ED2C90D5C99BE64C6B) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Oq77nB48Rn-rwgaLlA4hnw/zh-cn_image_0000002531106114.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=86CEA9CE2DE0C67F0E9A099130F91B58E73F1BCDAF4225B95CC363540D9A236C) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/DclcQtdqQmaVCIt9HpJZsw/zh-cn_image_0000002531226048.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=00FE9F4BCD408BCB62D4A3A011F75C5F21784F5A4A26BC33B7E74BD02DFD4F24) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GpzaKbncT16jtF_OeJx7_A/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C20C04239C2C51D8B26A67EEA44C160CACA089EEF226DC1B1BC9E0349FD958BC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QxzfjgwFRa62Z1pq5qpdmQ/zh-cn_image_0000002562026031.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=35E8761E8BBFD418BD5DA28C6736F14335AE6372A7E46423D4651CCFB32BCBEF) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/a1xtMoSrSM-L3ujpOBgSQQ/zh-cn_image_0000002562146017.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4CBC7E97115B4E51DA1C4FED71CDC36E51DB10DEA47122C72DED445BFD6EBC70) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/br2qJVMYQWatQXb6bqYzhQ/zh-cn_image_0000002531106116.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=AC9D5048B884CD4C21F60D5C016CEEFA24B76E2D15E2BFB4FB469A01367F9296) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/pu0gQteMTwSov_uHsxjz4A/zh-cn_image_0000002531226050.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=5245600CC943B69BD61B327E63445EDE56EA6ED8B6B0C2E5C6DA5110D494CA63) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jqO9UvEbS22tFGsO6tVZ-Q/zh-cn_image_0000002562026033.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=079AE19A69820BE84BF7A4C1AB7386E10A72B4446C7874A9D4084F20C51EC41D) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/T6SRypwRScmkghsqNkJkDg/zh-cn_image_0000002562146019.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=6C8335FF9145F3C0F008683891A243CED64343EC242FEC39522B35E51466BD3D) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/F3Xd70RpQlG1Jce7stvITg/zh-cn_image_0000002531106118.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C6AC853F55D65AF0CEC06D30F2546F9ADDE28805E6DD6F6EE24845E14A254FF0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Gy0FtAOFSFWcxls05FN0iw/zh-cn_image_0000002531226052.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C61705B1BF14C6BF6804518D08FC7A381830285E8338468164240B4398FC717E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/jvvU7NrYRxaLc9yNBexMsw/zh-cn_image_0000002562026035.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=F157D53AF44D51A1D075E332F88CC2EDCDF31E8BB17C85D1135C7F64E67C7F5E) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/r32_5jtpTua4n65TVKS7Cg/zh-cn_image_0000002562146021.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=F5DF189A8157FD7C616A74ECBA814D6A5834AAC122A71A7AC8369B37000103C5) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/blbsWIQsT_iu9OGIXDZALA/zh-cn_image_0000002531106120.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=FFA2B8ABD2E70284271478611F57B6236AFAE1676FE9A78ECF4FF0A1ECF387D8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fRlmlHaKRLSh1nuZnALoDg/zh-cn_image_0000002531226054.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4EFCAACC0DBD9D7C457D20A6F950F8BFC89ADEB69846F586CF3FAD9FEC1F31C3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V1mjjTDzQRSsnEbOPpnYCg/zh-cn_image_0000002562026037.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=89DB5DECEB7EBB9F56A69A506C27472FFE1AEB2CE3B1DD0740EF1994FDE138CE) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jxcPM5R7SCmNSusonCc0aQ/zh-cn_image_0000002562146023.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=8AF2CED626A89D1BA1D83ED26C5EA9AEA8F86E1C262AED20060104CB9B39CDE8) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ASfGTvrLSM2FUgj_QVWLyw/zh-cn_image_0000002531106122.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=E6017F3B0EE43AA98A714BEC426881FC8DA725064B7E3A1CF09435B3ACE01811) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wZrjWUDcS-6CHwiYaqccTQ/zh-cn_image_0000002531226056.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=74C3D056B514C3732E0B33F912D773A264DE1153E044D9B7728719F1FB44CC80) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/oASIdz_dQW-hs8rTRL7Tww/zh-cn_image_0000002562026039.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=8F2FB135085B1BAFCA9C37463F236AA6E52EFD806B5DBBDD1A89C8E4CBB0CC39) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/a4oALb_BThaymLQFVTVHaA/zh-cn_image_0000002562146025.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=98A32480A6A6BB6DAA50F309F602A6FF6162482C67CE42E7EE2AE3C748EF8A68) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Jqx8ArIWRX-y9eSLmeVi0w/zh-cn_image_0000002531106124.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=C1EDB11BBE16CA758DFDF7A5941101A575CB208857B700A68539ABA6887D2DC8) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/dBLJHSVeR4avgT_OYAHYEQ/zh-cn_image_0000002531226058.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=E9187143C9C6637E6E22AE1B7BE8BBC8479AA435189578CA5E76B4B97FBD3487) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/8pqRn1cYRVyqwr2newqOFg/zh-cn_image_0000002562026041.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=FF3A96041175C557A986C23529FC92BC94E26A64AC5072145E56C8E3DB18DF0C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4GvJyUxOR2ecmv_IPFCAaQ/zh-cn_image_0000002562146027.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=D0D37532B53F3B8D47742FCFDC1360BA56D28C796C5845CD0C351105C4E46925) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/0f2hKesHSJ-Ob3qcaY1CUQ/zh-cn_image_0000002531106126.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=101E5820745D1C1684070B093797C77E19E4835D83F1AA34672D36D3BB8D887E) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eV69HhchSOaz4n_yF74GVQ/zh-cn_image_0000002531226060.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=3FC22448E2ED04CACA456B30C779C91F52516C613E27B81A2EF0E03ADC7E514D) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/O19y5y2CSI2UGWaXxFS9zQ/zh-cn_image_0000002562026043.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=F6F2786D8F67A8C204DE16750A9DFCA04BD129339B493E19BCA5B36E88AAFCB0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xfQdLA5ZT76oVrC8yvrkpg/zh-cn_image_0000002562146029.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=7EA3A4D401D2284B7418919C8E9A34E14E9A6E660639F964976E596183673FAA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/JfxWl8mOTOyiD1mQfm-OVA/zh-cn_image_0000002531106128.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=29207020C3D6A7C177CB58D0DB5CD7A17D2BF375014CCEB3B39DAF7C93F96551) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IhJHv8ByQuyVSmMGbGKp-g/zh-cn_image_0000002531226062.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=3FA858E6D49D89026C0C18837D3D322B475D8FE60C4A782175057C3082BB196E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yasC9FFJSmCIM0IWuB4eBw/zh-cn_image_0000002562026045.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=2E52374F61BD3270C9021C7DC1A859D87C2704084ED1EE242A65622DD95CAD1D) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-voVzRYRSEiL5g3NmgL9Qw/zh-cn_image_0000002562146031.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=473055E4ECD121F2B14C3CC8BC2FF26DF6A87E8BDEB5DDBC4F26F438D43898FE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CLBScMeeR5ucLe8kiPIUNg/zh-cn_image_0000002531106130.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=4AEDA13223BF1E5953D62DBCACB1C881DD0D99AC221899F3DDA60DB907506758) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/gQmcqygQQ3ClntqIWGsWWA/zh-cn_image_0000002531226064.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=CE40D1C58C41D3A29EEC20AE241312EAE3568A992C2F14EDF77905FF4A1E91CE) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dxkx0DPKTwaohUnKFJSoXw/zh-cn_image_0000002562026047.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=DE9E7D7D31B76E06C642400C1637F27E5DFAAB3363E6C8088B741C274F5294D5) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/IGQREW9FQ4e00wZH6kACWA/zh-cn_image_0000002562146033.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=BC8FEEDE8568EE6FAA42F618E7EF0EC20D182372EDAA2EA58F395AE11B691F63) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nbFet5N3RripaMfi9K9IoA/zh-cn_image_0000002531106132.png?HW-CC-KV=V1&HW-CC-Date=20260321T021441Z&HW-CC-Expire=86400&HW-CC-Sign=5BB3AFEC8B6DA77B8CC672974B13DFD26CD8FBBAE6FF155863F4BDE68D6C8DEE) |
