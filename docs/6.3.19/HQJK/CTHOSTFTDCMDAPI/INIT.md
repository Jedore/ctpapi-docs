<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="45eb6ca8-dc53-47b6-90e9-6a9dfca6ae74"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="96e2e5cf-075e-407a-bfd7-6060c805c4c2"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="5e6addeb-8cb1-4c75-a3ed-6fbe3fff9aa8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5d553450-2f3e-4697-a263-4ee07e90f3a8"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="96527a03-a02f-424f-a282-bb410301bb20"></span>
## 5.FAQ
<p>无</p>
