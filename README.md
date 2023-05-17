# StressTestLocust
## Core

Locust是開源、使用Python開發、基於事件、支援分散式並且提供Web UI進行測試執行和結果展示的效能測試工具。

- 特性：
    - 模擬使用者操作:支援多協議，Locust可以用於壓測任意協議型別的系統
    - 併發機制:摒棄了程式和執行緒，採用協程（gevent）的機制，單臺測試機可以產生數千併發壓力
- Locust使用了以下幾個核心庫：

1) gevent
   gevent是一種基於協程的Python網路庫，它用到Greenlet提供的，封裝了libevent事件迴圈的高層同步API。
2) flask
   Python編寫的輕量級Web應用框架。
3) requests
   Python Http庫
4) msgpack-python
   MessagePack是一種快速、緊湊的二進位制序列化格式，適用於類似JSON的資料格式。msgpack-python主要提供MessagePack資料序列化及反序列化的方法。
5) pyzmq
   pyzmq是zeromq(一種通訊佇列)的Python實現,主要用來實現Locust的分散式模式執行

![img.png](img/img.png)

## Ref
原理介紹: https://juejin.cn/post/7081528999905591327
基本介紹：https://iter01.com/511735.html
使用 powershell 啟動 Locust: https://www.laitimes.com/article/3h1zm_3xr0r.html
wait_time 解釋：https://www.icoding.co/2020/09/%E7%94%A8-locust-io-%E4%BE%86%E5%81%9A-load-testing
有順序性執行 locust: https://iter01.com/645941.html
Locust WEB 解釋: https://www.796t.com/content/1544462851.html
POST 用法: https://gist.github.com/agconti/0f3886cbf1ce158e913e