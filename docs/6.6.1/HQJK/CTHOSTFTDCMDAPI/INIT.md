<p>初始化运行环境,只有调用后,接口才开始发起前置的连接请求。</p>
<span class="anchor" id="e519c3ec-51a1-4d0f-abed-704ab4f149d8"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="f88a076b-6f47-4fce-8443-d995070a62eb"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="28e0c538-9c6f-43a5-86c2-11b8809cf548"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5ba4f20d-ec63-42a0-9377-f5d993b30e86"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="91451d34-81db-4b9e-86da-e34f49614f17"></span>
## 5.FAQ
<p>无</p>
