## 目录结构

```
├── common                          // 公共层
│   ├── config.yaml                 // 公共配置
│   ├── generic.py                  // 公共方法
├── data                            // 数据层
├── file                            // 爬取文件存放区域
├── jobs                            // 工作层
├── logs                            // 日志层
├── report                          // 测试报告层
├── test                            // 测试用例代码
├── utils                           // 工具类
│   └── assert                      // 断言处理模块
│       └── assert.py
│       └── type.py                 // 断言类型
│   └── cache                       // 缓存处理模块
│       └── cache.py
│       └── redis.py
│   └── log                         // 日志处理模块
│       └── log.py
│       └── decorator.py            // 日志装饰器
│   └── sql                         // 数据库模块
│       └── mysql.py
│       └── sqlite.py
│   └── notify                      // 通知模块
│       └── ding_talk.py            // 钉钉通知
│       └── lark_suite.py           // 飞书通知
│       └── send_email.py           // 邮箱通知
│       └── firm_wechat.py          // 企业微信通知
├── Readme.md
```

