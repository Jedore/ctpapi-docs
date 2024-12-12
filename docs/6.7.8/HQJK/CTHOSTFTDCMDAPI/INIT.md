<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="2c253517-1784-4e66-983b-b5166d378333"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="f4dbf852-285c-48e1-b082-0775506a677f"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="b75dc2a2-d9c5-460b-9ee7-161e926ceddb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="160ff037-f470-4fcd-bd72-a141f9f3d412"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="48937049-4e95-4d49-8a53-d483f0c33b02"></span>
## 5.FAQ
<p>无</p>
