# Image-图片与视频-ArkTS组件-ArkUI（方舟UI框架）-应用框架 - 华为HarmonyOS开发者
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image

Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)、[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)和[DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawabledescriptor10)类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式，不支持apng和svga格式。

> **说明**
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
>
> 使用快捷组合键对Image组件复制时，Image组件必须处于获焦状态，如何获焦请参考[设置组件是否可获焦](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#设置组件是否可获焦)。Image组件默认不获焦，需将[focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)属性设置为true，即可使用Tab键将焦点切换到组件上，再将[focusOnTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusontouch9)属性设置为true，即可实现点击获焦。
>
> 图片格式支持SVG图源，SVG标签文档请参考[SVG标签说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg)。
>
> 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过[onVisibleAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event#onvisibleareachange)事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。
>
> 如果图片加载过程中出现白色块，请参考[Image白块解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution)。如果图片加载时间过长，请参考[预置图片资源加载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance)。

## 需要权限

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

## 子组件

无

## 接口

### Image

Image(src: PixelMap | ResourceStr | DrawableDescriptor)

通过图片数据源获取图片，用于后续渲染展示。

Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。

Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。

Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

> **说明**
> - Image直接传入URL可能会带来的潜在性能问题，例如：(1) 大图加载时无法提前下载，白块显示的时间较长；(2) 小图设置同步加载，在弱网环境下，可能会阻塞UI线程造成冻屏问题；(3) 在快速滑动的瀑布流中，无法提前对即将要显示的图片进行下载，导致滑动白块较多。不同场景下，性能问题会有不同的表现，建议将网络下载部分与Image的显示剥离，可提前下载或者异步下载。如果图片加载过程中出现白色块，请参考[Image白块解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution)。如果图片加载时间过长，请参考[预置图片资源加载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance)。
> - src由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。
> - 当Image组件入参为[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型时，只有当PixelMap对象发生变化（即指向一个新的PixelMap实例），Image组件才能感知到数据的变化。仅修改PixelMap对象的内容（如像素值）而不更换对象引用，无法触发数据变化的感知。
> - Image组件入参为Base64字符串时，Base64字符串通用格式为data:image/subtype;base64,Base64EncodedData，其中subtype为类型声明，Base64EncodedData为数据对应的base64编码，其他为固定字符串。例如：png图像对应的入参为data:image/png;base64,iVBORw0KGgo...。 1. image/subType用于声明数据内容的类型。Image组件不会强制校验声明的类型与Base64解码后的实际图片格式是否完全一致。在部分场景下，即使声明的类型与真实格式不一致，图片仍可能正常显示。为避免未来行为变化或未知问题，建议始终保持类型与实际图片格式一致。 2. Image组件不支持data:image/*;base64,Base64EncodedData的通配写法，subType必须显式声明具体的图片类型。 3. Image组件不支持通过Base64字符串形式加载SVG图片。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#pixelmap) | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)| [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawabledescriptor10) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。 1. PixelMap格式为像素图，常用于图片编辑的场景。 2. ResourceStr包含Resource和string格式。 string格式可用于加载网络图片和本地图片，常用于加载网络图片。当[使用相对路径引用本地图片](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例25使用相对路径显示图片)时，不支持跨包/跨模块调用该Image组件，建议使用Resource格式来管理需全局使用的图片资源。 从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resource目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable 设置为true，详见[resOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356)中相关介绍。 - 支持Base64字符串。 - 传入的字符串为https网络图片地址时，建议参考[示例2下载与显示静态网络图片](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例2下载与显示静态网络图片)。 - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。 Resource格式可以跨包/跨模块访问资源文件，是访问本地图片的推荐方式，具体示例参考[跨HAP/HSP包应用资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#跨haphsp包应用资源)。 3. 当传入资源id或name为普通图片时，生成DrawableDescriptor对象。传入[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)类型可播放PixelMap数组动画。 **说明：** - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。 - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |

### Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)

src新增[ImageContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagecontent12)类型，可指定对应的图形内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#pixelmap) | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)| [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawabledescriptor10)| [ImageContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagecontent12) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。 PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#image-1)的src参数说明。 传入[ImageContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagecontent12)类型，指定图像内容。 **说明：** - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。 - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |

### Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)

Image新增[imageAIOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageaioptions12)参数，为组件设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#pixelmap) | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)| [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawabledescriptor10) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#加载图片资源)。 PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#image-1)的src参数说明。 **说明：** - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。 - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |
| imageAIOptions | [ImageAIOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageaioptions12) | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

## 属性

属性的详细使用指导请参考[添加属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display#添加属性)。除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

> **说明**
> Image组件不支持设置通用属性[foregroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color#foregroundcolor)，可以通过Image组件的[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor)属性设置填充颜色。

### alt

alt(value: string | Resource | PixelMap)

设置图片加载过程中显示的占位图。

占位图支持使用[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)12+ | 是 | 设置图片加载过程中显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型图片，不支持网络图片。 - 支持Base64字符串。 - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。 默认值：null 由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。 |

### alt22+

alt(src: ResourceStr | PixelMap | ImageAlt)

设置图片加载过程中和加载失败时的占位图。

> **说明**
> 通过[ImageAlt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagealt22)配置占位图时，Image会根据用户配置的加载过程中和加载失败的占位图源生效，未配置时默认不显示。

占位图支持使用[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)| [ImageAlt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagealt22) | 是 | 设置图片加载过程中和加载失败时的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型图片，不支持网络图片。 - 支持Base64字符串。 - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。 |

### objectFit

objectFit(value: ImageFit)

设置图片的填充效果。未通过该接口设置时，默认为ImageFit.Cover，保持宽高比进行缩小或者放大。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagefit) | 是 | 图片的填充效果。 |

### imageMatrix15+

imageMatrix(matrix: ImageMatrix)

设置图片的变换矩阵。通过[ImageMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagematrix15对象说明)对象使用平移、旋转、缩放等函数，实现宫格缩略图的最佳呈现。SVG类型图源不支持该属性。

设置[resizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizable11)、[objectRepeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectrepeat)属性时，该属性设置不生效。该属性只针对图源做处理，不会触发Image组件的回调事件。

该属性与[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性强关联，仅在[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性设置为ImageFit.MATRIX时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [ImageMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagematrix15对象说明) | 是 | 图片的变换矩阵。 |

### objectRepeat

objectRepeat(value: ImageRepeat)

设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRepeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagerepeat) | 是 | 图片的重复样式。 默认值：ImageRepeat.NoRepeat |

### interpolation

interpolation(value: ImageInterpolation)

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageInterpolation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageinterpolation) | 是 | 图片的插值效果。 默认值：ImageInterpolation.Low 设置undefined时，取值为ImageInterpolation.None。 |

### renderMode

renderMode(value: ImageRenderMode)

设置图片的渲染模式。SVG类型图源不支持该属性。

设置[ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)时，该属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRenderMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagerendermode) | 是 | 图片的渲染模式为原色或黑白。 默认值：ImageRenderMode.Original |

### sourceSize

sourceSize(value: ImageSourceSize)

设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。SVG类型图源和PixelMap资源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageSourceSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagesourcesize18对象说明) | 是 | 图片解码尺寸参数，降低图片的分辨率，常用于需要让图片显示尺寸比组件尺寸更小的场景。和[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)接口的ImageFit.None配合使用时可在组件内显示小图。 |

### matchTextDirection

matchTextDirection(value: boolean)

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片是否跟随系统语言方向。 默认值：false，false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。 |

### fitOriginalSize

fitOriginalSize(value: boolean)

设置图片的显示尺寸是否跟随图源尺寸。

图片组件已设置width、height属性时，fitOriginalSize属性不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片的显示尺寸是否跟随图源尺寸。 默认值：false **说明：** 当不设置fitOriginalSize或者设置fitOriginalSize为false时，组件显示大小不跟随图源大小。 当设置fitOriginalSize为true时，组件显示大小跟随图源大小。 |

### fillColor

fillColor(value: ResourceColor)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 是 | 设置填充颜色。 **说明：** 默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。 从API version 21开始，当[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。当supportSvg2设置为false时，fillColor生效，替换SVG图片中所有可绘制元素的填充颜色。 |

### fillColor15+

fillColor(color: ResourceColor|ColorContent)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)。如果想重置填充颜色可以传入[ColorContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorcontent15)类型。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)|[ColorContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorcontent15) | 是 | 设置填充颜色。 **说明：** 默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。 从API version 21开始，当[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。 |

### fillColor20+

fillColor(color: ResourceColor|ColorContent|ColorMetrics)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)。如果想重置填充颜色可以传入[ColorContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorcontent15)类型。支持通过传入[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)|[ColorContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorcontent15)|[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12) | 是 | 设置填充颜色。 **说明：** 默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。 从API version 21开始，当[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。 |

### autoResize

autoResize(value: boolean)

设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失，因此可能会导致图片质量的下降（如：出现锯齿），这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。

原图尺寸和显示尺寸不匹配时，图片都会出现些许的失真、模糊。最佳清晰度配置建议：

图片缩小显示时：.autoResize(false) + .interpolation(.Medium)

图片放大显示时：.interpolation(.High)

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)和SVG时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片解码过程中是否对图源自动缩放。设置为true时，组件会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。如原图大小为800x1200，而显示区域大小为200x200，则图片会降采样解码到200x300的尺寸（实际计算过程中会依赖缩放和填充类型的配置，从而得到的计算结果会有差异），从而大幅度节省图片占用的内存。 默认值：false，false表示关闭图源自动缩放，true表示开启图源自动缩放。 |

### syncLoad8+

syncLoad(value: boolean)

设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

如果加载图片时出现闪烁，设置syncLoad为true。详情请参见[并发优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization#section715115119192)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。 默认值：false，false表示异步加载图片，true表示同步加载图片。 阻塞主线程超过6s将导致AppFreeze，具体参考[AppFreeze（应用冻屏）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)。 |

### copyOption9+

copyOption(value: CopyOptions)

设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。SVG图片不支持复制。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#copyoptions9) | 是 | 图片是否可复制。 默认值：CopyOptions.None |

### colorFilter9+

colorFilter(value: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

设置该属性时，[renderMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#rendermode)属性设置不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#colorfilter9) | [DrawingColorFilter12+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawingcolorfilter12) | 是 | 1. 给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。 2. 从API version12开始支持@ohos.graphics.drawing的ColorFilter类型作为入参。 **说明：** API version 11及之前，SVG类型图源不支持该属性。 从API version 12开始，该接口中的DrawingColorfilter类型支持在元服务中使用。其中，SVG类型的图源只有设置了stroke属性（无论是否有值）才会生效。 从API version 21开始，当[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)属性设置为true时，colorFilter属性对整个SVG图源起作用。 |

颜色滤镜通过一个4x5的矩阵来设置图像的颜色滤镜，矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。

当矩阵对角线值为1，其余值为0时，保持图片原有色彩。

**计算规则：**

如果输入的滤镜矩阵如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/5m7pTLo_ToOis4u_cz9eVA/zh-cn_image_0000002562715707.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=505CF4CB221F0F0B14C5BD3C6AE9A7219BD8C6CA9D40409737723F141E7579EA)

像素点为[R, G, B, A]，色值的范围[0, 255]

则过滤后的颜色为 [R’, G’, B’, A’]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/9zce8qSHTv6DCmu8o2x3-A/zh-cn_image_0000002531635836.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=E06B9DBDFDCCE2882BBCFA5E42FAEBDFFE08B9E0F5A38E69C160A061AB27D021)

该属性的具体使用可以参考[示例9](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例9为图像设置颜色滤镜效果)。

### draggable9+

draggable(value: boolean)

设置组件默认拖拽效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 组件默认拖拽效果，设置为true时，组件可拖拽，绑定的长按手势不生效。 API version 9及之前，默认值为false。API version 10及之后，默认值为true。 若用户需要设置自定义手势，则需要将draggable设置为false。设置为false之后，拖拽类事件不再触发。 |

### enableAnalyzer11+

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。具体使用指导请参考[AI识图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-imageanalyzer)。

不能和[overlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay#overlay)属性同时使用，两者同时设置时overlay中[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)属性将失效。该特性依赖设备能力。

分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)进行分析，目前仅支持[RGBA_8888](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#pixelmapformat7)类型，使用方式见[示例5开启图像AI分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例5开启图像ai分析)。

[alt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#alt)占位图不支持分析，[objectRepeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectrepeat)属性仅在取值为ImageRepeat.NoRepeat时支持分析，隐私遮罩属性[obscured](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-obscured#obscured)打开时不支持分析。

基于完整原始图像进行分析，设置[clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)、[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)、[borderRadius](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#borderradius)、[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)和[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性导致图像显示不完整，或使用[renderMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#rendermode)设置蒙层，仍基于完整原始图像进行分析。 [copyOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#copyoption9)属性不影响AI分析功能。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时设置该属性不生效。

> **说明**
> - 需要配置权限：ohos.permission.INTERNET。
> - 从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Image组件是否支持AI分析。 设置为true时，Image组件支持AI分析。设置为false时，Image组件不支持AI分析。 默认值：false |

### resizable11+

resizable(value: ResizableOptions)

设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。

设置合法的 [ResizableOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizableoptions11) 时，objectRepeat属性和orientation属性设置不生效。

当设置 top +bottom 大于原图的高或者 left + right 大于原图的宽时 [ResizableOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizableoptions11) 属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)和SVG时设置该属性不生效。

> **说明**
> 从API version 20开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResizableOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizableoptions11) | 是 | 图像拉伸时可调整大小的图像选项。 |

### privacySensitive12+

privacySensitive(supported: boolean)

设置是否支持卡片敏感隐私信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | 是 | 是否支持卡片敏感隐私信息。 默认值为false，表示不支持卡片敏感隐私信息，当设置为true时，隐私模式下图片将显示为半透明底板样式。 **说明：** 设置null则不敏感。 进入隐私模式需要卡片框架支持。 |

### dynamicRangeMode12+

dynamicRangeMode(value: DynamicRangeMode)

设置期望展示的图像动态范围。SVG类型图源不支持该属性。

**设备行为差异：** 该接口在手机、PC/2in1和Tablet设备中可正常生效，在其他设备类型中无效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DynamicRangeMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#dynamicrangemode12枚举说明) | 是 | 图像显示的动态范围。 默认值：DynamicRangeMode.STANDARD |

### orientation14+

orientation(orientation: ImageRotateOrientation)

设置图像内容的显示方向。

该属性对[alt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#alt)占位图不生效。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [ImageRotateOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagerotateorientation14) | 是 | 图像内容的显示方向。 仅支持静态位图的显示。 如果需要显示携带旋转角度信息或翻转信息的图片，建议使用ImageRotateOrientation.AUTO进行设置。 默认值：ImageRotateOrientation.UP 设置为undefined或null时，取值为ImageRotateOrientation.AUTO。 |

### hdrBrightness19+

hdrBrightness(brightness: number)

设置组件在显示HDR图片时的亮度。

SVG类型图源不支持该属性。

该属性与[dynamicRangeMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#dynamicrangemode12)属性同时设置时，[dynamicRangeMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#dynamicrangemode12)属性不生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 用于调整组件展示HDR图片的亮度，该接口仅对HDR图源生效。 默认值：1.0 取值范围：[0.0，1.0]，小于0和大于1.0时取1.0。0表示图片按照SDR亮度显示，1.0表示图片按照当前允许的最高HDR亮度显示。 |

### supportSvg221+

supportSvg2(enable: boolean)

开启或关闭[SVG标签解析能力增强功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities)，开启后相关SVG图片显示效果会有变化。

Image组件创建后，不支持动态修改该属性的值。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 控制是否开启SVG标签解析能力增强功能。 默认值：false true：支持SVG解析新能力；false：保持原有SVG解析能力。 |

### contentTransition21+

contentTransition(transition: ContentTransitionEffect)

图片内容发生变化时，触发过渡动效。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | [ContentTransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#contenttransitioneffect21对象说明) | 是 | 过渡动效的类型。 其中取值为ContentTransitionEffect.OPACITY表示淡入淡出效果，取值为ContentTransitionEffect.IDENTITY表示无动画效果。 默认值：ContentTransitionEffect.IDENTITY 设置为undefined或null时，取默认值ContentTransitionEffect.IDENTITY。 **说明**：对动态图片资源不生效。 |

## ImageContent12+

指定图像内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EMPTY | 0 | 空图像。 |

## ImageInterpolation

图片的插值效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | 最近邻插值。 |
| Low | 1 | 双线性插值。 |
| Medium | 2 | MipMap插值。 |
| High | 3 | Cubic插值，插值质量最高，可能会影响图片渲染的速度。 |

## ImageRenderMode

图片的渲染模式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Original | 0 | 原色渲染模式。 |
| Template | 1 | 黑白渲染模式。 |

## ResizableOptions11+

图像拉伸时可调整大小的图像选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slice | [EdgeWidths](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edgewidths9) | 否 | 是 | 边框宽度类型，用于描述组件边框不同方向的宽度。 **说明：** 只有当bottom和right同时大于0时，该属性生效。 当设置了top时，图片顶部拉伸，图片的像素值保持不变。 当设置了right时，图片右部拉伸，图片的像素值保持不变。 当设置了bottom时，图片底部拉伸，图片的像素值保持不变。 当设置了left时，图片左部拉伸，图片的像素值保持不变。 每个方向的宽度默认值为0，传入数字时默认单位为vp。 设置了EdgeWidths后的效果如图1（设置EdgeWidths效果图）所示。 |
| lattice12+ | [DrawingLattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawinglattice12) | 否 | 是 | 矩形网格对象。 **说明：** 通过@ohos.graphics.drawing的[createImageLattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice#createimagelattice12)接口创建Lattice类型作为入参。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格图像是固定的，不会被拉伸。其他位置的网格图像会根据slice进行拉伸。 该参数对[backgroundImageResizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundimageresizable12)接口不生效。 传入数字时默认单位为px。 |

**图1** 设置EdgeWidths效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/s22cuKYVTB6UY3hF8gPhlw/zh-cn_image_0000002562715723.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=F0293E204F90FA6E42581F6ED60AB08E3FFEBB980C644EC5F5A09944E2274E2E)

## ImageAlt22+

设置图片占位图。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placeholder | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 否 | 是 | 加载过程中的占位图。 |
| error | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 否 | 是 | 加载失败的占位图。 |

## DynamicRangeMode12+枚举说明

期望展示的图像动态范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH | 0 | 不受限动态范围，最大限度进行图片提亮。 |
| CONSTRAINT | 1 | 受限动态范围，受限进行图片提亮。 |
| STANDARD | 2 | 标准动态范围，不进行图片提亮。 |

## ImageRotateOrientation14+

期望的图像内容显示方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。 [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)和[DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#drawabledescriptor10)类型的图片不包含头信息，调用该接口时图片显示效果不变化。 **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Wv1m54lUTra9neLOGUYf1A/zh-cn_image_0000002531635852.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=9DF303E7450B12FBCCEB9445E56768C17C4BDC5D3CBD6D43C548CF07026B36F2) |
| UP | 1 | 默认按照当前图片的像素数据进行显示，不做任何处理。 **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RIGHT | 2 | 将当前图片顺时针旋转90度后显示。 **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/9DKrNrUfQfm8Dkl4bA7dew/zh-cn_image_0000002531795788.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=04DD1F6EB361382BFD1BFD87463AD1A37EE6E84A5DD6B7E945A27B9B15CCEBDE) |
| DOWN | 3 | 将当前图片顺时针旋转180度后显示。 **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/XDrMNvdbTp2RbnSMLHuFyw/zh-cn_image_0000002562555753.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=F2337AF4EE3E29FDB8AA5358D122013D8D57E05116387B0AA5574A418222AE8E) |
| LEFT | 4 | 将当前图片顺时针旋转270度后显示。 **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Izx2XM1NR0KDDqRHjp3bBA/zh-cn_image_0000002562715725.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=2281F68A6F5BA4D7770D2EB0B682551D9437FA2D9F05C6F6BFD5DEF26E08122C) |
| UP_MIRRORED20+ | 5 | 将当前图片水平翻转后显示。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/qyM83_XnRl2HX5otbWYTNg/zh-cn_image_0000002531635854.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=3DF8B466909FA67DCA6BE0AA27F89999C54235B989FDE227298AF646F13C5B63) |
| RIGHT_MIRRORED20+ | 6 | 将当前图片水平翻转再顺时针旋转90度后显示。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/D9vV8QgEQNyU7lc286qrRw/zh-cn_image_0000002531795790.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=BA235841E6A98742E0C24DC9A9C00FBB9F8853BADCCF44F4B05BB624CC25FA81) |
| DOWN_MIRRORED20+ | 7 | 将当前图片垂直翻转后显示。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/20Tba8PAT7W_j894OG1xDw/zh-cn_image_0000002562555755.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=2E6519F7FFF5CF9E801E5085A6A047D6CAADCFC6355DC8CAB8AB70736E22CD1A) |
| LEFT_MIRRORED20+ | 8 | 将当前图片水平翻转再顺时针旋转270度后显示。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/LocGyevwTzO3a2la4zgy8Q/zh-cn_image_0000002562715727.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=401B3B130903A57B04084A8692317331EDAC0E7AAA80F8D1C42BCF28AFB416FF) |

## ImageSourceSize18+对象说明

图片解码尺寸。

> **说明**
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | number | 否 | 否 | 图片解码尺寸宽度。 单位：vp **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | number | 否 | 否 | 图片解码尺寸高度。 单位：vp **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## DrawableDescriptor10+

type DrawableDescriptor = DrawableDescriptor

作为Image组件的入参对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#drawabledescriptor) | 返回一个DrawableDescriptor对象。 |

## DrawingColorFilter12+

type DrawingColorFilter = ColorFilter

颜色滤波器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-colorfilter) | 返回一个颜色滤波器。 |

## DrawingLattice12+

type DrawingLattice = Lattice

将图片按照矩形网格进行划分。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Lattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice) | 返回一个矩阵网格对象。 |

## ImageMatrix15+对象说明

type ImageMatrix = Matrix4Transit

当前的矩阵对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4#matrix4transit) | 返回当前的矩阵对象。 |

## ColorContent15+

指定颜色填充内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ORIGIN | ColorContent | 是 | 否 | 重置[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor)接口，效果上与不设置[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor)一致。 |

## 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

### onComplete

onComplete(callback: (event?: { width: number, height: number, componentWidth: number, componentHeight: number, loadingStatus: number,contentWidth: number, contentHeight: number, contentOffsetX: number, contentOffsetY: number }) => void)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 图片的宽。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| height | number | 是 | 图片的高。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| componentWidth | number | 是 | 组件的宽。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| componentHeight | number | 是 | 组件的高。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| loadingStatus | number | 是 | 图片加载成功的状态值。 **说明：** 返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。 **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| contentWidth10+ | number | 是 | 图片实际绘制的宽度。 单位：px **说明：** 仅在loadingStatus返回1时有效。 **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentHeight10+ | number | 是 | 图片实际绘制的高度。 单位：px **说明：** 仅在loadingStatus返回1时有效。 **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentOffsetX10+ | number | 是 | 实际绘制内容相对于组件自身的x轴偏移。 单位：px **说明：** 仅在loadingStatus返回1时有效。 **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentOffsetY10+ | number | 是 | 实际绘制内容相对于组件自身的y轴偏移。 单位：px **说明：** 仅在loadingStatus返回1时有效。 **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |

### onError9+

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageerrorcallback9) | 是 | 图片加载异常时触发的回调。 **说明：** 建议开发者使用此回调，可快速确认图片加载失败时的具体原因，参见[ImageError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageerror9)的错误信息详细介绍。 |

### onFinish

onFinish(event: () => void)

当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。

仅支持SVG格式的图片。当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。 |

## ImageErrorCallback9+

type ImageErrorCallback = (error: ImageError) => void

图片加载异常时触发此回调。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [ImageError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageerror9) | 是 | 图片加载异常时触发回调的返回对象。 |

## ImageError9+

图片加载异常时触发回调的返回对象。

当组件的参数类型为[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentWidth | number | 否 | 否 | 组件的宽。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| componentHeight | number | 否 | 否 | 组件的高。 单位：px **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| message10+ | string | 否 | 否 | 报错信息。 **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| error20+ | [BusinessError<void>](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#businesserror20) | 否 | 是 | 图片加载异常返回的报错信息，其中code为错误码，message为错误信息。报错信息请参考以下错误信息的详细介绍。 默认值：{ code : -1, message : "" } **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。 **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## BusinessError20+

type BusinessError<T = void> = BusinessError<T>

图片加载异常返回的错误信息。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [BusinessError<T>](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror) | 图片加载异常返回的错误信息。 |

以下是错误信息的详细介绍：ImageError的error属性为错误信息对象，其中code为错误码，message为错误信息。

| 错误码ID | 错误信息 | 错误信息发生阶段 | 图片加载类型 |
| --- | --- | --- | --- |
| 101000 | unknown source type. | 数据加载 | 未知类型 |
| 102010 | sync http task of uri cancelled. | 数据加载 | 网络文件 |
| 102011 | sync http task of uri failed. | 数据加载 | 网络文件 |
| 102012 | async http task of uri cancelled. | 数据加载 | 网络文件 |
| 102013 | async http task of uri failed. | 数据加载 | 网络文件 |
| 102030 | wrong code format. | 数据加载 | base64字符串文件 |
| 102031 | decode base64 image failed. | 数据加载 | base64字符串文件 |
| 102050 | path is too long. | 数据加载 | 沙箱文件 |
| 102051 | read data failed. | 数据加载 | 沙箱文件 |
| 102070 | get image data by name failed. | 数据加载 | 资源文件 |
| 102071 | get image data by id failed. | 数据加载 | 资源文件 |
| 102072 | uri is invalid. | 数据加载 | 资源文件 |
| 102090 | uri is invalid. | 数据加载 | 包内文件 |
| 102091 | get asset failed. | 数据加载 | 包内文件 |
| 102110 | open file failed. | 数据加载 | 媒体库文件 |
| 102111 | get file stat failed. | 数据加载 | 媒体库文件 |
| 102112 | read file failed. | 数据加载 | 媒体库文件 |
| 102130 | decoded data is empty. | 数据加载 | 媒体库缩略图文件 |
| 102131 | load shared memory image data timeout. | 数据加载 | 共享内存文件 |
| 103100 | make svg dom failed. | 数据加载 | 矢量图文件 |
| 103200 | image data size is invalid. | 数据加载 | 位图文件 |
| 111000 | image source create failed. | 数据解码 | 位图文件 |
| 111001 | pixelmap create failed. | 数据解码 | 位图文件 |

## 示例

### 示例1（加载基本类型图片）

该示例通过传入[Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)资源，加载png、gif、svg和jpg等基本类型的图片。

```typescript
@Entry
@Component
struct ImageExample1 {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {

          Image($r('app.media.ic_camera_master_ai_leaf'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
        Row() {

          Image($r('app.media.ic_camera_master_ai_clouded'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })

          Image($r('app.media.ic_public_favor_filled'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/D-boLbdeRhO-uDxXbZ8D4g/zh-cn_image_0000002531635856.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=AFC8850B4619F9EEA202C548FF8C3755148C68F7A5BF55A1A98589F796EC4177)

### 示例2（下载与显示静态网络图片）

加载网络图片时，默认网络超时是5分钟，建议使用alt配置加载时的占位图。使用[HTTP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request)工具包发送网络请求，接着将返回的数据解码为Image组件中的PixelMap，加载gif到PixelMap时，gif显示为静态图。图片开发可参考[Image Kit简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview)。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```typescript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample2 {
  @State pixelMapImg: PixelMap | undefined = undefined;

  aboutToAppear() {
    this.requestImageUrl('https://www.example.com/xxx.png');
  }

  requestImageUrl(url: string) {
    http.createHttp().request(url, (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}`);
      } else {
        let imgData: ArrayBuffer = data.result as ArrayBuffer;
        console.info(`request image success, size: ${imgData.byteLength}`);
        let imgSource: image.ImageSource = image.createImageSource(imgData);
        class sizeTmp {
          height: number = 100;
          width: number = 100;
        }
        let options: Record<string, number | boolean | sizeTmp> = {
          'alphaType': 0,
          'editable': false,
          'pixelFormat': 3,
          'scaleMode': 1,
          'size': { height: 100, width: 100 }
        }
        imgSource.createPixelMap(options).then((pixelMap: PixelMap) => {
          console.error('image createPixelMap success');
          this.pixelMapImg = pixelMap;
          imgSource.release();
        }).catch(() => {
          imgSource.release();
        })
      }
    })
  }

  build() {
    Column() {
      Image(this.pixelMapImg)

        .alt($r('app.media.img'))
        .objectFit(ImageFit.None)
        .width('100%')
        .height('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/rADTMAPhT26ALvMUf2oxFQ/zh-cn_image_0000002531795792.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=B875F6168C2F30AC6CC9838BCB5444B0118CEC45853A327359E0438A1AEB204E)

### 示例3（下载与显示网络gif图片）

该示例使用[cacheDownload.download](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request-cachedownload#cachedownloaddownload)接口下载网络gif图片。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

```typescript
import { cacheDownload } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State src: string = 'https://www.example.com/xxx.gif';

  async aboutToAppear(): Promise<void> {

    let options: cacheDownload.CacheDownloadOptions = {};
    try {

      cacheDownload.download(this.src, options);
      console.info(`success to download the resource. `);
    } catch (err) {
      console.error(`Failed to download the resource: code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {

      Image(this.src)
        .width(100)
        .height(100)
        .objectFit(ImageFit.Cover)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例4（为图片添加事件）

该示例为图片添加[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)和[onFinish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#onfinish)事件。

```typescript
@Entry
@Component
struct ImageExample3 {

  private imageOne: Resource = $r('app.media.earth');

  private imageTwo: Resource = $r('app.media.star');

  private imageThree: Resource = $r('app.media.moveStar');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageThree;
  build(){
    Column(){

      Image(this.src)
        .width(100)
        .height(100)
        .onClick(() => {
          this.src = this.imageTwo;
        })

      Image(this.src2)
        .width(100)
        .height(100)
        .onFinish(() => {

          this.src2 = this.imageOne;
        })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/wuNl7xvQTXODyh7xW6aUUw/zh-cn_image_0000002562555757.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=C8696E6B3865A8627971CE6516278EA9ED1B1FD7D6E151157A7D12D2A4E3D3B9)

### 示例5（开启图像AI分析）

该示例使用[enableAnalyzer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#enableanalyzer11)接口开启图像AI分析。

```typescript
import { image } from '@kit.ImageKit'

@Entry
@Component
struct ImageExample4 {
  @State imagePixelMap: image.PixelMap | undefined = undefined
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  async aboutToAppear() {
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.img'))
  }

  build() {
    Column() {
      Image(this.imagePixelMap, this.options)
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
        .width(200)
        .height(300)
        .margin({left: 10})
      Button('getTypes')
        .onClick(() => {
          this.aiController.getImageAnalyzerSupportTypes()
        })
    }
  }
  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent({
      bundleName: resource.bundleName,
      moduleName: resource.moduleName,
      id: resource.id
    })
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength))
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    })
    await imageSource.release()
    return createPixelMap
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/CMtAFzauT8yc-ju4JF48Mw/zh-cn_image_0000002562715729.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=C3A1CFFE9B729F148090B02662327C174CE2308893B98EA353085D933A5C97F1)

### 示例6（通过slice拉伸图片）

该示例通过[resizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizable11)属性的slice选项，调整不同方向对图片进行拉伸。

```typescript
@Entry
@Component
struct Index {
  @State top: number = 10;
  @State bottom: number = 10;
  @State left: number = 10;
  @State right: number = 10;

  build() {
    Column({ space: 5 }) {

      Image($r('app.media.landscape'))
        .width(200).height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      Image($r('app.media.landscape'))
        .resizable({
          slice: {

            left: `${this.left}px`,
            right: `${this.right}px`,
            top: `${this.top}px`,
            bottom: `${this.bottom}px`
          }
        })
        .width(200)
        .height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      Row() {
        Button('add top to ' + this.top).fontSize(10)
          .onClick(() => {
            this.top += 10;
          })
        Button('add bottom to ' + this.bottom).fontSize(10)
          .onClick(() => {
            this.bottom += 10;
          })
      }

      Row() {
        Button('add left to ' + this.left).fontSize(10)
          .onClick(() => {
            this.left += 10;
          })
        Button('add right to ' + this.right).fontSize(10)
          .onClick(() => {
            this.right += 10;
          })
      }

    }
    .justifyContent(FlexAlign.Start).width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/vct8mRUETuOw6lgMN3OMqQ/zh-cn_image_0000002531635858.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=C66CF40C188D529412B11EF34044887EF0F1799CE026FFB9BD35D9D412A16596)

### 示例7（通过lattice拉伸图片）

该示例使用[resizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizable11)属性的lattice选项，使用矩形网格对象对图片进行拉伸。

```typescript
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct drawingLatticeTest {
  private xDivs: Array<number> = [1, 2, 200];
  private yDivs: Array<number> = [1, 2, 200];
  private fXCount: number = 3;
  private fYCount: number = 3;
  private drawingLatticeFirst: DrawingLattice =
    drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.fXCount, this.fYCount);

  build() {
    Scroll() {
      Column({ space: 10 }) {
        Text('Original Image').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {

          Image($r('app.media.mountain'))
            .width(260).height(260)
        }.width('100%')

        Text('Resize by lattice').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {

          Image($r('app.media.mountain'))
            .objectRepeat(ImageRepeat.X)
            .width(260)
            .height(260)
            .resizable({
              lattice: this.drawingLatticeFirst
            })
        }.width('100%')
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/eHQizf-pRz25k5p8tU7aNw/zh-cn_image_0000002531795794.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=CF5EF6F14C165FD31482C9E8FEEFEDED6CA6FC839C78A5765E39F113A6D06FD3)

### 示例8（播放PixelMap数组动画）

该示例通过[AnimatedDrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#animateddrawabledescriptor12)对象播放PixelMap数组动画。

```typescript
import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample {
  pixelMaps: PixelMap[] = [];
  @State options: AnimationOptions = { iterations: 1 };
  @State animated: AnimatedDrawableDescriptor | undefined = undefined;

  async aboutToAppear() {
    this.pixelMaps = await this.getPixelMaps();
    this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
  }

  build() {
    Column() {
      Row() {
        Image(this.animated)
          .width('500px').height('500px')
          .onFinish(() => {
            console.info('finish');
          })
      }.height('50%')

      Row() {
        Button('once').width(100).padding(5).onClick(() => {
          this.options = { iterations: 1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.options = { iterations: -1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
      }
    }.width('50%')
  }

  private async getPixmapListFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap[] = await imageSource.createPixelMapList({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixelMaps() {

    let myPixelMaps: PixelMap[] = await this.getPixmapListFromMedia($r('app.media.mountain'));

    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.sky')));

    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.clouds')));

    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.landscape')));
    return myPixelMaps;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CYXRcIFNTxew9VJOGQksSQ/zh-cn_image_0000002562555759.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=974F6BB022776F65C11D71FC6F3858B7DF7EF89A7FA02CB99CC1275EEBE033CA)

### 示例9（为图像设置颜色滤镜效果）

该示例通过[colorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#colorfilter9)属性实现了给图像设置颜色滤镜效果。

```typescript
import { drawing, common2D } from '@kit.ArkGraphics2D';

@Entry
@Component
struct ImageExample3 {

  private imageOne: Resource = $r('app.media.svg1');

  private imageTwo: Resource = $r('app.media.1');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageTwo;
  private colorFilterMatrix: number[] = [1, 0, 0, 0, 0.5,
                                         0, 1, 0, 0, 0,
                                         0, 0, 1, 0, 0,
                                         0, 0, 0, 1, 0];
  private color: common2D.Color = {
    alpha: 255,
    red: 255,
    green: 0,
    blue: 0
  };
  @State drawingColorFilterFirst: ColorFilter | undefined = undefined;
  @State drawingColorFilterSecond: ColorFilter | undefined = undefined;
  @State drawingColorFilterThird: ColorFilter | undefined = undefined;

  build() {
    Column() {
      Image(this.src)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterFirst)
        .onClick(()=>{
          this.drawingColorFilterFirst =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
        })

      Image(this.src2)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterSecond)
        .onClick(()=>{
          this.drawingColorFilterSecond = new ColorFilter(this.colorFilterMatrix);
        })

      Image($r('app.media.svg2'))
        .width(110)
        .height(110)
        .margin(15)
        .colorFilter(this.drawingColorFilterThird)
        .onClick(()=>{
          this.drawingColorFilterThird =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/LdBWsn5nQg-coxxeP-EsAQ/zh-cn_image_0000002562715731.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=E221FC3E4A4F98134A6A6CEE1A1F6F40ED7C3D7CB15D236E127D299AFB5B1531)

### 示例10（为图像设置填充效果）

该示例通过[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性为图像设置填充效果。

```typescript
@Entry
@Component
struct ImageExample{
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {

          Image($r('app.media.sky'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP_START)

          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.BOTTOM_START)
        }
        Row() {

          Image($r('app.media.svg'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP_END)

          Image($r('app.media.jpg'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.CENTER)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/rRHD669XSgqIaRDdAO9Ksw/zh-cn_image_0000002531635860.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=B8946EE568D35D717C212629D333B057B959F71710433B0619029C086CE59283)

### 示例11（切换显示不同类型图片）

该示例展示了[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr)类型与[ImageContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagecontent12)类型作为数据源的显示图片效果。

```typescript
@Entry
@Component
struct ImageContentExample {
  @State imageSrcIndex: number = 0;

  @State imageSrcList: (ResourceStr | ImageContent)[] = [$r('app.media.app_icon'), ImageContent.EMPTY];

  build() {
    Column({ space: 10 }) {
      Image(this.imageSrcList[this.imageSrcIndex])
        .width(100)
        .height(100)
      Button('点击切换Image的src', { type: ButtonType.Capsule, stateEffect: false })
        .height(50)
        .onClick(() => {
          this.imageSrcIndex = (this.imageSrcIndex + 1) % this.imageSrcList.length;
        })
    }.width('100%')
    .padding(20)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/PiAjL6lnQAGrUNTI4V2OQA/zh-cn_image_0000002531795796.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=625D982A42A5B2887E4A4E91854799D7A0B4328D988A9974418637CD588126F2)

### 示例12（配置隐私隐藏）

该示例通过[privacySensitive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#privacysensitive12)属性展示了如何配置隐私隐藏，效果展示需要卡片框架支持。

```typescript
@Entry
@Component
struct ImageExample {
  build() {
    Column({ space: 10 }) {

      Image($r('app.media.startIcon'))
        .width(50)
        .height(50)
        .margin({top :30})
        .privacySensitive(true)
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/w1IAORbQTwuy972kiDS3OQ/zh-cn_image_0000002562555761.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=98118D1BFF4A925DB7556DDDFBD4E7B34742B3140738162948078DD1B030DE38)

### 示例13（为图片设置扫光效果）

该示例通过[linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel#lineargradient10)接口和[animateTo()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)接口实现了给图片设置扫光效果。

```typescript
import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample11 {
  private curve = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
  @State moveImg: string[] = ['imageScanEffect'];
  @State moveImgVisible: Visibility = Visibility.Visible;
  @State durationTime: number = 1500;
  @State iterationsTimes: number = -1;
  @State private opacityValue: number = 0.5;
  @State imageWidth: number = 450;
  @State visible: Visibility = Visibility.Hidden;
  @State stackBackgroundColor: string = '#E1E4E9';
  @State linePositionX: number = 0 - this.imageWidth;
  @State linePositionY: number = 0;
  @State imgResource: Resource | undefined = undefined;

  startupAnimate() {
    this.moveImg.pop();
    this.moveImg.push('imageScanEffect');
    setTimeout(() => {

      this.imgResource = $r('app.media.img');
    }, 3000);
    this.getUIContext()?.animateTo({
      duration: this.durationTime,
      curve: this.curve,
      tempo: 1,
      iterations: this.iterationsTimes,
      delay: 0
    }, () => {
      this.linePositionX = this.imageWidth;
    })
  }

  build() {
    Column() {
      Row() {
        Stack() {
          Image(this.imgResource)
            .width(this.imageWidth)
            .height(200)
            .objectFit(ImageFit.Contain)
            .visibility(this.visible)
            .onComplete(() => {
              this.visible = Visibility.Visible;
              this.moveImg.pop();
            })
            .onError(() =>{
              setTimeout(() => {
                this.visible = Visibility.Visible;
                this.moveImg.pop();
              }, 2600)
            })
          ForEach(this.moveImg, (item: string) => {
            Row()
              .width(this.imageWidth)
              .height(200)
              .visibility(this.moveImgVisible)
              .position({ x: this.linePositionX, y: this.linePositionY })
              .linearGradient({
                direction: GradientDirection.Right,
                repeating: false,
                colors: [[0xE1E4E9, 0], [0xFFFFFF, 0.75], [0xE1E4E9, 1]]
              })
              .opacity(this.opacityValue)
          })
        }
        .backgroundColor(this.visible ? this.stackBackgroundColor : undefined)
        .margin({top: 20, left: 20, right: 20})
        .borderRadius(20)
        .clip(true)
        .onAppear(() => {
          this.startupAnimate();
        })
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/sAswGvqZRyi9Ajv8NIVWvw/zh-cn_image_0000002562715733.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=EAC48A9F7D4B468EE49D5EA2329F8ADA5071BE4951142CF796DBF98908A0190C)

### 示例14（为图片添加变换效果）

该示例通过[imageMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imagematrix15)和[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性，为图片添加旋转和平移的效果。

从API version 15开始，新增imageMatrix属性。

```typescript
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .translate({ x: -400, y: -750 })
    .scale({ x: 0.5, y: 0.5 })
    .rotate({
      x: 2,
      y: 0.5,
      z: 3,
      centerX: 10,
      centerY: 10,
      angle: -10
    })

  build() {
    Row() {
      Column({ space: 50 }) {
        Column({ space: 5 }) {

          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.Contain)
            .width(150)
            .height(150)
          Text('图片无变换')
            .fontSize('25px')
        }
        Column({ space: 5 }) {

          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.None)
            .translate({ x: 10, y: 10 })
            .scale({ x: 0.5, y: 0.5 })
            .width(100)
            .height(100)
          Text('Image直接变换，默认显示图源左上角。')
            .fontSize('25px')
        }
        Column({ space: 5 }) {

          Image($r('app.media.example'))
            .objectFit(ImageFit.MATRIX)
            .imageMatrix(this.matrix1)
            .border({ width:2, color: Color.Black })
            .width(150)
            .height(150)
          Text('通过imageMatrix变换，调整图源位置，实现最佳呈现。')
            .fontSize('25px')
        }
      }
      .width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/D-7rOMJ4ShyEtqzo_ie3Ww/zh-cn_image_0000002531635862.jpeg?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=392851B0CF27D0A77D8ED39CF307D80660AC392BEE72D6F815D378E87C054ACE)

### 示例15（通过sourceSize设置图片解码尺寸）

该示例通过[sourceSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#sourcesize)接口自定义图片的解码尺寸。

```typescript
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {

      Image($r('app.media.sky'))
        .sourceSize({width:1393, height:1080})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)

      Image($r('app.media.sky'))
        .sourceSize({width:13, height:10})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/tKBrGuhxRrSZWnu-QRCl4w/zh-cn_image_0000002531795798.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=C0EEA0107321220229E65D94E62E2AD3BFB04ABF4D96B2961C78CEA824087402)

### 示例16（通过renderMode设置图片的渲染模式）

该示例通过[renderMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#rendermode)接口设置图片渲染模式为黑白模式。

```typescript
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {

      Image($r('app.media.sky'))
        .renderMode(ImageRenderMode.Template)
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/r_Wv8kPrSpGftggdwRj04w/zh-cn_image_0000002562555763.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=0563F5508BE185B6CACB8535EC90454A7B447345E0F5D5C7450E0F4B4BE7B0E9)

### 示例17（通过objectRepeat设置图片的重复样式）

该示例通过[objectRepeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectrepeat)接口在竖直轴上重复绘制图片。

```typescript
@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {

      Image($r('app.media.sky'))
        .objectRepeat(ImageRepeat.Y)
        .height('90%')
        .width('90%')
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/OZxIzpLzSFWX4s4SGtzKIg/zh-cn_image_0000002562715735.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=6F2CCE0154AA1CA6CC3A8F4AFBD3885C760139C229FE98695E56293BA41C2CC7)

### 示例18（设置SVG图片的填充颜色）

该示例通过[fillColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#fillcolor15)属性为SVG图片设置不同颜色的填充效果。

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('不设置fillColor')

      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
      Text('fillColor传入ColorContent.ORIGIN')

      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(ColorContent.ORIGIN)
      Text('fillColor传入Color.Blue')

      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(Color.Blue)
      Text('fillColor传入undefined')

      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(undefined)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/hv8kY-bpRqGua5U0sXN1OQ/zh-cn_image_0000002531635864.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=CC0379DA579F62637404092FAAE7047787435D51A91F74C28DD311AF38F52F34)

### 示例19（设置HDR图源动态提亮）

该示例通过[hdrBrightness](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#hdrbrightness19)属性调整HDR图源的亮度，将hdrBrightness从0调整到1。

从API version 19开始，新增hdrBrightness属性。

```typescript
import { image } from '@kit.ImageKit';

const TAG = 'AceImage';

@Entry
@Component
struct Index {

  @State imgUrl: string = 'img_1';
  @State bright: number = 0;
  aboutToAppear(): void {

    let img = this.getUIContext().getHostContext()?.resourceManager.getMediaByNameSync(this.imgUrl);

    if (img && img.buffer) {
      let imageSource = image.createImageSource(img?.buffer.slice(0));
      let imageInfo = imageSource.getImageInfoSync();

      if (imageInfo == undefined) {
        console.error(TAG, 'Failed to obtain the image information.');
      } else {

        console.info(TAG, 'imageInfo.isHdr:' + imageInfo.isHdr);
      }
    } else {
      console.error(TAG, 'Failed to obtain the image buffer.');
    }
  }

  build() {
    Column() {

      Image($r('app.media.img_1')).width('50%')
        .height('auto')
        .margin({ top: 160 })
        .hdrBrightness(this.bright)
      Button('图片动态提亮 0->1')
        .onClick(() => {

          this.getUIContext()?.animateTo({}, () => {
            this.bright = 1.0 - this.bright;
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

### 示例20（设置图片是否跟随系统语言方向）

该示例通过[matchTextDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#matchtextdirection)接口，设置手机语言为维语时图片是否显示镜像翻转显示效果。

```typescript
@Entry
@Component
struct Index {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {

          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(false)
        }
        Row() {

          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(true)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/IIO70XunT_SeNrQzX-FrhQ/zh-cn_image_0000002531795800.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=42FA4EE2FA9DF1BA02FD01514C62B258678DE3FDCE7C03E14F42115A3112846A)

### 示例21（设置图像内容的显示方向）

该示例通过[orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#orientation14)属性，设置图像内容的显示方向。

```typescript
@Entry
@Component
struct OrientationExample {
  build() {
    Column() {
      Row({ space: 25 }) {
        Column() {
          Text('AUTO')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.AUTO)
        }

        Column() {
          Text('UP')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP)
        }

        Column() {
          Text('RIGHT')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT)
        }
      }

      Row({ space: 25 }) {
        Column() {
          Text('DOWN')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN)
        }

        Column() {
          Text('LEFT')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT)
        }

        Column() {
          Text('UP_MIRRORED')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP_MIRRORED)
        }
      }

      Row({ space: 15 }) {
        Column() {
          Text('RIGHT_MIRRORED')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT_MIRRORED)
        }

        Column() {
          Text('DOWN_MIRRORED')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN_MIRRORED)
        }

        Column() {
          Text('LEFT_MIRRORED')

          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT_MIRRORED)
        }
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/GkGFuX78Rra6zULLFY6OhQ/zh-cn_image_0000002562555765.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=9998421E94E1A98CA05B1EDDB8FC49349ABBB35A1AF1C2AFB70E950B6DC6287D)

### 示例22（获取图片的exif信息并设置图像内容的显示方向）

该示例通过[getImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource#getimageproperty11)接口，获取图片的exif信息，再根据获取到的exif信息，通过[orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#orientation14)属性设置图像内容显示为正确方向。

```typescript
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

@Entry
@Component
struct Example {
  @State rotateOrientation: ImageRotateOrientation = ImageRotateOrientation.UP;
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State text1: string = 'The exif orientation is ';
  @State text2: string = 'Set orientation to ';

  getOrientation(orientation: string): ImageRotateOrientation {
    if (orientation == 'Top-right') {
      this.text2 = this.text2 + 'UP_MIRRORED';
      return ImageRotateOrientation.UP_MIRRORED;
    } else if (orientation == 'Bottom-right') {
      this.text2 = this.text2 + 'DOWN';
      return ImageRotateOrientation.DOWN;
    } else if (orientation == 'Bottom-left') {
      this.text2 = this.text2 + 'DOWN_MIRRORED';
      return ImageRotateOrientation.DOWN_MIRRORED;
    } else if (orientation == 'Left-top') {
      this.text2 = this.text2 + 'LEFT_MIRRORED';
      return ImageRotateOrientation.LEFT_MIRRORED;
    } else if (orientation == 'Right-top') {
      this.text2 = this.text2 + 'RIGHT';
      return ImageRotateOrientation.RIGHT;
    } else if (orientation == 'Right-bottom') {
      this.text2 = this.text2 + 'RIGHT_MIRRORED';
      return ImageRotateOrientation.RIGHT_MIRRORED;
    } else if (orientation == 'Left-bottom') {
      this.text2 = this.text2 + 'LEFT';
      return ImageRotateOrientation.LEFT;
    } else if (orientation == 'Top-left') {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    } else {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    }
  }

  async getFileBuffer(context: Context): Promise<ArrayBuffer | undefined> {
    try {
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

      const fileData: Uint8Array = await resourceMgr.getRawFileContent('hello.jpg');
      console.info('Successfully get RawFileContent');

      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (error) {
      console.error('Failed to get RawFileContent');
      return undefined;
    }
  }

  aboutToAppear() {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return;
    }
    this.getFileBuffer(context).then((buf: ArrayBuffer | undefined) => {
      let imageSource = image.createImageSource(buf);
      if (!imageSource) {
        return;
      }

      imageSource.getImageProperty(image.PropertyKey.ORIENTATION).then((orientation) => {
        this.rotateOrientation = this.getOrientation(orientation);
        this.text1 = this.text1 + orientation;
        let options: image.DecodingOptions = {
          'editable': true,
          'desiredPixelFormat': image.PixelMapFormat.RGBA_8888,
        }
        imageSource.createPixelMap(options).then((pixelMap: image.PixelMap) => {
          this.pixelMap = pixelMap;
          imageSource.release();
        });
      }).catch(() => {
        imageSource.release();
      });
    })
  }

  build() {
    Column({ space: 40 }) {
      Column({ space: 10 }) {
        Text('before').fontSize(20).fontWeight(700)

        Image($rawfile('hello.jpg'))
          .width(100)
          .height(100)
        Text(this.text1)
      }

      Column({ space: 10 }) {
        Text('after').fontSize(20).fontWeight(700)
        Image(this.pixelMap)
          .width(100)
          .height(100)
          .orientation(this.rotateOrientation)
        Text(this.text2)
      }
    }
    .height('80%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/WcxTKKpfT1qcNN2meOcTkg/zh-cn_image_0000002562715737.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=A250AFC815354B8A8D45A5F7236DA2F205C0C0DE19AFDD46B7513B421A8E456F)

### 示例23（动态切换SVG图片的填充颜色）

通过按钮切换不同色域下的颜色值，动态改变SVG图片的填充颜色效果，以展示[ColorMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#colormetrics12)类型的使用方式和显示差异。

```typescript
import { ColorMetrics } from '@kit.ArkUI';
@Entry
@Component
struct fillColorMetricsDemo {
  @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.631, 0.0392, 0.1294);
  @State sRGBRed: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.631, 0.0392, 0.1294);
  @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.09, 0.662 ,0.552);
  @State sRGBGreen: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.09, 0.662 ,0.552);
  @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0.290 ,0.686);
  @State sRGBBlue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0, 0.290 ,0.686);
  @State colorArray: (Color|undefined|ColorMetrics|ColorContent)[] = [
    this.p3Red, this.sRGBRed, this.p3Green, this.sRGBGreen, this.p3Blue,
    this.sRGBBlue, ColorContent.ORIGIN, Color.Gray, undefined
  ]
  @State colorArrayStr: string[] = [
    'P3 Red', 'SRGB Red', 'P3 Green', 'SRGB Green',
    'P3 Blue', 'SRGB Blue', 'ORIGIN', 'Gray', 'undefined'
  ]
  @State arrayIdx: number = 0
  build() {
    Column() {
      Text('FillColor is ' + this.colorArrayStr[this.arrayIdx])

      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.colorArray[this.arrayIdx])
      Button('ChangeFillColor')
        .onClick(()=>{
          this.arrayIdx = (this.arrayIdx + 1) % this.colorArray.length
        })
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Red')

      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBRed)
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Green')

      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBGreen)
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Blue')

      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBBlue)
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/I_A7WzyjRfC0Ht9IQtaUMg/zh-cn_image_0000002531635866.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=1A37516391873D630ADD8FE59E3B3E03D923B106CE41C6B54D8067208CBC5261)

### 示例24（使用应用沙箱路径显示图片）

在当前应用的haps/entry/files目录下预置一张名为cloud.png的图片，随后使用应用沙箱路径显示该图片。

```typescript
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  private getSandBoxUri(): string {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return '';
    }

    return fileUri.getUriFromPath(context.filesDir + '/cloud.png');
  }

  build() {
    Column() {
      Image(this.getSandBoxUri())
        .width(150)
        .height(150)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/HlWGmkXES4Oe2CSAQ4JVrw/zh-cn_image_0000002531795802.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=DB6D43E1CAFBACC213818FC756BF87F459B43FEFF7C652BD919637FFAD8ED399)

### 示例25（使用相对路径显示图片）

在工程pages目录同级位置创建common目录，在common目录下预置一张名为cloud1.png的图片，随后使用相对路径显示该图片。

```typescript
@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Image('common/cloud1.png')
        .width(100)
        .height(100)
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/HwYrAXf7SCaAR6WF-wZhfg/zh-cn_image_0000002531795802.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=2162C61413C8CC14A93AB7B83DC38645F58D2708F117AAA97C0507A3095C8431)

### 示例26（使用supportSvg2属性时，SVG图片的显示效果）

该示例通过设置[supportSvg2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#supportsvg221)属性，使SVG标签解析能力增强功能生效。

从API version 21开始，新增supportSvg2属性。

```typescript
@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('supportSvg2参数设置为true')

        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
          .supportSvg2(true)
          .margin({ bottom: 30 })
        Text('supportSvg2参数设置为false（默认值）')

        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/2JUSlLkmQ_ikeTCUZvJUSw/zh-cn_image_0000002562555767.png?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=BC90556171034CC369570A3BC48817A7884BC447E76A2BA2A3240471DCB84B30)

### 示例27（使用ContentTransition属性实现图片淡入淡出切换效果）

从API version 21开始，该示例演示了在点击图片切换图源时，通过[contentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#contenttransition21)属性实现淡入淡出效果，完成图片的平滑过渡。

```typescript
@Entry
@Component
struct ImageExample {

  @State imageResource: Resource = $r('app.media.icon');

  build() {
    Row() {
      Column() {
        Image(this.imageResource)
          .width(200)
          .height(200)

          .contentTransition(ContentTransitionEffect.OPACITY)
          .onClick(() => {

            this.imageResource = $r('app.media.cloud1')
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Vz3SMulBRiuxuhGUQi_0Sg/zh-cn_image_0000002562715739.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=7D74B7E2FD5E4CC0146BC2FF897CC61DB17E775F542FAE7383A3C8CFCC478372)

### 示例28（使用alt属性实现设置加载失败中图片和加载失败时图片）

该示例演示了在图片加载过程中和加载失败时，通过设置[alt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#alt22)属性实现图片加载过程中和图片加载失败时显示指定图片。

```typescript
@Entry
@Component
struct ImageExample {
  build() {
      Column() {
      Text('同时设置placeholder属性和error属性')

      Image("https://www.example.com/xxx.png")

        .alt({ placeholder: $r('app.media.startIcon'), error: $r('app.media.example') })
        .width(100)
        .height(100)
        .margin(20)
      Text('只设置placeholder属性')
      Image("https://www.example.com/xxx.png")
        .alt({ placeholder: $r('app.media.startIcon')})
        .width(100)
        .height(100)
        .margin(20)
      Text('只设置error属性')
      Image("https://www.example.com/xxx.png")
        .alt({error: $r('app.media.example')})
        .width(100)
        .height(100)
        .margin(20)
      }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ixZ3Cbx_SaO6qA2qJt5tsg/zh-cn_image_0000002531635868.gif?HW-CC-KV=V1&HW-CC-Date=20260324T022820Z&HW-CC-Expire=86400&HW-CC-Sign=7EB624E7F89873142AAC6351D95D6B6D6D864405F465038BB34C142CCE2009EF)
