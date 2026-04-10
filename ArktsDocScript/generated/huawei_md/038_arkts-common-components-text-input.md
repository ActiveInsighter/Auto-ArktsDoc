# 文本输入 (TextInput/TextArea/Search)
来源: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input

TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)和[TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)组件的API文档。Search是特殊的输入框组件，称为搜索框，默认样式包含搜索图标。具体用法请参考[Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)组件的API文档。

> **说明**
> 仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件。

## 创建输入框

TextInput是单行输入框，TextArea是多行输入框，Search是搜索框。通过以下接口创建这些组件。

```typescript
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

```typescript
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```typescript
Search(options?:{placeholder?: ResourceStr, value?: ResourceStr, controller?: SearchController, icon?: string})
```

- 单行输入框。 ```typescript TextInput() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/JRUi79MCQwWiMStfvUGvXg/zh-cn_image_0000002537172912.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=FF18EA9290A85D2D7BED93C4CE31EBF2B5B296D353F63CACA69DA161F71C8AB7)
- 多行输入框。 ```typescript TextArea() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/FBcP9EbYR_-HDCXfAkHesg/zh-cn_image_0000002537332834.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=E5D82ACA99C785D81ABFE9B69A248545CF47E506D135C8322F15B39F12FD06B9)
- 多行输入框文字超出一行时会自动折行。 ```typescript TextArea({ text: $r('app.string.CreatTextInput_textContent') })  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/9zjdSShuRESxVwFBc6_j4Q/zh-cn_image_0000002568172631.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=E1D40B209971860AB7902AB63BC76508AD4D6B1AFFBD0C762516099D5962A1DE)
- 搜索框。 ```typescript Search()  .searchButton($r('app.string.Creat_TextInput_Content')) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/9xUxwuKpTdi5BtlSD1ryFg/zh-cn_image_0000002568252627.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=017861A4958144AC03F32248861C951231265D0FE00EA455BB1E9273790251EB)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

### 基本输入模式（默认类型）

```typescript
TextInput()
  .type(InputType.Normal)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/natRH8ZkQDOLlXsffrvmGA/zh-cn_image_0000002537172914.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=5916B223EC116DBD0A16EC592DAB0C9EF1B4F113D938070721D8704B9219668A)

### 密码模式

包括Password密码输入模式、NUMBER_PASSWORD纯数字密码模式、NEW_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```typescript
TextInput()
  .type(InputType.Password)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/czWh8KNOSlWJWCSGKtpq8g/zh-cn_image_0000002537332836.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=C147EC8102C3EA34291D050D06BD7283E4D0DDFDA87D66B854D8401AD2A501AC)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```typescript
TextInput()
  .type(InputType.Email)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/RuT6WMxKRhqqOL8BXfjxbw/zh-cn_image_0000002568172633.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=22562A93D40AB24EAEBE4BD7936DB0014E517491FC2652B6CFB2F37CF7ECB8A7)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```typescript
TextInput()
  .type(InputType.Number)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/boJoYrMRTjS34ICQuUE_WA/zh-cn_image_0000002568252629.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=648B7CE4A80B5D4BE63E26E68A5168041101E8061916A2FBE03853F9A9985985)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

```typescript
TextInput()
  .type(InputType.PhoneNumber)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/JB8OPAV0S4eC6VNpSWnzJA/zh-cn_image_0000002537172916.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=76B356ADB35AA73AAE50AFF615EF0946EEDAD93795AC9F46B020DA2A95666774)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```typescript
TextInput()
  .type(InputType.NUMBER_DECIMAL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-6ojVaeyRY2zvsRdyT6S3g/zh-cn_image_0000002537332838.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=3902FAD74C36004064300581671F692AC0FF57AF56F1603E283B3E3A7351C926)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```typescript
TextInput()
  .type(InputType.URL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/FjLPZUhYSrqlmVF8xNWYpQ/zh-cn_image_0000002568172635.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=5E1FC68CD9CC44EE6A6AE7A4CF68C1357184B45DC13616D0B2298529377898A6)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```typescript
TextArea()
  .style(TextContentStyle.DEFAULT)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/CdQmkMj4RTOxDqb26H9aBA/zh-cn_image_0000002568252631.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=A9D7C0209B2BF7AC6E8505077826FB4EA9D618F104C3A4C8B65A114E3056CE20)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```typescript
TextArea()
  .style(TextContentStyle.INLINE)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/xn_sEY43Q0-WSfygY27wtw/zh-cn_image_0000002537172918.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=3AF459D90FDCB17343E06FD94FA5A406276901A5E3E00DC14366D02D18498660)

## 自定义样式

- 设置无输入时的提示文本。 ```typescript TextInput({ placeholder: $r('app.string.i_am_placeholder') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/JW1192jKSuuS_a6pT8Pyrg/zh-cn_image_0000002537332840.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=31FB894C3235FE7F2A7BC78448F27008DF87EBDB3A86E1A4D8235334E4729760)
- 设置输入框当前的文本内容。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/fzv1JE-5QMau4jRMy5UTsA/zh-cn_image_0000002568172637.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=176194792EC0E520E507F67BE3AB6698923A956002BD7FDF0686DC33B10AB018)
- 添加backgroundColor改变输入框的背景颜色。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') })  .backgroundColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/dUVNnQYmS6--CtDlWG7NzQ/zh-cn_image_0000002568252633.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=054E3D4A59A8CFB23C0C79AA00EC0A4273094D5C156AFECD34B5B3BB92C7C6F5) 更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。

## 添加事件

文本框主要用于获取用户输入的信息，并将信息处理成数据进行上传，绑定[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)事件可以获取输入框内改变的文本内容，绑定[onSubmit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsubmit)事件可以获取回车提交的文本信息，绑定[onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ontextselectionchange10)事件可以获取文本选中时手柄的位置信息或者编辑时光标的位置信息等等。用户也可以使用通用事件进行相应的交互操作。

> **说明**
> 在密码模式下，设置[showPassword](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showpassword12)属性时，在[onSecurityStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onsecuritystatechange12)回调中，建议增加状态同步，具体详见如下示例。
>
> [onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)回调仅支持系统输入法的场景。
>
> [onWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillchange15)的回调时序晚于[onWillInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwillinsert12)、[onWillDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onwilldelete12)，早于[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)、[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';

@Entry
@Component
struct TextInputEventAdd {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr2: string = '';
  @State textStr3: string = '';
  @State textStr4: string = '';
  @State textStr5: string = '';
  @State textStr6: string = '';
  @State textStr7: string = '';
  @State textStr8: string = '';
  @State textStr9: string = '';
  @State passwordState: boolean = false;
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        Text(`${this.textStr1}\n${this.textStr2}\n${this.textStr3}
          \n${this.textStr4}\n${this.textStr5}\n${this.textStr6}
          \n${this.textStr7}\n${this.textStr8}\n${this.textStr9}`)
          .fontSize(20)
          .width('70%')
        TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .type(InputType.Password)
          .showPassword(this.passwordState)
          .onChange((value: string) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onChange is triggering: ' + value);
            this.textStr1 = `onChange is triggering: ${value}`;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onSubmit is triggering: ' + enterKey + event.text);
            this.textStr2 = `onSubmit is triggering: ${enterKey} ${event.text}`;
          })
          .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onTextSelectionChange is triggering: ' + selectionStart + selectionEnd);
            this.textStr3 = `onTextSelectionChange is triggering: ${selectionStart} ${selectionEnd}`;
          })
          .onSecurityStateChange((isShowPassword: boolean) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onSecurityStateChange is triggering: ' + isShowPassword);
            this.passwordState = isShowPassword;
            this.textStr4 = `onSecurityStateChange is triggering: ${isShowPassword}`;
          })
          .onWillInsert((info: InsertValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr5 = `onWillInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
            return true;
          })
          .onDidInsert((info: InsertValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidInsert is triggering: ' + info.insertValue + info.insertOffset);
            this.textStr6 = `onDidInsert is triggering: ${info.insertValue} ${info.insertOffset}`;
          })
          .onWillDelete((info: DeleteValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr7 = `onWillDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onDidDelete is triggering: ' + info.deleteValue + info.deleteOffset);
            this.textStr8 = `onDidDelete is triggering: ${info.deleteValue} ${info.deleteOffset}`;
          })
          .onFocus(() => {

            hilog.info(DOMAIN, TAG, BUNDLE + 'onFocus is triggering');
            this.textStr9 = `onFocus is triggering`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/iQ1tVFVOSSywvgYXGs-JGA/zh-cn_image_0000002537172920.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=6618EF1B0859F08B07188503B4BB11C724A9BC4BFC00471DA6FA86CC3BD27527)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、搜索的菜单。

TextInput:

```typescript
TextInput({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ewHRe2jnSx2kJ7aAEUfcfA/zh-cn_image_0000002537332842.jpg?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=7FA8A6434516E01E41949DA80983276DDC073D263FE22BB7BF92DA263866603E)

TextArea:

```typescript
TextArea({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/kwEs2KlCRtyW3LuiBToLhg/zh-cn_image_0000002568172639.jpg?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=452376415B871BEFAF32E4773DA191EAAF459F591C28D9864809C002FF29AEDE)

## 禁用系统服务类菜单

从API version 20开始，支持使用[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)方法屏蔽文本选择菜单中的所有系统服务菜单项。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableSystemServiceMenuItem {
  aboutToAppear(): void {

    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {

    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {

        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Ld-Slr0URd-Xpk3VNht8VQ/zh-cn_image_0000002568252635.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=7A1534B687C50D73163848D5C7437DBA7AC7DA8660DCFC7FC61DCEF1886AA50E)

从API version 20开始，支持使用[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)方法屏蔽文本选择菜单中指定的系统服务菜单项。

```typescript
import { TextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct DisableMenuItem {
  aboutToAppear(): void {

    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE, TextMenuItemId.AI_WRITER])
  }

  aboutToDisappear(): void {

    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {

        TextInput({ text: $r('app.string.ProhibitSelectMenu_content') })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {

              return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/fusAKHzjS0-0JX76KrQ41w/zh-cn_image_0000002537172922.png?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=4A45D1575FB259EC1C9245DE2F76E32ADABC551B4C26DCFCD20685B83B08A3B8)

## 自动填充

输入框可以通过[contentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12)属性设置自动填充类型。

支持的类型请参考[ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12枚举说明)。

```typescript
TextInput({ placeholder: $r('app.string.Auto_Fill_PlaceHolder') })
  .width('95%')
  .height(40)
  .margin(20)
  .contentType(ContentType.EMAIL_ADDRESS)
```

## 设置属性

- 设置省略属性。 输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。 ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。 ```typescript TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })  .textOverflow(TextOverflow.Ellipsis)  .ellipsisMode(EllipsisMode.END)  .style(TextInputStyle.Inline)  .fontSize(30)  .margin(30) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/B_4zIqvkTSCsxwvpep_sxA/zh-cn_image_0000002537332844.jpg?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=C40FB277E8D90D6DE07ABB6E7AEF9823B6B1449C6672FBF7D641CDF04741D03A)
- 设置文本描边属性。 从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。 ```typescript TextInput({ text: 'Text with stroke' })  .width('100%')  .height(60)  .borderWidth(1)  .fontSize(40)  .strokeWidth(LengthMetrics.px(3.0))  .strokeColor(Color.Red) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/uK7AOFmUSVCDpnSzyWllxQ/zh-cn_image_0000002568172641.jpg?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=56B8FF1A82148C042B33BED6C33A1A980E79C309D8372E34841D851BDBE44C71)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```typescript
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/AEEPPxilSj6QE2kW7XrnfA/zh-cn_image_0000002568252637.jpg?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=727F44A0B332A40671C19E04CCA5C8D0A90F193239DFF6D25EF0A7904247CBDF)

## 键盘避让

键盘抬起后，具有滚动能力的容器组件在横竖屏切换时，才会生效键盘避让，若希望无滚动能力的容器组件也生效键盘避让，建议在组件外嵌套一层具有滚动能力的容器组件，比如[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)。

```typescript
@Entry
@Component
struct KeyboardAvoid {
  placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7'];

  build() {
    Scroll() {
      Column() {
        ForEach(this.placeHolderArr, (placeholder: string) => {
          TextInput({ placeholder: 'TextInput ' + placeholder })
            .margin(30)

        })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qLS3J3YoT3GTT3LgRjuHrA/zh-cn_image_0000002537172924.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=FEAFF08B9C13EF58F55B3C9BFAFFF0E3A513A5A006BCF157C0416B4A692DED9F)

## 光标避让

[keyBoardAvoidMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#keyboardavoidmode11)枚举中的OFFSET和RESIZE在键盘抬起后，不支持二次避让。如果想要支持光标位置在点击或者通过接口设置变化后发生二次避让，可以考虑使用OFFSET_WITH_CARET和RESIZE_CARET替换原有的OFFSET和RESIZE模式。

对于滚动容器更推荐使用RESIZE_WITH_CARET，非滚动容器应该使用OFFSET_WITH_CARET。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { KeyboardAvoidMode } from '@kit.ArkUI';
```

```typescript
onWindowStageCreate(windowStage: window.WindowStage): void {

  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err, data) => {
    let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
    windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET_WITH_CARET);
    if (err.code) {
      hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  });
}
```

```typescript
@Entry
@Component
struct CursorAvoid {
  @State caretPosition: number = 600;
  areaController: TextAreaController = new TextAreaController();
  text = 'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot,' +
    ' or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy,' +
    ' totally forgetting that there is something happy in our own life.\
    So the best way to destroy happiness is to look at something and focus on even the smallest flaw. ' +
    'It is the smallest flaw that would make us complain. And it is the complaint that leads to us becoming unhappy.\
    If one chooses to be happy, he will be blessed; if he chooses to be unhappy, he will be cursed. ' +
    'Happiness is just what you think will make you happy.' +
    'Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, ' +
    'or someone we hardly know. As a result, what we do remember is anything that makes others happy, ' +
    'anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life.\
  ';

  build() {
    Scroll() {
      Column() {
        Row() {
          Button('CaretPosition++: ' + this.caretPosition).onClick(() => {
            this.caretPosition += 1;
          }).fontSize(10)
          Button('CaretPosition--: ' + this.caretPosition).onClick(() => {
            this.caretPosition -= 1;
          }).fontSize(10)
          Button('SetCaretPosition: ').onClick(() => {
            this.areaController.caretPosition(this.caretPosition);
          }).fontSize(10)
        }

        TextArea({ text: this.text, controller: this.areaController })
          .width('100%')
          .fontSize('20fp')
      }
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/uPq3-t_RRD-SsBbySkIB0A/zh-cn_image_0000002537332846.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=D2743B3ABEB21D6847FD0B1DAD237F4CADBE119754DB16A864224746D24BB46E)

## 常见问题

### 如何设置TextArea的文本最少展示行数并自适应高度

**问题现象**

设置TextArea的初始高度来控制最少文本展示行数，当输入文本超过初始高度时，TextArea的高度自适应。

**解决措施**

设置[minLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minlines20)（从API version 20开始），或者设置height为"auto"，并使用[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)自行计算高度。

```typescript
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct TextExample {
  private textAreaPadding = 12;
  private setMaxLines = 3;
  private resourceManager = this.getUIContext().getHostContext()?.resourceManager;

  private changeText = this.resourceManager?.getStringByNameSync('NormalQuestion_change') as string;
  @State fullText: string = this.changeText;
  @State originText: string = this.changeText;
  @State uiContext: UIContext = this.getUIContext();
  @State uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
  textSize: SizeOptions = this.uiContextMeasure.measureTextSize({
    textContent: this.originText,
    fontSize: 18
  });

  build() {
    Column() {
      TextArea({ text: 'minLines: ' + this.fullText })
        .fontSize(18)
        .width(300)
        .minLines(3)

      Blank(50)

      TextArea({ text: 'constraintSize: ' + this.fullText })
        .fontSize(18)
        .padding({ top: this.textAreaPadding, bottom: this.textAreaPadding })
        .width(300)
        .height('auto')
        .constraintSize({

          minHeight: this.textAreaPadding * 2 +
            this.setMaxLines * this.getUIContext().px2vp(Number(this.textSize.height))
        })

      Blank(50)

      Button($r('app.string.NormalQuestion_AddInput'))
        .onClick(() => {
          this.fullText += this.changeText;
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .padding({ top: 30 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/gClIw9p3SbC0IlvipW0jlA/zh-cn_image_0000002568172643.gif?HW-CC-KV=V1&HW-CC-Date=20260410T025234Z&HW-CC-Expire=86400&HW-CC-Sign=C4F3AAAD3FCF879F02D32BA05980AA82C6462EABD50FDF528F58185DE7D79F8A)
