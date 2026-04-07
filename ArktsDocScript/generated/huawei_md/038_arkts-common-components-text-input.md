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

- 单行输入框。 ```typescript TextInput() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/z7K56xreR2Om0ECyaIOSwA/zh-cn_image_0000002566868129.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=7B4BEE54D5D5FC7AF35A50A8C33A1F47789386603619B6272FFFADBBFB9FA6F0)
- 多行输入框。 ```typescript TextArea() ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/5eHmU-9NS9OlJOUlhvphKw/zh-cn_image_0000002566708149.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=870D37AE9D6975E8962D923283FA50941E2BD618D65EBD6EF088EF231C018FF6)
- 多行输入框文字超出一行时会自动折行。 ```typescript TextArea({ text: $r('app.string.CreatTextInput_textContent') })  .width(300) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/hr9Zas5qTZG7m6dCwWInZA/zh-cn_image_0000002535788354.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=DD0DDF9BFFDE97A4E33AF2F090E628974BFB34FC4A166579E904392992E8F970)
- 搜索框。 ```typescript Search()  .searchButton($r('app.string.Creat_TextInput_Content')) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/AMmv6ro7RDe6JF6Pec2D7w/zh-cn_image_0000002535948300.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=8D6308A668612743385A458C14545B289B9871C220BCFD96ED69E847C3F244C2)

## 设置输入框类型

TextInput、TextArea和Search都支持设置输入框类型，通过type属性进行设置，但是各组件的枚举值略有不同。下面以单行输入框为例进行说明。

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#type)属性进行设置：

### 基本输入模式（默认类型）

```typescript
TextInput()
  .type(InputType.Normal)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/lFU5D1DNTSSeZjqqyxekHQ/zh-cn_image_0000002566868133.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=03CCD27ACEE044D2AE3AE1E1D6AC35B8656D3E72B69F9C69CC012BDD5CBB44E8)

### 密码模式

包括Password密码输入模式、NUMBER_PASSWORD纯数字密码模式、NEW_PASSWORD新密码输入模式。

以下示例是Password密码输入模式的输入框。

```typescript
TextInput()
  .type(InputType.Password)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/uFTdwAo7Qc2FHX9t-dVIsQ/zh-cn_image_0000002566708151.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=A6C06A49DCE285993A99CAA0B478D70C2810968268671CDBFA5B8407B67EA63E)

### 邮箱地址输入模式

邮箱地址输入模式的输入框，只能存在一个@符号。

```typescript
TextInput()
  .type(InputType.Email)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/E8t9HkzeQ8ytf9dg65sc9w/zh-cn_image_0000002535788356.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=C5A4EE86FE593C5F28CE7DD8FA627DA04789944EA7C730E9C11FF35C8E6CBF89)

### 纯数字输入模式

纯数字输入模式的输入框，只能输入数字[0-9]。

```typescript
TextInput()
  .type(InputType.Number)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WIUNPC4TQpOzY0seqCCepw/zh-cn_image_0000002535948302.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=4425009D567D4694DD8CCB07B2D54DD8924C989783397C92E8524C713BE1CDA7)

### 电话号码输入模式

电话号码输入模式的输入框，支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

```typescript
TextInput()
  .type(InputType.PhoneNumber)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/N-aMH1mWQbSkvMY2pIPCqQ/zh-cn_image_0000002566868135.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=2FECAC0F3D8928C7BE10EC28EC6B41DE0A28A3C343D855BF8386B702F1357F17)

### 带小数点的数字输入模式

带小数点的数字输入模式的输入框，只能输入数字[0-9]和小数点，只能存在一个小数点。

```typescript
TextInput()
  .type(InputType.NUMBER_DECIMAL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/3lx0adUKR1aWHR9HZCQEIg/zh-cn_image_0000002566708155.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=0FBB8C0B2DEA9BAE39D0DD315EE5FB7F0C2AFAF11A04B8F0E2778269D0897BC0)

### 带URL的输入模式

带URL的输入模式，无特殊限制。

```typescript
TextInput()
  .type(InputType.URL)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6dzzKVaER0SGJkJuzTAOig/zh-cn_image_0000002535788360.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=B7A85949B2864E65F912AB319E30E03925E2F62554F7BEF260E3D832AC7C057C)

## 设置输入框多态样式

TextInput、TextArea支持设置输入框多态样式，通过[style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#style10)属性进行设置。下面以多行输入框TextArea为例进行说明。

TextArea有以下2种类型可选择：默认风格，入参是TextContentStyle.DEFAULT；内联模式，也称内联输入风格，入参是TextContentStyle.INLINE。

### 默认风格

默认风格的输入框，在编辑态和非编辑态，样式没有区别。

```typescript
TextArea()
  .style(TextContentStyle.DEFAULT)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Xm9fP8V8RJ-ik_5nhDnNxA/zh-cn_image_0000002535948306.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=1333D8AA7DAE01D06109BB104EE5CA189DD15F5D5ED0CDA15C3DCB14BA0BA8F9)

### 内联模式

内联模式，也称内联输入风格。内联模式的输入框在编辑态和非编辑态样式有明显区分。

```typescript
TextArea()
  .style(TextContentStyle.INLINE)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/N0-qxtuURLK_7GrTZNXGKA/zh-cn_image_0000002566868137.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=DA5E896017AF6152C34A1C856E954445452EBAF25892A7AEF83D8DEBF522C226)

## 自定义样式

- 设置无输入时的提示文本。 ```typescript TextInput({ placeholder: $r('app.string.i_am_placeholder') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ojkrDrfrRR-lRvYm5sCXXQ/zh-cn_image_0000002566708157.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=588E0829FB861ED8752584389307DDF229BC107E9E5EAE34E4A129FCD4BB38BA)
- 设置输入框当前的文本内容。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') }) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/r2JdRiv9Qiul731YTG-wiA/zh-cn_image_0000002535788362.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=0D20F9259DA44CA749D81660CE74B2E7C235D7926AD6BA7C40C3660A84BC3C88)
- 添加backgroundColor改变输入框的背景颜色。 ```typescript TextInput({  placeholder: $r('app.string.i_am_placeholder'),  text: $r('app.string.i_am_current_text_content') })  .backgroundColor(Color.Pink) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/98h5ikHtR3a6CXxVjj9Ljw/zh-cn_image_0000002535948308.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=4A627C459A15A742D60A06D2CDA25E03357EA478E8B58202B865C112FAE7DB96) 更丰富的样式可以结合[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)实现。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/iUuJdQmoQ9ipGWKDx-B8rQ/zh-cn_image_0000002566868141.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=F3045E75B27C8AB47B04349E244505C94F129349DC5B3DEBBB70B002AB3B4759)

## 选中菜单

输入框中的文字被选中时会弹出包含剪切、复制、翻译、搜索的菜单。

TextInput:

```typescript
TextInput({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/a8odaDe4RrCapZLe8LRY2Q/zh-cn_image_0000002566708161.jpg?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=08E6C48DCF0B91B7D62D2F5D1EDC28A794FE7183619B19C602A19A1830804759)

TextArea:

```typescript
TextArea({ text: $r('app.string.show_selected_menu') })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/kuSCD9s7TpCC2vduRT87VQ/zh-cn_image_0000002535788364.jpg?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=536ACBF7F0E77C193297B7DB0BB833C32048AB9D719900B579FAE0082832DBC3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/mKfhLdEsSv-pHqQLBN4kVw/zh-cn_image_0000002535948312.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=5F2491C39F632D825DF439A749E49557029A754C43553715BB4209D8352A4DDA)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/MnTroXnuRouv1wN4GRUbAQ/zh-cn_image_0000002566868143.png?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=71B03A32A92A1CB45E482BCBD45FD27D46920B2BFDD50B98B79C52CC30FAE76A)

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

- 设置省略属性。 输入框可以通过[ellipsisMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)属性设置省略位置。 ellipsisMode属性需要配合[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)属性设置为TextOverflow.Ellipsis使用，单独设置ellipsisMode属性不生效。 ```typescript TextInput({ text: $r('app.string.Set_Omission_Property_textContent') })  .textOverflow(TextOverflow.Ellipsis)  .ellipsisMode(EllipsisMode.END)  .style(TextInputStyle.Inline)  .fontSize(30)  .margin(30) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/9C0cLLK-Q-2zg82F5SBpHw/zh-cn_image_0000002566708163.jpg?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=218DE70A52D82441A352F45176EFAAF6CD4E9F1D4988734A7459C5675AF97672)
- 设置文本描边属性。 从API version 20开始，输入框可以通过[strokeWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokewidth20)和[strokeColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#strokecolor20)属性设置文本的描边宽度及颜色。 ```typescript TextInput({ text: 'Text with stroke' })  .width('100%')  .height(60)  .borderWidth(1)  .fontSize(40)  .strokeWidth(LengthMetrics.px(3.0))  .strokeColor(Color.Red) ``` ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/qfp-zltcRaC8UCyLQheVKA/zh-cn_image_0000002535788368.jpg?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=5DA02F4BEB0C08D023AE77520E5C78433488BB4983C6118B791BFCB344C1BAF7)

## 设置文本行间距

从API version 20开始，支持通过[lineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#linespacing20)设置文本的行间距。如果不配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)时，首行上方和尾行下方默认会有行间距。如果onlyBetweenLines设置为true时，行间距仅适用于行与行之间，首行上方无额外行间距。

```typescript
TextArea({
  text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.'
})
  .fontSize(22)
  .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/7AsYOx8iShacchU1Td8R4Q/zh-cn_image_0000002535948314.jpg?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=60A5ACB527CEFB8F1022207E20AF16E409ABD2341E70C63626FB2FA22600711D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/APHYJAegTbaQA0n8-0rBUQ/zh-cn_image_0000002566868147.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=FFAEFCAFD1080AB1F985359166B2FD4930FD755173B9069B4834923B8ABA9C76)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/hvgHU1H9QBG4Bt0b7Wo_WA/zh-cn_image_0000002566708167.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=BD51D9CA346A7DABB776465BB20E6478D31AC410DA8A9D304BED68371776F09F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/_406TXJnQXu2XF5IkY0UPg/zh-cn_image_0000002535788370.gif?HW-CC-KV=V1&HW-CC-Date=20260407T024039Z&HW-CC-Expire=86400&HW-CC-Sign=8E7EDAD356D0A37D590475AA9AA8077BD9633F87E9241AA541F3AEB548074B00)
