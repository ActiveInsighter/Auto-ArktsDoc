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
| 系统会把8位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/MsGubtXLQAqnT-XqCdH1RA/zh-cn_image_0000002531226016.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A32EBED13AB6A6BE5A95BEA4F925B6BEB6B9BDC93BCFCD10289DF708055C3FAC) | 系统会把8位的十六进制颜色当#RGBA格式解析并显示。 例如fill="#ff000030"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/hoY8r7ysQSSTZZULQD2SEQ/zh-cn_image_0000002562025999.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=4B89B7B3B36F6E6F08ABE3E4A657FEC5F0521D0A9B0369EE445DCA6C6499FBE8) |

SVG图源属性设置7位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把7位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/mct86Xz-TCWGliRmSFUIIQ/zh-cn_image_0000002562145985.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=060D710BB987BE5E69727EA71A82266CC0EAB4EBE31C1163D44FF83166745931) | 系统会把7位十六进制颜色解析成默认黑色并显示。 例如fill="#BB88990"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zCulBZSMQYSG76AwACd6JA/zh-cn_image_0000002531106084.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=85E5BAD4544954A6FA095F70E8F8D93C6EA2FCFE6279113A56EFB735EA1FCC08) |

SVG图源属性设置4位十六进制格式的颜色时，示例图源和效果如下：

```typescript
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>
```

| 提升前 | 提升后 |
| --- | --- |
| 系统会把4位的十六进制颜色当#ARGB格式解析并显示。 例如fill="#8888"的矩形显示效果。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/S5Bym8PZT6ulIQqqraZkeA/zh-cn_image_0000002531226018.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=9B025E325C801C01E658B8604B612189CEADED75F58E5659D27862B88129DC05) | 系统会把4位的十六进制颜色当#RGBA解析并显示。 例如fill="#0000"的矩形显示效果（全透明）。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/IbEU8DcJQqyJc_jk4419SQ/zh-cn_image_0000002562026001.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C958E9C371E62547F70FC66B5C3C9A31950B497A650CFB49C601A437B4EFC4A7) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eK8rWI09Teu6wCQr5nJPMw/zh-cn_image_0000002562145987.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=FCB81E413237B76C33AAA6A23C554A5311CC5BE4C45AD82E05F89101F65820FA) | Image组件的colorFilter属性只对图源的stroke边框起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hDb7ycCaQae2i8EYs60ulw/zh-cn_image_0000002531106086.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=AD9D963BB15287A776A8C70A9500934B482BC5A8B3E77F5A1C4C93CD4B5B5CFD) | Image组件的colorFilter属性对整个SVG图源起作用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/2y43ulkURVC0VEYhefESkA/zh-cn_image_0000002531226020.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=14E813BFC70BF0B8C7E0D153889A78C371E1411DE46556D652FA528F4F71548A) |

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
| Image组件的fillColor属性只对SVG图源中fill='none'的元素仍然填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/193mMcO-S0KUZk0DgvIpDw/zh-cn_image_0000002562026003.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=318F75D42AC5627ECBF9015D6DC00B7E15E21481A9EBB9E3B85645244C4A645E) | Image组件的fillColor属性对SVG图源中fill='none'的元素不填充颜色。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/JpwqOTFISlm2gQmpBRS3vw/zh-cn_image_0000002562145989.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=75159B266819E13D87366F2FACCE8E65628C6DBE88437D2D7B44C451DDA7B6FA) |

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
| transform属性设置rotate旋转功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="rotate(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Gc1O_NdLS2GUdifGCdLB7A/zh-cn_image_0000002531106088.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C5A5375A43787BD2ED084B1597C0F23E6C2A05FFB3646AA4A2B12481602878FC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_At9qU-eRE-KRKfoWzpuQg/zh-cn_image_0000002531226022.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=2DAA8E019F710E213E388C1EEDD0866733F3FA109C64D917E9217B6691DDF2BF) |
| transform属性设置scale缩放功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="scale(0.77)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XMSf5UlzSby6QPdQC5aipg/zh-cn_image_0000002562026005.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=608AD39479CFE8313C607373BB299909F8719ACD1C2290BF813C86BBD69BF9AD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/-Y_PP3ulTaqz7w3GQ6cMQA/zh-cn_image_0000002562145991.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=495F263A3CC71B43584B24F27D11719033F422E07D99C400E6EC396775A155E5) |
| transform属性设置skewX按x轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewX(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/g95t-8LaQoeEiFO4MZvcWA/zh-cn_image_0000002531106090.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=0321A7E5D2FEBAC02F68CB4EF47D13DEC7B4BBD28B15B8CCA1F8321F0C0DCAE4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/a1PNeI0sQdGbHPkFV_unMQ/zh-cn_image_0000002531226024.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=7389099C0D15223DDD46C5381FF4DEE9A903AF0F5327CAED7D04C329DE3C8536) |
| transform属性设置skewY按y轴倾斜的功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="skewY(30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/rjffx4ftQIC97m0ASoOxeA/zh-cn_image_0000002562026007.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A3B243D4798808B50B33E84451A497FD8F10B3F3D6D549AEE19C2108C9B9758F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/IPo1iBkvS6uLCEGV_LNB_Q/zh-cn_image_0000002562145993.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=1C58FC73E0D6B46608570F8436BF32368E95774CE8F9A125AD316294FE50114F) |
| transform属性设置translate平移功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="translate(30,30)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ooxHBqleQzWNGjKkF2FVDw/zh-cn_image_0000002531106092.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=AA8F370510BE64A787456D90F66BDBFD5D7A4C24635B206102A50034F50D5E26) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KGhqJo_3QAS_Oh-wenTI5g/zh-cn_image_0000002531226026.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=841F6CAD633484C9243F043836BA3FBA79701AE6D37D2F9D6CDF8AA6BF485A44) |
| transform属性链式调用多个功能，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"'。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/_XSzxZabSN-YmDmdi1hCrg/zh-cn_image_0000002562026009.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A4EB5DDF75DA34E4C65681A961195A6FC6B14D14B63D55334FEACAB87144FF79) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WB-9znnzSlm64Gu2eFjkrA/zh-cn_image_0000002562145995.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=FF4ABBB62678A926CB81720A67C28F2ABF909D800F6781BFC32F7F82916526C1) |

### 支持rotate旋转功能局部中心点配置

SVG支持解析rotate旋转的局部中心点功能，例如'rotate(30, -10, -10)'的'30'是旋转角度，后2个参数'-10, -10'是旋转的局部中心点坐标。支持rotate局部中心点前后效果对比如下表格说明。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| SVG基本图形同时配置两个属性： 局部中心点和transform-origin，如'transform="rotate(30, -10, -10)" transform-origin="150 150"'。 | 按照局部中心点：rotate功能的最后2个参数指定的坐标偏移(x,y)作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/WBMjY2ihQg-MEOrMMy6g6w/zh-cn_image_0000002531106094.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C2182C4437B4B1A651AF41AD30B33D2A8BA95AAC7FA699E86E2C3BE887EE3BB7) | 按照全局中心点transform-origin属性指定的坐标偏移(x,y)加局部中心点坐标偏移的和作为变换中心点进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/nsZIAqlGT96dM19SAzkqNw/zh-cn_image_0000002531226028.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=3EE26A1A8491BE6A42590EEACF452B92AD6DD2FB1131CAA305A77BA6420750DF) |

### 支持矩阵(matrix)转换

SVG支持解析transform属性的matrix矩阵转换能力。matrix允许对元素进行复杂的线性变换，包括平移、旋转、缩放和倾斜等，例如matrix(a, b, c, d, e, f)。其中各个字段的元素作用如下：a‌控制元素在x方向上的缩放，b‌控制元素在x方向上的倾斜，c‌控制元素在y方向上的倾斜‌，d‌控制元素在y方向上的缩放‌，e控制元素在x方向上的平移‌，f控制元素在y方向上的平移。

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| transform属性设置matrix矩阵变换，同时配置transform-origin属性。 全局中心点值为图形元素右下角，如:'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"')。 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nOqsIxreR9KnpLVLgnhKGQ/zh-cn_image_0000002562026011.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=3E3E2BB5EA7C4C33B5F3F096118ECA4D78461C1A022DC73C12484D9569396848) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5FYNVTbHQrq6frtXlBf2Bg/zh-cn_image_0000002562145997.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=88EC94CAAEFA45D75486E9A8264813D5E004D7C268C76BDE255EEF1D4359C867) |

### 支持非法值校验

SVG支持校验transform属性非法值的能力。对于transform属性，当设置参数为非法值或者参数个数非法时，按如下表格说明处理：

> **说明**
> SVG图片最终显示效果受Image组件的'objectFit'参数值影响，为了确保SVG图形完整且正确的显示，文档中用例图片都配置了'objectFit(ImageFit.Contain)'，开发者需要根据实际显示效果正确配置objectFit参数。

| SVG场景 | 扩展前 | 扩展后 |
| --- | --- | --- |
| 当变形功能参数为非法值，如rotate旋转功能的角度参数为非法值：'transform="rotate(30deg)"'。 | 按照第一个参数可解析出的数值(30)作为旋转角度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/J28u8BgESKKUJy5IEn2l6w/zh-cn_image_0000002531106096.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C1EB848C5A031803C4BC20A20433EB2BF8C6B476E34889D2B69C0C44DC338FA8) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/EcVtPbH9R0C3g1ThaKC8lg/zh-cn_image_0000002531226030.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=528C73EF407517B0F0D8DABD68C209876A9EB0567F71CD45A9411A60659C02D9) |
| 当变形功能参数为非法值，如rotate旋转功能的局部中心点参数为非法：'transform="rotate(30,abc,abc)"'。 | 按照SVG的ViewPort左上角坐标点(0,0)作为变换中心点，并根据旋转角度30度进行旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/nEo1ZcJqQFaDTjBbLKjmOw/zh-cn_image_0000002562026013.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=0B9E9CD543071DBB5515E652FDCDEDA9E178EAF06AA58AE9791516FABCCC5ED4) | 不做旋转。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KpNxHNSPRgaXImGaK65GdA/zh-cn_image_0000002562145999.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=3E2778A9743F3E39B08C7991D3DF76A9C7F9AB13AAA0E75B376BC5EC494D89D8) |
| 当变形功能参数数量为非法时，如scale功能的参数个数为非法：'transform="scale(0.5, 0.5, 0.5)"'。 | 取前2个合法参数作为x轴和y轴的缩放比例(0.5,0.5)缩放。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/GoTzTwV9RGWIhvkunMoHlg/zh-cn_image_0000002531106098.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=7728529CB7304F9FE38192707DAA6AAE83FA2C08FB53A41D40B2C0D6BA8A0023) | 不做变形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/sHyhQyXzQAifR_TyrI4Vfw/zh-cn_image_0000002531226032.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=20E47585DB03604C2F059FE1549838EC1E57B5E6160AC16385DCDEBEA3785E64) |
| 当链式调用多个变形功能，其中某个功能参数为非法，如'transform="rotate(30) skewX(abc) scale(0.5, 0.5)"'。 | 不处理非法的变形功能skewX，处理合法的变形功能rotate和scale。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MNhTmHqRT9KXatitgn76Zg/zh-cn_image_0000002562026015.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=9405749EF45F91304E3FB686A313BD124D9F17561BC6F7889BF55EFA27914C25) | 所有的变形功能均不处理。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/DkcCpR9oRmu5BiVFeXFS0w/zh-cn_image_0000002562146001.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=41544F90497D47386274A21131BFB850246B6043AD178F6B4D6DEA941AA5C35B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/krxJcgkkRYiAphnKEQ_CZw/zh-cn_image_0000002531106100.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=D9DB5E5AB9C31A3D932FF22EE87AF14B5E5F32BE63E05815B2C7C583980A9004) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/FL8gcSEnSf-s_OviHqLR_g/zh-cn_image_0000002531226034.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=D71842597ABCF6D2DF2F42C14BC1D369E886833E4C8F460E44633FB38C341DF0) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8XUI3hD0RpiYqEYyjF_Sxw/zh-cn_image_0000002562026017.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=091D30C634C8AE179B52830400B5A8D8675B64A803CD307792BAD45567F653B4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/XgdWgq_mTbKbE_xSsSC4dg/zh-cn_image_0000002562146003.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=98DFFCE7A937E92E8AEF5F693B218853FDCB43F22210E64F41F184C7E95F6566) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/6sEhEPrbTKiGFAzHel5lcg/zh-cn_image_0000002531106102.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=0A42F07C70A0E6C3D7FCA8E95B1F4453102B50E6E2FBBC8531728EF6B60FEB48) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/frkhgIhMQaqv15-RjDFFZw/zh-cn_image_0000002531226036.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=85A4C22AAFA96E1FB25B5AD927F1F1FE2CBFE353EFEB213E6A199FE68E7D0266) |

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
| none | 按宽高比最小值进行统一缩放。 同时将SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， 将SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HikxhtJsQsGFat-LngwjKA/zh-cn_image_0000002562026019.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=2B265EE1EA2FC37001E589A645853342CBB0681A3C3F3B50C4F932E428ADE0FE) | 缩放元素的图形内容，使元素的边界完全匹配视图矩形。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/zUvT6SjQRpiyjZ3IQqEiuA/zh-cn_image_0000002562146005.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=5D75B4151F549C4530E00E365AAF6BA178A9864CD06656F93AAF22CC40FD8C6C) |

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
| xMinYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CeUm7lnuQpSO-smMXisXBQ/zh-cn_image_0000002531106104.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=4A70230404928BD0313B6FB5D90E6D996CE4D59DE7AAA15FB86990E8AEAC7EBD) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QeaoqrtwTI6igmpj9uyT0A/zh-cn_image_0000002531226038.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A351C792222FD178FB26012763507C249AAC1F40FBD85DC066C89B1681FF7D98) |
| xMaxYMin meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kPpcvB9sRwabtVzlYpm5Mg/zh-cn_image_0000002562026021.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=B57E882810A863FF6EC7511AB87C23F3A655E2A4A4818AA531A33F271E9CF774) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ivZ7iPxYQPWAxIWifJ1KFg/zh-cn_image_0000002562146007.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=15C84B2E19667A43F8F82D3CC7EB0AE34566486BA7B69FEDC8778BF92A6C1466) |
| xMinYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wZQkntFcTiuiHjiFYCTTZw/zh-cn_image_0000002531106106.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=DFA80DEE3363EBBA92F4F42D8A4558F56D3668EBEC7F9D55A49A50B774F15372) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/h6t6EC9pR5mQ5qTPslcfqg/zh-cn_image_0000002531226040.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=6CC10359C6CE934EC151E031BF16428E181910DCB0D2473077EDD1C3D61A7A58) |
| xMaxYMid meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/MahNlqwbQHShWSkIueJLyg/zh-cn_image_0000002562026023.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=49FEE59C0ED02491A1FB9922DA8A4154F7E225FDE9004D2A51F9FF4983C28F6C) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VAJaGi20TV2padLk7E_GKw/zh-cn_image_0000002562146009.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C4729C1251409A3E0CC5A8A0D98CD11E1F5C033D3588E3B7A501D25F4524093D) |
| xMinYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/P15cbpUUQMaVkJNUumgzcA/zh-cn_image_0000002531106108.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=8A2994F0924F026BDB94BC4A37AD33B236824AB8407A4725D30B4D389876500D) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/stYmfh7MTCSotVPU3b0SKw/zh-cn_image_0000002531226042.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=ECBA408C4F112CB2B338C4863FF7DFC586C9418528905599B5E59D07038D929E) |
| xMaxYMax meet | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dgMA5i3JQauH20lYjohUJQ/zh-cn_image_0000002562026025.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=9E3ED5F12EF448B6C944AEDE1FD837ADA853892810FFD7490FE045F007BAE13B) | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_pjHAW9-TgS-ZydTOuXv8A/zh-cn_image_0000002562146011.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=4C13E55FE512985E653997751CC0606B07E91DFEAB83BE98CD6D90834394782C) |
| xMinYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bfhAKlkWQM6laLnWgGTeuA/zh-cn_image_0000002531106110.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=9B57F7A745CA61290FD22196175705949C2FC4A6DAAAA0A49875D1860125E634) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yag93OgrSHa9z7whde7fMw/zh-cn_image_0000002531226044.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=41273AA072AD9A61654A67A065D519338AABA1D0E184519A9BA141909BBCB632) |
| xMidYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/KohZoDqrS7OdvWpHQ07tpA/zh-cn_image_0000002562026027.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=5DDAB0C68BC080FC3A1631A0C800E71D227BE6F797365ABA7F32030EB1253F9B) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MDiYMd-7TFSeIUskarK0Mw/zh-cn_image_0000002562146013.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=199AD180528A2AAB1D9DD946E474A597BD75ABA5CA2AF4EC5AC4192733DF5A25) |
| xMaxYMin slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/abZ7fuRHSDqfc4LbSqHkzg/zh-cn_image_0000002531106112.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=236507DEABBCC41D1E61653E668E2C1D336252F53D01D5FE2675A2BEBF6F1E53) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值与视图的Y的最小值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ptAOhSadQ7yoDs1gVRgfuA/zh-cn_image_0000002531226046.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=957314817289BBDE7CBE23C2EE7962FB46D727CD0730BB91E3AC58C4E2AE90F3) |
| xMinYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/JSfagPGsS6S_8zhTgVwsKQ/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=7E9D366A88702A7D422BD8CE644266D71BF13461CEFDCCC1FB5A55074FADDB68) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Y6CUxnEzQSK7kCZ-zklEmA/zh-cn_image_0000002562146015.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=986ABE070845BE97C8205239967325CCFF90C43D0A81539316E2B906CAB18B09) |
| xMidYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Oq77nB48Rn-rwgaLlA4hnw/zh-cn_image_0000002531106114.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=3FFC531E654907A5C76CF6F020B62AD4D69CEB3BEB940DA6BC6473014310F9DD) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/DclcQtdqQmaVCIt9HpJZsw/zh-cn_image_0000002531226048.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=CCDA8A04E62E9598D9E29C5A09E56068D83A16FF975B6301D2EBA6FC1F6F22FA) |
| xMaxYMid slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GpzaKbncT16jtF_OeJx7_A/zh-cn_image_0000002562026029.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=484FD2C4FDD560FBBB6C1174D78CE9F489B6A8C6F756EB772450DA4D875A93BC) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QxzfjgwFRa62Z1pq5qpdmQ/zh-cn_image_0000002562026031.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=FE94B6328AD21C38F011592B18D683733E5670CD497E0663EAC958718AF80932) |
| xMinYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/a1xtMoSrSM-L3ujpOBgSQQ/zh-cn_image_0000002562146017.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=E845889AC7CA6DCFE62798B977D8F63B901D34E99C588DE0DEF594A74B2B3EF3) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的最小值与视图的X的最小值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/br2qJVMYQWatQXb6bqYzhQ/zh-cn_image_0000002531106116.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=275D677A35B8BDDABE76AE9AB0ACB9973CAD0F8B3CEFCB2665FAC76DE56390D6) |
| xMidYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/pu0gQteMTwSov_uHsxjz4A/zh-cn_image_0000002531226050.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=686D778E7AB5A0A4EE30C0C534FE7B48B3098FCA4A5B039ADD42629077C49775) | 按宽高比最大值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/jqO9UvEbS22tFGsO6tVZ-Q/zh-cn_image_0000002562026033.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=09B9B98EE67ED5E5BECB7A74D12FA73C6B7AF8A9B76AFC00B920A18B512FAA0A) |
| xMaxYMax slice | 按宽高比最小值进行统一缩放。 SVG元素的viewBox属性的X的中点值与视图的X的中点值对齐， SVG元素的viewBox属性的Y的中点值与视图的Y的中点值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/T6SRypwRScmkghsqNkJkDg/zh-cn_image_0000002562146019.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=188C037123CEF508C09695A4A89F45C06579DABD02C1142E4E4453D902AA6E01) | 按宽高比最大值进行统一缩放。 将SVG元素的viewBox属性的X的最小值+元素的宽度与视图的X的最大值对齐， SVG元素的viewBox属性的Y的最小值+元素的高度与视图的Y的最大值对齐。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/F3Xd70RpQlG1Jce7stvITg/zh-cn_image_0000002531106118.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A3FEFAD7AA646DA6A40CCD10F7EED4FE081C0CB6560DDE468815FA2B6276ECC4) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Gy0FtAOFSFWcxls05FN0iw/zh-cn_image_0000002531226052.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=F8526D036E570A9A492346F377A51A7F0A6F284FCFEC9FEB8CC7B83F5E53C41A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/jvvU7NrYRxaLc9yNBexMsw/zh-cn_image_0000002562026035.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=6E9C6E6FABB91FCE379619A95A94F419813C54BE601AA819EEA9EEA9C4CCA83C) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/r32_5jtpTua4n65TVKS7Cg/zh-cn_image_0000002562146021.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=EFA10CD9D29B0AC5FD10B5F96B5AB4053548DEDC574B36A2A67F76D86BFD5B11) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/blbsWIQsT_iu9OGIXDZALA/zh-cn_image_0000002531106120.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=37B442C22D0EFCB520EBDAD1A1250BC7D1B195F7330ABB5407FC0DD1C4C44A2B) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fRlmlHaKRLSh1nuZnALoDg/zh-cn_image_0000002531226054.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=A973DA73F722717F61DADB709D9685CC9436701DCCE2319D063E3FA029C875DA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V1mjjTDzQRSsnEbOPpnYCg/zh-cn_image_0000002562026037.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=B1BFC658F67881ED3AD775BB85DDE934DB59C4BCA03960D4EDE7399FA78A6360) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jxcPM5R7SCmNSusonCc0aQ/zh-cn_image_0000002562146023.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=854E67F97506CA54D7DDC7DDE3E8D3A3D80D958CC72606507C53497AF070AA89) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ASfGTvrLSM2FUgj_QVWLyw/zh-cn_image_0000002531106122.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=87BC83921669DBAC54A932A1676BBD2B94A8461E4335FD2F9449680A74A31240) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/wZrjWUDcS-6CHwiYaqccTQ/zh-cn_image_0000002531226056.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=685FA1B18A128F03BB2D9FFC93DCC4FF8BB6DA295424B48AA9042D90F39EE807) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/oASIdz_dQW-hs8rTRL7Tww/zh-cn_image_0000002562026039.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=CFAF2015828BD87D3B797173FCC3CCADA8C15047AD5EB4F7BD02672C56AB3351) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/a4oALb_BThaymLQFVTVHaA/zh-cn_image_0000002562146025.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=CF33BB5AE033930C9FC59426C62BF72B6837C0FF0150CAF32BC2DC433D079E5D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Jqx8ArIWRX-y9eSLmeVi0w/zh-cn_image_0000002531106124.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=F839780996ABA016A8FD7617C3ED06335AD43C4731F34FCF9982B38FA5BE290F) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/dBLJHSVeR4avgT_OYAHYEQ/zh-cn_image_0000002531226058.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=B9C6E331776DAEB472C8DFBD4DCC9C20D1DF3DE948FA0E1337908D4164737826) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/8pqRn1cYRVyqwr2newqOFg/zh-cn_image_0000002562026041.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=D68232708B217254C1C6DE6BC723D09C96B5BBBF99E3C2ED8AA1A585E9CB9414) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4GvJyUxOR2ecmv_IPFCAaQ/zh-cn_image_0000002562146027.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=CA263F64CF15B8EE5A70AF4D2383EC4FD7C5AFFD0F8FE37698657FD9C0C3E51A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/0f2hKesHSJ-Ob3qcaY1CUQ/zh-cn_image_0000002531106126.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=4BF735F8BD779BF0096D869CB4681427AC4A7BAAABCD26FAD0AB8E416E914D26) |

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
| 图案不支持重复平铺。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eV69HhchSOaz4n_yF74GVQ/zh-cn_image_0000002531226060.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=B7E131A23FB7AF2DA954895F56CF08AD615DE1E4A5BCC0AE769AC0132C860A50) | 图案支持重复平铺 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/O19y5y2CSI2UGWaXxFS9zQ/zh-cn_image_0000002562026043.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=57070FCD7A820002C121468999E07A70A33B13B3D9BB5EF7D066598F30E2EDB3) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xfQdLA5ZT76oVrC8yvrkpg/zh-cn_image_0000002562146029.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=F77931748962DA64FD7A5E84DCE0FB2F8AFE152C0ABBA671B458EE63DC13AE84) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/JfxWl8mOTOyiD1mQfm-OVA/zh-cn_image_0000002531106128.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=D8C9250AB68B31C24D7F1BC4AB8E8A2895EA61C79DA16CFC02EEFBA468C235A9) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IhJHv8ByQuyVSmMGbGKp-g/zh-cn_image_0000002531226062.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=2642DC0AD43106DED7F719C96E4A540100D1C3151ADEEE1882717550DE050F70) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yasC9FFJSmCIM0IWuB4eBw/zh-cn_image_0000002562026045.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=C5E97A4A531CA3DBC79377D68B1591637AE94A14102C622DDDBED89239532302) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-voVzRYRSEiL5g3NmgL9Qw/zh-cn_image_0000002562146031.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=FE5F5FF6F296C91CCA279249E85B077AD81DDD47858B99F4D389A9BE114847B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CLBScMeeR5ucLe8kiPIUNg/zh-cn_image_0000002531106130.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=948DFD7F3EDFD563554627F3A339DC273E80718FD0541F9F006751F19EAAD17A) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/gQmcqygQQ3ClntqIWGsWWA/zh-cn_image_0000002531226064.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=CAE8AC479F668AC7C3C8853F778EEF5A794DF0747CDCA66538CFED1D6F424334) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dxkx0DPKTwaohUnKFJSoXw/zh-cn_image_0000002562026047.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=BB7AB0940416D6A849893FA3788E8B24DC2A1AC539E2C44A34EE67F3DE9BB0CA) |

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
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/IGQREW9FQ4e00wZH6kACWA/zh-cn_image_0000002562146033.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=DBCF4E0DE5A4ECEE8FBE0A9E0B0334DAC6C6C20C7F84AF9B500B5DB1C780B259) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nbFet5N3RripaMfi9K9IoA/zh-cn_image_0000002531106132.png?HW-CC-KV=V1&HW-CC-Date=20260323T023632Z&HW-CC-Expire=86400&HW-CC-Sign=84CD26DA35AA5DD39B7CE6287675FFC301915570BCAB79E9B2E5813BF7B1CB40) |
