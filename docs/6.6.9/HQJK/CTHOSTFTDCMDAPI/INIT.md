<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="8f17c91a-655c-4615-9b7b-b957b793265f"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="e9a4a7b1-a83d-4d21-b6af-ac9eb2329073"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="cac9957a-3104-4678-87c3-166cd5604134"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="060054e1-03e0-47a4-8ecd-935074012417"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="9563514f-e861-410b-b708-756459166668"></span>
## 5.FAQ
<p>无</p>
