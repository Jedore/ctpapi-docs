<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="28d63627-1d7b-4ecf-8c77-02c8539ff95a"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="028fb33a-f5e5-431c-996c-72a348988f78"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="77759169-bdc3-4751-86e2-79a5252d8801"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5b9a67d6-1506-4e2a-bef4-540fda4efb0c"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="ceb61d5d-9daf-48d1-a177-0ef3def876cb"></span>
## 5.FAQ
<p>无</p>
