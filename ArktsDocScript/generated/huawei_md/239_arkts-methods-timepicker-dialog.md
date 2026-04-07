# 时间滑动选择器弹窗 (TimePickerDialog)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog

以24小时的时间区间创建时间滑动选择器，展示在弹窗上。

> **说明**
> - 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)说明。
> - 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
> - 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos_id_picker_show_count_landscape')。

## TimePickerDialog

### show(deprecated)

static show(options?: TimePickerDialogOptions)

定义时间滑动选择器弹窗并弹出。

> **说明**
> 从API version 8开始支持，从API version 18开始废弃，建议使用[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)替代。showTimePickerDialog需先获取[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)实例后再进行调用。
>
> 从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TimePickerDialogOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog#timepickerdialogoptions对象说明) | 否 | 配置时间选择器弹窗的参数。 |

## TimePickerDialogOptions对象说明

时间选择器弹窗选项。

继承自[TimePickerOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useMilitaryTime | boolean | 否 | 是 | 时间是否以24小时制展示。 - true：时间以24小时制展示。 - false：时间以12小时制展示。 默认值：false **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| disappearTextStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular } } **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。 默认值： { color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular } } **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedTextStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细。 默认值： { color: '#ff007dff', font: { size: '20fp', weight: FontWeight.Medium } } **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。 **说明：** 1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。 2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED_RECTANGLE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。 **说明：** 1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。 2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED_RECTANGLE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box#dialogalignment枚举说明) | 否 | 是 | 设置弹窗在垂直方向上的对齐方式。 默认值：DialogAlignment.Default **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#offset) | 否 | 是 | 设置弹窗相对alignment所在位置的偏移量。 默认值：{ dx: 0 , dy: 0 } **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。 默认值：{ x: 0, y: 0, width: '100%', height: '100%' } **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAccept | (value: [TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)) => void | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | () => void | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | (value: [TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)) => void | 否 | 是 | 滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调。 **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 弹窗背板颜色。 默认值：Color.Transparent **说明：** 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。 默认值：BlurStyle.COMPONENT_ULTRA_THICK **说明：** 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。 **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。 **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | () => void | 否 | 是 | 弹窗弹出后的事件回调。 **说明：** 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | () => void | 否 | 是 | 弹窗消失后的事件回调。 **说明：** 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | () => void | 否 | 是 | 弹窗显示动效前的事件回调。 **说明：** 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | () => void | 否 | 是 | 弹窗退出动效前的事件回调。 **说明：** 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。 **说明：** 当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dateTimeOptions12+ | [DateTimeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl#datetimeoptionsdeprecated) | 否 | 是 | 设置时分是否显示前导0，目前只支持设置hour和minute参数。 默认值： hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。 minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。 **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。 - true：响应悬停态。 - false：不响应悬停态。 默认值：false **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。 默认值：HoverModeAreaType.BOTTOM_SCREEN **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onEnterSelectedArea18+ | Callback<[TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)> | 否 | 是 | 滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。 **说明：** 当enableCascade设置为true时，由于上午/下午列与小时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。 **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableCascade18+ | boolean | 否 | 是 | 设置上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。 - true：自动切换。 - false：不自动切换。 默认值：false 当enableCascade设置为true时，仅在loop参数同时为true时生效。 **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 设置是否开启触控反馈。 - true：开启触控反馈。 - false：不开启触控反馈。 默认值：true **说明**： 1. 设置为true后，其生效情况取决于系统的硬件是否支持。 2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下： "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] **元服务API**： 从API version 18开始，该接口支持在元服务中使用。 |

## 示例

> **说明**
> 推荐通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)来明确UI的执行上下文。

### 示例1（设置时间格式）

该示例通过useMilitaryTime、dateTimeOptions、format设置时间格式。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE,
            useMilitaryTime: false,
            dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            }
          });
        })
      Button('TimePickerDialog 24小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            useMilitaryTime: true,
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
          })
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Pt784nQZTj2Ka0DiuBB1Qg/zh-cn_image_0000002535789798.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=DF74C0844EE26F67367505EB134C66561240FC008F78E66D1769245089ACCDE6)

### 示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            disappearTextStyle: { color: '#297bec', font: { size: 15, weight: FontWeight.Lighter } },
            textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
            acceptButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: 'rgb(81, 81, 216)',
              fontSize: '26fp',
              fontWeight: FontWeight.Bolder,
              fontStyle: FontStyle.Normal,
              fontFamily: 'sans-serif',
              backgroundColor: '#A6ACAF',
              borderRadius: 20
            },
            cancelButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: Color.Blue,
              fontSize: '16fp',
              fontWeight: FontWeight.Normal,
              fontStyle: FontStyle.Italic,
              fontFamily: 'sans-serif',
              backgroundColor: '#50182431',
              borderRadius: 10
            },
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/McAEiTIlQHm61sOYGyNomQ/zh-cn_image_0000002535949744.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=654B1A2E6C2E5F5329B46233D1C18D427316E527D364ADEEB039D33CD3F3D720)

### 示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
            textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/QoxgjC70QYi_pvdmWwXvog/zh-cn_image_0000002566869577.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=F241EF56DD516A544C134241B79CF9D44F1BAB1A0376C85E66524613EE23C82F)

### 示例4（设置弹窗位置）

该示例通过alignment和offset设置弹窗的位置。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            alignment: DialogAlignment.Center,
            offset: { dx: 20 , dy: 0 },
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Jyt-_vjkSSe0lR6r3e0FnA/zh-cn_image_0000002566709595.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=5594DC48A4515F1E9E42713572AEBCE661C66438F9F4D1F25F897BD0E20102D3)

### 示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            maskRect: { x: 30, y: 60, width: '100%', height: '60%' },
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/zUNbf7xcR5-nHpIHT6-YfQ/zh-cn_image_0000002535789800.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=40B0B829ED0A7293D542278031C2F0113E62A0505E4CD7C3247C63B1540F9FDE)

### 示例6（设置弹窗背板）

该示例通过maskRect设置弹窗背板。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            backgroundColor: 'rgb(204, 226, 251)',
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER_FLOATING_SM,
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4mLztd-CRBGLCgAmSjtbkQ/zh-cn_image_0000002535949746.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=7C87915F0C4D9B1375AC178FDD0852EE4C533328D0FF612F6AB451A8D86446F8)

### 示例7（设置时间滑动选择器弹窗的起始时间）

该示例设置TimePickerDialog的起始时间。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            start: new Date('2022-07-22T08:30:00'),
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/8mmIUwheRkSXGi6fA-vBwQ/zh-cn_image_0000002566869579.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=43C5975581BC6A24ECC7A7A808598D47A8B5928961BF905BB94737F71295A6B8)

### 示例8（设置时间滑动选择器弹窗的结束时间）

该示例设置TimePickerDialog的结束时间。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            end: new Date('2022-07-22T15:20:00'),
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/tZ_fl96VSiSH6uQjaLMpIA/zh-cn_image_0000002566709597.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=6A04A1A953CDA80A648886DF815C6C32A67F3215F232661A01B7A837E3FF90AB)

### 示例9（设置上午下午跟随时间联动）

该示例通过配置enableCascade实现12小时制时上午下午跟随时间联动。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            enableCascade:true,
            onAccept: (value: TimePickerResult) => {

              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ZjHTQA0ETIy2MNgECLUWCA/zh-cn_image_0000002535789802.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=89E8F72601F4D6C6726D0E875E8F519065B6AFBB67EA8A49D42E088509282579)

### 示例10（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog#timepickerdialogoptions对象说明)，实现自定义背景模糊效果。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {

      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/YW6tex3KTJC2KZVPq23kCg/zh-cn_image_0000002535949748.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=07AE293C2DBC117E243A77488825B6AE593649DDD5F6E35490355087EA1F235F)

### 示例11（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog#timepickerdialogoptions对象说明)，实现自定义背景效果。

```typescript
@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {

      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/4FCvWFzURWKqTEyJ7OFcVg/zh-cn_image_0000002566869581.png?HW-CC-KV=V1&HW-CC-Date=20260407T024553Z&HW-CC-Expire=86400&HW-CC-Sign=35722BDF7772E0FB1EA4B857C4E9A2F8C4518C723563F76DDE57285BD56B1E88)
