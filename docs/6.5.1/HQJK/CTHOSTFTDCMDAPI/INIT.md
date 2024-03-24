<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="6fbd8d47-cce2-4754-abc6-708dd772e308"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="5a2137a8-e6b2-462f-8d4b-d2a3fd2ee380"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="43b3a82b-2f18-419f-9102-87bc00bfebd1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4b4187d7-3c01-48e5-bd82-90ef48097451"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="2f54633b-7bba-4c5a-9668-b1755433d5c6"></span>
## 5.FAQ
<p>无</p>
