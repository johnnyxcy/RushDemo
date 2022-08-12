/** *********************************************
 * 文件名: src/nls.ts
 * 创建时间: 2021-11-13 18:57:11
 * 作者: 许翀轶
 * 模块描述: 多语言入口
 Copyright (c) 2021 上海博佳医药科技有限公司
*********************************************  */

export interface ILocalizeInfo {
    key: string;
    comment: string[];
}

// /**
//  * Localize a message.
//  *
//  * `message` can contain `{n}` notation where it is replaced by the nth value in `...args`
//  * For example, `localize({ key: 'sayHello', comment: ['Welcomes user'] }, 'hello {0}', name)`
//  */
// export function localize(
//     info: ILocalizeInfo,
//     message: string,
//     ...args: (string | number | boolean | undefined | null)[]
// ): string {
//     return message;
// }
/**
 * Localize a message.
 *
 * `message` can contain `{n}` notation where it is replaced by the nth value in `...args`
 *  - string: For example, `localize('sayHello', 'hello {0}', name)`
 *  - ILocalizeInfo: For example, `localize({ key: 'sayHello', comment: ['Welcomes user'] }, 'hello {0}', name)`
 */
export function localize(
    _key: string | ILocalizeInfo,
    message: string,
    ..._args: (string | number | boolean | undefined | null)[]
): string {
    return message;
}
