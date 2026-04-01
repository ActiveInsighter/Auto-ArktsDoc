# 弹出框控制器
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller

ArkUI的弹出框控制器在绑定弹出框后，可提供对弹出框的操作能力，当前支持关闭功能。可以将控制器传入弹出框内容区域后进行操作。

从API version 18开始，可设置controller参数以绑定[DialogController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#dialogcontroller18)控制器，通过控制器能够操作弹出框。

## 使用约束

目前[openCustomDialogWithController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18)和[presentCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#presentcustomdialog18)支持通过controller参数来绑定弹出框进行操作，目前[getDialogController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api#getdialogcontroller18)支持获取自定义组件所在的弹出框的控制器。

> **说明**
> 一个弹出框控制器只能绑定一个弹出框，且操作只对该弹出框生效。
>
> 使用[getDialogController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api#getdialogcontroller18)获取弹出框控制器时，如果当前自定义组件不在弹出框中显示则获取为undefined。

## 创建自定义内容为ComponentContent的弹出框控制器

> **说明**
> 详细变量定义请参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller#完整示例)。

1. 初始化一个自定义弹出框内容区的入参类，内部包含弹出框控制器。 ```typescript class Params {  public text: string = '';  public dialogController: promptAction.CommonController = new promptAction.DialogController();  constructor(text: string, dialogController: promptAction.CommonController) {  this.text = text;  this.dialogController = dialogController;  } } ```
2. 初始化一个自定义的弹出框内容区，内部包含一个按钮，该按钮通过该自定义组件自带的弹出框控制器实现关闭功能。 ```typescript @Component struct MyComponent {  build() {  Column({ space: 5 }) {  Button($r('app.string.closeDialog_by_custom'))  .onClick(() => {  let dialogController: promptAction.DialogController = this.getDialogController();  if (dialogController !== undefined) {  dialogController.close();  }  })  }  } } ```
3. 初始化另一自定义弹出框内容区，其中包含一个Text组件和一个按钮，该按钮通过外部传递的弹出框控制器用于关闭弹出框，并且该内容区还包含前一个自定义弹出框内容区。 ```typescript @Builder function buildText(params: Params) {  Column({ space: 5 }) {  Text(params.text)  .fontSize(30)  if (params.dialogController !== undefined) {  Button($r('app.string.closeDialog_by_controller'))  .onClick(() => {  params.dialogController.close();  })  }  MyComponent()  }  .width(300)  .height(200)  .backgroundColor('#FFF0F0F0') } ```
4. 初始化一个弹出框控制器，并通过设置控制器参数来初始化一个弹出框内容实体对象。最后，通过调用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getPromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getpromptaction)方法获取[PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction)对象，再通过该对象调用[openCustomDialogWithController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18)接口，并且设置初始化的内容实体对象和控制器参数以创建弹出框。 ```typescript let dialogController: promptAction.CommonController = new promptAction.DialogController(); let contentNode: ComponentContent<Object> =  new ComponentContent(this.getUIContext(), wrapBuilder(buildText),  new Params(this.message, dialogController)); this.getUIContext().getPromptAction().openCustomDialogWithController(  contentNode, dialogController, this.baseDialogOptions).catch((err: BusinessError) => {  hilog.error(0x0000, 'dialogController',  'openCustomDialogWithController error: ' + err.code + ' ' + err.message); }); ```

## 创建自定义内容为CustomBuilder的弹出框控制器

> **说明**
> 详细变量定义请参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller#完整示例)。

1. 初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过外部传递的弹出框控制器实现关闭功能。 ```typescript @Builder customDialogComponent(dialogController: promptAction.DialogController) {  Column({ space: 5 }) {  Text(this.message)  .fontSize(30)  if (dialogController !== undefined) {  Button($r('app.string.closeDialog_by_outside'))  .onClick(() => {  dialogController.close();  })  }  }  .height(200)  .padding(5)  .justifyContent(FlexAlign.SpaceBetween)  .backgroundColor('#FFF0F0F0') } ```
2. 初始化一个弹出框控制器，并通过调用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getPromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getpromptaction)方法获取[PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction)对象，再通过该对象调用[presentCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#presentcustomdialog18)接口，设置初始化的内容实体对象和控制器参数以创建弹出框。 ```typescript let dialogController: promptAction.CommonController = new promptAction.DialogController(); this.getUIContext().getPromptAction().presentCustomDialog(() => {  this.customDialogComponent(dialogController); }, dialogController, this.dialogOptions).catch((err: BusinessError) => {  hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message); }); ```

## 创建自定义内容为CustomBuilderWithId的弹出框控制器

> **说明**
> 详细变量定义请参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller#完整示例)。

1. 初始化一个弹出框内容区，内部包含一个Text组件、一个通过外部传递的弹出框ID用于关闭弹出框的按钮和一个通过外部传递的弹出框控制器用于关闭弹出框的按钮。 ```typescript @Builder customDialogComponentWithId(dialogId: number, dialogController: promptAction.DialogController) {  Column({ space: 5 }) {  Text(this.message)  .fontSize(30)  if (dialogId !== undefined) {  Button($r('app.string.closeDialog_by_id'))  .onClick(() => {  this.getUIContext().getPromptAction().closeCustomDialog(dialogId);  })  }  if (dialogController !== undefined) {  Button($r('app.string.closeDialog_by_dialog_controller'))  .onClick(() => {  dialogController.close();  })  }  } } ```
2. 初始化一个弹出框控制器，并通过调用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getPromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getpromptaction)方法获取[PromptAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction)对象，再通过该对象调用[presentCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#presentcustomdialog18)接口，设置初始化的内容实体对象和控制器参数以创建弹出框。 ```typescript let dialogController: promptAction.CommonController = new promptAction.DialogController(); this.getUIContext().getPromptAction().presentCustomDialog((dialogId: number) => {  this.customDialogComponentWithId(dialogId, dialogController); }, dialogController, this.dialogOptions).catch((err: BusinessError) => {  hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message); }); ```

## 在CustomDialogController内容区直接获取弹出框控制器

> **说明**
> 详细变量定义请参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller#完整示例)。

1. 初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过弹出框控制器关闭弹出框。 ```typescript @CustomDialog @Component struct CustomDialogExample {  controller?: CustomDialogController;  build() {  Column({ space: 5 }) {  Text($r('app.string.my_content'))  .fontSize(30)  Button($r('app.string.closeDialog_by_dialog'))  .onClick(() => {  let dialogController: PromptActionDialogController = this.getDialogController();  if (dialogController !== undefined) {  dialogController.close();  }  })  }  .height(200)  .backgroundColor('#FFF0F0F0')  } } ```
2. 初始化一个自定义弹出框构造器，关联自定义弹出框内容区。 ```typescript let customDialogController: CustomDialogController = new CustomDialogController({  builder: CustomDialogExample(), }); customDialogController.open(); ```

## 使用控制器获取弹出框的状态

在自定义弹出框场景中，从API version 20 开始，可以通过控制器调用[getState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#getstate20)接口获取弹出框状态。

> **说明**
> 详细变量定义请参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller#完整示例)。

初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过调用getState获取当前弹出框状态。

```typescript
@Builder
customDialogComponentGetState(dialogController: promptAction.DialogController) {
  Column({ space: 5 }) {
    Text(this.message)
      .fontSize(30)
    if (dialogController !== undefined) {

      Button($r('app.string.click_check_status'))
        .onClick(() => {
          hilog.info(0x0000, 'dialogController', 'state:' + dialogController.getState());
        })
    }
  }
  .height(200)
  .padding(5)
  .justifyContent(FlexAlign.SpaceBetween)
  .backgroundColor('#FFF0F0F0')
}
```

## 完整示例

通过外部传递的弹出框控制器和自定义组件自带的弹出框控制器，在自定义弹出框内容区域内实现关闭功能。

```typescript
import { ComponentContent, promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Params {
  public text: string = '';
  public dialogController: promptAction.CommonController = new promptAction.DialogController();

  constructor(text: string, dialogController: promptAction.CommonController) {
    this.text = text;
    this.dialogController = dialogController;
  }
}

@Component
struct MyComponent {
  build() {
    Column({ space: 5 }) {

      Button($r('app.string.closeDialog_by_custom'))
        .onClick(() => {
          let dialogController: promptAction.DialogController = this.getDialogController();
          if (dialogController !== undefined) {
            dialogController.close();
          }
        })
    }
  }
}

@Builder
function buildText(params: Params) {
  Column({ space: 5 }) {
    Text(params.text)
      .fontSize(30)
    if (params.dialogController !== undefined) {

      Button($r('app.string.closeDialog_by_controller'))
        .onClick(() => {
          params.dialogController.close();
        })
    }
    MyComponent()
  }
  .width(300)
  .height(200)
  .backgroundColor('#FFF0F0F0')
}

@CustomDialog
@Component
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column({ space: 5 }) {

      Text($r('app.string.my_content'))
        .fontSize(30)

      Button($r('app.string.closeDialog_by_dialog'))
        .onClick(() => {
          let dialogController: PromptActionDialogController = this.getDialogController();
          if (dialogController !== undefined) {
            dialogController.close();
          }
        })
    }
    .height(200)
    .backgroundColor('#FFF0F0F0')
  }
}

@Entry
@Component
export struct DialogController {
  private message = 'dialog';
  private baseDialogOptions: promptAction.BaseDialogOptions = {
    isModal: false,
    autoCancel: false
  };
  private dialogOptions: promptAction.DialogOptions = {
    isModal: false,
    autoCancel: false
  };

  @Builder
  customDialogComponent(dialogController: promptAction.DialogController) {
    Column({ space: 5 }) {
      Text(this.message)
        .fontSize(30)
      if (dialogController !== undefined) {

        Button($r('app.string.closeDialog_by_outside'))
          .onClick(() => {
            dialogController.close();
          })
      }
    }
    .height(200)
    .padding(5)
    .justifyContent(FlexAlign.SpaceBetween)
    .backgroundColor('#FFF0F0F0')
  }

  @Builder
  customDialogComponentWithId(dialogId: number, dialogController: promptAction.DialogController) {
    Column({ space: 5 }) {
      Text(this.message)
        .fontSize(30)
      if (dialogId !== undefined) {

        Button($r('app.string.closeDialog_by_id'))
          .onClick(() => {
            this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
          })
      }
      if (dialogController !== undefined) {

        Button($r('app.string.closeDialog_by_dialog_controller'))
          .onClick(() => {
            dialogController.close();
          })
      }
    }
  }

  @Builder
  customDialogComponentGetState(dialogController: promptAction.DialogController) {
    Column({ space: 5 }) {
      Text(this.message)
        .fontSize(30)
      if (dialogController !== undefined) {

        Button($r('app.string.click_check_status'))
          .onClick(() => {
            hilog.info(0x0000, 'dialogController', 'state:' + dialogController.getState());
          })
      }
    }
    .height(200)
    .padding(5)
    .justifyContent(FlexAlign.SpaceBetween)
    .backgroundColor('#FFF0F0F0')
  }

  build() {
    NavDestination() {
      Column({ space: 5 }) {

        Button($r('app.string.open_custom_dialog_with_controller'))
          .onClick(() => {
            let dialogController: promptAction.CommonController = new promptAction.DialogController();
            let contentNode: ComponentContent<Object> =
              new ComponentContent(this.getUIContext(), wrapBuilder(buildText),
                new Params(this.message, dialogController));
            this.getUIContext().getPromptAction().openCustomDialogWithController(
              contentNode, dialogController, this.baseDialogOptions).catch((err: BusinessError) => {
              hilog.error(0x0000, 'dialogController',
                'openCustomDialogWithController error: ' + err.code + ' ' + err.message);
            });
          })

        Button($r('app.string.present_custom_dialog'))
          .onClick(() => {
            let dialogController: promptAction.CommonController = new promptAction.DialogController();
            this.getUIContext().getPromptAction().presentCustomDialog(() => {
              this.customDialogComponent(dialogController);
            }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
              hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
            });
          })

        Button($r('app.string.custom_builder_with_id'))
          .onClick(() => {
            let dialogController: promptAction.CommonController = new promptAction.DialogController();
            this.getUIContext().getPromptAction().presentCustomDialog((dialogId: number) => {
              this.customDialogComponentWithId(dialogId, dialogController);
            }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
              hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
            });
          })

        Button($r('app.string.custom_dialog_controller_dialog'))
          .onClick(() => {
            let customDialogController: CustomDialogController = new CustomDialogController({
              builder: CustomDialogExample(),
            });
            customDialogController.open();
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/zbPXLvI3Qpud_Hp167q_Ig/zh-cn_image_0000002565210301.gif?HW-CC-KV=V1&HW-CC-Date=20260401T132850Z&HW-CC-Expire=86400&HW-CC-Sign=F88C445609DBA5895008F78346587D26ECD02BE5D4873898EFA213D9CB5480FA)
