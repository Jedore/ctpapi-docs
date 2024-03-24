<p>获取API的版本信息</p>
<span class="anchor" id="343565c1-3a00-4d1b-8667-7666dd68efeb"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="222b1283-f68a-4802-8045-ea45580ea26f"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="c4e80c7e-2d5b-4fec-9d8e-0ec18d0db2bb"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="28617dce-4ce5-48bb-b047-b3f389ea364e"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
LOG(pUserApi-&gt;GetApiVersion());
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="eecf6a63-458f-463b-8326-4f5061fcb417"></span>
## 5.FAQ
<p>无</p>
