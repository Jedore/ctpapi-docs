<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="f9e06220-92ee-4e34-a77a-1da98bc20ddc"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="214e9b33-f774-44d3-9c46-5186ec0cea1b"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="94d48043-6330-4526-9e45-da544aaee3d5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e9d294b3-fe7e-4507-9725-5a2992d33bff"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="1b4b3ed8-5044-437a-8853-dec897e6e9a5"></span>
## 5.FAQ
<p>无</p>
