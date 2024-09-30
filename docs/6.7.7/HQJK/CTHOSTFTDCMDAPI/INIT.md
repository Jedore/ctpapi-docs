<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="82d0d74a-b655-48ff-b4c0-406efa644693"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="a8b4150e-6043-47eb-b974-dc14ff3dea2f"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="b454abe9-9a83-4ce5-b4c4-0d4305d19ded"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7fc3dcb7-91f0-4407-9934-db6b3e3f2a5c"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="e72ac244-6b3b-4c4d-9fe0-01540188a277"></span>
## 5.FAQ
<p>无</p>
